# ScottPlot 5 项目结构导航

> 以 `src/ScottPlot5/` 为根目录 · 源码地图 · 2026-10-18

---

## 一、解决方案全景

```
src/ScottPlot5/
│
├── ScottPlot5/                     ← 🔷 核心库（NuGet: ScottPlot）
├── ScottPlot5 Controls/            ← 🔶 跨平台控件（8 个 NuGet 包）
├── ScottPlot5 Cookbook/            ← 📖 示例代码生成器 → scottplot.net
├── ScottPlot5 Demos/               ← 🎮 4 套演示程序
├── ScottPlot5 Tests/               ← 🧪 测试项目
├── ScottPlot5 Benchmarks/          ← ⏱  BenchmarkDotNet 性能测试
├── .editorconfig
└── Key.snk                         ← 强名称签名密钥
```

---

## 二、核心库 `ScottPlot5/` 内部结构

### 2.1 根目录（API 入口层）

```
ScottPlot5/
├── Plot.cs                         ← 用户主入口：new Plot() / Add / SavePng / Render
├── PlottableAdder.cs               ← Plot.Add.Scatter() 等 ~60 个工厂方法
├── RenderPack.cs                   ← 单次渲染上下文：CanvasState, Layout, Paint, Elapsed
├── AxisManager.cs                  ← 多轴管理器：Add/Remove/Find/AutoScale
├── LayoutManager.cs                ← 布局计算：DataRect vs PanelRect
├── Multiplot.cs                    ← 多图容器：new Multiplot(plot)
├── MultiplotSharedAxisManager.cs   ← 多图共享轴
├── Drawing.cs                      ← SkiaSharp 封装：DrawLines, DrawMarkers, DrawText
├── Generate.cs                     ← 样本数据生成器
├── Fonts.cs                        ← 字体检测/回退/管理
├── FontExtensions.cs               ← 字体扩展方法
├── ImageOperations.cs              ← 图像操作：Resize/Crop/Rotate
├── DataOperations.cs               ← 数据操作：ResizeHalf/Convolve
├── DataSourceUtilities.cs          ← 数据源辅助工具
├── BinarySearchComparer.cs         ← 双精度二分查找
├── GenericComparer.cs              ← 泛型比较器
├── NumericConversion.cs            ← 数值类型转换
├── RandomDataGenerator.cs          ← 随机数据生成（测试用）
├── SampleData.cs                   ← 固定样本数据
├── SampleImages.cs                 ← 内嵌示例图片
├── Version.cs / Usings.cs          ← 版本号 / 全局 using
├── ScottPlot.csproj                ← 项目文件（net462, netstandard2.0, net8/9/10）
├── autoformat.bat / nuget-readme.md
```

### 2.2 目录分类一览

```
ScottPlot5/
├── Primitives/             109  ← Layer 2: 原子数据结构
├── Interfaces/             ~60  ← Layer 2: 核心接口
├── DataSources/             28  ← Layer 3: 数据源实现
├── Plottables/              61  ← Layer 4: 可绘制物
│   └── Interactive/         11  ← 可拖拽交互元素
├── Rendering/                1  ← Layer 5: 渲染入口
│   └── RenderActions/       25  ← 每步一个独立文件
├── Interactivity/           ~25  ← Layer 6: 交互系统
├── TickGenerators/          15  ← 刻度生成
├── LayoutEngines/            5  ← 布局引擎
├── AxisPanels/              12  ← 轴面板
├── AxisRules/               16  ← 轴约束规则
├── AxisLimitManagers/        3  ← 实时轴范围管理
├── AutoScalers/              1  ← 自动缩放策略
├── Panels/                   4  ← 图表面板（标题/图例/ColorBar）
├── Grids/                    1  ← 网格线
├── Markers/                 26  ← 26 种标记形状
├── ArrowShapes/              7  ← 箭头形状
├── Colormaps/               35  ← 科学配色方案
├── Palettes/                26  ← 分类调色板
├── PathStrategies/           4  ← 连线策略（直线/样条/阶梯）
├── Statistics/               6  ← 统计计算
├── Finance/                  2  ← 金融指标
├── Hatches/                  5  ← 图案填充
├── DataGenerators/           3  ← 实时数据生成
├── DataViews/                3  ← 数据流视图
├── FontResolvers/            2  ← 字体解析
├── Collections/              1  ← CircularBuffer
├── CompilerServices/         2  ← 编译时工具
├── MultiplotLayouts/         2  ← 多图布局
├── LegendLayouts/            1  ← 图例排版
├── IO/                       1  ← I/O 辅助
└── LegendLayouts/            1  ← 图例排版
```

