# ScottPlot 5 Plottables 层架构剖析

> 职责：Plottable 层深度剖析 — 统一 IPlottable 契约 · IHas* Mixin 接口 · 全分类矩阵

---

## 数据流视角

```
// 构造链路
Plot myPlot = new();  → 创建 Plot（PlottableList、Axes、RenderManager、Legend）
myPlot.Add.Scatter(xs, ys);  → PlottableAdder 工厂方法
  → 自动包装数据源 (ScatterSourceDoubleArray)
  → 自动取色 (从 Plot 的调色板循环)
  → new Scatter(source) → Plot.PlottableList.Add()

// 样式链路
scatter.LineWidth = 3;        → 属性转发 → LineStyle.Width = 3（无需重建对象）
scatter.MarkerColor = Colors.Blue;  → MarkerStyle.Color = Blue
```

---

## 一、总览：Plottable 分类矩阵

```
┌──────────────────────────────────────────────────────────────────────┐
│                     Plottables 层全景                                  │
├───────────────┬──────────────┬───────────────┬──────────────────────┤
│ 散点/信号     │ 柱状/条形    │ 金融图表       │ 矢量/箭头            │
├───────────────┼──────────────┼───────────────┼──────────────────────┤
│ 热力/等值     │ 饼图/径向    │ 极坐标/雷达    │ 统计图表             │
├───────────────┼──────────────┼───────────────┼──────────────────────┤
│ 直线/跨度     │ 形状图形    │ 标注/文字      │ 实时数据             │
├───────────────┼──────────────┼───────────────┼──────────────────────┤
│ 交互工具      │ 装饰器      │ 其他          │ SubplotPreRender     │
└───────────────┴──────────────┴───────────────┴──────────────────────┘
```

---

## 二、Plottable 统一模式

每个 Plottable 遵循统一模板：`IPlottable` 核心契约 + 按需组合 IHas* Mixin 接口（IHasLine, IHasMarker, IHasFill 等），样式属性通过转发模式委托给对应的 Style 对象。

核心方法：`IsVisible` · `Axes` · `GetAxisLimits()` · `Render()` · `LegendItems`。详见 [02-primitives](02-primitives.md)（接口定义）和 [05-rendering](05-rendering.md)（Render 调用流程）。

---

## 三、按类别逐一分析

### 3.1 散点/信号系列 (7个)

| Plottable | 数据源 | 核心特性 | 接口链 |
|---|---|---|---|
| **Scatter** | `IScatterSource` | XY散点+连线+填充 | `IPlottable, IHasLine, IHasMarker, IHasLegendText` |
| **Signal** | `ISignalSource` | 等间距大数据，SegmentedTree 降采样 | `IPlottable, IHasLine, IHasMarker, IHasLegendText` |
| **SignalXY** | `ISignalXYSource` | 不等间距大数据降采样 | `IPlottable, IHasLine, IHasMarker, IHasLegendText` |
| **SignalConst** | `SignalConstSource<T>` | **已标记 [Obsolete]**：内部即 Signal + SegmentedTree，新代码请直接用 Signal | 继承自 `Signal` |
| **LinePlot** | `CoordinateLine` | 两点确定一条直线 | `IPlottable, IHasLine, IHasMarker, IHasLegendText` |
| **FunctionPlot** | `IFunctionSource` | y=f(x) 函数拟合 | `IPlottable, IHasLine` |
| **FillY** | `IScatterSource` + `IScatterSource?` | 两条曲线间区域填充 | `IPlottable, IHasLine, IHasFill` |

**Scatter.Render 核心流程**：
```
Data.GetScatterPoints() → Coordinates[]
  → Axes.GetPixel()    → Pixel[] (坐标→像素转换)
  → PathStrategy.GetPath()  → SKPath (连线策略: 直线/样条/阶梯)
  → 绘制填充 (if FillY)
  → 绘制线条 (LineStyle.Apply)
  → 逐个绘制标记 (MarkerStyle.Render)
```

### 3.2 柱状/条形系列 (3个)

| Plottable | 数据 | 特性 |
|---|---|---|
| **BarPlot** | `List<Bar>` | 垂直/水平柱状图，每柱独立样式 |
| **LollipopPlot** | `IEnumerable<Coordinates>` 或 `double[]` 值 | 棒棒糖图（柱+端点） |
| **Coxcomb** | `IList<PieSlice>` | 玫瑰图（面积=值） |

**Bar 数据结构**：
```csharp
public class Bar
{
    double Position, Value, ValueBase;
    double ErrorPositive, ErrorNegative;
    string Label;
    FillStyle FillStyle;   // 每柱独立颜色
    LineStyle BorderStyle;
    LabelStyle LabelStyle;
    Orientation Orientation;  // Vertical / Horizontal
}
```

### 3.3 金融图表 (3个)

