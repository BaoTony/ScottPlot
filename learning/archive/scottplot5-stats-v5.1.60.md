# ScottPlot5 全库源码统计

> ScottPlot5 版本：**5.1.60**（提取自 ScottPlot.csproj，便于跨版本比对）
> 由 `learning/scripts/scottplot5-stats.py` 自动生成，供 `learning/` 编号文档核对数字口径。

## 一、解决方案全貌（src/ScottPlot5 下各项目）

| 项目 | .cs 文件数 | 代码行数 |
|---|---:|---:|
| ScottPlot5 | 577 | 50071 |
| ScottPlot5 Benchmarks | 5 | 148 |
| ScottPlot5 Controls | 55 | 4400 |
| ScottPlot5 Cookbook | 92 | 11857 |
| ScottPlot5 Demos | 125 | 8060 |
| ScottPlot5 Sandbox | 55 | 1768 |
| ScottPlot5 Tests | 95 | 8720 |

## 二、核心库分层地图（ScottPlot5 各目录 .cs 文件数）

| 目录 | .cs 文件数 |
|---|---:|
| (根目录散文件) | 23 |
| ArrowShapes | 8 |
| AutoScalers | 1 |
| AxisLimitManagers | 3 |
| AxisPanels | 11 |
| AxisRules | 17 |
| Collections | 1 |
| Colormaps | 38 |
| CompilerServices | 2 |
| DataGenerators | 3 |
| DataSources | 28 |
| DataViews | 3 |
| Finance | 2 |
| FontResolvers | 2 |
| Grids | 1 |
| Hatches | 5 |
| IO | 1 |
| Interactivity | 37 |
| Interfaces | 51 |
| LayoutEngines | 5 |
| LegendLayouts | 1 |
| Markers | 26 |
| MultiplotLayouts | 5 |
| NamedColors | 7 |
| Palettes | 26 |
| Panels | 4 |
| PathStrategies | 4 |
| PlotStyles | 2 |
| Plottables | 72 |
| Primitives | 109 |
| Rendering | 26 |
| Reporting | 3 |
| StarAxes | 3 |
| Statistics | 7 |
| Stylers | 2 |
| Testing | 4 |
| TickGenerators | 30 |
| Triangulation | 4 |

## 三、Primitives 基础类型分类

| 种类 | 个数 | 类型（最多列 8 个） |
|---|---:|---|
| struct | 37 | Angle, AxisLimits, AxisLimits3d, Color, Colors, ContextMenuItem, CoordinateLine, CoordinateOffset 等 |
| record struct | 3 | ContourLine, IndexRange, PixelOffset |
| class | 46 | ArrowStyle, Axes, AxisGradientColorPosition, AxisSpanUnderMouse, BackgroundStyle, Bar, BarSeries, Box 等 |
| interface | 2 | IAutoScaler, IAxisLimitManager |
| enum | 21 | Alignment, ArrowAnchor, ArrowShape, AxisGradientDirection, ConnectStyle, Cursor, Edge, FontSlant 等 |

## 四、核心库接口统计（合计 61 个）

| 目录 | 个数 | 接口（最多列 6 个） |
|---|---:|---|
| Interfaces | 50 | IArrowShape, IAxes, IAxis, IAxisRule, IColormap, IDataSource … |
| Interactivity | 4 | IMouseAction, IMouseButtonAction, IUserAction, IUserActionResponse |
| Primitives | 2 | IAutoScaler, IAxisLimitManager |
| TickGenerators | 2 | IDateTimeTickGenerator, ITimeUnit |
| DataViews | 1 | IDataStreamerView |
| Plottables | 1 | IRenderStrategy |
| Triangulation | 1 | IEdge |

## 五、DataSources 类型与实现的接口

