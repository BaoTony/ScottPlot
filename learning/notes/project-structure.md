# ScottPlot 5 项目结构导航

> 源码地图 · 对照 01-07 学习文档使用 · 2026-10-18

---

## 一、仓库顶层

```
ScottPlot/
├── src/                        ← 所有源码
│   └── ScottPlot5/             ← 唯一条目：ScottPlot 5 的完整解决方案
├── learning/                   ← 【外部学习笔记，非项目源码】
│   ├── 01-architecture/        ← 架构与数据链路
│   ├── 02-primitives/          ← Primitives 层
│   ├── 03-datasources/         ← 数据源系统
│   ├── 04-plottables/          ← Plottables 层
│   ├── 05-rendering/           ← 渲染管道
│   ├── 06-interactivity/       ← 交互系统
│   ├── 07-controls/            ← 跨平台控件
│   └── notes/                  ← 实用笔记（入门指南、编译指南、本文）
├── CHANGELOG.md
├── CONTRIBUTING.md
├── README.md
└── LICENSE
```

---

## 二、解决方案内部结构

```
src/ScottPlot5/
├── ScottPlot5/                 ← 🔷 核心库（NuGet 包：ScottPlot）
├── ScottPlot5 Controls/        ← 🔶 跨平台控件（8 个 NuGet 包）
├── ScottPlot5 Cookbook/        ← 📖 Cookbook 示例代码生成器
├── ScottPlot5 Demos/           ← 🎮 演示程序
├── ScottPlot5 Benchmarks/      ← ⏱  性能基准测试
├── ScottPlot5 Tests/           ← 🧪 测试项目
├── .editorconfig
└── Key.snk                     ← 强名称签名密钥
```

---

## 三、核心库详细结构 `ScottPlot5/`

### 3.1 根目录文件（API 入口层）

| 文件 | 大小 | 职责 |
|------|------|------|
| **Plot.cs** | 大 | 用户主入口：`new Plot()`、`Add`、`SavePng`、`Render` |
| **PlottableAdder.cs** | 大 | `Plot.Add.Scatter()` 等工厂方法（~60 个重载） |
| **RenderPack.cs** | 中 | 单次渲染上下文：Canvas、Layout、Paint、Axes |
| **AxisManager.cs** | 大 | 多轴管理器：添加/移除/查找轴、AutoScale |
| **LayoutManager.cs** | 中 | 布局计算：数据区域 vs 面板区域 |
| **Multiplot.cs** | 中 | 多图容器：`new Multiplot(plot)` |
| **MultiplotSharedAxisManager.cs** | 中 | 多图共享轴管理器 |
| **Drawing.cs** | 中 | 绘图辅助：DrawLines、DrawMarkers、DrawText |
| **Generate.cs** | 中 | 示例数据生成器 |
| **Fonts.cs** | 中 | 字体管理、检测、回退 |
| **FontExtensions.cs** | 小 | 字体扩展方法 |
| **ImageOperations.cs** | 中 | 图像操作：缩放、裁剪、Rotate |
| **DataOperations.cs** | 中 | 数据操作：ResizeHalf、Convolve |
| **DataSourceUtilities.cs** | 小 | 数据源辅助工具 |
| **BinarySearchComparer.cs** | 小 | 双精度二分查找 |
| **GenericComparer.cs** | 小 | 泛型比较器 |
| **NumericConversion.cs** | 小 | 数值类型转换 |
| **RandomDataGenerator.cs** | 中 | 随机数据生成（测试/示例用） |
| **SampleData.cs** | 中 | 固定样本数据 |
| **SampleImages.cs** | 中 | 内嵌示例图片 |
| **Usings.cs** | — | 全局 using |
| **Version.cs** | — | 版本号 |
| **ScottPlot.csproj** | — | 项目文件（5 个 TFM） |

### 3.2 目录分类

