# ScottPlot 5 全数据链路梳理

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

### 1.2 IScatterSource 详细链路

```
用户数据 (double[] xs, double[] ys, List<Coordinates>...)
    │
    ▼
ScatterSourceDoubleArray / ScatterSourceCoordinates / ScatterSourceGenericArray<T>
    │ 实现 IScatterSource: GetScatterPoints(), GetNearest(), GetLimitsX(), GetLimitsY()
    │
    ▼
Scatter(dataSource) 构造函数 ← PlottableAdder.Scatter(xs, ys)
    │ 构造函数自动将 double[] xs/ys 包装成 ScatterSourceDoubleArray
    │
    ▼
Scatter.Render(RenderPack rp)
    │ ① 读取 Data.GetScatterPoints() → Coordinates[]
    │ ② Coordinates[] 通过 rp.Axes 转换为 Pixel[]  ← 坐标系→像素坐标
    │ ③ PathStrategy (Straight / CubicSpline) 生成 SKPath
    │ ④ Canvas.DrawPath() 绘制线条
    │ ⑤ 逐个绘制 Marker (if MarkerShape != None)
    │
    ▼
SkiaSharp Canvas (像素输出)
```

### 1.3 ISignalSource 详细链路（高性能大数据路径）

```
用户数据 (double[] ys, double samplePeriod, double xOffset)
    │
    ▼
SignalSourceDoubleArray / SignalSourceGenericArray<T>
    │ 实现 ISignalSource: GetYs(), GetPixelsToRender(), Period, XOffset, YOffset, YScale
    │
    ▼
Signal(signalSource) 构造函数 ← PlottableAdder.Signal(ys, period)
    │
    ▼
Signal.Render(RenderPack rp)
    │ ① 调用 Data.GetPixelColumns()  → SignalMinMaxInt32[] (降采样后的 Y 范围)
    │     └─ 内部使用 SegmentedTree → O(log n) 区间 min/max 查询
    │ ② 每个像素列绘制一个"竖线"(min→max)，形成填充区域
    │ ③ 每个像素列绘制一个"点"(均值)，形成走势线
    │
    ▼
大数据优化关键：百万级数据 → N个像素宽 → 只需绘制 N*2 个点
```

### 1.4 SegmentedTree 降采样原理

```
原始数据: [y0, y1, y2, y3, y4, y5, ..., y_n]
                    ↓ 构建分段树
              ┌── Root[min,max] ──┐
          ┌─ Left[min,max]    Right[min,max] ─┐
        ...                               ...
                    ↓ 查询区间 [start, end]
            O(log n) 获得该区间的 min/max
                    ↓
        渲染时: 屏幕宽度 800px → 800 个区间查询
        每个区间 O(log n) → 总复杂度 O(w * log n)
        对比全量 O(n): n=1,000,000 时, 800*log(1M) ≈ 800*20 = 16,000 << 1,000,000
```

### 1.5 其他数据源一览

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

---

## 链路②：Plottable 构造与样式链路

### 2.1 完整流程

```
用户代码                         ScottPlot 内部
──────────────────────────────────────────────────
Plot myPlot = new();         →  创建 Plot 对象
  ├─ PlottableAdder Add      →  new PlottableAdder(this)
  ├─ PlotPlottableManager
  │   PlottableList          →  List<IPlottable>
  ├─ IAxisManager Axes       →  AxisManager (5 轴)
  ├─ RenderManager           →  RenderManager (25 步)
  └─ Legend                  →  Legend

myPlot.Add.Scatter(xs, ys);  →  PlottableAdder.Scatter()
  │ ① double[] xs/ys → new ScatterSourceDoubleArray(xs, ys)
  │ ② 获取下一个自动颜色 (Palette.GetNextColor)
  │ ③ new Scatter(dataSource) { Color = autoColor }
  │ ④ Plot.PlottableList.Add(scatter)
  │ ⑤ 返回 Scatter 对象给用户
  │
  ▼
scatter.LineWidth = 3;       →  用户继续定制样式 (链式)
scatter.MarkerSize = 10;     →  修改 Plottable 的属性
scatter.Color = Colors.Red;  →  无需重建数据源
```

### 2.2 PlottableAdder 工厂方法汇总

```
PlottableAdder
├── Scatter(xs, ys)           → new Scatter(source)
├── Signal(ys, period)        → new Signal(source)
├── SignalXY(xs, ys)          → new SignalXY(source)
├── Bar(bars)                 → new BarPlot(bars)
├── Pie(slices)               → new PiePlot(slices)
├── BoxPlot(boxes)            → new Box(boxes)
├── Heatmap(data)             → new Heatmap(source)
├── Candlestick(ohlcs)        → new Candlestick(ohlcs)
├── OHLC(ohlcs)               → new Ohlc(ohlcs)
├── ErrorBar(xs, ys, err)    → new ErrorBar(source)
├── VectorField(vectors)      → new VectorField(source)
├── Text(text, x, y)          → new Text
├── Line(x1,y1, x2,y2)        → new LinePlot
├── Ellipse(x,y,rx,ry)        → new Ellipse
├── Arrow(...)                → new Arrow
├── Marker(x,y)               → new Marker
├── Callout(text, x, y)       → new Callout
├── Image(image, rect)        → new ImageMap
├── Polygon(coords)           → new Polygon
├── Radar(values)             → new Radar
├── SmithChart()              → new SmithChart
├── DataLogger()              → new DataLogger (实时追加)
├── DataStreamer()            → new DataStreamer (实时滚动)
├── AxisLine(y) / VerticalLine(x) / HorizontalLine(y)
├── Crosshair(x, y)           → new Crosshair
├── Annotation(text)          → new Annotation
├── AnimatedArrows()          → new AnimatedArrows
└── ... 40+
```