---

## 三、核心目录逐个详解

### 3.1 `Primitives/` — 原子数据结构 (109 files)

> 详细参考：`learning/02-primitives/primitives-architecture.md`

所有上层组件的共享基础，分为以下子类别：

```
Primitives/
├── 坐标与几何 (15)   Coordinates, Pixel, CoordinateRect, PixelRect,
│                     CoordinateLine, PixelLine, CoordinateRange, Angle, ...
├── 样式系统 (18)     LineStyle, FillStyle, MarkerStyle, FontStyle,
│                     BackgroundStyle, GridStyle, LabelStyle, TickMarkStyle,
│                     ArrowStyle, Gradient, ConnectStyle, ...
├── 颜色系统 (2+70)   Color, Colors（静态工厂，数千命名颜色）
├── 轴与范围 (12)     Axes, AxisLimits, ExpandingAxisLimits, AxisLimits3d, ...
├── 图例 (4)          Legend, LegendItem, LegendLayout
├── 布局 (6)          Layout, PixelPadding, FractionRect, Alignment, ...
├── 数据承载 (6)      Bar, OHLC, PieSlice, Box, Population, Range
├── 交互 (3)          ContextMenuItem, Cursor, InteractiveHandle
└── 其他 (20+)        Platform, RenderDetails, SvgImage, CanvasState, ...
```

| 关键类型 | 作用 |
|---------|------|
| `Coordinates` | 数据空间中的点（double X, double Y） |
| `Pixel` | 屏幕空间中的点（float X, float Y） |
| `CoordinateRect` | 数据空间矩形 → `ExpandingAxisLimits.Expand()` |
| `PixelRect` | 屏幕空间矩形 → `Contains()` 剪裁判断 |
| `Axes` | 坐标转换枢纽：`GetPixel(coord)` / `GetCoordinate(pixel)` |
| `Color` | `readonly struct`，`WithAlpha()` 返回新值 |
| `LineStyle` | 线型+颜色+宽度+图案+抗锯齿 |
| `FillStyle` | 填充色+图案填充+抗锯齿 |
| `AxisLimits` / `ExpandingAxisLimits` | 范围计算，后者只增不减 |

### 3.2 `Interfaces/` — 核心接口 (~60 files)

系统的可扩展点——每个接口代表一个策略模式插入位置：

```
Interfaces/
├── IPlottable.cs              ← 所有图表的统一契约
├── IRenderAction.cs           ← 渲染管道步骤
├── IRenderLast.cs             ← 覆盖层渲染（标注/Tooltip）
├── IPlottableGL.cs            ← OpenGL 加速 Plottable
├── IScatterSource.cs          ← 离散 XY 数据源
├── ISignalSource.cs           ← 等间距信号源
├── ISignalXYSource.cs         ← XY 信号源
├── IOHLCSource.cs             ← K 线数据源
├── IVectorFieldSource.cs      ← 向量场数据源
├── IAxes.cs / IAxis.cs        ← 轴接口
├── IGrid.cs                   ← 网格接口
├── IPanel.cs                  ← 面板接口
├── IPlotControl.cs            ← 跨平台控件统一接口
├── IPlotMenu.cs               ← 右键菜单接口
├── IMultiplot.cs              ← 多图接口
├── IHasLine/IHasMarker/IHasFill/...  ← 样式 Mixin 接口
├── IColormap.cs / IPalette.cs ← 颜色映射/调色板
├── IHatch.cs                  ← 图案填充
├── IArrowShape.cs             ← 箭头形状
├── IPathStrategy.cs           ← 连线策略
├── ITickGenerator.cs          ← 刻度生成器
├── IAxisRule.cs               ← 轴约束规则
├── ILayoutEngine.cs           ← 布局引擎
├── IFontResolver.cs           ← 字体解析器
└── ...
```