```
ScottPlot5/
├── Primitives/       ← Layer 2: 原子数据结构（109 个文件）
├── Interfaces/       ← Layer 2: 核心接口定义（60+ 个接口）
├── DataSources/      ← Layer 3: 数据源实现（28 个文件）
├── Plottables/       ← Layer 4: 可绘制物（61 个文件）
├── Rendering/        ← Layer 5: 渲染管道（仅 RenderManager.cs）
├── Interactivity/    ← Layer 6: 交互系统
├── TickGenerators/   ← 刻度生成器
├── LayoutEngines/    ← 布局引擎
├── LegendLayouts/    ← 图例布局
├── AxisPanels/       ← 轴面板渲染
├── AxisRules/        ← 轴约束规则
├── AxisLimitManagers/← 实时轴范围管理
├── AutoScalers/      ← 自动缩放策略
├── Panels/           ← 图表面板（标题、图例、ColorBar）
├── Grids/            ← 网格线
├── Markers/          ← 标记形状绘制（26 种）
├── ArrowShapes/      ← 箭头形状
├── Colormaps/        ← 颜色映射（35 种配色）
├── Hatches/          ← 图案填充
├── Statistics/       ← 统计计算
├── Finance/          ← 金融指标（布林带、SMA）
├── DataGenerators/   ← 实时数据生成器
├── DataViews/        ← 数据流视图
├── FontResolvers/    ← 字体解析器
├── Collections/      ← 数据结构（CircularBuffer）
├── CompilerServices/ ← 编译时工具
├── MultiplotLayouts/ ← 多图布局
├── IO/               ← I/O 辅助
└── LegendLayouts/    ← 图例排版
```

---

## 四、核心目录逐个说明

### 4.1 `Primitives/` — Layer 2: 原子数据结构

> 详细参考：[learning/02-primitives/primitives-architecture.md](../../learning/02-primitives/primitives-architecture.md)

```
Primitives/ (109 files)
├── 坐标与几何 (15)
│   Coordinates, Pixel, CoordinateRect, PixelRect, CoordinateLine, PixelLine,
│   CoordinateRange, CoordinatePath, PixelPath, CoordinateOffset, Angle, ...
├── 样式系统 (18)
│   LineStyle, FillStyle, MarkerStyle, FontStyle, BackgroundStyle, GridStyle,
│   LabelStyle, TickMarkStyle, ArrowStyle, Gradient, Colormap, ...
├── 颜色系统 (70+)
│   Color, Colors (静态工厂，数千种命名颜色)
├── 轴与范围 (12)
│   Axes, AxisLimits, ExpandingAxisLimits, AxisLimits3d, ...
├── 图例 (4)
│   Legend, LegendItem, LegendLayout
├── 布局 (6)
│   Layout, PixelPadding, FractionRect, Alignment, ...
├── 数据承载 (6)
│   Bar, OHLC, PieSlice, Box, Population, Range, ...
└── 交互 (3)
│   ContextMenuItem, Cursor, InteractiveHandle
```

**使用指引**：做任何样式/坐标相关开发，先找 `Primitives/` 中的对应类型，它们是所有上层代码的共享基础。

### 4.2 `Interfaces/` — Layer 2: 核心接口定义

> 关键接口一览

```
Interfaces/ (60+ files)
├── IPlottable.cs          ← 所有 Plottable 必须实现
├── IRenderAction.cs       ← 渲染管道步骤
├── IRenderLast.cs         ← 最后渲染（覆盖层）
├── IPlottableGL.cs        ← OpenGL Plottable
├── IScatterSource.cs      ← 离散数据源
├── ISignalSource.cs       ← 信号数据源
├── ISignalXYSource.cs     ← XY 信号源
├── IOHLCSource.cs         ← K线数据源
├── IVectorFieldSource.cs  ← 向量场数据源
├── IAxes.cs / IAxis.cs    ← 轴接口
├── IGrid.cs               ← 网格接口
├── IPanel.cs              ← 面板接口
├── IPlotControl.cs        ← 跨平台控件统一接口
├── IPlotMenu.cs           ← 右键菜单接口
├── IMultiplot.cs          ← 多图接口
├── IHasLine / IHasMarker / IHasFill / ... ← 样式 Mixin
├── IColormap.cs           ← 颜色映射
├── IPalette.cs            ← 调色板
├── IHatch.cs              ← 图案填充
├── IArrowShape.cs         ← 箭头形状
└── ... (ITickGenerator, IAxisRule, ILayoutEngine, IFontResolver, ...)
```

**使用指引**：理解系统的可扩展点——每个接口代表一个"策略模式"插入点，实现对应接口即可替换默认行为。

### 4.3 `DataSources/` — Layer 3: 数据源实现

> 详细参考：[learning/03-datasources/datasources-architecture.md](../../learning/03-datasources/datasources-architecture.md)