| 类型 | 种类 | 实现的数据源接口 |
|---|---|---|
| CacheScatterLimitsDecorator | class | IScatterSource, IScatterSource |
| CoordinateDataSource | class | IDataSource |
| DataLoggerSource | class | (基类间接实现) |
| DataStreamerSource | class | (基类间接实现) |
| FastSignalSourceDouble | class | ISignalSource, IDataSource |
| FunctionSource | class | IFunctionSource |
| GrowListView | class | (基类间接实现) |
| ListViewDecorator | class | (基类间接实现) |
| MinMaxCache | class | (基类间接实现) |
| OHLCSourceArray | class | IOHLCSource |
| OHLCSourceBase | class | IOHLCSource |
| OHLCSourceList | class | IOHLCSource |
| ReadOnlyListExtensions | class | (基类间接实现) |
| ScatterSourceCoordinatesArray | class | IScatterSource, IDataSource |
| ScatterSourceCoordinatesList | class | IScatterSource, IDataSource |
| ScatterSourceDoubleArray | class | IScatterSource, IDataSource |
| ScatterSourceGenericArray | class | IScatterSource, IDataSource |
| ScatterSourceGenericList | class | IScatterSource, IDataSource |
| SegmentedTree | class | (基类间接实现) |
| SelectListView | class | (基类间接实现) |
| SignalConstSource | class | (基类间接实现) |
| SignalInterpolation | class | (基类间接实现) |
| SignalRangeY | struct | (基类间接实现) |
| SignalSourceBase | class | (基类间接实现) |
| SignalSourceDouble | class | ISignalSource, IDataSource |
| SignalSourceGenericArray | class | ISignalSource, IDataSource |
| SignalSourceGenericList | class | ISignalSource, IDataSource |
| SignalXYSourceDoubleArray | class | ISignalXYSource, IDataSource |
| SignalXYSourceGenericArray | class | ISignalXYSource, IDataSource |
| SignalXYSourceGenericList | class | ISignalXYSource, IDataSource |
| SkipListView | class | (基类间接实现) |
| TakeListView | class | (基类间接实现) |
| VectorFieldDataSourceCoordinatesList | class | IVectorFieldSource, IDataSource |
| ZipListView | class | (基类间接实现) |

## 六、Plottable 图表类（实现 IPlottable）

| 位置 | .cs 文件数 |
|---|---:|
| Plottables/Interactive | 10 |
| Plottables 根目录 | 61 |
| **合计** | **72** |

（按类声明识别：常规 60 个，Interactive 10 个；部分类经由 PlottableBase 间接实现 IPlottable，故以文件数为准）

## 七、RenderManager 渲染管线步骤

1. PreRenderLock
2. ClearCanvas
3. ReplaceNullAxesWithDefaults
4. AutoScaleUnsetAxes
5. ContinuouslyAutoscale
6. ExecutePlottableAxisManagers
7. ApplyAxisRulesBeforeLayout
8. CalculateLayout
9. RenderFigureBackground
10. ApplyAxisRulesAfterLayout
11. RegenerateTicks
12. RenderStartingEvent
13. RenderDataBackground
14. StoreGLState
15. RenderGridsBelowPlottables
16. RestoreGLState
17. RenderPlottables
18. RenderGridsAbovePlottables
19. RenderLegends
20. RenderPanels
21. RenderBorders
22. RenderZoomRectangle
23. SyncGLPlottables
24. RenderPlottablesLast
25. RenderBenchmark
（管道中调用 25 步；RenderActions 目录文件数 25）

## 八、Plot.Add 添加方法（127 个，含重载；分部文件 1 个）