### 3.3 `DataSources/` — 数据源 (28 files)

> 详细参考：`learning/03-datasources/datasources-architecture.md`

```
DataSources/
├── IScatterSource 实现 (7)
│   ScatterSourceDoubleArray, ScatterSourceCoordinatesArray,
│   ScatterSourceGenericArray/List, ScatterSourceWithCachedLimits, ...
├── ISignalSource 实现 (9)
│   SignalSourceDouble, SignalSourceGenericArray/List,
│   SignalConstSource, FastSignalSourceDouble, SignalInterpolation, ...
├── ISignalXYSource 实现 (3)
│   SignalXYSourceDoubleArray, SignalXYSourceGenericArray/List
├── IOHLCSource 实现 (3)
│   OHLCSourceArray/List, OHLCSourceBase
├── 实时数据 (2)
│   DataLoggerSource, DataStreamerSource
├── 优化引擎 (3)
│   SegmentedTree ← O(log n) 区间 MinMax 查询，大数据降采样核心
│   MinMaxCache   ← 缓存区间查询结果
│   ScatterSourceWithCachedLimits ← 缓存 Limits 的装饰器
└── 其他 (3)
    FunctionSource, CoordinateDataSource, VectorFieldDataSourceCoordinatesList
```

| 关键区别 | ScatterSource | SignalSource |
|---------|--------------|--------------|
| X 值 | 任意离散 | 等间距（sampleRate） |
| 大数据性能 | 全量渲染 | SegmentedTree 降采样 |
| 实时追加 | 不支持 | DataLoggerSource |

### 3.4 `Plottables/` — 可绘制物 (61 + 11 交互元素)

> 详细参考：`learning/04-plottables/plottables-architecture.md`

```
Plottables/
├── 散点/信号 (6)   Scatter, Signal, SignalXY, SignalConst, LinePlot, Markers
├── 柱状/条形 (3)   BarPlot, LollipopPlot, Bracket
├── 金融图表 (3)    CandlestickPlot, OHLCPlot, FinancialTimeAxis
├── 热力/等值 (4)   Heatmap, IsoLines, ContourLines, TINPlot
├── 饼图/径向 (4)   Pie, PieBase, Coxcomb, RadialGaugePlot
├── 极坐标/雷达 (4) PolarAxis, Radar, SmithChartAxis, Phasor
├── 统计图表 (3)    BoxPlot, HistogramBars, PopulationSymbol
├── 直线/跨度 (7)   VerticalLine, HorizontalLine, VerticalSpan,
│                    HorizontalSpan, AxisLine, AxisSpan, FloatingAxis
├── 形状图形 (5)    Rectangle, Ellipse, Polygon, ImageRect, ImageMarker
├── 标注/文字 (3)   Text, Annotation, Callout
├── 实时数据 (3)    DataLogger, DataStreamer, DataStreamerXY
├── 箭头/矢量 (3)   Arrow, VectorField, ErrorBar
├── 工具/辅助 (5)   Benchmark, ZoomRectangle, ScaleBar, TickModifierLabel,
│                    RadialGauge, Tooltip, Crosshair, FillY
├── 装饰器 (2)      DraggablePlottableDecorator, HittablePlottableDecorator
│
└── Interactive/ (11)  ← 可拖拽交互元素
    InteractiveVerticalLine, InteractiveHorizontalLine,
    InteractiveVerticalSpan, InteractiveHorizontalSpan,
    InteractiveRectangle, InteractiveMarker,
    InteractiveLineSegment, InteractiveTrendLine, ...
    └── SubplotPreRenderActions/
        SharedVerticalLine    ← 跨子图共享交互线
```