```
DataSources/ (28 files)
├── IScatterSource 实现 (7)
│   ScatterSourceDoubleArray, ScatterSourceCoordinatesArray,
│   ScatterSourceGenericArray, ScatterSourceGenericList, ...
├── ISignalSource 实现 (9)
│   SignalSourceDouble, SignalSourceGenericArray, SignalSourceBase,
│   SignalConstSource, FastSignalSourceDouble, SignalInterpolation, ...
├── ISignalXYSource 实现 (3)
│   SignalXYSourceDoubleArray, SignalXYSourceGenericArray, ...
├── IOHLCSource 实现 (3)
│   OHLCSourceArray, OHLCSourceList, OHLCSourceBase
├── 实时数据 (2)
│   DataLoggerSource, DataStreamerSource
├── 优化引擎 (3)
│   SegmentedTree, MinMaxCache, ScatterSourceWithCachedLimits
├── 其他 (4)
│   FunctionSource, CoordinateDataSource, VectorFieldDataSourceCoordinatesList, ...
```

**使用指引**：想理解大数据降采样 → `SignalSourceDouble` + `SegmentedTree`；想理解实时数据 → `DataLoggerSource`。

### 4.4 `Plottables/` — Layer 4: 可绘制物

> 详细参考：[learning/04-plottables/plottables-architecture.md](../../learning/04-plottables/plottables-architecture.md)

```
Plottables/ (61 files)
├── 散点/信号 (6)  → Scatter, Signal, SignalXY, SignalConst, LinePlot, Markers
├── 柱状/条形 (3)  → BarPlot, LollipopPlot, Bracket
├── 金融图表 (3)  → CandlestickPlot, OHLCPlot, FinancialTimeAxis
├── 热力/等值 (4)  → Heatmap, IsoLines, ContourLines, TINPlot
├── 饼图/径向 (3)  → Pie, Coxcomb, RadialGaugePlot
├── 极坐标/雷达 (4) → PolarAxis, Radar, SmithChartAxis, Phasor
├── 统计图表 (3)  → BoxPlot, PopulationSymbol, HistogramBars
├── 直线/跨度 (7)  → VerticalLine, HorizontalLine, VerticalSpan, HorizontalSpan,
│                    AxisLine, AxisSpan, FloatingAxis
├── 形状图形 (5)  → Rectangle, Ellipse, Polygon, ImageRect, ImageMarker
├── 标注/文字 (3)  → Text, Annotation, Callout
├── 实时数据 (3)  → DataLogger, DataStreamer, DataStreamerXY
├── 箭头/矢量 (3)  → Arrow, VectorField, ErrorBar
├── 工具/辅助 (4)  → Benchmark, ZoomRectangle, ScaleBar, TickModifierLabel
├── 混合 (3)       → FillY, Crosshair, Tooltip
└── 装饰器 (2)     → DraggablePlottableDecorator, HittablePlottableDecorator
```

**使用指引**：每个 Plottable 文件遵循统一模式（`IPlottable` + `IHas*` Mixin + `IScatterSource`）；添加新图表类型 → 复制 `Scatter.cs` 改 `Render()` 即可。

### 4.5 `Rendering/` — Layer 5: 渲染管道

```
Rendering/ (1 file)
└── RenderManager.cs    ← 25 步 RenderAction 管道调度器
```

> 详细参考：[learning/05-rendering/rendering-architecture.md](../../learning/05-rendering/rendering-architecture.md)

RenderManager 是整个引擎唯一入口，它初始化 25 个 `IRenderAction` 并依次执行。渲染中产生的临时状态存在 `RenderPack` 中。每个步骤前后 `CanvasState.Save()/RestoreAll()` 保证隔离。

### 4.6 `Interactivity/` — Layer 6: 交互系统

> 详细参考：[learning/06-interactivity/interactivity-controls-architecture.md](../../learning/06-interactivity/interactivity-controls-architecture.md)