| Plottable | 数据 | 特性 | 接口 |
|---|---|---|---|
| **OhlcPlot** | `IOHLCSource` | 开/高/低/收盘—竖线 | `IPlottable` |
| **CandlestickPlot** | `IOHLCSource` | 蜡烛图，自动红涨绿跌着色 | `IPlottable` |
| **FinancialTimeAxis** | — | 金融时间轴（忽略非交易时段） | 特殊轴管理 |

### 3.4 热力/等值系列 (4个)

| Plottable | 数据 | 关键差异 |
|---|---|---|
| **Heatmap** | `double[,]` | 最常用热力图，Colormap 映射 |
| **IsoLines** | `double[,]` | 等值线（等高线） |
| **ContourLines** | `List<ContourLine>` | 用户提供等值线数据 |
| **TINPlot** | 三角网结点 | 不规则三角网插值热力图 |

**Heatmap 核心**：
```csharp
class Heatmap : IPlottable, IHasColorAxis
{
    double[,] Intensities;
    IColormap Colormap;        // Viridis 等 38 种
    CoordinateRect? Extent;    // 定义热力区域在坐标空间的位置
    CellAlignment CellAlignment; // 单元格对齐方式

    void Render(RenderPack rp)
    {
        // 1. 遍历 Intensities[,]
        // 2. 归一化 → fraction [0,1]
        // 3. Colormap.GetColor(fraction)
        // 4. SKRect 逐个绘制彩色矩形单元格
        // 5. 可选: 绘制 ColorBar (颜色轴)
    }
}
```

### 3.5 饼图/径向系列 (4个)

| Plottable | 基类 | 特性 |
|---|---|---|
| **Pie** | `PieBase` | 标准饼图 + Donut 模式 (DonutFraction) |
| **PieBase** | — | 抽象基类，处理标签和爆裂 |
| **RadialGaugePlot** | — | 径向仪表盘（多指针） |
| **RadialGauge** | internal 模型类 | RadialGaugePlot 的组成单元（非独立图表、非公开 API） |

### 3.6 极坐标/雷达/特殊轴 (4个)

| Plottable | 用途 |
|---|---|
| **PolarAxis** | 极坐标轴（半径+角度） |
| **Radar** | 雷达图（多轴多系列） |
| **TriangularAxis** | 三轴图（三元相图） |
| **SmithChartAxis** | 史密斯圆图（射频工程） |

**独特性**：这些图表有自己的专用轴类型（`IStarAxis` 等），不依赖标准 `IXAxis`/`IYAxis`。

### 3.7 矢量/箭头 (2个)

| Plottable | 数据 | 特性 |
|---|---|---|
| **VectorField** | `IVectorFieldSource` | 矢量场（箭头网格） |
| **Arrow** | `Coordinates` 起点+终点 | 单条箭头 |

### 3.8 统计图表 (3个)

| Plottable | 数据 | 特性 |
|---|---|---|
| **BoxPlot** | `List<Box>` | 箱线图（Min/Q1/Median/Q3/Max/Outliers） |
| **ErrorBar** | 直接持有 `IReadOnlyList` 属性（无数据源接口） | XY 误差棒图 |
| **HistogramBars** | `Histogram` | 直方图/频率分布 |

### 3.9 直线/跨度系列 (8个)

| Plottable | 线条类型 | 注解 |
|---|---|---|
| **HorizontalLine** | 水平线 Y=const | 继承自 `AxisLine` |
| **VerticalLine** | 垂直线 X=const | 继承自 `AxisLine` |
| **AxisLine** | 轴辅助线 | 基准类，支持拖拽 |
| **HorizontalSpan** | 水平填充区域 | Y1~Y2 |
| **VerticalSpan** | 垂直填充区域 | X1~X2 |
| **AxisSpan** | 轴区域 | 基准类，支持拖拽 |
| **ScaleBar** | 比例尺 | 地图比例尺 |
| **FloatingAxis** | 浮动轴 | 独立于 Plot 标准轴的游离坐标轴 |

### 3.10 形状图形 (5个)

| Plottable | 描述 |
|---|---|
| **Rectangle** | 矩形（坐标空间） |
| **Ellipse** | 椭圆/扇形/环形扇区 |
| **Polygon** | 自定义多边形 |
| **Marker** | 单点标记 |
| **Markers** | 多点标记（批量渲染） |

### 3.11 标注/文字 (7个)

| Plottable | 用途 |
|---|---|
| **Annotation** | 文本注释（自动背景+边框） |
| **Text** | 纯文本 |
| **Crosshair** | 十字光标 |
| **Tooltip** | 悬浮提示框 |
| **Callout** | 标注箭头+文本框 |
| **Bracket** | 括号标注（两点间弧形标注） |
| **Benchmark** | 性能信息显示 |

### 3.12 实时数据 (3个)

| Plottable | 数据源 | 特性 |
|---|---|---|
| **DataLogger** | `DataLoggerSource` | 追加模式，自动跟踪Y范围 |
| **DataStreamer** | `DataStreamerSource` | 环形缓冲，固定窗口 |
| **DataStreamerXY** | — | 环形缓冲+XY独立 |

`DataLogger` 实现 `IManagesAxisLimits`，在渲染前自动更新轴范围。