每个 Plottable 都继承统一代码模板：

```
class XxxPlot : IPlottable, IHasLine, IHasMarker, IHasLegendText, ...
{
    bool IsVisible { get; set; }      // 可见性
    IAxes Axes { get; set; }          // 坐标系引用
    AxisLimits GetAxisLimits()        // 告诉 Plot 数据范围
    void Render(RenderPack rp)         // 画自己
    IEnumerable<LegendItem> LegendItems // 图例项
}
```

### 3.5 `Rendering/` — 渲染管道

> 详细参考：`learning/05-rendering/rendering-architecture.md`

```
Rendering/
├── RenderManager.cs             ← 25 步管道调度器：初始化 → foreach 依次执行
└── RenderActions/ (25 files)    ← 每步独立文件，实现 IRenderAction
    ├── 01_PreRenderLock.cs              ← 获取渲染锁（防止并发渲染）
    ├── 02_ClearCanvas.cs                ← 清空画布
    ├── 03_ReplaceNullAxesWithDefaults   ← 未设轴的 Plottable → 默认轴
    ├── 04_AutoScaleUnsetAxes            ← 自动缩放未手动设定的轴
    ├── 05_ContinuouslyAutoscale         ← 持续自动缩放（DataStreamer）
    ├── 06_ExecutePlottableAxisManagers  ← 执行 Plottable 的轴管理器
    ├── 07_ApplyAxisRulesBeforeLayout    ← 应用布局前轴约束
    ├── 08_CalculateLayout               ← 计算布局：DataRect + PanelRects
    ├── 09_RenderFigureBackground        ← 绘制图表背景
    ├── 10_ApplyAxisRulesAfterLayout     ← 应用布局后轴约束
    ├── 11_RegenerateTicks               ← 根据 DataRect.Width 重新生成刻度
    ├── 12_RenderStartingEvent           ← 触发 RenderStarting 事件
    ├── 13_RenderDataBackground          ← 绘制数据区背景
    ├── 14_StoreGLState                  ← 备份 OpenGL 状态
    ├── 15_RenderGridsBelowPlottables    ← 绘制 Plottable 下层网格
    ├── 16_RestoreGLState                ← 恢复 OpenGL 状态
    ├── 17_RenderPlottables              ← 绘制所有 Plottable
    ├── 18_RenderGridsAbovePlottables    ← 绘制 Plottable 上层网格
    ├── 19_RenderLegends                 ← 绘制图例
    ├── 20_RenderPanels                  ← 绘制面板（标题、ColorBar）
    ├── 21_RenderBorders                 ← 绘制边框
    ├── 22_RenderZoomRectangle           ← 绘制缩放矩形
    ├── 23_SyncGLPlottables              ← 同步 OpenGL Plottable
    ├── 24_RenderPlottablesLast          ← 绘制覆盖层（IRenderLast）
    └── 25_RenderBenchmark               ← 绘制性能面板
```

关键原则：每个步骤前后 `rp.CanvasState.Save()` / `RestoreAll()` 保证隔离。

### 3.6 `Interactivity/` — 交互系统 (~25 files)

> 详细参考：`learning/06-interactivity/interactivity-controls-architecture.md`

```
Interactivity/
├── UserInputProcessor.cs          ← 统一事件入口
├── IUserAction.cs                 ← 平台无关事件抽象
├── IUserActionResponse.cs         ← 响应器接口（责任链）
├── ResponseInfo.cs                ← 响应状态（IsPrimary 独占标志）
├── KeyboardState.cs               ← 键盘状态机
├── Key.cs / MouseButton.cs        ← 按键枚举
├── MouseAxisManipulation.cs       ← 鼠标轴操作辅助
├── StandardKeys.cs                ← 标准键定义
├── StandardMouseButtons.cs        ← 标准鼠标键定义
│
├── UserActions/ (12 files)        ← 12 种原始事件
│   MouseMove, LeftMouseDown/Up, MiddleMouseDown/Up,
│   RightMouseDown/Up, MouseWheelDown/Up, KeyDown/Up, Unknown
│
└── UserActionResponses/ (13 files) ← 12 种响应器
    MouseDragPan, MouseDragZoom, MouseDragZoomRectangle,
    MouseWheelZoom, MouseInteractWithPlottables,
    SingleClickAutoscale, SingleClickContextMenu,
    DoubleClickBenchmark, KeyboardPanAndZoom,
    KeyboardAutoscale, DoubleClickResponse,
    KeyPressResponse, SingleClickResponse
```