```
Interactivity/
├── UserInputProcessor.cs          ← 统一事件入口
├── IUserAction.cs                 ← 平台无关的事件抽象
├── IUserActionResponse.cs         ← 响应器接口（责任链模式）
├── ResponseInfo.cs                ← 响应状态（IsPrimary 独占机制）
├── KeyboardState.cs               ← 键盘状态机
├── Key.cs / MouseButton.cs        ← 按键枚举
├── UserActions/ (12 files)        ← 12 种原始事件类型
│   MouseMove, LeftMouseDown/Up, MiddleMouseDown/Up,
│   RightMouseDown/Up, MouseWheelDown/Up, KeyDown/Up
└── UserActionResponses/ (13 files)← 12 种响应器
    MouseDragPan, MouseDragZoom, MouseDragZoomRectangle,
    MouseWheelZoom, MouseInteractWithPlottables,
    SingleClickAutoscale, SingleClickContextMenu,
    DoubleClickBenchmark, KeyboardPanAndZoom, KeyboardAutoscale, ...
```

**使用指引**：自定义交互 → 实现 `IUserActionResponse` → `UserInputProcessor.UserActionResponses.Insert(index, ...)`。

### 4.7 `TickGenerators/` — 刻度生成

```
TickGenerators/ (15 files)
├── NumericAutomatic       ← 自动数值刻度（最常用）
├── NumericFixedInterval   ← 固定间隔数值刻度
├── NumericManual          ← 手动指定刻度
├── DateTimeAutomatic      ← 自动日期刻度
├── DateTimeFixedInterval  ← 固定间隔日期刻度
├── DateTimeManual         ← 手动指定日期刻度
├── FinancialTickGenerator ← 金融图表专用（跳过非交易日）
├── DecimalTickSpacingCalculator ← 十进制间隔计算
├── LabelFormatters        ← 刻度标签格式化
├── LogMinorTickGenerator  ← 对数刻度次刻度
├── EvenlySpacedMinorTickGenerator ← 均匀次刻度
├── EmptyTickGenerator     ← 空刻度（隐藏刻度）
└── ITimeUnit / IDateTimeTickGenerator / ITickGenerator
```

### 4.8 其他重要目录

| 目录 | 文件数 | 一句话 |
|------|--------|--------|
| `LayoutEngines/` | 5 | 数据区域计算：`Automatic`、`FixedDataArea`、`FixedPadding`、`MatchedDataRect` |
| `AxisPanels/` | 12 | 轴渲染：`BottomAxis`、`LeftAxis`、`DateTimeXAxis`、`MirroredXAxis` 等 |
| `AxisRules/` | 16 | 轴约束：`LockedLeft`、`SquarePreserveX`、`MinimumSpan` 等 |
| `AxisLimitManagers/` | 3 | 动态轴范围：`Full`（经典）、`Slide`（实时滚动）、`FixedWidth` |
| `AutoScalers/` | 1 | 自适应缩放：`FractionalAutoScaler` |
| `Panels/` | 4 | `TitlePanel`、`LegendPanel`、`ColorBar`、`PanelBase` |
| `Markers/` | 26 | 26 种标记形状的 SkiaSharp 绘制实现 |
| `Colormaps/` | 35 | 35 种科学配色方案（Viridis、Jet、Heat 等） |
| `Statistics/` | 6 | `Histogram`、`LinearRegression`、`KernelDensity`、`Descriptive` 等 |
| `Finance/` | 2 | `BollingerBands`、`SimpleMovingAverage` |

---

## 五、控件项目 `ScottPlot5 Controls/`

> 详细参考：[learning/07-controls/controls-architecture.md](../../learning/07-controls/controls-architecture.md)

```
ScottPlot5 Controls/
├── ScottPlot.WinForms/        ← NuGet: ScottPlot.WinForms
│   FormsPlot.cs, FormsPlotMenu.cs, FormsPlotGL.cs, FormsPlotViewer.cs
├── ScottPlot.WPF/             ← NuGet: ScottPlot.WPF
│   WpfPlot.cs, WpfPlotMenu.cs, WpfPlotGL.cs, WpfPlotViewer.cs
├── ScottPlot.Avalonia/        ← NuGet: ScottPlot.Avalonia
│   AvaPlot.cs, AvaPlotMenu.cs
├── ScottPlot.Blazor/          ← NuGet: ScottPlot.Blazor
│   BlazorPlot.razor, BlazorPlotGL.razor, BlazorPlotMenu.cs
├── ScottPlot.Eto/             ← NuGet: ScottPlot.Eto
│   EtoPlot.cs, EtoPlotMenu.cs
├── ScottPlot.Maui/            ← NuGet: ScottPlot.Maui
│   MauiPlot.cs, MauiPlotMenu.cs, Platforms/{Android,iOS,...}
├── ScottPlot.WinUI/           ← NuGet: ScottPlot.WinUI
│   WinUIPlot.cs, WinUIPlotMenu.cs
├── ScottPlot.OpenGL/          ← NuGet: ScottPlot.OpenGL
│   ScatterGL.cs, ScatterGLCustom.cs, GLPrograms/
└── ScottPlot.GLControl/       ← （在核心库项目中，非独立 NuGet）
```