### 3.13 交互工具 (10个) 与装饰器 (2个)

```
Interactive/（10 个文件，实现 IPlottable 可被拖拽交互）
├── InteractiveMarker          ← 拖拽标记
├── InteractiveLineSegment      ← 拖拽线段
├── InteractiveVerticalLine     ← 拖拽垂直线
├── InteractiveHorizontalLine   ← 拖拽水平线
├── InteractiveVerticalSpan     ← 拖拽垂直区域
├── InteractiveHorizontalSpan   ← 拖拽水平区域
├── InteractiveTrendLine        ← 拖拽趋势线
├── InteractiveRectangle        ← 拖拽矩形选框
├── InteractiveVerticalLineSegment   ← 可调垂直线段
└── InteractiveHorizontalLineSegment ← 可调水平线段

装饰器 (根目录 Wrappers，包裹任意 IPlottable):
├── DraggablePlottableDecorator ← 使任意 Plottable 可拖拽
└── HittablePlottableDecorator  ← 使任意 Plottable 可点击检测
```

> 注意：`ZoomRectangle` 位于 Plottables 根目录，但实现的是 `IZoomRectangle`
> 而非 `IPlottable`——它是缩放框的绘制模型，由渲染管道第 22 步专门绘制。

---

## 四、Plottable 实现的核心接口一览

```
IPlottable        → 必须实现: IsVisible, Axes, GetAxisLimits(), Render(), LegendItems
IHasLine / IHasMarker / IHasFill / IHasLegendText / ... → 样式 Mixin（见下方说明）
IGetNearest       → GetNearest() 最近点查询
IManagesAxisLimits→ UpdateAxisLimits() 自动轴范围（DataLogger 实现）
IRenderLast       → RenderLast() 最后渲染（覆盖在坐标轴上）
IPlottableGL      → GPU 渲染契约（核心库内无实现者，供 OpenGL 附加包实现）
IHasInteractiveHandles → 交互句柄
```

样式 Mixin 接口（IHasLine / IHasMarker / IHasFill / IHasLegendText / IHasArrow /
IHasLabel / IHasOutline / IHasShadow / IHasBackground / IHasColorAxis）的完整属性
清单与转发模式：见 [02-primitives §三](./02-primitives.md#三样式系统)。

---

## 五、Render 方法模式分类

### 模式 A：数据驱动渲染（Scatter / Signal / BarPlot / Heatmap 等）
```
Render(rp):
  获取数据 → 坐标转换(1:1像素映射) → 裁剪 → Canvas绘制
```

### 模式 B：轴驱动渲染（AxesLine / Span / Crosshair）
```
Render(rp):
  从 Axes 计算像素位置 → Canvas绘制 (无需遍历数据)
```

### 模式 C：装饰器代理（DraggablePlottableDecorator / HittablePlottableDecorator）
```
Render(rp):
  被装饰者.Render(rp)                 ← 先画原图
  + 额外的交互手柄/点击区域             ← 再叠加交互层
```

### 模式 D：专用渲染（Pie / Polar / Triangular / SmithChart）
```
Render(rp):
  用自己的算法计算像素布局（Pie按角度、Polar按半径角度...）
  → Canvas绘制（不经过标准 Axes 转换）
```

---

## 六、关键设计洞察

1. **IPlottable 是最小合约**：只需 `IsVisible` + `Axes` + `GetAxisLimits()` + `Render()` + `LegendItems` 五步即可自定义图表类型。

2. **样式接口是可选插件**：`IHasLine`, `IHasMarker`, `IHasFill` 等是 mixin，Plottable 按需实现。RenderManager 通过 `is IHasLine line` 做运行时类型检测来应用通用样式。

3. **GUI 线程安全的分离**：Plottable 的 `Render()` 方法在渲染管道中被调用（第17步 `RenderPlottables`），此时所有数据处理在线程安全的上下文中完成。交互拖拽（`Interactive*` 系列）在 UI 线程中修改数据，然后触发 `Refresh()`。

4. **装饰器模式增强功能**：`DraggablePlottableDecorator` 和 `HittablePlottableDecorator` 可以包裹任何 `IPlottable`，动态添加拖拽或点击检测能力。这是开闭原则的实践。

5. **IRenderLast 控制 Z 序**：默认所有 Plottable 在第17步 `RenderPlottables` 中绘制，实现了 `IRenderLast` 的 Plottable 在第24步 `RenderPlottablesLast` 中绘制，确保它们出现在最上层（如缩放矩形、十字光标、标注）。

6. **FinancialTimeAxis 的巧妙设计**：不是一个独立的轴类型，而是一个特殊 Plottable，在渲染时介入 `AxisManager` 的行为，实现"跳过非交易时段"的 X 轴显示。

7. **SignalConst 已成历史**：`SignalConst<T>` 已标记 `[Obsolete]`，其内部就是 `Signal` + `SignalConstSource<T>`（SegmentedTree 预构建优化）。新代码直接用 `Add.Signal()` 即可。