责任链机制：`UserInputProcessor` 按 `UserActionResponses[]` 顺序依次尝试匹配，第一个匹配成功后设置 `IsPrimary = true` 独占后续事件。

### 3.7 其余辅助目录

#### 轴系统

```
TickGenerators/ (15)
├── NumericAutomatic/Manual/FixedInterval, DecimalTickSpacingCalculator
├── DateTimeAutomatic/Manual/FixedInterval, FinancialTickGenerator
├── LogMinorTickGenerator, EvenlySpacedMinorTickGenerator, EmptyTickGenerator
└── LabelFormatters, IDateTimeTickGenerator, ITimeUnit

AxisPanels/ (12)
├── AxisBase → BottomAxis, LeftAxis, RightAxis, TopAxis
├── DateTimeXAxis, XAxisBase, YAxisBase
├── MirroredXAxis, MirroredYAxis
└── Experimental/LeftAxisWithSubtitle

AxisRules/ (16)
├── LockedLeft/Right/Top/Bottom/CenterX/CenterY/Horizontal/Vertical
├── MaximumBoundary/Span, MinimumBoundary/Span
└── SnapToTicksX/Y, SquarePreserveX/Y, SquareZoomOut

AxisLimitManagers/ (3)
├── Full.cs ← 经典模式（显示全部数据）
├── Slide.cs ← 滑动窗口（实时数据用）
└── FixedWidth.cs ← 固定宽度窗口

AutoScalers/ (1)
└── FractionalAutoScaler
```

#### 布局与面板

```
LayoutEngines/ (5)
├── Automatic, FixedDataArea, FixedPadding, MatchedDataRect, LayoutEngineBase

Panels/ (4)
├── TitlePanel, LegendPanel, ColorBar, PanelBase

Grids/ (1)
└── DefaultGrid

LegendLayouts/ (1)
└── Wrapping
```

#### Markers — 26 种标记形状

```
Markers/
├── 填充风格：FilledCircle, FilledSquare, FilledDiamond,
│              FilledTriangleUp/Down, TriUp, TriDown
├── 开放风格：OpenCircle, OpenSquare, OpenDiamond,
│              OpenTriangleUp/Down, OpenCircleWithCross/Dot/Eks
├── 特殊形状：Asterisk, Cross, Eks, HashTag, HorizonalBar, VerticalBar,
│              CircleWithLineLeft/Right, TriangleWithLineLeft/Right, None
```

#### Colormaps — 35 种科学配色

```
Colormaps/
├── 经典：Jet, Turbo, Viridis, Plasma, Inferno, Magma, Grayscale
├── 海洋：Haline, Deep, Ice, Solar, Rain, Delta, Algae, Amp, Tempo, Thermal
├── 陆地：Topo, Turbid, Matter, Speed, Dense
├── 风格：MellowRainbow, Oxy, Phase
├── 适配：Custom, CustomInterpolated, CustomPalette, Inverted, Reversed, InvertedHue
└── 其他：Balance, Blues, Curl, Diff, Greens, Tarn
```

#### Palettes — 26 种分类调色板

```
Palettes/
├── 经典：Normal, Dark, LightSpectrum, LightOcean, Frost
├── 易用：Category10, Category20, ColorblindFriendly, ColorblindFriendlyDark
├── 主题：Nord, OneHalf, OneHalfDark, Nero, PolarNight, Penumbra, Aurora
├── 风格：Microcharts, PastelWheel, Building, Amber, Redness
└── 其他：Tsitsulin, SummerSplash, SnowStorm, DarkPastel, Custom
```

