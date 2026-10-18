# ScottPlot 5 全数据链路总览

> 本文是 5 条核心链路的**鸟瞰图**。各链路的深度剖析见对应分层文档（02-07），本文不重复其内容。

---

## 总览

ScottPlot 5 的数据流可归纳为 **5 条核心链路**，覆盖从"用户写入数据"到"屏幕绘制像素"再到"文件导出"的完整过程。

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     ScottPlot 5 数据流全景图                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  链路①: 数据源链路                                                        │
│  [用户数据] → [IXXXSource] → [坐标轴推算] → [IPlottable.Axes]             │
│                                                                         │
│  链路②: Plottable 构造与样式链路                                           │
│  [Plot.Add.XXX()] → [PlottableAdder] → [new Plottable(data)] → [Plot.PlottableList.Add()] │
│                                                                         │
│  链路③: 渲染管道 (Render Pipeline)                                        │
│  [RenderManager.Render()] → 25 步 RenderAction 管道 → [SkiaSharp Canvas] │
│                                                                         │
│  链路④: GUI 交互链路 (WinForms/WPF/Avalonia/Blazor/...)                   │
│  [鼠标/键盘事件] → [UserInputProcessor] → [IUserActionResponse[]] → [Plot.Modify → Refresh] │
│                                                                         │
│  链路⑤: 静态导出链路                                                       │
│  [Plot.GetImage()] → [RenderManager.Render()] → [SkiaSharp.SKImage] → [.SavePng()] │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 链路①：数据源链路 (Data → Source → Render)

### 1.1 两种核心数据源架构

| 数据源类型 | 接口 | 适用场景 | 优化策略 |
|---|---|---|---|
| **离散点** | `IScatterSource` | 散点图、非等间距数据 | 全量渲染 |
| **等间距信号** | `ISignalSource` | 大数据量、等间距采样 | SegmentedTree 降采样 |

### 1.2 核心链路主干

```
Scatter 路径 (离散):
用户数据 (double[] xs, ys)
  → PlottableAdder.Scatter() 自动包装为 ScatterSourceDoubleArray
      （并自动包裹 CacheScatterLimitsDecorator 缓存 Limits）
  → Scatter.Render(rp)
      ① Data.GetScatterPoints() → Coordinates[]（ZipView 惰性视图，零拷贝）
      ② Axes.GetPixel() → 坐标→像素转换
      ③ PathStrategy (Straight/CubicSpline) 生成 SKPath → 绘制
      ④ 逐个绘制 Marker

Signal 路径 (等间距大数据):
用户数据 (double[] ys, samplePeriod)
  → PlottableAdder.Signal() 包装为 SignalSourceDouble
  → Signal.Render(rp)
      ① Data.GetPixelColumns() → 每像素列查 SegmentedTree 得 min/max
      ② 每像素列画一条竖线 (min→max) + 一个点 (均值)
  → 大数据关键：百万点 → N 像素宽 → 只绘 N*2 个图形元素
```

> SegmentedTree 的树结构、O(log n) 查询算法与性能公式：见 [05-datasources](./05-datasources.md)。

### 1.3 其他数据源一览

| 数据源接口 | 对应 Plottable | 用途 |
|---|---|---|
| `IScatterSource` | Scatter | XY 散点图 |
| `ISignalSource` | Signal | 等间距大数据 |
| `ISignalXYSource` | SignalXY | 不等间距大数据 |
| `IOHLCSource` | OHLC / Candlestick | K线图 |
| `IErrorBarSource` | ErrorBar | 误差棒 |
| `IVectorSource` | VectorField | 矢量场 |
| `IFunctionSource` | FunctionPlot | 函数绘图 |
| `IHeatmapSeries` | Heatmap | 热力图数据 |

> 数据源选型决策树与实现矩阵：见 [05-datasources](./05-datasources.md)。

---

## 链路②：Plottable 构造与样式链路

```
用户代码                         ScottPlot 内部
──────────────────────────────────────────────────
Plot myPlot = new();         →  创建 Plot 对象
  ├─ PlottableAdder Add      →  工厂方法集合（~60 个 Add.XXX()）
  ├─ PlottableList           →  List<IPlottable>
  ├─ AxisManager Axes        →  5 轴管理
  ├─ RenderManager           →  25 步渲染管道
  └─ Legend                  →  图例

myPlot.Add.Scatter(xs, ys);  →  包装数据源 → 自动取色 → 加入 PlottableList → 返回对象
scatter.LineWidth = 3;       →  属性转发，直接改 LineStyle.Width（无需重建）
```

- `IPlottable` 最小契约：`IsVisible` + `Axes` + `GetAxisLimits()` + `Render()` + `LegendItems`
- 样式能力通过 `IHasLine` / `IHasMarker` / `IHasFill` 等 Mixin 接口按需组合

> 样式系统、Mixin 体系与属性转发细节：见 [04-primitives](./04-primitives.md)。
> 全部 Plottable 分类与统一模板：见 [06-plottables](./06-plottables.md)。

---

## 链路③：渲染管道 (Render Pipeline)

### 3.1 触发方式

