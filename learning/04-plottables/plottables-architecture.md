# ScottPlot 5 Plottables 层架构剖析

> 61 主文件 + 11 个 Interactive 文件 = 72 个文件 · ~8,400 行代码 · 占核心库 16.8%

---

## 一、总览：Plottable 分类矩阵

```
┌──────────────────────────────────────────────────────────────────────┐
│                     Plottables 层全景 (72 files)                       │
├───────────────┬──────────────┬───────────────┬──────────────────────┤
│ 散点/信号 (6)  │ 柱状/条形 (3)│ 金融图表 (3)   │ 矢量/箭头 (2)        │
├───────────────┼──────────────┼───────────────┼──────────────────────┤
│ 热力/等值 (4)  │ 饼图/径向 (4)│ 极坐标/雷达 (4)│ 统计图表 (3)         │
├───────────────┼──────────────┼───────────────┼──────────────────────┤
│ 直线/跨度 (7)  │ 形状图形 (5) │ 标注/文字 (6) │ 实时数据 (3)         │
├───────────────┼──────────────┼───────────────┼──────────────────────┤
│ 交互工具 (11)  │ 装饰器 (2)  │ 其他 (4)      │                      │
└───────────────┴──────────────┴───────────────┴──────────────────────┘
```

---

## 二、Plottable 统一模式

每个 Plottable 遵循完全相同的代码模板：

```
class XxxPlot : IPlottable, IHasLine, IHasMarker, IHasLegendText, ...
{
    // ═══ 1. 接口实现 ═══
    bool IsVisible { get; set; }
    IAxes Axes { get; set; }        ← 坐标变换
    AxisLimits GetAxisLimits()      ← 计算数据范围
    void Render(RenderPack rp)      ← 绘制
    IEnumerable<LegendItem> LegendItems  ← 图例
    string LegendText { get; set; }  ← 图例文本

    // ═══ 2. 样式属性（转发模式） ═══
    LineStyle LineStyle { get; set; }
    float LineWidth { get => LineStyle.Width; set => LineStyle.Width = value; }
    Color LineColor { get => LineStyle.Color; set => LineStyle.Color = value; }

    MarkerStyle MarkerStyle { get; set; }
    MarkerShape MarkerShape { get => MarkerStyle.Shape; set => MarkerStyle.Shape = value; }
    // ...

    // ═══ 3. 数据源 ═══
    IScatterSource Data { get; }   ← 持有对数据源的引用
}
```

---

## 三、按类别逐一分析

### 3.1 散点/信号系列 (6个)

| Plottable | 数据源 | 核心特性 | 接口链 |
|---|---|---|---|
| **Scatter** | `IScatterSource` | XY散点+连线+填充 | `IPlottable, IHasLine, IHasMarker, IHasLegendText` |
| **Signal** | `ISignalSource` | 等间距大数据，SegmentedTree 降采样 | `IPlottable, IHasLine, IHasMarker, IHasLegendText` |
| **SignalXY** | `ISignalXYSource` | 不等间距大数据降采样 | `IPlottable, IHasLine, IHasMarker, IHasLegendText` |
| **SignalConst** | `ISignalSource` | 全部 Y 值相同，O(1) 极速 | `IPlottable, IHasLine, IHasMarker` |
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
| **LollipopPlot** | `List<Bar>` + `List<Coordinates>` | 棒棒糖图（柱+端点） |
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

| Plottable | 数据 | 特性 |
|---|---|---|
| **OHLCPlot** | `IOHLCSource` | 开/高/低/收盘—竖线 | `IHasLegendText` |
| **CandlestickPlot** | `IOHLCSource` | 蜡烛图，自动红涨绿跌着色 | `IPlottableGL, IHasLegendText` |
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
| **RadialGauge** | — | 单个径向仪表 |

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
| **ErrorBar** | `IErrorBarSource` | XY 误差棒图 |
| **HistogramBars** | 统计数据 | 直方图/频率分布 |

### 3.9 直线/跨度系列 (7个)

| Plottable | 线条类型 | 注解 |
|---|---|---|
| **HorizontalLine** | 水平线 Y=const | 继承自 `AxisLine` |
| **VerticalLine** | 垂直线 X=const | 继承自 `AxisLine` |
| **AxisLine** | 轴辅助线 | 基准类，支持拖拽 |
| **HorizontalSpan** | 水平填充区域 | Y1~Y2 |
| **VerticalSpan** | 垂直填充区域 | X1~X2 |
| **AxisSpan** | 轴区域 | 基准类，支持拖拽 |
| **ScaleBar** | 比例尺 | 地图比例尺 |