**通用模式**（每个控件 ~80 行）：

```
平台事件 → UserInputProcessor.Process() → Plot 状态变化 → Refresh() → RenderManager.Render(canvas, rect)
```

---

## 六、测试与工具项目

### 6.1 测试项目

```
ScottPlot5 Tests/
├── Unit Tests/                               ← 核心单元测试
│   ├── UnitTests/PrimitiveTests/             ← Primitives 层测试
│   ├── UnitTests/TickGenerators/             ← 刻度生成器测试
│   ├── RenderTests/Figure/                   ← 整图对比测试
│   ├── RenderTests/Plottable/                ← Plottable 渲染测试
│   ├── InteractivityTests/                   ← 交互系统测试
│   ├── CodeTests/                            ← 代码规范测试
│   ├── FontTests/                            ← 字体测试
│   └── Statistics/                           ← 统计测试
└── Graphical Test Runner/                    ← WinForms 可视化测试运行器
```

### 6.2 其他工具项目

| 项目 | 用途 |
|------|------|
| `ScottPlot5 Cookbook/` | 自动扫描 Plottable → 生成 HTML 示例页 → 输出到 scottplot.net |
| `ScottPlot5 Demos/` | 3 套演示程序（Avalonia、WinForms、WPF、Blazor） |
| `ScottPlot5 Benchmarks/` | BenchmarkDotNet 性能测试 |

---

## 七、常用导航速查

### "我想找..."

| 问题 | 去这里 |
|------|--------|
| 某个 API 怎么实现的？ | `Plot.cs` → 跟踪方法调用 |
| 如何在渲染管道中插入步骤？ | `Rendering/RenderManager.cs` |
| 如何添加新的图表类型？ | 复制 `Plottables/Scatter.cs` 参考 |
| 如何添加新的坐标轴类型？ | `AxisPanels/` + `Interfaces/IAxis.cs` |
| 如何自定义交互？ | `Interactivity/UserActionResponses/` |
| 数据是怎么降采样的？ | `DataSources/SignalSourceDouble.cs` → `SegmentedTree.cs` |
| 颜色系统有哪些能力？ | `Primitives/Color.cs` + `Primitives/Colors.cs` |
| 字体怎么管理的？ | `Fonts.cs` + `FontResolvers/` |
| 刻度怎么计算的？ | `TickGenerators/NumericAutomatic.cs` |

### "我想改..."

| 问题 | 去这里 |
|------|--------|
| 默认颜色/样式 | `Plot.cs` 构造函数 → `Plot.ApplyDefaultStyle()` |
| 默认交互行为 | `UserInputProcessor.cs` 构造函数 |
| 默认轴行为 | `AxisManager.cs` |
| 默认布局 | `LayoutEngines/Automatic.cs` |
| 默认刻度 | `TickGenerators/NumericAutomatic.cs` |

---

## 八、交叉引用

| 文档 | 适合场景 |
|------|---------|
| [getting-started.md](getting-started.md) | 新手入门，API 使用 |
| [build-guide.md](build-guide.md) | 编译、工作负载、跳过 Android |
| [usage-caveats.md](usage-caveats.md) | 常见陷阱与注意事项 |
| [01-architecture/](../../learning/01-architecture/) | 5 条数据链路全解析 |
| [02-primitives/](../../learning/02-primitives/) | Coord/Pixel/Color 等原子层 |
| [03-datasources/](../../learning/03-datasources/) | Scatter/Signal/SegmentedTree |
| [04-plottables/](../../learning/04-plottables/) | 72 种图表类型详解 |
| [05-rendering/](../../learning/05-rendering/) | 25 步渲染管道 |
| [06-interactivity/](../../learning/06-interactivity/) | 交互系统责任链 |
| [07-controls/](../../learning/07-controls/) | 8 个跨平台控件 |