```
① 显式调用: plot.Render(canvas)   ← 手动渲染到 SKCanvas
② 自动触发: plot.Refresh()        ← PlotControl 自动管理
③ 数据更新: scatter.DataChanged   ← 标记脏状态后下一次 Refresh
④ 事件触发: RenderFinished 事件   ← 订阅者响应
⑤ 静态导出: plot.SavePng()        ← 内部 Build→Render→Encode
```

### 3.2 25 步管道关键步骤（摘录）

完整 25 步序列、RenderPack 结构与每步源码剖析：见 [07-rendering](./07-rendering.md)。

```
 4  AutoScaleUnsetAxes        ★ 未手动设置范围的轴 → 自动计算（HasBeenSet 标志）
 8  CalculateLayout           ★ 测量所有面板 → 计算 Figure/Data 布局矩形
11  RegenerateTicks           ★ 根据布局后 DataRect 尺寸重新生成刻度
17  RenderPlottables          ★★★ 裁剪 + 遍历绘制所有可见 IPlottable
24  RenderPlottablesLast      ★ 绘制 IRenderLast Plottable（覆盖在轴上方）
```

**隔离原则**：每个 RenderAction 前后自动 `CanvasState.Save()` / `RestoreAll()`，各步骤绘制状态互不影响（详见 05）。

### 3.3 Plottable.Render() 内部坐标转换

```
IPlottable.Render(RenderPack rp)
  ├── ① 获取数据（可能涉及降采样）
  ├── ② 坐标转换: plottable.Axes.GetPixel(coord)
  │     └─ IXAxis/IYAxis 内部维护 (CoordRange → PixelRange) 线性映射
  ├── ③ 裁剪: 只绘制 rp.DataRect 范围内的对象
  └── ④ 绘制到 Canvas: rp.Canvas.DrawLine/Paint/Path/Circle/Text...
```

---

## 链路④：GUI 交互链路

```
鼠标/键盘事件（平台控件捕获）
  → UserInputProcessor.ProcessXXX()     ← 平台事件封装为 IUserAction
  → 遍历 UserActionResponses[] 责任链    ← 第一个匹配者独占（IsPrimary）
  → 修改 Plot 状态（如 Axes.Pan / SetLimits）
  → PlotControl.Refresh()               ← 触发 25 步渲染管道
```

> 交互全流程（以 MouseDragPan 为例）、默认响应器优先级与自定义方法：
> 见 [08-interactivity](./08-interactivity.md)。
> 8 套平台控件的实现对比与 IPlotControl 抽象：见 [09-controls](./09-controls.md)。

---

## 链路⑤：静态导出链路

```
plot.SavePng("chart.png", 800, 600)
  │
  ├── ② Plot.GetImage(800, 600)
  │     ├─ new SKSurface(800, 600)
  │     ├─ RenderManager.Render(surface.Canvas, PixelRect(0,0,800,600))
  │     └─ 返回 SKImage
  │
  ├── ③ 编码输出: image.Encode(SKEncodedImageFormat.Png, quality) → byte[]
  └── ④ 写入文件: File.WriteAllBytes("chart.png", bytes)
```

支持的导出格式（全部走 `GetImage → Render → Encode` 同一条路）：
`SavePng() SaveJpeg() SaveBmp() SaveWebp() SaveSvg() GetImageBytes()`

---

## 关键数据结构速查

| 结构 | 命名空间 | 作用 |
|---|---|---|
| `Plot` | ScottPlot | 顶级入口，持有所有子组件 |
| `PlottableAdder.Add` | ScottPlot | 工厂方法集合 |
| `IPlottable` | ScottPlot | 所有图表类型的基接口 |
| `IScatterSource` | ScottPlot | XY 离散数据源 |
| `ISignalSource` | ScottPlot | 等间距大数据源 |
| `RenderManager` | ScottPlot.Rendering | 25 步渲染管道调度 |
| `RenderPack` | ScottPlot | 单次渲染的上下文数据包 |
| `IRenderAction` | ScottPlot.Rendering | 渲染步骤接口 |
| `UserInputProcessor` | ScottPlot.Interactivity | 统一输入事件处理 |
| `IPlotControl` | ScottPlot | 跨平台控件抽象 |
| `Coordinates` | ScottPlot | XY 坐标值 (double) |
| `Pixel` | ScottPlot | 屏幕像素值 (float) |
| `AxisLimits` | ScottPlot | 轴范围 (Left,Right,Bottom,Top) |
| `PixelRect` | ScottPlot | 像素矩形区域 |
| `SKCanvas` | SkiaSharp | 底层绘图画布 |

---

## 渲染性能关键点

```
性能瓶颈      优化策略                 关键代码位置
────────────────────────────────────────────────────
大数据散点    Signal 替代 Scatter       ISignalSource + SegmentedTree
大量 Marker   逐个渲染 → 批量渲染       Scatter.Render() 中的 Marker 循环
多图元        视口裁剪                  rp.DataRect.Contains(pixel)
实时更新      DataLogger/DataStreamer   Plottables/DataLogger.cs
OpenGL 加速   IPlottableGL + 自定义     GL 相关 RenderActions
多轴图        AxisManager              Plot.Axes (5轴: Bottom/Top/Left/Right/Color)
```