### 3.10 形状图形 (5个)

| Plottable | 描述 |
|---|---|
| **Rectangle** | 矩形（坐标空间） |
| **Ellipse** | 椭圆/扇形/环形扇区 |
| **Polygon** | 自定义多边形 |
| **Marker** | 单点标记 |
| **Markers** | 多点标记（批量渲染） |

### 3.11 标注/文字 (6个)

| Plottable | 用途 |
|---|---|
| **Annotation** | 文本注释（自动背景+边框） |
| **Text** | 纯文本 |
| **Crosshair** | 十字光标 |
| **Tooltip** | 悬浮提示框 |
| **Callout** | 标注箭头+文本框 |
| **Benchmark** | 性能信息显示 |

### 3.12 实时数据 (3个)

| Plottable | 数据源 | 特性 |
|---|---|---|
| **DataLogger** | `DataLoggerSource` | 追加模式，自动跟踪Y范围 |
| **DataStreamer** | `DataStreamerSource` | 环形缓冲，固定窗口 |
| **DataStreamerXY** | — | 环形缓冲+XY独立 |

`DataLogger` 实现 `IManagesAxisLimits`，在渲染前自动更新轴范围。

### 3.13 交互工具 (11个 + 2个装饰器)

```
Interactive/
├── InteractiveMarker          ← 拖拽标记
├── InteractiveLineSegment      ← 拖拽线段
├── InteractiveVerticalLine     ← 拖拽垂直线
├── InteractiveHorizontalLine   ← 拖拽水平线
├── InteractiveVerticalSpan     ← 拖拽垂直区域
├── InteractiveHorizontalSpan   ← 拖拽水平区域
├── InteractiveTrendLine        ← 拖拽趋势线
├── InteractiveRectangle        ← 拖拽矩形选框
├── InteractiveVerticalLineSegment   ← 可调垂直线段
├── InteractiveHorizontalLineSegment ← 可调水平线段
└── ZoomRectangle              ← 缩放矩形

装饰器 (Wrappers):
├── DraggablePlottableDecorator ← 使任意 Plottable 可拖拽
└── HittablePlottableDecorator  ← 使任意 Plottable 可点击检测
```

---

## 四、Plottable 实现的核心接口一览

```
IPlottable        → 必须实现: IsVisible, Axes, GetAxisLimits(), Render(), LegendItems
IHasLine          → LineStyle, LineWidth, LineColor, LinePattern
IHasMarker        → MarkerStyle, MarkerShape, MarkerSize, MarkerFillColor, MarkerLineColor
IHasFill          → FillStyle, FillColor, FillHatchColor, FillHatch
IHasLegendText    → LegendText
IHasArrow         → ArrowStyle
IHasLabel         → LabelStyle
IHasOutline       → OutlineStyle
IHasShadow        → Shadow color/offset
IHasBackground    → Background color
IHasColorAxis     → Color axis (热力图等)
IHasInteractiveHandles → 交互句柄
IGetNearest       → GetNearest() 最近点查询
IManagesAxisLimits→ UpdateAxisLimits() 自动轴范围
IRenderLast       → RenderLast() 最后渲染（覆盖在坐标轴上）
IPlottableGL      → GPU 渲染 (Candlestick等)
```

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

3. **GUI 线程安全的分离**：Plottable 的 `Render()` 方法在渲染管道中被调用（第14步），此时所有数据处理在线程安全的上下文中完成。交互拖拽（`Interactive*` 系列）在 UI 线程中修改数据，然后触发 `Refresh()`。

4. **装饰器模式增强功能**：`DraggablePlottableDecorator` 和 `HittablePlottableDecorator` 可以包裹任何 `IPlottable`，动态添加拖拽或点击检测能力。这是开闭原则的实践。

5. **IRenderLast 控制 Z 序**：默认所有 Plottable 在第14步 `RenderPlottables` 中绘制，实现了 `IRenderLast` 的 Plottable 在第16步 `RenderPlottablesLast` 中绘制，确保它们出现在最上层（如缩放矩形、十字光标、标注）。

6. **FinancialTimeAxis 的巧妙设计**：不是一个独立的轴类型，而是一个特殊 Plottable，在渲染时介入 `AxisManager` 的行为，实现"跳过非交易时段"的 X 轴显示。

7. **SignalConst 的极简化**：当知道所有 Y 值相同时，不需要逐点计算，只需要一个点——这是性能优化的极限案例。