### 2.3 样式属性体系

```
IPlottable (基接口)
├── bool IsVisible
├── IAxes Axes                 ← 绑定坐标系
├── IEnumerable<LegendItem> LegendItems
├── AxisLimits GetAxisLimits()
└── void Render(RenderPack rp)

附加样式接口 (mixin pattern)
├── IHasLine       → LineStyle { Width, Pattern, Color }
├── IHasMarker     → MarkerStyle { Shape, Size, FillColor, LineColor }
├── IHasFill       → FillStyle { Color, Hatch Pattern }
├── IHasLabel      → Label { Text, Style, Rotation }
├── IHasLegendText → LegendText
├── IHasArrow      → ArrowStyle
├── IHasColorAxis  → 颜色映射轴
└── IDataSource    → MinRenderIndex, MaxRenderIndex
```

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

### 3.2 25 步渲染序列 (RenderManager.RenderActions)

```
步骤 | RenderAction                        | 核心职责
────┼────────────────────────────────────┼──────────────────────────────────
 1  │ PreRenderLock                       │ 触发 PreRenderLock 事件(用户可加锁/同步)
 2  │ ClearCanvas                         │ 清空画布 (含半透明背景补偿)
 3  │ ReplaceNullAxesWithDefaults         │ 未绑定轴的 Plottable → 默认轴
 4  │ AutoScaleUnsetAxes                  │ ★ 未手动设置范围的轴 → 自动计算
 5  │ ContinuouslyAutoscale               │ 连续自动缩放 (条件性, 仅当 ContinuousAutoscale=true)
 6  │ ExecutePlottableAxisManagers        │ DataLogger 等 IManagesAxisLimits Plottable 管理轴
 7  │ ApplyAxisRulesBeforeLayout          │ 布局前应用轴规则 (如最小范围约束)
 8  │ CalculateLayout                     │ ★ 测量所有面板 → 计算 Figure/Data 布局矩形
 9  │ RenderFigureBackground              │ 绘制图表背景 (Figure 区域)
10  │ ApplyAxisRulesAfterLayout           │ 布局后应用轴规则 (如锁定纵横比)
11  │ RegenerateTicks                     │ ★ 根据布局后 DataRect 尺寸重新生成所有轴的刻度
12  │ RenderStartingEvent                 │ 触发 RenderStarting 事件
13  │ RenderDataBackground                │ 绘制数据区背景 (Data 区域)
14  │ StoreGLState                        │ 备份 OpenGL 状态 (GL混用 Bug 修复)
15  │ RenderGridsBelowPlottables          │ 绘制下层网格线 (在数据之下)
16  │ RestoreGLState                      │ 恢复 OpenGL 状态
17  │ RenderPlottables                    │ ★★★ 核心：裁剪+遍历绘制所有可见 IPlottable
18  │ RenderGridsAbovePlottables          │ 绘制上层网格线 (在数据之上)
19  │ RenderLegends                       │ 绘制图例
20  │ RenderPanels                        │ 绘制面板 (轴标签、标题、刻度等)
21  │ RenderBorders                       │ 绘制图表边框
22  │ RenderZoomRectangle                 │ 绘制中键拖拽缩放矩形
23  │ SyncGLPlottables                    │ 同步 GPU Plottable 渲染
24  │ RenderPlottablesLast                │ ★ 绘制 IRenderLast Plottable (覆盖在轴上方)
25  │ RenderBenchmark                     │ 绘制右上角性能基准信息
```

**关键：每次 RenderOnce() 中 CanvasState 自动 Save/RestoreAll 隔离各步骤**

```csharp
foreach (IRenderAction action in RenderActions)
{
    rp.CanvasState.Save();      // 保存画布状态
    action.Render(rp);          // 执行该步骤
    rp.CanvasState.RestoreAll(); // 恢复到初始状态
    record(action.GetType().Name, elapsed);
}
```

### 3.3 RenderPack — 渲染上下文数据包

```
RenderPack (每次 RenderOnce() 创建, using 释放)
├── Plot Plot              ← 回到 Plot 引用, 可访问所有 Plottable
├── SKCanvas Canvas        ← SkiaSharp 绘图画布
├── CanvasState CanvasState ← 画布状态机 (Save/Restore/Clip/Translate)
├── Paint Paint            ← 可复用的 SKPaint (Dispose 时释放)
├── PixelRect FigureRect   ← 图表总区域 (Figure)
├── PixelRect ScaledFigureRect ← 缩放后的图表区域
├── PixelRect DataRect     ← 数据区域 (CalculateLayout 后填充)
├── Layout Layout          ← 布局结果 (各面板尺寸)
└── TimeSpan Elapsed       ← 自 RenderPack 创建以来的耗时
```