Annotation, AnnularEllipticalSector, AnnularEllipticalSector, AnnularSector, AnnularSector, Arc, Arc, Arrow, Arrow, Arrow, BackgroundText, Bar, Bar, Bars, Bars, Bars, Bars, Box, Boxes, Bracket, Bracket, Bracket, Callout, Callout, Candlestick, Candlestick, Circle, Circle, CircleSector, CircleSector, ColorBar, ContourLines, ContourLines, Coxcomb, Coxcomb, Crosshair, DataLogger, DataLogger, DataStreamer, DataStreamerXY, Ellipse, Ellipse, EllipticalArc, EllipticalArc, EllipticalSector, EllipticalSector, ErrorBar, FillY, FillY, FillY, Function, Function, Heatmap, Heatmap, Histogram, HorizontalLine, HorizontalSpan, ImageMarker, ImageRect, InteractiveHorizontalLine, InteractiveHorizontalLineSegment, InteractiveHorizontalSpan, InteractiveLineSegment, InteractiveMarker, InteractiveRectangle, InteractiveTrendLine, InteractiveVerticalLine, InteractiveVerticalLineSegment, InteractiveVerticalSpan, Legend, Line, Line, Line, Lollipop, Lollipop, Lollipop, Marker, Marker, Markers, Markers, Markers, OHLC, Phasor, Phasor, Pie, Pie, Plottable, PolarAxis, Polygon, Population, Radar, Radar, Radar, Radar, RadialGaugePlot, Ranges, Rectangle, Rectangle, ScaleBar, Scatter, Scatter, Scatter, Scatter, Scatter, Scatter, ScatterLine, ScatterLine, ScatterLine, ScatterLine, ScatterPoints, ScatterPoints, ScatterPoints, ScatterPoints, Signal, Signal, SignalXY, SignalXY, SmithChartAxis, StackedRanges, Text, Text, Tooltip, Tooltip, TriangularAxis, VectorField, VerticalLine, VerticalSpan

## 九、Interactivity 交互层

- UserActions（用户输入动作）：12 个 → KeyDown, KeyUp, LeftMouseDown, LeftMouseUp, MiddleMouseDown, MiddleMouseUp, MouseMove, MouseWheelDown, MouseWheelUp, RightMouseDown, RightMouseUp, Unknown
- UserActionResponses（响应器文件）：13 个 → DoubleClickBenchmark, DoubleClickResponse, KeyPressResponse, KeyboardAutoscale, KeyboardPanAndZoom, MouseDragPan, MouseDragZoom, MouseDragZoomRectangle, MouseInteractWithPlottables, MouseWheelZoom, SingleClickAutoscale, SingleClickContextMenu, SingleClickResponse
- UserInputProcessor 默认注册：10 个（13 处调用）→ MouseInteractWithPlottables, MouseDragZoomRectangle, MouseDragPan, MouseDragZoom, MouseWheelZoom, SingleClickAutoscale, SingleClickContextMenu, DoubleClickBenchmark, KeyboardPanAndZoom, KeyboardAutoscale

## 十、常用枚举与集合口径

| 枚举/集合 | 个数 |
|---|---:|
| MarkerShape（枚举成员） | 26 |
| ArrowShape（枚举成员） | 8 |
| Edge（枚举成员） | 4 |
| Alignment（枚举成员） | 9 |
| IColormap 实现 | 38 |
| IPalette 实现 | 26 |

Colormap：Algae, Amp, Balance, Blues, Curl, Custom, CustomInterpolated, CustomPalette, Deep, Delta, Dense, Diff, Grayscale, GrayscaleReversed, Greens, Haline, Ice, Inferno, Inverted, InvertedHue, Jet, Magma, Matter, MellowRainbow, Oxy, Phase, Plasma, Rain, Reversed, Solar, Speed, Tarn, Tempo, Thermal, Topo, Turbid, Turbo, Viridis

Palette：Amber, Aurora, Building, Category10, Category20, ColorblindFriendly, ColorblindFriendlyDark, Custom, Dark, DarkPastel, Frost, LightOcean, LightSpectrum, Microcharts, Nero, Nord, Normal, OneHalf, OneHalfDark, PastelWheel, Penumbra, PolarNight, Redness, SnowStorm, SummerSplash, Tsitsulin

## 十一、平台控件（ScottPlot5 Controls）

| 平台项目 | .cs 文件数 | IPlotControl 实现 |
|---|---:|---|
| ScottPlot.Avalonia | 4 | AvaPlot |
| ScottPlot.Blazor | 4 | BlazorPlotBase |
| ScottPlot.Eto | 3 | EtoPlot |
| ScottPlot.Maui | 9 | MauiPlot |
| ScottPlot.OpenGL | 17 | - |
| ScottPlot.WPF | 7 | WpfPlotBase |
| ScottPlot.WinForms | 8 | FormsPlotBase |
| ScottPlot.WinUI | 3 | WinUIPlot |