#### 统计与数学

```
Statistics/ (6)
├── Histogram, Descriptive, LinearRegression,
├── KernelDensity, ProbabilityDensity, Series

Finance/ (2)
├── BollingerBands, SimpleMovingAverage
```

#### 其他辅助

```
PathStrategies/ (4)       连线策略：Straight, QuadHalfPoint(阶梯), CubicSpline, Arrows
ArrowShapes/ (7)          箭头形状：Arrowhead, Chevron, Pentagon, Double, Single, ...
Hatches/ (5)              图案填充：Checker, Dots, Grid, Square, Striped
DataGenerators/ (3)       实时数据生成：FinancialDataGenerator, RandomWalker, RandomWalker2D
DataViews/ (3)            数据流视图：Scroll, Wipe, IDataStreamerView
FontResolvers/ (2)        字体解析：SystemFontResolver, FileFontResolver
Collections/ (1)          CircularBuffer
CompilerServices/ (2)     CompilerServices, Index
MultiplotLayouts/ (2)     Columns, CustomGrid
IO/ (1)                   BitmapHeader
```

---

## 四、控件项目 `ScottPlot5 Controls/`

> 详细参考：`learning/07-controls/controls-architecture.md`

```
ScottPlot5 Controls/
├── ScottPlot.WinForms/     NuGet: ScottPlot.WinForms
│   FormsPlot, FormsPlotGL, FormsPlotMenu, FormsPlotViewer, ...
├── ScottPlot.WPF/          NuGet: ScottPlot.WPF
│   WpfPlot, WpfPlotGL, WpfPlotMenu, WpfPlotViewer, ...
├── ScottPlot.Avalonia/     NuGet: ScottPlot.Avalonia
│   AvaPlot, AvaPlotMenu, ...
├── ScottPlot.Blazor/       NuGet: ScottPlot.Blazor
│   BlazorPlot.razor, BlazorPlotGL.razor, BlazorPlotMenu, ...
├── ScottPlot.Eto/          NuGet: ScottPlot.Eto
│   EtoPlot, EtoPlotMenu, ...
├── ScottPlot.Maui/         NuGet: ScottPlot.Maui
│   MauiPlot, MauiPlotMenu, Platforms/{Android,iOS,MacCatalyst,Tizen,Windows}
├── ScottPlot.WinUI/        NuGet: ScottPlot.WinUI
│   WinUIPlot, WinUIPlotMenu, ...
├── ScottPlot.OpenGL/       NuGet: ScottPlot.OpenGL
│   ScatterGL, ScatterGLCustom, GLPrograms/ (12 个 Shader 文件)
└── ScottPlot.GLControl     （在核心库中，非独立 NuGet）
```

**统一模式**（每个控件 ~80 行核心代码）：

```
平台事件 → UserInputProcessor.Process(action)
    → Plot 状态修改
    → Refresh()
    → RenderManager.Render(canvas, rect)
```

---

## 五、测试与工具项目

### 5.1 测试

```
ScottPlot5 Tests/
│
├── Unit Tests/
│   ├── UnitTests/PrimitiveTests/         ← 原子类型测试
│   ├── UnitTests/TickGenerators/         ← 刻度生成器测试
│   ├── RenderTests/
│   │   ├── Figure/                       ← 整图对比测试
│   │   ├── Plottable/                    ← 各 Plottable 渲染测试
│   │   ├── AutoScale/Layout/Legend/...   ← 子系统测试
│   ├── InteractivityTests/
│   │   ├── UserInputActionTests/         ← 8 种响应器独立测试
│   │   └── KeyboardStateTests
│   ├── CodeTests/                        ← 代码规范检查
│   ├── FontTests/                        ← 字体检测/测量
│   ├── Statistics/                       ← 统计算法测试
│   └── TestImages/                       ← 测试用图片资源
│
└── Graphical Test Runner/                ← WinForms 可视化结果对比
```