### 3.4 Plottable.Render() 内部坐标转换

```
IPlottable.Render(RenderPack rp)
  │
  ├── ① 获取数据 (可能涉及降采样)
  │     Data.GetScatterPoints() → Coordinates[]
  │
  ├── ② 坐标转换 (Coordinates → Pixel)
  │     plottable.Axes.GetPixel(coord)     ← Axes 持有 DataRect
  │     └─ IXAxis/IYAxis 内部维护: (CoordRange → PixelRange) 线性映射
  │
  ├── ③ 裁剪
  │     只绘制 rp.DataRect 范围内的对象 (性能优化)
  │     利用 rp.DataRect.Contains(pixel) 判断可见性
  │
  └── ④ 绘制到 Canvas
        rp.Canvas.DrawLine/Paint/Path/Circle/Text...
```

---

## 链路④：GUI 交互链路

### 4.1 WinForms 交互全路径

```
用户操作                     WinForms 控件                    ScottPlot 内部
──────────────────────────────────────────────────────────────────────────────
鼠标左键按下 (x,y)
  → FormsPlot.OnMouseDown()
      → UserInputProcessor.ProcessMouseDown(x, y)
          │
          ├── 遍历 UserActionResponses (响应器列表)
          │   ├── MouseDragPan.Process()   ← 检查是否匹配拖拽条件
          │   ├── MouseDragZoom.Process()
          │   ├── MouseWheelZoom.Process()
          │   ├── SingleClickContext.Process()
          │   ├── DoubleClickBenchmark.Process()
          │   └── ...
          │
          ├── 匹配到 MouseDragPan:
          │   ① 记录起始位置 _startMouse
          │   ② 标记状态为 Dragging (不触发 Render)
          │
          ▼
鼠标移动 (dx, dy)
  → MouseDragPan.Respond() 持续更新
      │ ① 计算 Δx, Δy (像素位移)
      │ ② 转换为坐标位移: Δcoord = Δpixel * (coordRange / pixelRange)
      │ ③ Plot.Axes.SetLimits(newLimits) ← 修改轴范围
      │ ③ PlotControl.Refresh()           ← 触发重新渲染
      │     └→ RenderManager.Render() → 25步管道 → 新图像
      │
      ▼
鼠标弹起
  → MouseDragPan.ProcessCompleted()
      │ ① 拖拽结束，最终确认轴范围
      │ ② 触发 AxisLimitsChanged 事件
      │ ③ PlotControl.Refresh()
```

### 4.2 IPlotControl 跨平台抽象

```
IPlotControl (接口)
├── Plot Plot                    ← 核心 Plot 对象
├── IMultiplot Multiplot         ← 多子图
├── void Refresh()               ← 触发布局+渲染
├── UserInputProcessor           ← 统一输入处理
├── IPlotMenu Menu               ← 右键菜单
├── GRContext (OpenGL)           ← 硬件加速上下文
│
├─ WinForms: FormsPlot            (ScottPlot.WinForms)
├─ WPF:     WpfPlot              (ScottPlot.WPF)
├─ Avalonia: AvaPlot              (ScottPlot.Avalonia)
├─ MAUI:    MauiPlot             (ScottPlot.Maui)
├─ Blazor:  BlazorPlot           (ScottPlot.Blazor)
├─ WinUI:   WinUIPlot            (ScottPlot.WinUI)
├─ Eto:     EtoPlot              (ScottPlot.Eto)
└─ OpenGL:  FormsPlotGL          (ScottPlot.OpenGL)

每个控件内部模式相同:
  控件构造函数 → 创建 Plot → 创建 RenderManager → 注册 UserInputProcessor
  控件 OnPaint  → PlotControl.Refresh() → RenderManager.Render(SKCanvas)
```

---

## 链路⑤：静态导出链路

```
plot.SavePng("chart.png", 800, 600)
  │
  ├── ① 确定尺寸
  │     width=800, height=600
  │
  ├── ② Plot.GetImage(800, 600)
  │     ├─ new SKSurface(800, 600)
  │     ├─ RenderManager.Render(surface.Canvas, PixelRect(0,0,800,600))
  │     └─ 返回 SKImage
  │
  ├── ③ 编码输出
  │     image.Encode(SKEncodedImageFormat.Png, quality)
  │        → byte[]
  │
  └── ④ 写入文件
        File.WriteAllBytes("chart.png", bytes)
```

支持的导出格式 (通过 GetImage + SKImage.Encode):
```
SavePng()  SaveJpeg()  SaveBmp()  SaveWebp()  SaveSvg()  GetImageBytes()
└── 全部走 Plot.GetImage() → RenderManager.Render() → encode
```

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
| `Coordinates` | ScottPlot | XY 坐标值 |
| `Pixel` | ScottPlot | 屏幕像素值 |
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