### 5.2 其他工具项目

| 项目 | 用途 |
|------|------|
| `ScottPlot5 Cookbook/` | 扫描 Plottable → 生成 500+ 带截图示例 → 输出网站 |
| `ScottPlot5 Demos/` | 4 套演示程序 |
| `ScottPlot5 Benchmarks/` | BenchmarkDotNet 性能基准测试 |

#### Demo 程序明细

```
ScottPlot5 Demos/
├── Avalonia Demo/            ← Avalonia 演示（MVVM 架构）
│   ├── Demos/                ← 40+ 个独立 Demo 窗口
│   ├── ViewModels/           ← MVVM ViewModel 层
│   └── Views/                ← MVVM View 层
├── ScottPlot5 WinForms Demo/ ← WinForms 演示
│   └── Demos/                ← 多套 .Designer/.resx 演示窗体
├── ScottPlot5 WPF Demo/      ← WPF 演示
│   └── DemoWindows/          ← DisplayScaling, MultiThreading, Quickstart
└── ScottPlot5 Blazor/        ← Blazor WebAssembly 演示
    ├── Pages/                ← Quickstart, Recipe, Signal
    ├── Services/             ← IRecipesService, IResizeService
    └── wwwroot/              ← 静态资源（Bootstrap, highlight.js, OpenIconic）
```

---

## 六、导航速查

### "我想找..."

| 问题 | 路径 |
|------|------|
| `Plot.Add.Scatter()` 怎么实现的？ | `PlottableAdder.cs` |
| 渲染管道怎么插入步骤？ | `Rendering/RenderManager.cs` → `RenderActions[]` |
| 如何新增图表类型？ | 复制 `Plottables/Scatter.cs` 参考 |
| 如何新增坐标轴？ | `AxisPanels/AxisBase.cs` + `Interfaces/IAxis.cs` |
| 如何自定义交互？ | `Interactivity/` → 实现 `IUserActionResponse` |
| 大数据如何降采样？ | `DataSources/SignalSourceDouble.cs` → `SegmentedTree.cs` |
| 颜色系统有哪些能力？ | `Primitives/Color.cs` + `Colors.cs` |
| 字体怎么管理的？ | `Fonts.cs` + `FontResolvers/` |
| 刻度怎么计算的？ | `TickGenerators/NumericAutomatic.cs` |
| 柱状图怎么画的？ | `Plottables/BarPlot.cs` |
| 实时数据怎么处理？ | `Plottables/DataLogger.cs` + `DataSources/DataLoggerSource.cs` |

### "我想改..."

| 问题 | 路径 |
|------|------|
| 默认颜色/样式 | `Plot.cs` → `ApplyDefaultStyle()` |
| 默认交互行为 | `Interactivity/UserInputProcessor.cs` |
| 默认轴行为 | `AxisManager.cs` |
| 默认布局 | `LayoutEngines/Automatic.cs` |
| 默认刻度 | `TickGenerators/NumericAutomatic.cs` |
| 默认字体 | `Fonts.cs` → `SetBestFont()` |

### "我想了解..."

| 问题 | 学习文档 |
|------|---------|
| 5 条核心数据链路 | `learning/01-architecture/data-chains.md` |
| Primitives 层详解 | `learning/02-primitives/primitives-architecture.md` |
| DataSources 层详解 | `learning/03-datasources/datasources-architecture.md` |
| Plottables 层详解 | `learning/04-plottables/plottables-architecture.md` |
| 渲染管道详解 | `learning/05-rendering/rendering-architecture.md` |
| 交互系统详解 | `learning/06-interactivity/interactivity-controls-architecture.md` |
| 跨平台控件详解 | `learning/07-controls/controls-architecture.md` |
| 新手入门 | `learning/notes/getting-started.md` |
| 编译指南 | `learning/notes/build-guide.md` |
| 常见陷阱 | `learning/notes/usage-caveats.md` |