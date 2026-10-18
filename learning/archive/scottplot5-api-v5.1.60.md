# ScottPlot5 公共 API 签名清单

> ScottPlot5 版本：**5.1.60**（提取自 ScottPlot.csproj，便于跨版本比对）
> 由 `learning/scripts/scottplot5-api.py` 自动生成（声明口径，仅 public；protected/internal 不计入）。

## 摘要

| 命名空间 | 类型数 | 成员数 |
|---|---:|---:|
| `ScottPlot.ArrowShapes` | 8 | 8 |
| `ScottPlot.AutoScalers` | 1 | 12 |
| `ScottPlot.AxisLimitManagers` | 3 | 11 |
| `ScottPlot` | 199 | 2244 |
| `ScottPlot.AxisPanels` | 10 | 61 |
| `ScottPlot.AxisPanels.Experimental` | 1 | 6 |
| `ScottPlot.AxisRules` | 17 | 37 |
| `ScottPlot.Collections` | 1 | 21 |
| `ScottPlot.Colormaps` | 36 | 104 |
| `System.Runtime.CompilerServices` | 2 | 1 |
| `ScottPlot.DataGenerators` | 3 | 6 |
| `ScottPlot.DataSources` | 26 | 243 |
| `ScottPlot.DataViews` | 3 | 9 |
| `ScottPlot.Finance` | 2 | 10 |
| `ScottPlot.FontResolvers` | 2 | 10 |
| `ScottPlot.Grids` | 1 | 15 |
| `ScottPlot.Hatches` | 6 | 9 |
| `ScottPlot.IO` | 1 | 19 |
| `ScottPlot.Interactivity` | 12 | 56 |
| `ScottPlot.Interactivity.UserActionResponses` | 13 | 60 |
| `ScottPlot.Interactivity.UserActions` | 12 | 52 |
| `ScottPlot.LayoutEngines` | 5 | 5 |
| `ScottPlot.LegendLayouts` | 1 | 1 |
| `ScottPlot.MultiplotLayouts` | 5 | 12 |
| `ScottPlot.NamedColors` | 6 | 1182 |
| `ScottPlot.Palettes` | 26 | 106 |
| `ScottPlot.Panels` | 4 | 38 |
| `ScottPlot.PathStrategies` | 4 | 5 |
| `ScottPlot.PlotStyles` | 2 | 2 |
| `ScottPlot.Plottables` | 60 | 1096 |
| `ScottPlot.Plottables.Interactive` | 10 | 163 |
| `ScottPlot.Plottables.Interactive.SubplotPreRenderActions` | 1 | 2 |
| `ScottPlot.Rendering.RenderActions` | 25 | 25 |
| `ScottPlot.Rendering` | 1 | 16 |
| `ScottPlot.Reporting` | 3 | 18 |
| `ScottPlot.StarAxes` | 3 | 7 |
| `ScottPlot.Statistics` | 8 | 79 |
| `ScottPlot.Statistics.Tests` | 1 | 7 |
| `ScottPlot.Stylers` | 2 | 9 |
| `ScottPlot.Testing` | 4 | 55 |
| `ScottPlot.TickGenerators` | 15 | 71 |
| `ScottPlot.TickGenerators.Financial` | 5 | 6 |
| `ScottPlot.TickGenerators.TimeUnits` | 9 | 45 |
| `ScottPlot.Triangulation` | 12 | 69 |

**合计：580 个类型，6036 个成员（conversion 1，ctor 218，field 199，indexer 1，method 1995，operator 41，property 3581），其中 999 项带官方 /// 注释摘要**

## ScottPlot.ArrowShapes

### `public class Arrowhead : IArrowShape`
<!-- ArrowShapes\Arrowhead.cs -->

```csharp
public class Arrowhead : IArrowShape
public void Render(RenderPack rp, PixelLine arrowLine, ArrowStyle arrowStyle)
```

### `public class ArrowheadLine : IArrowShape`
<!-- ArrowShapes\ArrowheadLine.cs -->

```csharp
public class ArrowheadLine : IArrowShape
public void Render(RenderPack rp, PixelLine arrowLine, ArrowStyle arrowStyle)
```

### `public class Chevron : IArrowShape`
<!-- ArrowShapes\Chevron.cs -->

```csharp
public class Chevron : IArrowShape
public void Render(RenderPack rp, PixelLine arrowLine, ArrowStyle arrowStyle)
```

### `public class Double : IArrowShape`
<!-- ArrowShapes\Double.cs -->

```csharp
public class Double : IArrowShape
public void Render(RenderPack rp, PixelLine arrowLine, ArrowStyle arrowStyle)
```

### `public class DoubleLine : IArrowShape`
<!-- ArrowShapes\DoubleLine.cs -->

```csharp
public class DoubleLine : IArrowShape
public void Render(RenderPack rp, PixelLine arrowLine, ArrowStyle arrowStyle)
```

### `public class Pentagon : IArrowShape`
<!-- ArrowShapes\Pentagon.cs -->

```csharp
public class Pentagon : IArrowShape
public void Render(RenderPack rp, PixelLine arrowLine, ArrowStyle arrowStyle)
```

### `public class Single : IArrowShape`
<!-- ArrowShapes\Single.cs -->

```csharp
public class Single : IArrowShape
public void Render(RenderPack rp, PixelLine arrowLine, ArrowStyle arrowStyle)
```

### `public class SingleLine : IArrowShape`
<!-- ArrowShapes\SingleLine.cs -->

```csharp
public class SingleLine : IArrowShape
public void Render(RenderPack rp, PixelLine arrowLine, ArrowStyle arrowStyle)
```

## ScottPlot.AutoScalers

### `public class FractionalAutoScaler : IAutoScaler`
<!-- AutoScalers\FractionalAutoScaler.cs -->

```csharp
public class FractionalAutoScaler : IAutoScaler
public double LeftFraction { get, set; }
public double RightFraction { get, set; }
public double BottomFraction { get, set; }
public double TopFraction { get, set; }
public bool InvertedX { get, set; }
public bool InvertedY { get, set; }
// Pad the data area with the given fractions of whitespace. A value of 0.1 means 10% padding (5% on each side of the data area).
public FractionalAutoScaler(double horizontal = .1, double vertical = .15)
// Pad each side of the data area with the exact fraction of whitespace. 0.05 means 5% whitespace on that side of the data area.
public FractionalAutoScaler(double left, double right, double bottom, double top)
public void SetMarginsX(double horizontal = .1)
public void SetMarginsY(double vertical = .15)
public void AutoScaleAll(IEnumerable<IPlottable> plottables)
public AxisLimits GetAxisLimits(Plot plot, IXAxis xAxis, IYAxis yAxis)
```

## ScottPlot.AxisLimitManagers

### `public class FixedWidth : IAxisLimitManager`
<!-- AxisLimitManagers\FixedWidth.cs -->

```csharp
public class FixedWidth : IAxisLimitManager
// Fractional amount to expand the axis vertically if data runs outside the current view
public double ExpandFractionY = 0.5
public CoordinateRange GetRangeX(CoordinateRange viewRangeX, CoordinateRange dataRangeX)
public CoordinateRange GetRangeY(CoordinateRange viewRangeY, CoordinateRange dataRangeY)
```

### `public class Full : IAxisLimitManager`
<!-- AxisLimitManagers\Full.cs -->
> Show the entire range of data, changing the axis limits only when the data extends outside the current view.

```csharp
public class Full : IAxisLimitManager
// Defines the amount of whitespace added to the right of the data when data runs outside the current view. 1.0 for a view that tightly fits the data and is always changing. 2.0 for a view that doubles the horizontal span when new data runs outside the current view.
public double ExpansionRatio { get, set; }
public CoordinateRange GetRangeX(CoordinateRange viewRangeX, CoordinateRange dataRangeX)
public CoordinateRange GetRangeY(CoordinateRange viewRangeY, CoordinateRange dataRangeY)
```

### `public class Slide : IAxisLimitManager`
<!-- AxisLimitManagers\Slide.cs -->
> Slide the view to the right to keep the newest data points in view

```csharp
public class Slide : IAxisLimitManager
// Amount of horizontal area to display (in axis units)
public double Width { get, set; }
// Defines the amount of whitespace added to the right of the data when data runs outside the current view. 0 for a view that slides every time new data is added 1 for a view that only slides forward when new data runs off the screen
public double PaddingFractionX = 0
// Defines the amount of whitespace added to the top or bottom of the data when data runs outside the current view. 0 sets axis limits to tightly fit the data height 1 sets axis limits to double the vertical span in the direction of the vertical overflow
public double PaddingFractionY = .5
public CoordinateRange GetRangeX(CoordinateRange viewRangeX, CoordinateRange dataRangeX)
public CoordinateRange GetRangeY(CoordinateRange viewRangeY, CoordinateRange dataRangeY)
```

## ScottPlot

### `public enum Alignment { UpperLeft, UpperCenter, UpperRight, MiddleLeft, MiddleCenter, MiddleRight, LowerLeft, LowerCenter, LowerRight, }`
<!-- Primitives\Alignment.cs -->
> Represents the location of a point relative to a rectangle. UpperLeft means the point is at the top left of the rectangle.

```csharp
public enum Alignment { UpperLeft, UpperCenter, UpperRight, MiddleLeft, MiddleCenter, MiddleRight, LowerLeft, LowerCenter, LowerRight, }
成员: UpperLeft, UpperCenter, UpperRight, MiddleLeft, MiddleCenter, MiddleRight, LowerLeft, LowerCenter, LowerRight
```

### `public static class AlignmentExtensions`
<!-- Primitives\Alignment.cs -->

```csharp
public static class AlignmentExtensions
public static Alignment[,] AlignmentMatrix = { {Alignment.UpperLeft, Alignment.UpperCenter, Alignment.UpperRight }, {Alignment.MiddleLeft, Alignment.MiddleCenter, Alignment.MiddleRight }, {Alignment.LowerLeft, Alignment.LowerCenter, Alignment.LowerRight }, }
public static float HorizontalFraction(this Alignment alignment) [扩展方法]
public static float VerticalFraction(this Alignment alignment) [扩展方法]
public static bool IsUpperEdge(this Alignment a) [扩展方法]
public static bool IsLowerEdge(this Alignment a) [扩展方法]
public static bool IsLeftEdge(this Alignment a) [扩展方法]
public static bool IsRightEdge(this Alignment a) [扩展方法]
public static SKTextAlign ToSKTextAlign(this Alignment alignment) [扩展方法]
```

### `public enum AlphaType { Unknown = 0, Opaque, Premultiplied, Unpremultiplied, }`
<!-- Primitives\Image.cs -->

```csharp
public enum AlphaType { Unknown = 0, Opaque, Premultiplied, Unpremultiplied, }
成员: Unknown, Opaque, Premultiplied, Unpremultiplied
```

### `public struct Angle`
<!-- Primitives\Angle.cs -->

```csharp
public struct Angle
public double Degrees { get, set; }
public double Radians { get, set; }
public readonly Angle Inverted
public readonly Angle Normalized { get; }
public static Angle FromDegrees(double degrees)
public static Angle FromRadians(double radians)
public static Angle FromFraction(double fraction, bool clockwise = false)
public static Angle FromFraction(double fraction, Angle start, bool clockwise = false)
public override readonly string ToString()
public static Angle operator +(Angle a)
public static Angle operator -(Angle a)
public static Angle operator +(Angle a, Angle b)
public static Angle operator -(Angle a, Angle b)
public static Angle operator *(Angle a, double b)
public static Angle operator *(double a, Angle b)
public static Angle operator /(Angle a, double b)
public static Angle operator %(Angle a, double b)
public static bool operator ==(Angle a, Angle b)
public static bool operator !=(Angle a, Angle b)
public readonly override bool Equals(object? obj)
public readonly override int GetHashCode()
```

### `public enum ArrowAnchor { Center, Tip, Tail, }`
<!-- Primitives\ArrowAnchor.cs -->

```csharp
public enum ArrowAnchor { Center, Tip, Tail, }
成员: Center, Tip, Tail
```

### `public enum ArrowShape { Single, SingleLine, Double, DoubleLine, Arrowhead, ArrowheadLine, Pentagon, Chevron, }`
<!-- Primitives\ArrowShape.cs -->

```csharp
public enum ArrowShape { Single, SingleLine, Double, DoubleLine, Arrowhead, ArrowheadLine, Pentagon, Chevron, }
成员: Single, SingleLine, Double, DoubleLine, Arrowhead, ArrowheadLine, Pentagon, Chevron
```

### `public static class ArrowShapeExtensions`
<!-- Primitives\ArrowShape.cs -->

```csharp
public static class ArrowShapeExtensions
public static IArrowShape GetShape(this ArrowShape shape) [扩展方法]
```

### `public class ArrowStyle : IHasLine, IHasFill`
<!-- Primitives\ArrowStyle.cs -->

```csharp
public class ArrowStyle : IHasLine, IHasFill
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public Color LineColor { get, set; }
public LinePattern LinePattern { get, set; }
public FillStyle FillStyle { get, set; }
public Color FillColor { get, set; }
public Color FillHatchColor { get, set; }
public IHatch? FillHatch { get, set; }
public ArrowAnchor Anchor { get, set; }
public bool IsVisible { get, set; }
public float ArrowWidth { get, set; }
public float ArrowheadAxisLength { get, set; }
public float ArrowheadLength { get, set; }
public float ArrowheadWidth { get, set; }
// The arrow will always be rendered to be at least this long (in pixels). If too small, its base will move away from the tip.
public float MinimumLength { get, set; }
// The arrow will always be rendered to its length never exceeds this value (in pixels). If too large, its base will move toward the tip.
public float MaximumLength { get, set; }
// Back the arrow away from its tip along its axis by this many pixels
public float Offset { get, set; }
public void ApplyToPaint(Paint paint)
public void Render(SKCanvas canvas, PixelLine line, Paint paint)
```

### `public class Axes : IAxes`
<!-- Primitives\Axes.cs -->
> This object holds an X axis and Y axis and performs 2D coordinate/pixel conversions

```csharp
public class Axes : IAxes
public IXAxis XAxis { get, set; }
public IYAxis YAxis { get, set; }
public PixelRect DataRect { get, set; }
public static Axes Default
public Axes()
public Coordinates GetCoordinates(Pixel pixel)
public double GetCoordinateX(float pixel)
public double GetCoordinateY(float pixel)
public Pixel GetPixel(Coordinates coordinates)
public PixelLine GetPixelLine(CoordinateLine line)
public float GetPixelX(double xCoordinate)
public float GetPixelY(double yCoordinate)
public PixelRect GetPixelRect(CoordinateRect rect)
```

### `public class AxisGradientColorPosition(Color color, double position)`
<!-- Primitives\AxisGradientColorPosition.cs -->
> Defines position of a color in a gradient at a particular position in axis units

```csharp
public class AxisGradientColorPosition(Color color, double position)
public Color Color { get, set; }
public double Position { get, set; }
```

### `public enum AxisGradientDirection { /// <summary> /// Assumes <see cref="AxisGradientColorPosition"/> positions are on the X axis /// </summary> Horizontal, /// <summary> /// Assumes <see cref="AxisGradientColorPosition"/> positions are on the Y axis /// </summary> Vertical, }`
<!-- Primitives\AxisGradientDirection.cs -->
> Describes the direction a is using for its position

```csharp
public enum AxisGradientDirection { /// <summary> /// Assumes <see cref="AxisGradientColorPosition"/> positions are on the X axis /// </summary> Horizontal, /// <summary> /// Assumes <see cref="AxisGradientColorPosition"/> positions are on the Y axis /// </summary> Vertical, }
成员: Horizontal, Vertical
```

### `public readonly struct AxisLimits : IEquatable<AxisLimits>`
<!-- Primitives\AxisLimits.cs -->
> This object represents the rectangular visible area on a 2D coordinate system. It simply stores a but has axis-related methods to act upon it.

```csharp
public readonly struct AxisLimits : IEquatable<AxisLimits>
public double Left { get; }
public double Right { get; }
public double Bottom { get; }
public double Top { get; }
public double HorizontalSpan
public double VerticalSpan
public double HorizontalCenter
public double VerticalCenter
public Coordinates Center
public CoordinateRange XRange
public CoordinateRange YRange
public CoordinateRange HorizontalRange
public CoordinateRange VerticalRange
public CoordinateRect Rect
public static AxisLimits Default { get; }
public bool IsRealX
public bool IsRealY
public bool IsReal
public bool HasArea
public AxisLimits(Coordinates coordinates)
public AxisLimits(CoordinateRect rect)
public AxisLimits(double left, double right, double bottom, double top)
public AxisLimits(CoordinateRange xRange, CoordinateRange yRange)
public AxisLimits(IEnumerable<IPlottable> plottables)
public AxisLimits(IEnumerable<Coordinates> coordinates)
public AxisLimits(IEnumerable<Coordinates3d> coordinates)
public AxisLimits InvertedVertically()
public AxisLimits InvertedHorizontally()
public AxisLimits ExpandedToInclude(AxisLimits otherLimits)
public static AxisLimits FromPoint(double x, double y)
public static AxisLimits FromPoint(Coordinates c)
public override string ToString()
public string ToString(int digits)
public static AxisLimits NoLimits
public static AxisLimits Unset
public static AxisLimits VerticalOnly(double yMin, double yMax)
public static AxisLimits HorizontalOnly(double xMin, double xMax)
// Return a new expanded to include the given and .
public AxisLimits Expanded(double x, double y)
// Return a new expanded to include the given .
public AxisLimits Expanded(Coordinates coordinates)
// Return a new expanded to include all corners of the given .
public AxisLimits Expanded(CoordinateRect rect)
// Return a new expanded to include the area defined by .
public AxisLimits Expanded(AxisLimits limits)
public AxisLimits WithPan(double deltaX, double deltaY)
public AxisLimits WithZoom(double fracX, double fracY)
public AxisLimits WithZoom(double fracX, double fracY, double zoomToX, double zoomToY)
public bool Contains(double x, double y)
public bool Contains(Coordinates pt)
public bool Equals(AxisLimits other)
public override bool Equals(object? obj)
public static bool operator ==(AxisLimits a, AxisLimits b)
public static bool operator !=(AxisLimits a, AxisLimits b)
public override int GetHashCode()
```

### `public readonly struct AxisLimits3d`
<!-- Primitives\AxisLimits3d.cs -->

```csharp
public readonly struct AxisLimits3d
public readonly double XMin
public readonly double XMax
public readonly double YMin
public readonly double YMax
public readonly double ZMin
public readonly double ZMax
public AxisLimits AxisLimits2d
public static AxisLimits3d FromPoints(IEnumerable<Coordinates3d> coordinates)
```

### `public class AxisManager`
<!-- AxisManager.cs -->

```csharp
public class AxisManager
// Logic that determines padding around the data area when is called
public IAutoScaler AutoScaler { get, set; }
// A special panel
public Panels.TitlePanel Title { get; }
// All axes
public IEnumerable<IAxis> GetAxes()
// All X axes
public IEnumerable<IXAxis> GetXAxes()
// All Y axes
public IEnumerable<IYAxis> GetYAxes()
// All axes with the given edge
public IEnumerable<IAxis> GetAxes(Edge edge)
// Returns all axes, panels, and the title
public IPanel[] GetPanels()
// The primary horizontal axis above the plot
public IXAxis Top
// The primary horizontal axis below the plot
public IXAxis Bottom
// The primary vertical axis to the left of the plot
public IYAxis Left
// The primary vertical axis to the right of the plot
public IYAxis Right
// Indicates whether the axis limits have been set (manually or by autoscale)
public bool LimitsHaveBeenSet
// The standard grid that is added when a Plot is created. Users can achieve custom grid functionality by disabling the visibility of this grid and adding their own classes to the List of .
public DefaultGrid DefaultGrid { get, set; }
// List of custom grids. If in use, it is likely the default grid visibility should be disabled.
public List<IGrid> CustomGrids { get; }
// Return the and all
public List<IGrid> AllGrids
// Rules that are applied before each render
public List<IAxisRule> Rules { get; }
// If enabled, AutoScale() will be called at the start of each render. This can negatively impact performance of plots with an extremely large number of data points.
public bool ContinuouslyAutoscale { get, set; }
// When is true, this action is called before each frame is rendered. Users can assign their own static function to customize continuous autoscaling behavior.
public Action<RenderPack> ContinuousAutoscaleAction { get, set; }
public static void DefaultContinuousAutoscaleAction(RenderPack rp)
// Contains state and logic for axes
public AxisManager(Plot plot)
// Apply a single color to the label, tick labels, tick marks, and frame of all axes
public void Color(Color color)
// Apply a single color to the label, tick labels, tick marks, and frame of the specified axis
public void Color(IAxis axis, Color color)
// Set visibility of the frame on every axis
public void Frame(bool enable)
// Set thickness of the frame on every axis
public void FrameWidth(float width)
// Set color of the frame on every axis
public void FrameColor(Color color)
// Remove all axes that lie on the given edge.
public void Remove(Edge edge)
// Remove the given axis from the plot
public void Remove(IAxis axis)
// Remove the given Panel
public void Remove(IPanel panel)
public void AddPanel(IPanel panel)
// Remove all bottom axes, create a DateTime bottom axis, add it to the plot, and return it.
public DateTimeXAxis DateTimeTicksBottom()
// Remove all bottom axes, create a numeric bottom axis, add it to the plot, and return it.
public BottomAxis NumericTicksBottom()
public Plottables.TickModifierLabel SetupMultiplierNotation(IAxis axis)
public void AddYAxis(IYAxis axis)
public void AddXAxis(IXAxis axis)
// Crete a new axis, add it to the plot, and return it
public LeftAxis AddLeftAxis()
public void AddLeftAxis(IYAxis axis)
// Crete a new axis, add it to the plot, and return it
public RightAxis AddRightAxis()
public void AddRightAxis(IYAxis axis)
// Crete a new axis, add it to the plot, and return it
public BottomAxis AddBottomAxis()
public void AddBottomAxis(IXAxis axis)
// Crete a new axis, add it to the plot, and return it
public TopAxis AddTopAxis()
public void AddTopAxis(IXAxis axis)
public void SetLimitsX(double left, double right, IXAxis xAxis)
public void SetLimitsY(double bottom, double top, IYAxis yAxis)
public void SetLimitsX(double left, double right)
public void SetLimitsY(double bottom, double top)
public void SetLimits(double left, double right, double bottom, double top)
public void SetLimits(double left, double right, double bottom, double top, IXAxis xAxis, IYAxis yAxis)
public void SetLimits(double? left = null, double? right = null, double? bottom = null, double? top = null)
public void SetLimits(CoordinateRect rect)
public void SetLimitsX(CoordinateRect limits)
public void SetLimitsY(CoordinateRect limits)
public void SetLimitsX(AxisLimits limits)
public void SetLimitsX(AxisLimits limits, IXAxis xAxis)
public void SetLimitsY(AxisLimits limits)
public void SetLimitsY(AxisLimits limits, IYAxis yAxis)
public void SetLimits(AxisLimits limits)
public void SetLimits(AxisLimits limits, IXAxis xAxis, IYAxis yAxis)
public void SetLimits(CoordinateRange xRange, CoordinateRange yRange)
// Adjust the horizontal axis so values descend from left to right
public void InvertX()
// Adjust the horizontal axis so values ascend from left to right
public void RectifyX()
// Adjust the vertical axis so values descend from bottom to top
public void InvertY()
// Adjust the vertical axis so values ascend from bottom to top
public void RectifyY()
// Return the 2D axis limits for the default axes
public AxisLimits GetLimits()
// Return the 2D axis limits for the given X/Y axis pair
public AxisLimits GetLimits(IXAxis xAxis, IYAxis yAxis)
// Return the 2D axis limits for the given X/Y axis pair
public AxisLimits GetLimits(IAxes axes)
// Return the 2D axis limits of data for all plottables using the default axes
public AxisLimits GetDataLimits()
// Return the 2D axis limits of data for all plottables using the given axes
public AxisLimits GetDataLimits(IXAxis xAxis, IYAxis yAxis)
// Adds the default X and Y axes to all plottables with unset axes
public void ReplaceNullAxesWithDefaults()
// Automatically scale all axes to fit the data in all plottables
public void AutoScale(bool? invertX = null, bool? invertY = null)
// Autoscale the given axes to accommodate the data from all plottables that use them
public void AutoScale(IXAxis xAxis, IYAxis yAxis, bool horizontal = true, bool vertical = true)
// Automatically expand the default axes to fit the data in all plottables.
public void AutoScaleExpand()
// Automatically expand the provided axes to fit the data in all plottables.
public void AutoScaleExpand(IXAxis xAxis, IYAxis yAxis)
// Automatically expand the provided axes horizontally to fit the data in all plottables.
public void AutoScaleExpandX(IXAxis xAxis)
// Automatically expand the default horizontal axis to fit the data in all plottables.
public void AutoScaleExpandX()
// Automatically expand the provided axes vertically to fit the data in all plottables.
public void AutoScaleExpandY(IYAxis yAxis)
// Automatically expand the default vertical axis to fit the data in all plottables.
public void AutoScaleExpandY()
// Autoscale the bottom horizontal axis limits to fit the data of all plotted objects
public void AutoScaleX()
// Autoscale the left vertical axis limits to fit the data of all plotted objects
public void AutoScaleY()
// Autoscale the supplied horizontal axis limits to fit the data of all plotted objects
public void AutoScaleX(IXAxis xAxis)
// Autoscale the supplied vertical axis limits to fit the data of all plotted objects
public void AutoScaleY(IYAxis yAxis)
// Autoscale the default (left and bottom) axis limits to fit the data of the supplied plottables
public void AutoScale(IEnumerable<IPlottable> plottables)
// Autoscale the default bottom horizontal axis limits to fit the data of the supplied plottables
public void AutoScaleX(IEnumerable<IPlottable> plottables)
// Autoscale the default left vertical axis limits to fit the data of the supplied plottables
public void AutoScaleY(IEnumerable<IPlottable> plottables)
// Adjust limits all axes to pan the pixel distance between two points
public void Pan(Pixel mouseDown, Pixel mouseUp)
// Adjust limits all axes to pan given pixel distance
public void Pan(PixelOffset offset)
// Adjust limits all axes to pan by the given distance in coordinate space
public void Pan(CoordinateOffset distance)
// Modify zoom for all axes as if the mouse were right-clicked and dragged
public void Zoom(Pixel px1, Pixel px2)
// Zoom into (frac >1) or out of (frac <1) the given point.
public void Zoom(Pixel px, double fracX, double fracY)
// Modify limits of all axes to apply the given zoom. Fractional values >1 zoom in and <1 zoom out.
public void Zoom(double fracX = 1.0, double fracY = 1.0)
// Modify limits of all axes to apply the given zoom. Fractional values >1 zoom in and <1 zoom out.
public void ZoomIn(double fracX = 1.0, double fracY = 1.0)
// Zoom out so the new view is the given fraction of the original view
public void ZoomOut(double x = 1.0, double y = 1.0)
// Zoom out so the new view is the given fraction of the original view
public void ZoomOutX(double x = 1.0)
// Zoom out so the new view is the given fraction of the original view
public void ZoomOutY(double y = 1.0)
// Reset plot data margins to their default value.
public void Margins()
// Define the amount of whitespace to place around the data area when calling . Values are a fraction from 0 (tightly fit the data) to 1 (lots of whitespace).
public void Margins(double horizontal = 0.1, double vertical = .15)
// Define the amount of whitespace to place on the left and right of the data area when calling . Values are a fraction from 0 (tightly fit the data) to 1 (lots of whitespace).
public void MarginsX(double horizontal = 0.1)
// Define the amount of whitespace to place on the bottom and top of the data area when calling . Values are a fraction from 0 (tightly fit the data) to 1 (lots of whitespace).
public void MarginsY(double vertical = 0.15)
// Auto-scale to tightly fit the data so there is no spacing between data points and the edge of the data area
public void TightMargins()
// Define the amount of whitespace to place around the data area when calling . Values are a fraction from 0 (tightly fit the data) to 1 (lots of whitespace).
public void Margins(double left = .05, double right = .05, double bottom = .07, double top = .07)
// Force pixels to have a 1:1 scale ratio. This allows circles to always appear as circles and not stretched ellipses.
public void SquareUnits()
// If true, force pixels to have a 1:1 scale ratio. This allows circles to always appear as circles and not stretched ellipses. If false, disable axis rules related to square units and restore default behavior.
public void SquareUnits(bool enable)
// Helper method to set visibility of all axes and title panels. Hiding all panels allows the data area to the extend to the edge of the figure. This method hides the title, but call "Plot.Title()" to re-enable it.
public void Frameless(bool hideAllPanels = true)
// Set anti-aliasing for axis frames, tick marks, and grid lines
public void AntiAlias(bool enable)
// Hairline mode causes lines to always render exactly 1 pixel wide regardless of . This function controls hairline behavior for all axis frames. tick marks, and grid lines.
public void Hairline(bool enable)
// Add a link to another plot's axis so its limits update when limits of an axis from this plot changes
public void Link(IAxis thisPlotAxis, IAxis otherPlotAxis, Plot otherPlot)
// Add a link to the target plot control so its axis limits update when this plot's axis limits change
public void Link(IPlotControl target, bool x = true, bool y = true)
// Add a link to the target plot so its axis limits update when this plot's axis limits change
public void Link(Plot target, bool x = true, bool y = true)
// Remove all linked axes rules
public void UnlinkAll()
// Remove all linked axes rules involving the target plot control
public void Unlink(IPlotControl target)
// Remove all linked axes rules involving the target plot
public void Unlink(Plot target)
// Remove all linked axes rules involving the given axis
public void Unlink(IAxis axis)
// This is called in the render system after AxisLimitsChanged has been invoked
public void ApplyLinkedAxisRules()
```

### `public class AxisSpanUnderMouse`
<!-- Primitives\AxisSpanUnderMouse.cs -->

```csharp
public class AxisSpanUnderMouse
public required Plottables.AxisSpan Span
public required Coordinates MouseStart
public required CoordinateRange OriginalRange
public bool ResizeEdge1
public bool ResizeEdge2
public bool IsResizing
public bool IsMoving
public bool IsResizingVertically
public bool IsResizingHorizontally
public void DragTo(Coordinates mouseNow)
```

### `public class BackgroundStyle : IDisposable`
<!-- Primitives\BackgroundStyle.cs -->

```csharp
public class BackgroundStyle : IDisposable
public Color Color { get, set; }
public FillStyle FillStyle { get, set; }
public ImagePosition ImagePosition { get, set; }
public bool AntiAlias = true
public Image? _Image
public Image? Image { get, set; }
public void Dispose()
public PixelRect GetImageRect(PixelRect targetRect)
public void Render(RenderPack rp, PixelRect target)
```

### `public class Bar : IHasFill, IHasLine`
<!-- Primitives\Bar.cs -->
> Represents a single bar in a bar chart

```csharp
public class Bar : IHasFill, IHasLine
// Position (not the value) of the bar. Increment position of successive bars so they do not overlap. For simple bar plots, position of successive bars is 1, 2, 3, etc. on the horizontal axis.
public double Position { get, set; }
// The value this bar represents. This is the top of the bar for bars representing positive values.
public double Value { get, set; }
// The position where the bar begins. This is the bottom of the bar for bars representing positive values. Typically this is zero, so bars extend from zero toward their value.
public double ValueBase { get, set; }
// Thickness of the bar in the same units as . Typically the size of each bar is equal to or less than the difference in between adjacent bars.
public double Size { get, set; }
// Size of the error bar extending from
public double Error { get, set; }
// Width of the error bar whiskers in axis units (same units as )
public double ErrorSize { get, set; }
public bool IsVisible { get, set; }
public FillStyle FillStyle { get, set; }
public Color FillHatchColor { get, set; }
public IHatch? FillHatch { get, set; }
public Color FillColor { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public Color BorderColor { get, set; }
public float BorderLineWidth { get, set; }
public float ErrorLineWidth { get, set; }
public bool ErrorPositive { get, set; }
public bool ErrorNegative { get, set; }
// Text to display on, above, or below the bar. Typically this is the string representation of the value of the bar.
public string Label { get, set; }
// If enabled, labels will be rendered last (after all other plottables)
public bool LabelOnTop { get, set; }
// Text to display on, above, or below the bar. Typically this is the string representation of the value of the bar.
public string ValueLabel { get, set; }
// Enabling this causes the value label to be rendered in the center of the bar
public bool CenterLabel { get, set; }
// Place the value label this many pixels away from the edge of the bar
public float LabelOffset { get, set; }
// Labels for bars less than this value will be displayed beneath the bar. Set this value to negative infinity to force labels to be always on top of the bar.
public double LabelInvertWhenValueBelow = 0
public Orientation Orientation { get, set; }
public CoordinateRect Rect { get; }
public IEnumerable<CoordinateLine> ErrorLines { get; }
public AxisLimits AxisLimits { get; }
public void Render(RenderPack rp, IAxes axes, LabelStyle labelStyle)
public void RenderBody(RenderPack rp, IAxes axes)
public void RenderText(RenderPack rp, IAxes axes, LabelStyle labelStyle)
```

### `public class BarSeries`
<!-- Primitives\BarSeries.cs -->
> Holds a collection of bars which are all styled the same and have a common label

```csharp
public class BarSeries
public IList<Bar> Bars { get, set; }
public string? Label { get, set; }
public Color Color { get, set; }
```

### `public sealed class BinarySearchComparer : IComparer<Coordinates>, IComparer<double>, IComparer<RootedCoordinateVector>, IComparer<RootedPixelVector>`
<!-- BinarySearchComparer.cs -->
> for various types provided by ScottPlot

```csharp
public sealed class BinarySearchComparer : IComparer<Coordinates>, IComparer<double>, IComparer<RootedCoordinateVector>, IComparer<RootedPixelVector>
// Thread-Safe singleton
public static readonly BinarySearchComparer Instance = new()
public static IComparer<T> GetComparer<T>()
public int Compare(Coordinates a, Coordinates b)
public int Compare(double a, double b)
public int Compare(RootedPixelVector x, RootedPixelVector y)
public int Compare(RootedCoordinateVector x, RootedCoordinateVector y)
```

### `public class Box : IHasFill, IHasLine`
<!-- Primitives\Box.cs -->
> Holds values for drawing a box-and-whisker symbol

```csharp
public class Box : IHasFill, IHasLine
public double Position { get, set; }
public double BoxMin { get, set; }
public double BoxMax { get, set; }
public double? BoxMiddle { get, set; }
public double? WhiskerMin { get, set; }
public double? WhiskerMax { get, set; }
public double Width { get, set; }
public double WhiskerSizeFraction { get, set; }
public double WhiskerSize
public Orientation Orientation { get, set; }
public bool IsVisible { get, set; }
public FillStyle FillStyle { get, set; }
public Color FillColor { get, set; }
public Color FillHatchColor { get, set; }
public IHatch? FillHatch { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public FillStyle Fill { get, set; }
public LineStyle Stroke { get, set; }
public AxisLimits GetAxisLimits()
public void Render(RenderPack rp, IAxes axes)
```

### `public class CanvasState(SKCanvas canvas)`
<!-- Primitives\CanvasState.cs -->
> This object manages wraps a SKCanvas and manages calls to SkiaSharp methods to ensure state is tracked across complex render systems.

```csharp
public class CanvasState(SKCanvas canvas)
// Number of times was called without
public int SaveLevels { get, set; }
// Save the current state of the canvas. This state can be recalled by calling .
public void Save()
// Restore the canvas to the state the last time was called. This method will throw if a canvas is restored more times than it was saved. Use the method to restore a canvas to its original state if the number of saves is unknown.
public void Restore()
// Restore the canvas to its original state, regardless of how many times was called.
public void RestoreAll()
// Restore the canvas to its original state. Disables all clipping and transformations.
public void DisableClipping()
// Clip the canvas so drawing will only occur within the given rectangle.
public void Clip(PixelRect rect)
public void Translate(float dX, float dY)
public void Translate(Pixel delta)
public void RotateDegrees(double degrees)
public void RotateDegrees(double degrees, Pixel px)
public void RotateRadians(double radians)
public void RotateRadians(double radians, Pixel px)
```

### `public readonly struct Color`
<!-- Primitives\Color.cs -->

```csharp
public readonly struct Color
public readonly byte Red
public readonly byte Green
public readonly byte Blue
public readonly byte Alpha
public byte R
public byte G
public byte B
public byte A
public uint ARGB { get; }
public double Opacity { get; }
public uint PremultipliedARGB { get; }
public override string ToString()
public Color(byte red, byte green, byte blue, byte alpha = 255)
public Color(float red, float green, float blue, float alpha = 1)
public Color(string hexCode) : this(Hex2Argb(hexCode))
public Color(uint argb)
public Color(SKColor color)
public Color(System.Drawing.Color color)
public static bool operator ==(Color a, Color b)
public static bool operator !=(Color a, Color b)
public override int GetHashCode()
public override bool Equals(object? obj)
public readonly Color WithRed(byte red)
public readonly Color WithGreen(byte green)
public readonly Color WithBlue(byte blue)
public readonly Color WithAlpha(byte alpha)
public readonly Color WithAlpha(double alpha)
public readonly Color WithOpacity(double opacity = .5)
public static Color Gray(byte value)
public static Color FromARGB(int argb)
public static Color FromARGB(uint argb)
public static Color FromHex(string hex)
public static Color FromHtml(string html)
// Create a collection of colors from a collection of hex strings formatted like "#66AA99"
public static Color[] FromHex(IEnumerable<string> hex)
// Create a ScottPlot color from a System Drawing Color
public static Color FromColor(System.Drawing.Color color)
// return a string like "#6699AA" or "#6699AA42" if a semitransparent alpha is in use
public string ToHex()
// Create a ScottPlot color from a SkiaSharp Color
public static Color FromSKColor(SKColor skcolor)
// Create a ScottPlot color from a System Drawing Color
public static Color FromSDColor(System.Drawing.Color sdColor)
// return a string like "#6699AA"
public string ToStringRGB()
// return a string like "#6699AAFF"
public string ToStringRGBA()
// Create a SkiaSharp color
public SkiaSharp.SKColor ToSKColor()
// Create a System Drawing color
public System.Drawing.Color ToSDColor()
// Luminance as a fraction from 0 to 1
public float Luminance
// Hue as a fraction from 0 to 1
public float Hue
// Saturation as a fraction from 0 to 1
public float Saturation
// Hue, Saturation, and Luminance (as fractions from 0 to 1)
public (float h, float s, float l) ToHSL()
// Create a Color given Hue, Saturation, and Luminance (as fractions from 0 to 1)
public static Color FromHSL(float hue, float saturation, float luminosity, float alpha = 1)
public Color WithLightness(float lightness = .5f)
// Amount to lighten the color (from 0-1). Larger numbers produce lighter results.
public Color Lighten(double fraction = .5f)
// Amount to darken the color (from 0-1). Larger numbers produce darker results.
public Color Darken(double fraction = .5f)
public Color Inverted()
public Color InvertedHue()
// Return this color mixed with another color.
public Color MixedWith(Color otherColor, double fraction)
public Color InterpolateRgb(Color c1, double fraction)
public Color[] InterpolateArrayRgb(Color c1, int steps)
static public Color InterpolateRgb(Color c1, Color c2, double fraction)
static public Color[] InterpolateRgbArray(Color c1, Color c2, int steps)
public static Color RandomHue()
public static System.Drawing.Color ToColor(ScottPlot.Color color)
```

### `public static class Colormap`
<!-- Primitives\Colormap.cs -->

```csharp
public static class Colormap
public static IColormap Default { get, set; }
// Return an array containing every available colormap
public static IColormap[] GetColormaps()
public static Image GetImage(IColormap colormap, int width, int height)
public static IColormap FromColors(Color[] colors, bool smooth = true)
```

### `public struct Colors`
<!-- Primitives\Colors.cs -->

```csharp
public struct Colors
public static Color AliceBlue
public static Color AntiqueWhite
public static Color Aqua
public static Color Aquamarine
public static Color Azure
public static Color Beige
public static Color Bisque
public static Color Black
public static Color BlanchedAlmond
public static Color Blue
public static Color BlueViolet
public static Color Brown
public static Color BurlyWood
public static Color CadetBlue
public static Color Chartreuse
public static Color Chocolate
public static Color Coral
public static Color CornflowerBlue
public static Color Cornsilk
public static Color Crimson
public static Color Cyan
public static Color DarkBlue
public static Color DarkCyan
public static Color DarkGoldenRod
public static Color DarkGray
public static Color DarkGrey
public static Color DarkGreen
public static Color DarkKhaki
public static Color DarkMagenta
public static Color DarkOliveGreen
public static Color DarkOrange
public static Color DarkOrchid
public static Color DarkRed
public static Color DarkSalmon
public static Color DarkSeaGreen
public static Color DarkSlateBlue
public static Color DarkSlateGray
public static Color DarkSlateGrey
public static Color DarkTurquoise
public static Color DarkViolet
public static Color DeepPink
public static Color DeepSkyBlue
public static Color DimGray
public static Color DimGrey
public static Color DodgerBlue
public static Color FireBrick
public static Color FloralWhite
public static Color ForestGreen
public static Color Fuchsia
public static Color Gainsboro
public static Color GhostWhite
public static Color Gold
public static Color GoldenRod
public static Color Gray
public static Color Grey
public static Color Green
public static Color GreenYellow
public static Color HoneyDew
public static Color HotPink
public static Color IndianRed
public static Color Indigo
public static Color Ivory
public static Color Khaki
public static Color Lavender
public static Color LavenderBlush
public static Color LawnGreen
public static Color LemonChiffon
public static Color LightBlue
public static Color LightCoral
public static Color LightCyan
public static Color LightGoldenRodYellow
public static Color LightGray
public static Color LightGrey
public static Color LightGreen
public static Color LightPink
public static Color LightSalmon
public static Color LightSeaGreen
public static Color LightSkyBlue
public static Color LightSlateGray
public static Color LightSlateGrey
public static Color LightSteelBlue
public static Color LightYellow
public static Color Lime
public static Color LimeGreen
public static Color Linen
public static Color Magenta
public static Color Maroon
public static Color MediumAquaMarine
public static Color MediumBlue
public static Color MediumOrchid
public static Color MediumPurple
public static Color MediumSeaGreen
public static Color MediumSlateBlue
public static Color MediumSpringGreen
public static Color MediumTurquoise
public static Color MediumVioletRed
public static Color MidnightBlue
public static Color MintCream
public static Color MistyRose
public static Color Moccasin
public static Color NavajoWhite
public static Color Navy
public static Color OldLace
public static Color Olive
public static Color OliveDrab
public static Color Orange
public static Color OrangeRed
public static Color Orchid
public static Color PaleGoldenRod
public static Color PaleGreen
public static Color PaleTurquoise
public static Color PaleVioletRed
public static Color PapayaWhip
public static Color PeachPuff
public static Color Peru
public static Color Pink
public static Color Plum
public static Color PowderBlue
public static Color Purple
public static Color RebeccaPurple
public static Color Red
public static Color RosyBrown
public static Color RoyalBlue
public static Color SaddleBrown
public static Color Salmon
public static Color SandyBrown
public static Color SeaGreen
public static Color SeaShell
public static Color Sienna
public static Color Silver
public static Color SkyBlue
public static Color SlateBlue
public static Color SlateGray
public static Color SlateGrey
public static Color Snow
public static Color SpringGreen
public static Color SteelBlue
public static Color Tan
public static Color Teal
public static Color Thistle
public static Color Tomato
public static Color Transparent
public static Color Turquoise
public static Color Violet
public static Color Wheat
public static Color White
public static Color WhiteSmoke
public static Color Yellow
public static Color YellowGreen
public static Color C0
public static Color C1
public static Color C2
public static Color C3
public static Color C4
public static Color C5
public static Color C6
public static Color C7
public static Color C8
public static Color C9
readonly static public Color[] Category10 = new Category10().Colors
readonly static public Color[] Category20 = new Category20().Colors
readonly static public Color[] ColorblindFriendly = new ColorblindFriendly().Colors
readonly static public Color[] ColorblindFriendlyDark = new ColorblindFriendlyDark().Colors
public static Color ScottPlotPurple
public static Color ScottPlotPink
// Return a collection of colors with random hues. Because hues are random, near-matches may be present.
public static Color[] RandomHue(int count)
// Return a collection of colors with maximum saturation and evenly-spaced hues
public static IEnumerable<Color> Rainbow(int count)
public static List<(string, Color)> GetNamedColors()
```

### `public class Windows : NamedColors.WindowsStandardColors`（嵌套于 Colors）
> Default Windows Colors

```csharp
public class Windows : NamedColors.WindowsStandardColors
```

### `public class Xkcd : NamedColors.XkcdColors`（嵌套于 Colors）
> Colors from the xkcd color name survey https://xkcd.com/color/rgb/

```csharp
public class Xkcd : NamedColors.XkcdColors
```

### `public enum ConnectStyle { /// <summary> /// Connect points with straight lines /// </summary> Straight, /// <summary> /// Connect points with a line horizontally, then vertically /// </summary> StepHorizontal, /// <summary> /// Connect points with a line vertically, then horizontally /// </summary> StepVertical, }`
<!-- Primitives\ConnectStyle.cs -->

```csharp
public enum ConnectStyle { /// <summary> /// Connect points with straight lines /// </summary> Straight, /// <summary> /// Connect points with a line horizontally, then vertically /// </summary> StepHorizontal, /// <summary> /// Connect points with a line vertically, then horizontally /// </summary> StepVertical, }
成员: Straight, StepHorizontal, StepVertical
```

### `public struct ContextMenuItem`
<!-- Primitives\ContextMenuItem.cs -->
> Represents a single item in a right-click pop-up menu

```csharp
public struct ContextMenuItem
public bool IsSeparator { get, set; }
public string Label { get, set; }
public Action<Plot> OnInvoke { get, set; }
```

### `public record struct ContourLine(CoordinatePath Path, double Z)`
<!-- Primitives\ContourLine.cs -->

```csharp
public record struct ContourLine(CoordinatePath Path, double Z)
```

### `public readonly struct CoordinateLine`
<!-- Primitives\CoordinateLine.cs -->
> Represents a straight line in coordinate space

```csharp
public readonly struct CoordinateLine
public readonly double X1
public readonly double X2
public readonly double Y1
public readonly double Y2
public readonly double XMin
public readonly double XMax
public readonly double YMin
public readonly double YMax
public double XSpan
public double YSpan
public double Slope
public double SlopeRadians
public double SlopeDegrees
public double YIntercept
public float Length
public Coordinates Start
public Coordinates End
public Coordinates Center
public CoordinateLine(double x1, double y1, double x2, double y2)
public CoordinateLine(Coordinates pt1, Coordinates pt2)
public CoordinateLine(double x, double y, double slope)
public CoordinateLine(Coordinates point, double slope)
public override string ToString()
// Adjust the line to fit within the boundaries of the given rectangle. The slope and Y intercept will not be changed.
public CoordinateLine ExtendTo(CoordinateRect rect)
// Return the X position on the line at the given Y
public double X(double y = 0)
// Return the Y position on the line at the given X
public double Y(double x = 0)
public CoordinateLine WithDelta(double dX, double dY)
public CoordinateLine Reversed()
public CoordinateRect BoundingBox()
```

### `public readonly struct CoordinateOffset(double x, double y)`
<!-- Primitives\CoordinateOffset.cs -->

```csharp
public readonly struct CoordinateOffset(double x, double y)
public double X { get; }
public double Y { get; }
```

### `public readonly struct CoordinatePath(Coordinates[] points, bool close)`
<!-- Primitives\CoordinatePath.cs -->

```csharp
public readonly struct CoordinatePath(Coordinates[] points, bool close)
public readonly Coordinates[] Points = points
public readonly bool Close = close
public static CoordinatePath Closed(Coordinates[] points)
public static CoordinatePath Open(Coordinates[] points)
public static CoordinatePath Closed(IEnumerable<Coordinates> points)
public static CoordinatePath Open(IEnumerable<Coordinates> points)
```

### `public readonly struct CoordinateRange(double value1, double value2)`
<!-- Primitives\CoordinateRange.cs -->
> Represents a range of values between a pair of bounding coordinates on a single axis. Inverted ranges are permitted, but is always less than and indicates whether this range is inverted.

```csharp
public readonly struct CoordinateRange(double value1, double value2)
public readonly double Value1 = value1
public readonly double Value2 = value2
public readonly double Min = Math.Min(value1, value2)
public readonly double Max = Math.Max(value1, value2)
public readonly bool IsInverted = value1 > value2
// Distance from to (may be negative)
public double Span
// Value located in the center of the range, between and (may be negative)
public double Center
// Distance from to (always positive)
public double Length
// Return the present range rectified so is not greater than
public CoordinateRange Rectified()
public override string ToString()
// This magic value is used to indicate the range has not been set. It is equal to an inverted infinite range [∞, -∞]
public static CoordinateRange NotSet
// This magic value is used to indicate the range has no defined limits. It is equal to an inverted infinite range [NaN, NaN]
public static CoordinateRange NoLimits
// Returns true if the given position is within the range (inclusive)
public bool Contains(double value)
// Indicates whether two ranges have any overlapping values
public bool Overlaps(CoordinateRange other)
// Return the range of values spanned by the given collection (ignoring NaN)
public static CoordinateRange Extrema(IEnumerable<double> values)
// Return a new range expanded to include the given point
public CoordinateRange Expanded(double value)
public bool Equals(CoordinateRange other)
public static bool operator ==(CoordinateRange a, CoordinateRange b)
public static bool operator !=(CoordinateRange a, CoordinateRange b)
public override bool Equals(object? obj)
public override int GetHashCode()
```

### `public class CoordinateRangeMutable : IEquatable<CoordinateRangeMutable> // TODO: rename to MutableCoordinateRange or something`
<!-- Primitives\CoordinateRangeMutable.cs -->
> Represents a range of values between two coordinates on a single axis

```csharp
public class CoordinateRangeMutable : IEquatable<CoordinateRangeMutable> // TODO: rename to MutableCoordinateRange or something
public double Min { get, set; }
public double Max { get, set; }
public double Center
public double Span
public bool HasBeenSet
public CoordinateRange ToCoordinateRange
public CoordinateRange ToRectifiedCoordinateRange
public CoordinateRangeMutable(double min, double max)
public static CoordinateRangeMutable Infinity
public override string ToString()
// Returns true if the given position is within the range (inclusive)
public bool Contains(double position)
// Expand the range if needed to include the given point
public void Expand(double value)
// Expand this range if needed to ensure the given range is included
public void Expand(CoordinateRangeMutable range)
// Expand this range if needed to ensure the given range is included
public void Expand(CoordinateRange range)
// This infinite inverted range is used to indicate a range that has not yet been set
public static CoordinateRangeMutable NotSet
// Reset this range to inverted infinite values to indicate the range has not yet been set
public void Reset()
public void Set(double min, double max)
public void Set(CoordinateRange range)
public void Set(CoordinateRangeMutable range)
public void Set(IAxis otherAxis)
public void Pan(double delta)
public void PanMouse(float mouseDeltaPx, float dataSizePx)
public void ZoomFrac(double frac)
public void ZoomOut(double multiple)
public void ZoomMouseDelta(float deltaPx, float dataSizePx)
public void ZoomFrac(double frac, double zoomTo)
public bool Equals(CoordinateRangeMutable? other)
public override bool Equals(object? obj)
public static bool operator ==(CoordinateRangeMutable a, CoordinateRangeMutable b)
public static bool operator !=(CoordinateRangeMutable a, CoordinateRangeMutable b)
public override int GetHashCode()
```

### `public struct CoordinateRect : IEquatable<CoordinateRect>`
<!-- Primitives\CoordinateRect.cs -->
> Describes a rectangle in 2D coordinate space.

```csharp
public struct CoordinateRect : IEquatable<CoordinateRect>
public double Left { get, set; }
public double Right { get, set; }
public double Bottom { get, set; }
public double Top { get, set; }
public double HorizontalCenter
public double VerticalCenter
public Coordinates Center
public Coordinates TopLeft
public Coordinates TopRight
public Coordinates BottomLeft
public Coordinates BottomRight
public CoordinateRange XRange
public CoordinateRange YRange
public CoordinateSize Size
public double Width
public double Height
public double Area
public bool HasArea
public bool IsInvertedX
public bool IsInvertedY
public CoordinateRect(CoordinateRange xRange, CoordinateRange yRange)
public CoordinateRect(CoordinateRangeMutable xRange, CoordinateRangeMutable yRange)
public CoordinateRect(IAxes axes) : this(axes.XAxis.Range, axes.YAxis.Range)
public CoordinateRect(Coordinates pt1, Coordinates pt2)
public CoordinateRect(double left, double right, double bottom, double top)
public CoordinateRect(Coordinates point, CoordinateSize size)
public static CoordinateRect UnitSquare
public bool Contains(double x, double y)
public bool ContainsX(double x)
public bool ContainsY(double y)
public CoordinateRect Expanded(Coordinates point)
public bool Contains(Coordinates point)
public static CoordinateRect Empty
public CoordinateRect WithTranslation(Coordinates p)
public CoordinateRect WithTranslation(double x, double y)
public override string ToString()
public bool Equals(CoordinateRect other)
public override bool Equals(object? obj)
public static bool operator ==(CoordinateRect a, CoordinateRect b)
public static bool operator !=(CoordinateRect a, CoordinateRect b)
public override int GetHashCode()
```

### `public struct CoordinateSize : IEquatable<CoordinateSize>`
<!-- Primitives\CoordinateSize.cs -->

```csharp
public struct CoordinateSize : IEquatable<CoordinateSize>
public double Width
public double Height
public double Area
public CoordinateSize(double width, double height)
public bool Equals(CoordinateSize other)
public override bool Equals(object? obj)
public static bool operator ==(CoordinateSize a, CoordinateSize b)
public static bool operator !=(CoordinateSize a, CoordinateSize b)
public override int GetHashCode()
```

### `public struct Coordinates : IEquatable<Coordinates>`
<!-- Primitives\Coordinates.cs -->
> Represents a point in coordinate space (X and Y axis units)

```csharp
public struct Coordinates : IEquatable<Coordinates>
public double X { get, set; }
public double Y { get, set; }
public bool AreReal
// Define a new coordinate at the given X and Y location (in axis units)
public Coordinates(double x, double y)
// Create an array of coordinates from individual arrays of X and Y positions
public static Coordinates[] Zip(double[] xs, double[] ys)
public double DistanceSquared(Coordinates pt)
public double Distance(Coordinates pt)
public override string ToString()
public static Coordinates NaN
public static Coordinates Zero
public static Coordinates Origin
public static Coordinates Infinity
// The inverse of the present coordinate. E.g., the point (X, Y) becomes (Y, X).
public readonly Coordinates Rotated
public bool Equals(Coordinates other)
public override bool Equals(object? obj)
public static bool operator ==(Coordinates a, Coordinates b)
public static bool operator !=(Coordinates a, Coordinates b)
public override int GetHashCode()
public CoordinateRect ToRect(double radiusX, double radiusY)
public CoordinateRect ToRect(double radius)
public Coordinates WithDelta(double dX, double dY)
public readonly (double X, double Y) Deconstruct()
public static Coordinates operator +(Coordinates a, Coordinates b)
```

### `public struct Coordinates3d : IEquatable<Coordinates3d>`
<!-- Primitives\Coordinates3d.cs -->
> Represents a 3d point in coordinate space

```csharp
public struct Coordinates3d : IEquatable<Coordinates3d>
public double X { get, set; }
public double Y { get, set; }
public double Z { get, set; }
public bool AreReal
public Coordinates3d(double x, double y, double z)
public double DistanceSquared(Coordinates3d pt)
public double Distance(Coordinates3d pt)
public override string ToString()
public static Coordinates3d NaN
public static Coordinates3d Origin
public static Coordinates3d Infinity
public bool Equals(Coordinates3d other)
public override bool Equals(object? obj)
public static bool operator ==(Coordinates3d a, Coordinates3d b)
public static bool operator !=(Coordinates3d a, Coordinates3d b)
public override int GetHashCode()
public Coordinates3d WithDelta(double dX, double dY, double dZ)
public Coordinates Coordinates2d()
```

### `public enum Cursor { Arrow, No, Wait, Hand, Cross, SizeAll, SizeNorthSouth, SizeWestEast, }`
<!-- Primitives\Cursor.cs -->

```csharp
public enum Cursor { Arrow, No, Wait, Hand, Cross, SizeAll, SizeNorthSouth, SizeWestEast, }
成员: Arrow, No, Wait, Hand, Cross, SizeAll, SizeNorthSouth, SizeWestEast
```

### `public static class DataOperations`
<!-- DataOperations.cs -->

```csharp
public static class DataOperations
public static double[,] ResizeHalf(double[,] values)
public static double[,] ReplaceNullWithNaN(double?[,] values)
public static double?[,] ReplaceNaNWithNull(double[,] values)
public static void Multiply2D(double[,] values, double mult)
public static double[] SumVertically(IEnumerable<double[]> arrays)
```

### `public readonly struct DataPoint`
<!-- Primitives\DataPoint.cs -->
> Represents a specific point in a DataSource

```csharp
public readonly struct DataPoint
public readonly double X
public readonly double Y
public readonly int Index
public Coordinates Coordinates
public bool IsReal
public DataPoint(double x, double y, int index)
public DataPoint(Coordinates coordinates, int index)
public static DataPoint None
```

### `public static class DataSourceUtilities`
<!-- DataSourceUtilities.cs -->

```csharp
public static class DataSourceUtilities
// Check if a collection is in ascending order
public static bool IsAscending<T>(this IEnumerable<T> values, IComparer<T>? comparer) [扩展方法]
public static int BinarySearch<T, TList>(this TList sortedList, int index, int length, T value, IComparer<T>? comparer) where TList : IEnumerable<T> [扩展方法]
// Searches a range of elements in a sorted for a value using a binary search algorithm.
public static int BinarySearch<T>( this IReadOnlyList<T> sortedList, int index, int length, T value, IComparer<T>? comparer = null) [扩展方法]
public static int GetClosestIndex(double[] sortedList, double value, IndexRange indexRange)
public static int GetClosestIndex(List<double> sortedList, double value, IndexRange indexRange)
public static int GetClosestIndex(Coordinates[] sortedList, Coordinates value, IndexRange indexRange)
public static int GetClosestIndex(List<Coordinates> sortedList, Coordinates value, IndexRange indexRange)
// Gets the closest index to a specified from the
public static int GetClosestIndex<TValue, TList>(this TList sortedList, TValue value, IndexRange indexRange, IComparer<TValue>? comparer) where TList : IEnumerable<TValue> // expects IList & IReadOnlyList [扩展方法]
// Calculates the maximum count of indexes available to render in an 's collection
public static int GetRenderIndexCount(this IDataSource dataSource) [扩展方法]
// Creates a new
public static IndexRange GetRenderIndexRange(this IDataSource dataSource) [扩展方法]
// Scale the by applying the and the
public static double ScaleXY(double value, double scalingFactor, double offset)
// The type of value - will be converted to a double via
public static double ScaleXY<T>(T value, double scalingFactor, double offset)
// Scale a value from the collection by the and
public static double ScaleXY<T>(T[] collection, int index, double scalingFactor, double offset)
public static double ScaleXY<T>(IReadOnlyList<T> collection, int index, double scalingFactor, double offset)
// Scale the by applying the and the
public static double UnscaleXY(double value, double scalingFactor, double offset)
// Scale a coordinate by applying the offsets and the scaling factors.
public static Coordinates ScaleCoordinate(Coordinates coordinate, double xScalingFactor, double xOffset, double yScalingFactor, double yOffset)
public static Coordinates UnScaleCoordinate(Coordinates coordinate, double xScalingFactor, double xOffset, double yScalingFactor, double yOffset)
// Unscale a coordinate
public static Coordinates UnScaleCoordinate(Coordinates pixelCoordinate, RenderDetails renderInfo, double xScalingFactor = 1, double xOffset = 0, double yScalingFactor = 1, double yOffset = 0, IXAxis? xaxis = null, IYAxis? yaxis = null)
// Checks and decides to call the Fast or Original method accordingly
public static DataPoint GetNearestSmart(IDataSource dataSource, Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance, IXAxis? xAxis = null, IYAxis? yAxis = null)
// Checks and decides to call the Fast or Original method accordingly
public static DataPoint GetNearestXSmart(IDataSource dataSource, Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance, IXAxis? xAxis = null)
// Get the nearest datapoint on the plot from the , based on the and the
public static DataPoint GetNearest(IDataSource dataSource, Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance, IXAxis? xAxis = null, IYAxis? yAxis = null)
// Get the nearest datapoint from the , based on the X location and the
public static DataPoint GetNearestX(IDataSource dataSource, Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance, IXAxis? xAxis = null)
// This is a faster way to locate the nearest DataPoint from the collection, but it requires the collection to be sorted in ascending order. ( Signal | SignalXY )
public static DataPoint GetNearestFast(IDataSource dataSource, Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance, IXAxis? xAxis = null, IYAxis? yAxis = null)
// Get the nearest datapoint from the , based on the X location and the
public static DataPoint GetNearestXFast(IDataSource dataSource, Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance, IXAxis? xAxis = null)
```

### `public static class Drawing`
<!-- Drawing.cs -->
> Common operations using the default rendering system.

```csharp
public static class Drawing
public static void DrawLine(SKCanvas canvas, Paint paint, PixelLine pixelLine)
public static void DrawLine(SKCanvas canvas, Paint paint, Pixel pt1, Pixel pt2)
public static void DrawLine(SKCanvas canvas, Paint paint, PixelLine pxLine, LineStyle lineStyle)
public static void DrawLines(SKCanvas canvas, Paint paint, IEnumerable<PixelLine> pxLines, LineStyle lineStyle)
public static void DrawLine(SKCanvas canvas, Paint paint, Pixel pt1, Pixel pt2, LineStyle lineStyle)
public static void DrawLine(SKCanvas canvas, Paint paint, Pixel pt1, Pixel pt2, Color color, float width = 1, bool antiAlias = true, LinePattern pattern = default)
public static void DrawArrow(SKCanvas canvas, Paint paint, SKPath path, ArrowStyle arrowStyle)
public static void DrawPath(SKCanvas canvas, Paint paint, SKPath path, SKShader? shader)
public static void DrawPath(SKCanvas canvas, Paint paint, IEnumerable<Pixel> pixels, LineStyle lineStyle, bool close = false)
public static void FillPath(SKCanvas canvas, Paint paint, IEnumerable<Pixel> pixels, FillStyle fillStyle, PixelRect rect)
public static void FillPath(SKCanvas canvas, Paint paint, SKPath path, FillStyle fillStyle)
public static void DrawPath(SKCanvas canvas, Paint paint, IEnumerable<Pixel> pixels, LineStyle lineStyle, string label, LabelStyle labelStyle, bool close = false)
public static void DrawTextOnPath(SKCanvas canvas, Paint paint, SKPath path, string text, float xOffset, float yOffset)
public static void DrawPath(SKCanvas canvas, Paint paint, PixelPath path, LineStyle lineStyle)
public static void DrawPath(SKCanvas canvas, Paint paint, PixelPath path, LineStyle lineStyle, string text, LabelStyle labelStyle)
public static void DrawPath(SKCanvas canvas, Paint paint, PixelPath path, FillStyle fillStyle)
public static void FillPath(SKCanvas canvas, Paint paint, PixelPath path, FillStyle fillStyle)
public static void DrawPath(SKCanvas canvas, Paint paint, IEnumerable<Pixel> pixels, FillStyle fillStyle)
public static void FillPath(SKCanvas canvas, Paint paint, IEnumerable<Pixel> pixels, FillStyle fillStyle)
public static void DrawPath(SKCanvas canvas, Paint paint, SKPath path, LineStyle lineStyle)
public static void DrawPath(SKCanvas canvas, Paint paint, SKPath path, FillStyle fillStyle, PixelRect rect)
public static void FillPath(SKCanvas canvas, Paint paint, SKPath path, FillStyle fillStyle, PixelRect rect)
public static void DrawLines(SKCanvas canvas, Paint paint, IEnumerable<Pixel> pixels, LineStyle lineStyle)
public static void DrawLines(SKCanvas canvas, Paint paint, SKPath path, LineStyle lineStyle)
public static void FillRectangle(SKCanvas canvas, PixelRect rect, Paint paint, FillStyle fillStyle)
public static void DrawRoundRectangle(SKCanvas canvas, PixelRect rect, Paint paint, float radiusX, float radiusY)
public static void DrawRectangle(SKCanvas canvas, PixelRect rect, Paint paint, LineStyle lineStyle)
public static void DrawDebugRectangle(SKCanvas canvas, Paint paint, PixelRect rect, Pixel? point = null, Color? color = null, float lineWidth = 3)
public static void DrawCircle(SKCanvas canvas, Pixel center, float radius, LineStyle lineStyle, Paint paint)
public static void DrawCircle(SKCanvas canvas, Pixel center, float radius, FillStyle fillStyle, Paint paint)
public static void FillCircle(SKCanvas canvas, Pixel center, float radius, FillStyle fillStyle, Paint paint)
public static void DrawOval(SKCanvas canvas, Paint paint, LineStyle lineStyle, PixelRect rect)
public static void FillOval(SKCanvas canvas, Paint paint, FillStyle fillStyle, PixelRect rect)
public static void DrawArc(SKCanvas canvas, Paint paint, LineStyle lineStyle, PixelRect rect, float startAngle, float sweepAngle)
public static void DrawEllipticalArc(SKCanvas canvas, Paint paint, LineStyle lineStyle, PixelRect rect, float startAngle, float sweepAngle)
public static void DrawAnnularSector(SKCanvas canvas, Paint paint, LineStyle lineStyle, PixelRect rect, PixelRect innerRect, float startAngle, float sweepAngle)
public static void FillAnnularSector(SKCanvas canvas, Paint paint, FillStyle fillStyle, PixelRect rect, PixelRect innerRect, float startAngle, float sweepAngle)
public static void DrawEllipticalAnnulus(SKCanvas canvas, Paint paint, LineStyle lineStyle, PixelRect outerRect, PixelRect innerRect)
public static void FillEllipticalAnnulus(SKCanvas canvas, Paint paint, FillStyle fillStyle, PixelRect outerRect, PixelRect innerRect)
public static void DrawSector(SKCanvas canvas, Paint paint, LineStyle lineStyle, PixelRect rect, float startAngle, float sweepAngle)
public static void FillSector(SKCanvas canvas, Paint paint, FillStyle fillStyle, PixelRect rect, float startAngle, float sweepAngle)
public static void DrawMarker(SKCanvas canvas, Paint paint, Pixel pixel, MarkerStyle style)
public static void DrawMarkers(SKCanvas canvas, Paint paint, IEnumerable<Pixel> pixels, MarkerStyle style)
public static void DrawMarkers(SKCanvas canvas, Paint paint, IReadOnlyList<Pixel> pixels, MarkerStyle style, IColormap colormap)
public static SKBitmap BitmapFromArgbs(uint[] argbs, int width, int height)
public static SKColorFilter GetMaskColorFilter(Color foreground, Color? background = null)
public static SKSurface CreateSurface(int width, int height)
public static void SavePng(SKSurface surface, string filename)
public static void DrawImage(SKCanvas canvas, SKBitmap image, PixelRect target, Paint paint)
public static void DrawImage(SKCanvas canvas, SKImage image, PixelRect target, Paint paint)
public static void DrawImage(SKCanvas canvas, Image image, PixelRect target, Paint paint)
public static void DrawText(SKCanvas canvas, string text, Pixel px, Paint paint)
public static void DrawShapedText(SKCanvas canvas, SKShaper shaper, string text, Pixel px, Paint paint)
```

### `public enum Edge { Left, Right, Bottom, Top }`
<!-- Primitives\Edge.cs -->

```csharp
public enum Edge { Left, Right, Bottom, Top }
成员: Left, Right, Bottom, Top
```

### `public static class EdgeExtensions`
<!-- Primitives\Edge.cs -->

```csharp
public static class EdgeExtensions
// True for bottom and top axes
public static bool IsHorizontal(this Edge edge) [扩展方法]
// True for left and right axes
public static bool IsVertical(this Edge edge) [扩展方法]
```

### `public class ExpandingAxisLimits : IEquatable<ExpandingAxisLimits>`
<!-- Primitives\ExpandingAxisLimits.cs -->
> A stateful analog to deisgned to expand to include given data

```csharp
public class ExpandingAxisLimits : IEquatable<ExpandingAxisLimits>
public double Left { get, set; }
public double Right { get, set; }
public double Bottom { get, set; }
public double Top { get, set; }
public double HorizontalSpan
public double VerticalSpan
public bool IsRealX
public bool IsRealY
public bool IsReal
public bool HasArea
public AxisLimits AxisLimits
// Create a new set of expanding axis limits with no leimits set initially
public ExpandingAxisLimits()
// Create a new set of expanding axis limits starting from the given axis limits
public ExpandingAxisLimits(AxisLimits initialLimits)
public ExpandingAxisLimits(IEnumerable<IPlottable> plottables)
public override string ToString()
public void SetX(double left, double right)
public void SetY(double bottom, double top)
// Expanded limits to include the given and .
public void Expand(double x, double y)
public void Expand(IPlottable plottable)
// Expanded limits to include the given .
public void ExpandX(double x)
// Expanded limits to include the given .
public void ExpandY(double y)
// Expanded limits to include the given .
public void Expand(Coordinates coordinates)
// Expanded limits to include the given .
public void Expand(IEnumerable<Coordinates> coordinates)
// Expanded limits to include the given .
public void Expand(IEnumerable<Coordinates3d> coordinates)
public void Expand(CoordinateRect rect)
public void Expand(AxisLimits limits)
public void ExpandX(AxisLimits limits)
public void ExpandY(AxisLimits limits)
public bool Equals(ExpandingAxisLimits? other)
public bool Equals(AxisLimits other)
public override bool Equals(object? obj)
public static bool operator ==(ExpandingAxisLimits a, ExpandingAxisLimits b)
public static bool operator !=(ExpandingAxisLimits a, ExpandingAxisLimits b)
public static bool operator ==(ExpandingAxisLimits a, AxisLimits b)
public static bool operator !=(ExpandingAxisLimits a, AxisLimits b)
public override int GetHashCode()
```

### `public class FillStyle`
<!-- Primitives\FillStyle.cs -->
> This configuration object (reference type) permanently lives inside objects which require styling. It is recommended to use this object as an init-only property.

```csharp
public class FillStyle
public Color Color { get, set; }
public Color HatchColor { get, set; }
public IHatch? Hatch { get, set; }
public bool HasValue
public bool AntiAlias { get, set; }
public bool IsVisible { get, set; }
public bool CanBeRendered { get; }
public FillStyle()
public FillStyle(Color color)
public void Render(RenderPack rp, PixelRect rect)
public void Render(SKCanvas canvas, PixelRect rect, Paint paint)
public void ApplyToPaint(Paint paint, PixelRect rect)
```

### `public static class FontExtensions`
<!-- FontExtensions.cs -->

```csharp
public static class FontExtensions
public static SKFontStyleWidth ToSKFontStyleWidth(this FontSpacing width) [扩展方法]
public static SKFontStyleSlant ToSKFontStyleSlant(this FontSlant slant) [扩展方法]
public static SKFontStyleWeight ToSKFontStyleWeight(this FontWeight weight) [扩展方法]
```

### `public enum FontSlant { Upright = 0, Italic = 1, Oblique = 2 }`
<!-- Primitives\FontSlant.cs -->

```csharp
public enum FontSlant { Upright = 0, Italic = 1, Oblique = 2 }
成员: Upright, Italic, Oblique
```

### `public enum FontSpacing { UltraCondensed = 1, ExtraCondensed = 2, Condensed = 3, SemiCondensed = 4, Normal = 5, SemiExpanded = 6, Expanded = 7, ExtraExpanded = 8, UltraExpanded = 9 }`
<!-- Primitives\FontSpacing.cs -->

```csharp
public enum FontSpacing { UltraCondensed = 1, ExtraCondensed = 2, Condensed = 3, SemiCondensed = 4, Normal = 5, SemiExpanded = 6, Expanded = 7, ExtraExpanded = 8, UltraExpanded = 9 }
成员: UltraCondensed, ExtraCondensed, Condensed, SemiCondensed, Normal, SemiExpanded, Expanded, ExtraExpanded, UltraExpanded
```

### `public class FontStyle`
<!-- Primitives\FontStyle.cs -->
> This configuration object (reference type) permanently lives inside objects which require styling. It is recommended to use this object as an init-only property.

```csharp
public class FontStyle
public SKTypeface Typeface
public string Name { get, set; }
public FontWeight Weight { get, set; }
public FontSlant Slant { get, set; }
public FontSpacing Width { get, set; }
public bool Bold { get, set; }
public bool Italic { get, set; }
public Color Color { get, set; }
public float Size { get, set; }
public bool AntiAlias { get, set; }
public override string ToString()
public static SKTypeface CreateTypefaceFromName(string font, bool bold, bool italic)
public static SKTypeface CreateTypefaceFromFile(string path)
// Use the characters in to determine an installed system font most likely to support this character set.
public void SetBestFont(string text)
public FontStyle Clone()
public void ApplyToPaint(Paint paint)
```

### `public enum FontWeight { Invisible = 0, Thin = 100, ExtraLight = 200, Light = 300, Normal = 400, Medium = 500, SemiBold = 600, Bold = 700, ExtraBold = 800, Black = 900, ExtraBlack = 1000, }`
<!-- Primitives\FontWeight.cs -->

```csharp
public enum FontWeight { Invisible = 0, Thin = 100, ExtraLight = 200, Light = 300, Normal = 400, Medium = 500, SemiBold = 600, Bold = 700, ExtraBold = 800, Black = 900, ExtraBlack = 1000, }
成员: Invisible, Thin, ExtraLight, Light, Normal, Medium, SemiBold, Bold, ExtraBold, Black, ExtraBlack
```

### `public static class Fonts`
<!-- Fonts.cs -->
> Cross-platform tools for working with fonts

```csharp
public static class Fonts
// Collection of font resolvers that return typefaces from font names and style information
public static List<IFontResolver> FontResolvers { get; }
// Add a font resolver that creates a typeface from a TTF file
public static void AddFontFile(string name, string path, bool bold = false, bool italic = false)
public static FontWeight? DefaultWeight { get, set; }
public static FontSlant? DefaultSlant { get, set; }
public static FontSpacing? DefaultWidth { get, set; }
public static SKTypeface? DefaultFontStyle { get, set; }
// This font is used for almost all text rendering.
public static string Default { get, set; }
// Name of a sans-serif font present on the system
public static string Sans { get, set; }
// Name of a serif font present on the system
public static string Serif { get, set; }
// Name of a monospace font present on the system
public static string Monospace { get, set; }
// Default system font name
public static string System
public static bool Exists(string fontName)
public static bool Exists(string fontName, bool bold, bool italic)
// Returns a typeface for the requested font name and style. A cached typeface will be used if it exists, otherwise one will be created, cached, and returned.
public static SKTypeface GetTypeface(string fontName, FontWeight weight, FontSlant slant, FontSpacing spacing)
// Returns a typeface for the requested font name and style. A cached typeface will be used if it exists, otherwise one will be created, cached, and returned.
public static SKTypeface GetTypeface(string fontName, bool bold, bool italic)
public static SKTypeface GetTypeface(string fontName, bool bold, bool italic, FontSpacing width)
// Use the characters in the string to determine an installed system font most likely to support this character set. Returns the system font if an ideal font cannot be determined.
public static string Detect(string text)
public static string GetDefaultFontFamily()
public static List<string> GetCandidateFontsForString(List<int> standaloneCodePoints)
public static int CountMissingGlyphs(string fontName, List<int> standaloneCodePoints)
public static List<int> GetStandaloneCodePoints(string inputText)
public static List<string> ConvertStringToTextElements(string textString)
// Take a single text element ("grapheme cluster") as input, and return one or more Unicode code points. The code points are represented with signed ints since that is idiomatic for C#, even though they are always unsigned values.
public static List<int> ConvertTextElementToUtf32CodePoints(string textElement)
public static List<int> GetStandaloneCodePoints(IEnumerable<List<int>> codePointLists)
public static void Reset()
```

### `public readonly struct FractionRect`
<!-- Primitives\FractionRect.cs -->
> Describes a rectangular region of a larger rectangle using fractional units

```csharp
public readonly struct FractionRect
public double Left { get; }
public double Top { get; }
public double Width { get; }
public double Height { get; }
public double Right
public double Bottom
public FractionRect(double left, double top, double width, double height)
public PixelRect GetPixelRect(PixelRect fullRect)
public PixelRect GetPixelRect(float width, float height)
public static FractionRect Full
public static FractionRect Column(int columnIndex, int columnCount)
public static FractionRect Row(int rowIndex, int rowCount)
public static FractionRect GridCell(int columnIndex, int rowIndex, int columnCount, int rowCount)
```

### `public static class Generate`
<!-- Generate.cs -->
> This class contains methods which generate sample data for testing and demonstration purposes

```csharp
public static class Generate
public static RandomDataGenerator RandomData { get; }
public static FinancialDataGenerator Financial { get; }
// Return an array of evenly-spaced numbers
public static double[] Consecutive(int count = 51, double delta = 1, double first = 0)
// Return an array of sine waves between -1 and 1. Values are multiplied by then shifted by . Phase shifts the sine wave horizontally between 0 and 2 Pi.
public static double[] Sin(int count = 51, double mult = 1, double offset = 0, double oscillations = 1, double phase = 0)
// Return an array for a sigmoidal curve that rises from zero to
public static double[] Sigmoidal(int count, double mult = 1.0, double steepness = 1.0)
// Return an array of cosine waves between -1 and 1. Values are multiplied by then shifted by . Phase shifts the sine wave horizontally between 0 and 2 Pi.
public static double[] Cos(int count = 51, double mult = 1, double offset = 0, double oscillations = 1, double phase = 0)
public static double[] NoisySin(int count = 51, double magnitude = 1)
// An exponential curve that rises from 0 to over points with random positive noise that scales with the underlying signal. The rate constant of the exponential curve is .
public static double[] NoisyExponential(int count, double mult = 1000, double noise = .5, double tau = 5)
public static double[] SquareWave(uint cycles = 20, uint pointsPerCycle = 1_000, double duty = .5, double low = 0, double high = 1)
// Generate a square wave by summing sine waves with decreasing amplitudes at odd harmonics of the fundamental frequency
public static double[] SquareWaveFromSines(int pointCount = 1000, double oscillations = 2, int sineCount = 5)
public static double[] Zeros(int count)
public static double[] Ones(int count)
public static double[] Repeating(int count, double value)
public static double[] NaN(int count)
// Return values from to (inclusive) separated by
public static double[] Range(double start, double stop, double step = 1)
// Return values from to (inclusive) separated by
public static double[] RangeWithStep(double start, double stop, double step = 1)
// Return values from to (inclusive)
public static double[] RangeWithCount(double start, double stop, int count)
// Generates a 2D array of numbers with constant spacing.
public static double[,] Consecutive2D(int rows, int columns, double spacing = 1, double offset = 0)
// Generates a 2D sine pattern.
public static double[,] Sin2D(int width, int height, double xPeriod = .2, double yPeriod = .2, double multiple = 100)
// Generate a 2D array in a diagonal gradient pattern
public static double[,] Ramp2D(int width, int height, double min = 0, double max = 1)
public static RootedCoordinateVector[] SampleVectors(int columns = 10, int rows = 10, double oscillations = 1)
// Return a series of values starting with and each randomly deviating from the previous by at most .
public static double[] RandomWalk(int count, double mult = 1, double offset = 0)
public static double[] Random(int count, double min = 0, double max = 1)
// Return an array of random values from to
public static double[] RandomSample(int count, double min = 0, double max = 1)
// Sequence of ascending numbers with random spacing between values.
public static double[] RandomAscending(int count, double minDelta = 0, double maxDelta = 1)
public static double[] RandomNormal(int count, double mean = 0, double stdDev = 1)
// RandomSample integer between zero (inclusive) and (exclusive)
public static int RandomInteger(int max)
// RandomSample integer between (inclusive) and (exclusive)
public static int RandomInteger(int min, int max)
// RandomSample integers between zero (inclusive) and (exclusive)
public static int[] RandomIntegers(int count, int max)
// RandomSample integers between (inclusive) and (exclusive)
public static int[] RandomIntegers(int count, int min, int max)
// RandomSample integer between 0 (inclusive) and 1 (exclusive)
public static double RandomNumber()
// RandomSample integer between 0 (inclusive) and (exclusive)
public static double RandomNumber(double max)
// RandomSample integer between (inclusive) and (exclusive)
public static double RandomNumber(double min, double max)
// Return a number normally distributed around the given according to the standard deviation.
public static double RandomNormalNumber(double mean = 0, double stdDev = 1)
// Random numbers between zero (inclusive) and (exclusive)
public static double[] RandomNumbers(int count, double max)
// Random numbers between (inclusive) and (exclusive)
public static double[] RandomNumbers(int count, double min, double max)
// Return a copy of the given array with random values added to each point
public static double[] AddNoise(double[] input, double magnitude = 1)
// Mutate the given array by adding a random value to each point
public static void AddNoiseInPlace(double[] values, double magnitude = 1)
// Modify the array to add a sine wave with the given parameters
public static double[] AddSinInPlace(double[] values, double mult = 1, double offset = 0, double oscillations = 1, double phase = 0)
// Return a new array containing the given one plus a sine wave with the given parameters
public static double[] AddSin(double[] values, double mult = 1, double offset = 0, double oscillations = 1, double phase = 0)
public static char RandomChar()
public static string RandomString(int length)
public static CoordinateRect RandomCoordinateRect(double xMult = 1, double yMult = 1, double width = .1, double height = .1)
public static CoordinateLine RandomCoordinateLine(double xMult = 1, double yMult = 1, double xOffset = 0, double yOffset = 0)
public static Coordinates RandomCoordinates(double xMult = 1, double yMult = 1, double xOffset = 0, double yOffset = 0)
public static Coordinates[] RandomCoordinates(int count, double xMult = 1, double yMult = 1, double xOffset = 0, double yOffset = 0)
public static Coordinates RandomLocation()
public static Coordinates RandomLocation(AxisLimits limits)
public static Coordinates[] RandomLocations(int count)
public static Coordinates[] RandomLocations(int count, AxisLimits limits)
public static System.DateTime[] Consecutive(int count, System.DateTime start, TimeSpan timeSpan)
public static System.DateTime[] ConsecutiveDateTimes(int count, System.DateTime start, TimeSpan timeSpan)
public static System.DateTime[] ConsecutiveDays(int count, int year = 2023, int month = 1, int day = 1)
public static System.DateTime[] ConsecutiveDays(int count, System.DateTime start)
public static System.DateTime[] ConsecutiveWeekdays(int count, int year = 2023, int month = 1, int day = 1)
public static System.DateTime[] ConsecutiveWeekdays(int count, System.DateTime start)
public static System.DateTime[] ConsecutiveHours(int count)
public static System.DateTime[] ConsecutiveHours(int count, System.DateTime start)
public static System.DateTime[] ConsecutiveQuarterHours(int count, System.DateTime start)
public static System.DateTime[] ConsecutiveMinutes(int count, System.DateTime start)
public static System.DateTime[] ConsecutiveSeconds(int count, System.DateTime start)
public static System.DateTimeOffset[] Consecutive(int count, System.DateTimeOffset start, TimeSpan timeSpan)
public static System.DateTimeOffset[] ConsecutiveDateTimes(int count, System.DateTimeOffset start, TimeSpan timeSpan)
public static System.DateTimeOffset[] ConsecutiveDays(int count, System.DateTimeOffset start)
public static System.DateTimeOffset[] ConsecutiveWeekdays(int count, System.DateTimeOffset start)
public static System.DateTimeOffset[] ConsecutiveHours(int count, System.DateTimeOffset start)
public static System.DateTimeOffset[] ConsecutiveQuarterHours(int count, System.DateTimeOffset start)
public static System.DateTimeOffset[] ConsecutiveMinutes(int count, System.DateTimeOffset start)
public static System.DateTimeOffset[] ConsecutiveSeconds(int count, System.DateTimeOffset start)
public static OHLC RandomOHLC()
public static OHLC RandomOHLC(System.DateTime date)
public static List<OHLC> RandomOHLCs(int count)
public static List<OHLC> RandomOHLCs(int count, System.DateTime startDate)
public static Box RandomBox(double position)
public static Color RandomHue()
public static Color RandomColor()
// Generate a dark color by defining the maximum value to use for R, G, and B
public static Color RandomColor(byte max)
public static Color RandomColor(IColormap colormap)
public static Color[] RandomColors(int count, IColormap colormap)
public static MarkerShape RandomMarkerShape()
public static MarkerShape RandomFilledMarkerShape()
public static CoordinateLine RandomLine()
public static LinePattern RandomLinePattern()
public readonly static DataGenerators.RandomWalker RandomWalker = new(0)
```

### `public static class DateTime`（嵌套于 Generate）

```csharp
public static class DateTime
// Date of the first ScottPlot commit
public static readonly System.DateTime ExampleDate = new(2018, 01, 03)
// Evenly-spaced DateTimes
public static System.DateTime[] Consecutive(int count, System.DateTime start, TimeSpan step)
public static System.DateTime[] Weekdays(int count, System.DateTime start)
public static System.DateTime[] Weekdays(int count)
public static System.DateTime[] Days(int count, System.DateTime start)
public static System.DateTime[] Days(int count)
public static System.DateTime[] Hours(int count, System.DateTime start)
public static System.DateTime[] Hours(int count)
public static System.DateTime[] Minutes(int count, System.DateTime start)
public static System.DateTime[] Minutes(int count)
public static System.DateTime[] Seconds(int count, System.DateTime start)
public static System.DateTime[] Seconds(int count)
```

### `public static class GenericComparer<T>`
<!-- GenericComparer.cs -->
> Generic helper used to provide on supported types.

```csharp
public static class GenericComparer<T>
// An appropriate for this type.
public static readonly IComparer<T> Default = GetComparer()
```

### `public class Gradient(GradientType gradientType = GradientType.Linear) : IHatch`
<!-- Primitives\Gradient.cs -->

```csharp
public class Gradient(GradientType gradientType = GradientType.Linear) : IHatch
// Describes the geometry of a color gradient used to fill an area
public GradientType GradientType { get, set; }
// Get or set the start angle in degrees for sweep gradient
public float StartAngle { get, set; }
// Get or set the end angle in degrees for sweep gradient
public float EndAngle { get, set; }
// Get or set how the shader should handle drawing outside the original bounds.
public SKShaderTileMode TileMode { get, set; }
// Start of linear gradient
public Alignment AlignmentStart { get, set; }
// End of linear gradient
public Alignment AlignmentEnd { get, set; }
// Colors used for the gradient, or null to use the Hatch colors.
public Color[] Colors { get, set; }
// Get or set the positions (in the range of 0..1) of each corresponding color, or null to evenly distribute the colors.
public float[] ColorPositions { get, set; }
public SKShader GetShader(Color backgroundColor, Color hatchColor, PixelRect rect)
public static Gradient FromAxisLimits(RenderPack rp, AxisLimits limits, AxisGradientDirection direction, IAxes axes, List<AxisGradientColorPosition> colorPositions)
```

### `public enum GradientType { Linear, Radial, Sweep, TwoPointConical }`
<!-- Primitives\GradientType.cs -->
> Describes the geometry of a color gradient used to fill an area

```csharp
public enum GradientType { Linear, Radial, Sweep, TwoPointConical }
成员: Linear, Radial, Sweep, TwoPointConical
```

### `public class GridCell`
<!-- Primitives\GridCell.cs -->
> Represents a single cell in a rectangular grid.

```csharp
public class GridCell
public GridCell(int rowIndex, int colIndex, int rowCount, int colCount, int rowSpan = 1, int colSpan = 1)
// Return the rectangle for this cell given the dimensions of the full grid
public PixelRect GetRect(PixelRect figureRect)
```

### `public class GridStyle`
<!-- Primitives\GridStyle.cs -->

```csharp
public class GridStyle
public bool IsVisible { get, set; }
public LineStyle MajorLineStyle { get, set; }
public LineStyle MinorLineStyle { get, set; }
public int MaximumNumberOfGridLines { get, set; }
// When set to false the grid will be rendered on top of plottables instead of beneath them.
public bool IsBeneathPlottables { get, set; }
// Fill the region between every other pair of major grid lines with this color.
public Color FillColor1 { get, set; }
// Fill the region between every other pair of major grid lines with this color.
public Color FillColor2 { get, set; }
public void Render(RenderPack rp, IAxis axis, IEnumerable<Tick> ticks)
```

### `public enum HorizontalAlignment { Left, Center, Right, }`
<!-- Primitives\HorizontalAlignment.cs -->

```csharp
public enum HorizontalAlignment { Left, Center, Right, }
成员: Left, Center, Right
```

### `public static class HorizontalAlignmentExtensions`
<!-- Primitives\HorizontalAlignment.cs -->

```csharp
public static class HorizontalAlignmentExtensions
public static SKTextAlign ToSKTextAlign(this HorizontalAlignment ha) [扩展方法]
```

### `public interface IArrowShape`
<!-- Interfaces\IArrowShape.cs -->
> Contains settings and logic for how to draw an arrow once the base and tip pixels have been determined

```csharp
public interface IArrowShape
public void Render(RenderPack rp, PixelLine pxLine, ArrowStyle arrowStyle)
```

### `public interface IAutoScaler`
<!-- Primitives\IAutoScaler.cs -->
> Contains logic for determining new axis limits when Autoscale() is called

```csharp
public interface IAutoScaler
// Autoscale every unset axis used by plottables.
public void AutoScaleAll(IEnumerable<IPlottable> plottables)
public bool InvertedX { get, set; }
public bool InvertedY { get, set; }
```

### `public interface IAxes`
<!-- Interfaces\IAxes.cs -->
> This interface describes a pair of 1D axes. It is intended to be stored inside objects, defining which axes they use and providing logic for coordinate/pixel conversions.

```csharp
public interface IAxes
```

### `public static class IAxesExtensions`
<!-- Interfaces\IAxes.cs -->

```csharp
public static class IAxesExtensions
public static void SetSpanX(this IAxes axes, double span) [扩展方法]
public static void SetSpanY(this IAxes axes, double span) [扩展方法]
public static PixelPath GetPixelPath(this IAxes axis, CoordinatePath path) [扩展方法]
public static PixelPath[] GetPixelPaths(this IAxes axis, CoordinatePath[] paths) [扩展方法]
```

### `public interface IAxis : IPanel`
<!-- Interfaces\IAxis.cs -->
> This interface describes a 1D axis (horizontal or vertical). Responsibilities include: min/max management, unit/pixel conversion, tick generation (and rendering), axis label rendering, and self-measurement for layout purposes.

```csharp
public interface IAxis : IPanel
// Replace the with a pre-loaded with the given ticks.
public void SetTicks(double[] xs, string[] labels)
// Use the to generate ticks with ideal spacing.
public void RegenerateTicks(PixelLength size, Paint paint)
```

### `public static class IAxisExtensions`
<!-- Interfaces\IAxis.cs -->

```csharp
public static class IAxisExtensions
public static CoordinateRange GetRange(this IAxis axis) [扩展方法]
public static bool IsInverted(this IAxis axis) [扩展方法]
public static void RemoveTickGenerator(this IAxis axis) [扩展方法]
// Set the axis size to zero and disable tick generation. This method allows the data area to rest against the edge of the figure (e.g., when collapsing space between stacked plots in a multiplot)
public static void Collapse(this IAxis axis) [扩展方法]
```

### `public interface IAxisLimitManager`
<!-- Primitives\IAxisLimitManager.cs -->
> An axis manager contains logic to suggest axis limits given the current view and size of the data.

```csharp
public interface IAxisLimitManager
```

### `public static class IAxisLimitManagerExtensions`
<!-- Primitives\IAxisLimitManager.cs -->

```csharp
public static class IAxisLimitManagerExtensions
// Return recommended axis limits given the current view and size of the data
public static AxisLimits GetAxisLimits(this IAxisLimitManager manager, AxisLimits viewLimits, AxisLimits dataLimits) [扩展方法]
```

### `public interface IAxisRule`
<!-- Interfaces\IAxisRule.cs -->
> These rules are applied just before each render

```csharp
public interface IAxisRule
```

### `public interface IColormap`
<!-- Interfaces\IColormap.cs -->

```csharp
public interface IColormap
```

### `public static class IColormapExtensions`
<!-- Interfaces\IColormap.cs -->

```csharp
public static class IColormapExtensions
// Returns an array of colors evenly spaced along the colormap
public static Color[] GetColors( this IColormap colormap, int count, double minFraction = 0, double maxFraction = 1) [扩展方法]
// Return the color for an item at index of a collection of size . The and may be customized to restrict sampling to a portion of the colormap.
public static Color GetColor(this IColormap cmap, int index, int count, double startFraction = 0, double endFraction = 1) [扩展方法]
public static Color GetColor(this IColormap cmap, double position, Range range) [扩展方法]
public static IColormap Reversed(this IColormap cmap) [扩展方法]
public static Image GetImageHorizontal(this IColormap colormap, int height = 1, int width = 256) [扩展方法]
public static Image GetImageVertical(this IColormap colormap, int height = 256, int width = 1) [扩展方法]
public static IColormap Invert(this IColormap original) [扩展方法]
public static IColormap InvertHue(this IColormap original) [扩展方法]
```

### `public interface IDataSource`
<!-- Interfaces\IDataSource.cs -->
> Internal interface used for Utility Functions within

```csharp
public interface IDataSource
```

### `public interface IFinancialTickGenerator`
<!-- Interfaces\IFinancialTickGenerator.cs -->

```csharp
public interface IFinancialTickGenerator
```

### `public interface IFontResolver`
<!-- Interfaces\IFontResolver.cs -->
> Provides functionality that converts a requested typeface into a physical font

```csharp
public interface IFontResolver
```

### `public interface IFunctionSource`
<!-- Interfaces\IFunctionSource.cs -->

```csharp
public interface IFunctionSource
```

### `public interface IGetNearest`
<!-- Interfaces\IGetNearest.cs -->
> This interface is used by plottables that can locate a within a specified range of a coordinate on the plot.

```csharp
public interface IGetNearest
```

### `public interface IGrid`
<!-- Interfaces\IGrid.cs -->
> Implement this interface to create a custom grid

```csharp
public interface IGrid
```

### `public interface IHasArrow`
<!-- Interfaces\IHasArrow.cs -->

```csharp
public interface IHasArrow
public float ArrowWidth { get, set; }
public float ArrowheadAxisLength { get, set; }
public float ArrowheadLength { get, set; }
public float ArrowheadWidth { get, set; }
```

### `public interface IHasBackground`
<!-- Interfaces\IHasBackground.cs -->

```csharp
public interface IHasBackground
```

### `public interface IHasColorAxis`
<!-- Interfaces\IHasColorAxis.cs -->

```csharp
public interface IHasColorAxis
```

### `public interface IHasFill`
<!-- Interfaces\IHasFill.cs -->

```csharp
public interface IHasFill
```

### `public interface IHasInteractiveHandles`
<!-- Interfaces\IHasInteractiveHandles.cs -->

```csharp
public interface IHasInteractiveHandles
// Return the interactive handle inside the rectangle
public InteractiveHandle? GetHandle(CoordinateRect rect)
// Called when the given handle has been pressed (typically the start of a drag)
public void PressHandle(InteractiveHandle handle)
// Called when the given handle has been moved (typically the result of a click-drag)
public void MoveHandle(InteractiveHandle handle, Coordinates point)
// Called when the given handle has been released (typically the end of a drag)
public void ReleaseHandle(InteractiveHandle handle)
```

### `public interface IHasLegendText`
<!-- Interfaces\IHasLegendText.cs -->

```csharp
public interface IHasLegendText
```

### `public interface IHasLine`
<!-- Interfaces\IHasLine.cs -->
> Classes with a can implement this to guide addition of standard shortcuts to its most commonly used properties.

```csharp
public interface IHasLine
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
```

### `public interface IHasMarker`
<!-- Interfaces\IHasMarker.cs -->

```csharp
public interface IHasMarker
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public float MarkerLineWidth { get, set; }
public Color MarkerColor { get, set; }
```

### `public interface IHasOutline`
<!-- Interfaces\IHasOutline.cs -->

```csharp
public interface IHasOutline
public LineStyle OutlineStyle { get; }
public float OutlineWidth { get, set; }
public LinePattern OutlinePattern { get, set; }
public Color OutlineColor { get, set; }
```

### `public interface IHasShadow`
<!-- Interfaces\IHasShadow.cs -->

```csharp
public interface IHasShadow
```

### `public interface IHatch`
<!-- Interfaces\IHatch.cs -->

```csharp
public interface IHatch
```

### `public interface ILayoutEngine`
<!-- Interfaces\ILayoutEngine.cs -->
> This interface describes a class that decides how to lay-out a collection of panels around the edges of a figure and create a final layout containing size and position of all panels and also the size and position of the data area.

```csharp
public interface ILayoutEngine
public Layout GetLayout(PixelRect figureRect, Plot plot, Paint paint)
```

### `public interface ILegendLayout`
<!-- Interfaces\ILegendLayout.cs -->

```csharp
public interface ILegendLayout
```

### `public interface IManagesAxisLimits`
<!-- Interfaces\IManagesAxisLimits.cs -->
> This interface is applied to plottables which modify axis limits at render time. The update method is called at render time before the ticks are calculated.

```csharp
public interface IManagesAxisLimits
```

### `public interface IMarker`
<!-- Interfaces\IMarker.cs -->
> Describes logic necessary to render a marker at a point

```csharp
public interface IMarker
```

### `public interface IMinorTickGenerator`
<!-- Interfaces\IMinorTickGenerator.cs -->

```csharp
public interface IMinorTickGenerator
```

### `public interface IMultiThreadedPlotControl`
<!-- Interfaces\IMultiThreadedPlotControl.cs -->

```csharp
public interface IMultiThreadedPlotControl
```

### `public interface IMultiplot`
<!-- Interfaces\IMultiplot.cs -->

```csharp
public interface IMultiplot
// Logic for linking subplot axis limits together.
public MultiplotSharedAxisManager SharedAxes { get; }
// Actions invoked before each render to coordinate shared state between subplots.
public List<IMultiplotPreRenderAction> PreRenderActions { get; }
```

### `public static class IMultiplotExtensions`
<!-- Interfaces\IMultiplot.cs -->

```csharp
public static class IMultiplotExtensions
// Reset this multiplot so it only contains the given plot
public static void Reset(this IMultiplot multiplot, Plot plot) [扩展方法]
// Reset this multiplot so it only contains the first plot
public static void Reset(this IMultiplot multiplot) [扩展方法]
// Create a new image, render the multiplot onto it, and return it
public static Image Render(this IMultiplot multiplot, int width, int height) [扩展方法]
// Render the multiplot into the clip boundary of the given surface.
public static void Render(this IMultiplot multiplot, SKSurface surface) [扩展方法]
// Save the multiplot as a PNG image file
public static SavedImageInfo SavePng(this IMultiplot multiplot, string filename, int width = 800, int height = 600) [扩展方法]
// Create a new plot, add it to the collection of subplots, and return it
public static Plot AddPlot(this IMultiplot multiplot) [扩展方法]
// Add (or remove) plots until the target number of subplots is achieved
public static void AddPlots(this IMultiplot multiplot, int total) [扩展方法]
// Return the plot beneath the given pixel according to the last render. Returns null if no render occurred or the pixel is not over a plot.
public static Plot? GetPlotAtPixel(this IMultiplot multiplot, Pixel pixel) [扩展方法]
// Number of subplots in this multiplot
public static int Count(this IMultiplot multiplot) [扩展方法]
// Add the given plot to the collection of subplots
public static void AddPlot(this IMultiplot multiplot, Plot plot) [扩展方法]
// Remove the given plot from the collection of subplots
public static void RemovePlot(this IMultiplot multiplot, Plot plot) [扩展方法]
// Return the plot at the given index
public static Plot GetPlot(this IMultiplot multiplot, int index) [扩展方法]
// Return all plots in this multiplot
public static Plot[] GetPlots(this IMultiplot multiplot) [扩展方法]
// Set bottom and top axis size to zero between each subplot so plots can be stacked vertically without any space between them.
public static void CollapseVertically(this IMultiplot multiplot) [扩展方法]
```

### `public interface IMultiplotLayout`
<!-- Interfaces\IMultiplotLayout.cs -->

```csharp
public interface IMultiplotLayout
```

### `public interface IMultiplotPreRenderAction`
<!-- Interfaces\IMultiplotPreRenderAction.cs -->
> An action that may be included in the collection of which gets invoked at the start of a multiplot render, before any subplots are rendered. Useful for coordinating information across subplots (e.g., shared axes or plottable positions).

```csharp
public interface IMultiplotPreRenderAction
// Called at the start of a multiplot render, before any of the subplots are rendered.
public void Invoke()
```

### `public interface IOHLCSource`
<!-- Interfaces\IOHLCSource.cs -->

```csharp
public interface IOHLCSource
```

### `public interface IPalette`
<!-- Interfaces\IPalette.cs -->

```csharp
public interface IPalette
// All colors in this palette
public Color[] Colors { get; }
// Display name
public string Name { get; }
// Additional information such as the source of this palette
public string Description { get; }
// Return the Nth color (wrapping around if N is larger than the number of colors)
public Color GetColor(int index)
```

### `public static class IPaletteExtensions`
<!-- Interfaces\IPalette.cs -->

```csharp
public static class IPaletteExtensions
public static Color[] GetColors(this IPalette palette, int count) [扩展方法]
public static IPalette Inverted(this IPalette palette) [扩展方法]
public static IPalette InvertedHue(this IPalette palette) [扩展方法]
public static int Count(this IPalette palette) [扩展方法]
```

### `public interface IPanel`
<!-- Interfaces\IPanel.cs -->
> A panel is a rectangular region outside the data area of a plot. Example panels include axes, colorbars, and titles

```csharp
public interface IPanel
// If false, the panel will not be displayed or report any size
public bool IsVisible { get, set; }
// Disallow the panel to be smaller than this
public float MinimumSize { get, set; }
// Disallow the panel to be larger than this
public float MaximumSize { get, set; }
```

### `public static class IPanelExtensions`
<!-- Interfaces\IPanel.cs -->

```csharp
public static class IPanelExtensions
// Returns true for X axes (bottom and top)
public static bool IsHorizontal(this IPanel panel) [扩展方法]
// Returns true for Y axes (left and right)
public static bool IsVertical(this IPanel panel) [扩展方法]
// Set min and max size to the same value to force this size to always be used
public static void LockSize(this IPanel panel, float size) [扩展方法]
// Remove all pixel size constraints
public static void ResetSize(this IPanel panel) [扩展方法]
```

### `public interface IPathStrategy`
<!-- Interfaces\IPathStrategy.cs -->
> Strategy for generating a path that connects a collection of pixels

```csharp
public interface IPathStrategy
public SKPath GetPath(IEnumerable<Pixel> pixels)
```

### `public interface IPlotControl`
<!-- Interfaces\IPlotControl.cs -->

```csharp
public interface IPlotControl
// Apply the platform-specific equivalent cursor
public void SetCursor(Cursor cursor)
```

### `public static class IPlotControlExtensions`
<!-- Interfaces\IPlotControl.cs -->

```csharp
public static class IPlotControlExtensions
public static Plot? GetPlotAtPixel(this IPlotControl plotControl, Pixel pixel) [扩展方法]
```

### `public interface IPlotMenu`
<!-- Interfaces\IPlotMenu.cs -->

```csharp
public interface IPlotMenu
public List<ContextMenuItem> ContextMenuItems { get; }
public void Reset()
public void Clear()
public void Add(string Label, Action<Plot> action)
public void AddSeparator()
```

### `public interface IPlottable`
<!-- Interfaces\IPlottable.cs -->
> Any object that renders shapes on the canvas using scale information from the axes must implement this interface.

```csharp
public interface IPlottable
```

### `public interface IPlottableGL : IPlottable`
<!-- Interfaces\IPlottableGL.cs -->
> This interface is applied to plottables which can be rendered directly on the GPU using an OpenGL shader

```csharp
public interface IPlottableGL : IPlottable
```

### `public interface IRenderAction`
<!-- Interfaces\IRenderAction.cs -->

```csharp
public interface IRenderAction
```

### `public interface IRenderLast`
<!-- Interfaces\IRenderLast.cs -->

```csharp
public interface IRenderLast
```

### `public interface IScatterSource`
<!-- Interfaces\IScatterSource.cs -->
> Represents a series of data points with distinct X and Y positions in coordinate space.

```csharp
public interface IScatterSource
public CoordinateRange GetLimitsX()
public CoordinateRange GetLimitsY()
public int MinRenderIndex { get, set; }
public int MaxRenderIndex { get, set; }
```

### `public interface ISignalSource`
<!-- Interfaces\ISignalSource.cs -->
> This interface is used by plottables to access data while rendering. This interface describes Y data sampled along an X axis at a fixed period.

```csharp
public interface ISignalSource
// Do not display data above this index
public int MaximumIndex { get, set; }
// Do not display data below this index
public int MinimumIndex { get, set; }
public CoordinateRange GetLimitsX()
public CoordinateRange GetLimitsY()
```

### `public interface ISignalXYSource`
<!-- Interfaces\ISignalXYSource.cs -->

```csharp
public interface ISignalXYSource
// Multiply Y values by this scale factor (before applying offset)
public double YScale { get, set; }
// Multiply X values by this scale factor (before applying offset)
public double XScale { get, set; }
// Do not display data below this index
public int MinimumIndex { get, set; }
// Do not display data above this index
public int MaximumIndex { get, set; }
// If enabled, Xs will be vertical and Ys will be horizontal.
public bool Rotated { get, set; }
```

### `public interface IStarAxis`
<!-- Interfaces\IStarAxis.cs -->

```csharp
public interface IStarAxis
public void Render(RenderPack rp, IAxes axes, double maxSpokeLength, int numSpokes, float rotationDegrees = 0)
```

### `public interface ITickGenerator`
<!-- Interfaces\ITickGenerator.cs -->

```csharp
public interface ITickGenerator
```

### `public interface IVectorFieldSource`
<!-- Interfaces\IVectorFieldSource.cs -->

```csharp
public interface IVectorFieldSource
public IReadOnlyList<RootedCoordinateVector> GetRootedVectors()
public CoordinateRange GetLimitsX()
public CoordinateRange GetLimitsY()
public int MinRenderIndex { get, set; }
public int MaxRenderIndex { get, set; }
```

### `public interface IXAxis : IAxis`
<!-- Interfaces\IXAxis.cs -->
> Horizontal axis

```csharp
public interface IXAxis : IAxis
public double Width { get; }
```

### `public interface IYAxis : IAxis`
<!-- Interfaces\IYAxis.cs -->
> Vertical axis

```csharp
public interface IYAxis : IAxis
public double Height { get; }
```

### `public interface IZoomRectangle`
<!-- Interfaces\IZoomRectangle.cs -->

```csharp
public interface IZoomRectangle
```

### `public class Image : IDisposable`
<!-- Primitives\Image.cs -->
> Bitmap representation of an image with helper methods for manipulating the image and enabling IO with other platforms

```csharp
public class Image : IDisposable
public int Width
public int Height
public PixelSize Size
public PixelFormat PixelFormat
public AlphaType AlphaType
// Create an Image from the snapshot of an existing Surface
public Image(SKSurface surface)
// Create an Image from a file on disk
public Image(string filename)
// Create an Image from a byte array of image data encoded in a common file format
public Image(byte[] bytes)
// Create an Image from an existing bitmap
public Image(SKBitmap bmp)
// Create a black Image with the given dimensions
public Image(int width, int height) : this(width, height, Colors.Black)
// Create a black Image with the given dimensions
public Image(PixelSize size) : this((int)size.Width, (int)size.Height, Colors.Black)
// Create an image filled with the given color
public Image(int width, int height, Color color)
// Create a grayscale Image from a 2D array of bytes. R, G, and B channels will all be set to the given value for each pixel.
public Image(byte[,] pixelArray)
// Create an Image from a 3D array of bytes with axes representing Y position, X position, and Color
public Image(byte[,,] pixelArray)
// Return the image as a platform-agnostic byte array that can be consumed by any common image library
public byte[] GetImageBytes(ImageFormat format = ImageFormat.Png, int quality = 100)
public SavedImageInfo SaveJpeg(string path, int quality = 85)
public SavedImageInfo SavePng(string path)
public SavedImageInfo SaveBmp(string path)
public SavedImageInfo SaveWebp(string path, int quality = 85)
public SavedImageInfo Save(string path, ImageFormat format = ImageFormat.Png, int quality = 85)
public void Dispose()
// Draw the image onto the given canvas
public void Render(SKCanvas canvas, PixelRect target, Paint paint, bool antiAlias)
// Return the image as a 2D byte array grayscale image with axes representing X and Y positions. Grayscale values for each pixel are the mean of R, G, and B channels.
public byte[,] GetArrayGrayscale()
// Return the image as a 3D byte array with axes representing X position, Y position, and Color
public byte[,,] GetArrayRGB()
// Return a new image with brightness/contrast maximized to fit the range of the data
public Image GetAutoscaledImage()
// Return a new image with dimensions scaled by the given scale factor. A scale factor of 2.0 will double the size of the returned image.
public Image Scaled(double scale, bool antiAlias = true)
// Return a new image with dimensions scaled by the given scale factors. A scale factor of 2.0 will double the size of the returned image.
public Image Scaled(double scaleX, double scaleY, bool antiAlias = true)
// Return a new image resized to fit the given dimensions.
public Image Resized(int newWidth, int newHeight, bool antiAlias = true)
```

### `public enum ImageFormat { Bmp, Jpeg, Png, Webp, Svg, }`
<!-- Primitives\ImageFormat.cs -->

```csharp
public enum ImageFormat { Bmp, Jpeg, Png, Webp, Svg, }
成员: Bmp, Jpeg, Png, Webp, Svg
```

### `public static class ImageFormatExtensions`
<!-- Primitives\ImageFormat.cs -->

```csharp
public static class ImageFormatExtensions
public static bool IsRasterFormat(this ImageFormat format) [扩展方法]
public static SKEncodedImageFormat ToSKFormat(this ImageFormat fmt) [扩展方法]
```

### `public static class ImageFormats`
<!-- Primitives\ImageFormat.cs -->

```csharp
public static class ImageFormats
public static ImageFormat FromFileExtension(string ext)
public static ImageFormat FromFilename(string filename)
```

### `public static class ImageOperations`
<!-- ImageOperations.cs -->

```csharp
public static class ImageOperations
public static string GetImageHtml(byte[] bytes, string imageType = "png", string classContent = "", string styleContent = "")
```

### `public enum ImagePosition { /// <summary> /// Image placed at the upper-left of the rectangle with no scaling. /// </summary> TopLeft, /// <summary> /// Image placed at the center of the rectangle with no scaling. /// </summary> Center, /// <summary> /// Fill image in X and Y to completely fill the area. /// The aspect ratio may change, appearing to distort the image. /// </summary> Stretch, /// <summary> /// Scale the image as large as possible such that it will fit /// entirely within the rectangle. This may result in whitespace /// on the edges if the image and rectangle have different aspect ratios. /// </summary> Fill, /// <summary> /// Scale the image by zooming in so it entirely fills the /// rectangle. It the aspect ratios are not the same, some of /// the image may lie outside the rectangle after scaling. Zoom, }`
<!-- Primitives\ImagePosition.cs -->
> Describes how to size and position an image inside a given rectangle

```csharp
public enum ImagePosition { /// <summary> /// Image placed at the upper-left of the rectangle with no scaling. /// </summary> TopLeft, /// <summary> /// Image placed at the center of the rectangle with no scaling. /// </summary> Center, /// <summary> /// Fill image in X and Y to completely fill the area. /// The aspect ratio may change, appearing to distort the image. /// </summary> Stretch, /// <summary> /// Scale the image as large as possible such that it will fit /// entirely within the rectangle. This may result in whitespace /// on the edges if the image and rectangle have different aspect ratios. /// </summary> Fill, /// <summary> /// Scale the image by zooming in so it entirely fills the /// rectangle. It the aspect ratios are not the same, some of /// the image may lie outside the rectangle after scaling. Zoom, }
成员: TopLeft, Center, Stretch, Fill, Zoom
```

### `public static class ImageScaleModeExtensions`
<!-- Primitives\ImagePosition.cs -->

```csharp
public static class ImageScaleModeExtensions
// Return the image rectangle to display inside a target rectangle
public static PixelRect GetRect(this ImagePosition position, PixelSize imageSize, PixelRect targetRect) [扩展方法]
```

### `public readonly record struct IndexRange(int Min, int Max)`
<!-- Primitives\IndexRange.cs -->
> Represents a range of indexes in an array (inclusive)

```csharp
public readonly record struct IndexRange(int Min, int Max)
// The IndexRange that represents an empty collection
public static readonly IndexRange None = new IndexRange(-1, -1, 0)
public int Length { get; }
public bool IsValid
```

### `public class InteractiveHandle(IHasInteractiveHandles parent, Cursor cursor, int index = 0)`
<!-- Primitives\InteractiveHandle.cs -->

```csharp
public class InteractiveHandle(IHasInteractiveHandles parent, Cursor cursor, int index = 0)
// The plottable this handle belongs to. This is useful when events pass handles themselves.
public IHasInteractiveHandles Parent { get; }
// The index that uniquely identifies this handle. This value is only useful for interactive objects with multiple handles.
public int Index { get; }
// Cursor the control should use when interacting with this handle
public Cursor Cursor { get; }
public override string ToString()
```

### `public class Label : LabelStyle`
<!-- Primitives\LabelStyle.cs -->

```csharp
public class Label : LabelStyle
```

### `public class LabelStyle`
<!-- Primitives\LabelStyle.cs -->

```csharp
public class LabelStyle
// Set this to globally enable support for right-to-left (RTL) languages
public static bool RTLSupport { get, set; }
public bool IsVisible { get, set; }
public string Text { get, set; }
public Alignment Alignment { get, set; }
// Rotation in degrees clockwise from 0 (horizontal text)
public float Rotation { get, set; }
public Color ForeColor { get, set; }
public Color BackColor { get, set; }
public Color BackgroundColor { get, set; }
public Color BorderColor { get, set; }
public float BorderWidth { get, set; }
public PixelRect LastRenderPixelRect { get, set; }
public Color ShadowColor { get, set; }
public PixelOffset ShadowOffset { get, set; }
public bool AntiAliasBackground { get, set; }
public bool AntiAliasText { get, set; }
public bool SubpixelText { get, set; }
public SKTypeface? Font { get, set; }
public string FontName { get, set; }
public float FontSize { get, set; }
public bool Bold { get, set; }
public bool Underline { get, set; }
public double UnderlineWidth { get, set; }
public double UnderlineOffset { get, set; }
// Manually defined line height in pixels. If not defined, the default line spacing will be used (according to the typeface, size, etc.)
public float? LineSpacing { get, set; }
public bool Italic = false
public bool AntiAlias = true
public float Padding { get, set; }
public PixelPadding PixelPadding { get, set; }
public float PointSize = 0
public bool PointFilled = false
public Color PointColor = Colors.Magenta
public float OffsetX = 0
public float OffsetY = 0
public float BorderRadiusX = 0
public float BorderRadiusY = 0
public float BorderRadius { get, set; }
// If supplied, this label will be displayed as an image and its text and styling properties will be ignored
public Image? Image { get, set; }
public static LabelStyle Default
// Use the characters in to determine an installed system font most likely to support this character set.
public void SetBestFont()
public void ApplyToPaint(Paint paint)
// Return size information for the contents of the property
public MeasuredText Measure(Paint paint) // NOTE: This should never be called internally
public MeasuredText Measure(string text, Paint paint)
// Use the Label's size and to determine where it should be drawn relative to the given rectangle (aligned to the rectangle according to ).
public Pixel GetRenderLocation(PixelRect rect, Alignment rectAlignment, float offsetX, float offsetY, Paint paint)
public void Render(SKCanvas canvas, Pixel px, Paint paint, string text, bool bottom = true)
public void Render(SKCanvas canvas, Pixel px, Paint paint, bool bottom = true)
public (string text, float height) MeasureHighestString(string[] strings, Paint paint)
public (string text, PixelLength width) MeasureWidestString(string[] strings, Paint paint)
```

### `public abstract class LabelStyleProperties : IHasLabel`
<!-- Primitives\LabelStyleProperties.cs -->
> Classes with a can inherit this to include shortcuts to its most commonly used properties.

```csharp
public abstract class LabelStyleProperties : IHasLabel
public abstract LabelStyle LabelStyle { get, set; }
public float LabelOffsetX { get, set; }
public float LabelOffsetY { get, set; }
public float LabelRotation { get, set; }
public float LabelPadding { set; }
public PixelPadding LabelPixelPadding { get, set; }
public PixelRect LabelLastRenderPixelRect
public string LabelText { get, set; }
public Alignment LabelAlignment { get, set; }
public string LabelFontName { get, set; }
public float LabelFontSize { get, set; }
public float? LabelLineSpacing { get, set; }
public bool LabelItalic { get, set; }
public bool LabelBold { get, set; }
public bool LabelUnderline { get, set; }
public double LabelUnderlineWidth { get, set; }
public double LabelUnderlineOffset { get, set; }
public Color LabelFontColor { get, set; }
public Color LabelBackgroundColor { get, set; }
public float LabelBorderRadius { get, set; }
public float LabelBorderRadiusX { get, set; }
public float LabelBorderRadiusY { get, set; }
public float LabelBorderWidth { get, set; }
public Color LabelBorderColor { get, set; }
public Color LabelShadowColor { get, set; }
public PixelOffset LabelShadowOffset { get, set; }
```

### `public readonly struct Layout : IEquatable<Layout>`
<!-- Primitives\Layout.cs -->

```csharp
public readonly struct Layout : IEquatable<Layout>
// Size of the figure this layout represents
public readonly PixelRect FigureRect { get; }
// Final size of the data area
public readonly PixelRect DataRect { get; }
// Distance (pixels) each panel is to be placed from the edge of the data rectangle
public readonly Dictionary<IPanel, float> PanelOffsets { get; }
// Size (pixels) of each panel in the dimension perpendicular to the data edge it is placed on
public readonly Dictionary<IPanel, float> PanelSizes { get; }
public Layout(PixelRect figureRect, PixelRect dataRect, Dictionary<IPanel, float> sizes, Dictionary<IPanel, float> offsets)
public bool Equals(Layout other)
```

### `public class LayoutManager`
<!-- LayoutManager.cs -->
> A collection of methods for making common adjustments to plot layouts

```csharp
public class LayoutManager
public ILayoutEngine LayoutEngine { get, set; }
public LayoutManager(Plot plot)
// Automatically resize the layout on each render to achieve the best fit
public void Default()
// Apply a fixed layout using the given rectangle to define the data area
public void Fixed(PixelRect dataRect)
// Apply a fixed layout using the given padding to define space between the data area and the edge of the figure
public void Fixed(PixelPadding padding)
// Helper method to set visibility of all axes and title panels. Hiding all panels allows the data area to the extend to the edge of the figure. This method hides the title, but call "Plot.Title()" to re-enable it.
public void Frameless(bool hideAllPanels = true)
```

### `public class Legend(Plot plot) : IPlottable, IHasOutline, IHasBackground, IHasShadow`
<!-- Primitives\Legend.cs -->

```csharp
public class Legend(Plot plot) : IPlottable, IHasOutline, IHasBackground, IHasShadow
public Plot Plot { get; }
public bool IsVisible { get, set; }
// Position of the legend relative to the data area
public Alignment Alignment { get, set; }
// Position of the legend relative to the data area
public Alignment Location { get, set; }
// Stack items in the legend according to this preferred orientation
public Orientation Orientation { get, set; }
// Distance from the edge of the data area to the edge of the legend
public PixelPadding Margin { get, set; }
// Distance between the legend frame and the items within it
public PixelPadding Padding { get, set; }
// Width of the symbol in a legend item
public float SymbolWidth { get, set; }
// Height of the symbol in a legend item
public float SymbolHeight { get, set; }
// Padding between a symbol and label within a legend item
public float SymbolPadding { get, set; }
// Space separating legend items
public PixelPadding InterItemPadding { get, set; }
// Items in this list will always be displayed in the legend
public List<LegendItem> ManualItems { get, set; }
// If enabled, items in horizontal oriented legends will not be aligned in columns but instead resized tightly to fit their contents
public bool TightHorizontalWrapping { get, set; }
public bool ShowItemRectangles_DEBUG { get, set; }
// Enabling this allows multi-language text in the figure legend, but may slow down the render loop.
public bool SetBestFontOnEachRender { get, set; }
// If set, this overrides the value in the LegendItem's FontStyle
public float? FontSize { get, set; }
// If set, this overrides the value in the LegendItem's FontStyle
public string? FontName { get, set; }
// If set, this overrides the value in the LegendItem's FontStyle
public Color? FontColor { get, set; }
public FillStyle Font { get, set; }
public bool AllowMultiline { get, set; }
public ILegendLayout Layout { get, set; }
public PixelSize LastRenderSize { get, set; }
public LineStyle OutlineStyle { get, set; }
public float OutlineWidth { get, set; }
public LinePattern OutlinePattern { get, set; }
public Color OutlineColor { get, set; }
public FillStyle BackgroundFill { get, set; }
public FillStyle BackgroundFillStyle { get; }
public Color BackgroundColor { get, set; }
public Color BackgroundHatchColor { get, set; }
public IHatch? BackgroundHatch { get, set; }
public FillStyle ShadowFill { get, set; }
public FillStyle ShadowFillStyle { get; }
public Color ShadowColor { get, set; }
public PixelOffset ShadowOffset { get, set; }
public Alignment ShadowAlignment { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
// If supplied, always use this marker shape
public MarkerShape? MarkerShapeOverride { get, set; }
public bool DisplayPlottableLegendItems { get, set; }
// If enabled, the legend will include items from hidden plottables. They will be partially painted over using the background color to simulate semitransparency.
public bool ShowItemsFromHiddenPlottables { get, set; }
// This property controls how visible legend items are when their parent control's visibility is disabled. This property is only used when is enabled.
public double HiddenItemOpacity { get, set; }
public virtual LegendItem[] GetItems()
public LegendLayout GetLayout(PixelSize size, Paint paint)
// Return an Image containing just the legend
public Image GetImage()
// Return contents of a SVG image containing just the legend
public string GetSvgXml()
// This is called automatically by the render manager
public virtual void Render(RenderPack rp)
public void Render(SKCanvas canvas, Paint paint, PixelRect rect, Alignment alignment)
```

### `public class LegendItem : LabelStyleProperties, IHasMarker, IHasLine, IHasFill, IHasArrow, IHasLabel`
<!-- Primitives\LegendItem.cs -->

```csharp
public class LegendItem : LabelStyleProperties, IHasMarker, IHasLine, IHasFill, IHasArrow, IHasLabel
public bool IsVisible { get, set; }
// Plottable this legend item is associated with
public IPlottable? Plottable { get, set; }
// If populated, this legend item will appear at the top in the legend, sequenced in order according to this index.
public int? Index { get, set; }
public override LabelStyle LabelStyle { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public FillStyle FillStyle { get, set; }
public Color FillColor { get, set; }
public Color FillHatchColor { get, set; }
public IHatch? FillHatch { get, set; }
public LineStyle OutlineStyle { get, set; }
public float OutlineWidth { get, set; }
public LinePattern OutlinePattern { get, set; }
public Color OutlineColor { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
public ArrowStyle ArrowStyle { get, set; }
public Color ArrowLineColor { get, set; }
public float ArrowLineWidth { get, set; }
public Color ArrowFillColor { get, set; }
public float ArrowMinimumLength { get, set; }
public float ArrowMaximumLength { get, set; }
public float ArrowOffset { get, set; }
public ArrowAnchor ArrowAnchor { get, set; }
public float ArrowWidth { get, set; }
public float ArrowheadAxisLength { get, set; }
public float ArrowheadLength { get, set; }
public float ArrowheadWidth { get, set; }
public LineStyle Line { get, set; }
public MarkerStyle Marker { get, set; }
public string Label { get, set; }
public static IEnumerable<LegendItem> None
public static IEnumerable<LegendItem> Single(LegendItem item)
public static IEnumerable<LegendItem> Single(IPlottable plottable, string label, MarkerStyle markerStyle)
public static IEnumerable<LegendItem> Single(IPlottable plottable, string label, MarkerStyle markerStyle, LineStyle lineStyle)
public static IEnumerable<LegendItem> Single(IPlottable plottable, string label, LineStyle lineStyle)
public static IEnumerable<LegendItem> Single(IPlottable plottable, string label, FillStyle fillStyle)
public static IEnumerable<LegendItem> Single(IPlottable plottable, string label, FillStyle fillStyle, LineStyle lineStyle)
public static IEnumerable<LegendItem> Single(IPlottable plottable, string label, LineStyle lineStyle, MarkerStyle markerStyle)
```

### `public readonly struct LegendLayout`
<!-- Primitives\LegendLayout.cs -->

```csharp
public readonly struct LegendLayout
required public LegendItem[] LegendItems { get, init; }
required public PixelRect LegendRect { get, init; }
required public PixelRect[] LabelRects { get, init; }
required public PixelRect[] SymbolRects { get, init; }
public static LegendLayout NoLegend
```

### `public class Line`
<!-- Primitives\Line.cs -->

```csharp
public class Line
public Coordinates Start { get, set; }
public Coordinates End { get, set; }
public static Line Default
public LineStyle Style { get, set; }
// Create a default line using x and y values
public Line(double x1, double y1, double x2, double y2)
// Create a default line using coordinates
public Line(Coordinates start, Coordinates end)
// Create a styled line using x and y values, LinePattern, and LineStyle information
public Line(double x1, double y1, double x2, double y2, LineStyle style)
// Create a styled line using coordinates, LinePattern, and LineStyle information
public Line(Coordinates start, Coordinates end, LineStyle style)
public override string ToString()
```

### `public readonly struct LinePattern(float[] intervals, float phase, string name)`
<!-- Primitives\LinePattern.cs -->

```csharp
public readonly struct LinePattern(float[] intervals, float phase, string name)
public static LinePattern Solid { get; }
public static LinePattern Dashed { get; }
public static LinePattern DenselyDashed { get; }
public static LinePattern Dotted { get; }
public float[] Intervals { get; }
public float Phase { get; }
public string Name { get; }
public static LinePattern[] GetAllPatterns()
public SKPathEffect GetPathEffect()
```

### `public class LineStyle`
<!-- Primitives\LineStyle.cs -->
> This configuration object (reference type) permanently lives inside objects which require styling. It is recommended to use this object as an init-only property.

```csharp
public class LineStyle
// Width of the line (in pixels)
public float Width { get, set; }
// If enabled, is ignored and lines are rendered as a single pixel (regardless of scale factor)
public bool Hairline { get, set; }
// If enabled will make this line appear hand drawn.
public bool HandDrawn { get, set; }
public double HandDrawnSegmentLength { get, set; }
public double HandDrawnJitter { get, set; }
public Color Color { get, set; }
public LinePattern Pattern { get, set; }
public bool IsVisible { get, set; }
public bool AntiAlias { get, set; }
public bool Rounded { get, set; }
public SKStrokeCap StrokeCap { get, set; }
public SKStrokeJoin StrokeJoin { get, set; }
public float StrokeMiter { get, set; }
public static LineStyle None
public LineStyle Clone()
public LineStyle()
public LineStyle(float width)
public LineStyle(float width, Color color)
public LineStyle(float width, Color color, LinePattern pattern)
public bool CanBeRendered { get; }
public void Render(SKCanvas canvas, Pixel[] starts, Pixel[] ends, Paint paint)
public void Render(SKCanvas canvas, PixelLine[] lines, Paint paint)
public void Render(RenderPack rp, PixelLine line)
public void Render(SKCanvas canvas, PixelLine line, Paint paint)
public void Render(RenderPack rp, PixelRect rect)
public void Render(SKCanvas canvas, PixelRect rect, Paint paint, bool contract = false)
public void Render(SKCanvas canvas, SKPath path, Paint paint)
public void Render(SKCanvas canvas, Paint paint, PixelLine line)
public void ApplyToPaint(Paint paint)
```

### `public class LinkedAxisRule(IAxis sourceAxis, IAxis targetAxis, Plot targetPlot)`
<!-- Primitives\LinkedAxisRule.cs -->

```csharp
public class LinkedAxisRule(IAxis sourceAxis, IAxis targetAxis, Plot targetPlot)
public IAxis SourceAxis { get; }
public IAxis TargetAxis
public Plot TargetPlot
```

### `public class Location`
<!-- Primitives\Location.cs -->
> Describes X/Y location in pixel or coordinate space

```csharp
public class Location
public LocationUnit Unit { get, init; }
public double X { get, set; }
public double Y { get, set; }
public Pixel GetPixel()
public Coordinates GetCoordinates()
public static Location Pixel(float x, float y)
public static Location Coordinates(float x, float y)
public static Location Unspecified { get; }
```

### `public enum LocationUnit { Unspecified, Coordinates, Pixel, }`
<!-- Primitives\LocationUnit.cs -->

```csharp
public enum LocationUnit { Unspecified, Coordinates, Pixel, }
成员: Unspecified, Coordinates, Pixel
```

### `public enum MarkerShape { None, FilledCircle, OpenCircle, FilledSquare, OpenSquare, FilledTriangleUp, OpenTriangleUp, FilledTriangleDown, OpenTriangleDown, FilledDiamond, OpenDiamond, Eks, Cross, VerticalBar, HorizontalBar, TriUp, TriDown, Asterisk, HashTag, OpenCircleWithDot, OpenCircleWithCross, OpenCircleWithEks, CircleWithLineLeft, CircleWithLineRight, TriangleWithLineLeft, TriangleWithLineRight }`
<!-- Primitives\MarkerShape.cs -->
> Standard markers supported by ScottPlot. See demo app for information about creating custom marker shapes.

```csharp
public enum MarkerShape { None, FilledCircle, OpenCircle, FilledSquare, OpenSquare, FilledTriangleUp, OpenTriangleUp, FilledTriangleDown, OpenTriangleDown, FilledDiamond, OpenDiamond, Eks, Cross, VerticalBar, HorizontalBar, TriUp, TriDown, Asterisk, HashTag, OpenCircleWithDot, OpenCircleWithCross, OpenCircleWithEks, CircleWithLineLeft, CircleWithLineRight, TriangleWithLineLeft, TriangleWithLineRight }
成员: None, FilledCircle, OpenCircle, FilledSquare, OpenSquare, FilledTriangleUp, OpenTriangleUp, FilledTriangleDown, OpenTriangleDown, FilledDiamond, OpenDiamond, Eks, Cross, VerticalBar, HorizontalBar, TriUp, TriDown, Asterisk, HashTag, OpenCircleWithDot, OpenCircleWithCross, OpenCircleWithEks, CircleWithLineLeft, CircleWithLineRight, TriangleWithLineLeft, TriangleWithLineRight
```

### `public static class MarkerShapeExtensions`
<!-- Primitives\MarkerShape.cs -->

```csharp
public static class MarkerShapeExtensions
// Get the marker object for a standard marker shape
public static IMarker GetMarker(this MarkerShape shape) [扩展方法]
// Used to determine whether a color passed into a LineStyle constructor will be treated as line color or fill color.
public static bool IsLineOnly(this MarkerShape shape) [扩展方法]
```

### `public class MarkerStyle : IHasLine, IHasFill, IHasOutline`
<!-- Primitives\MarkerStyle.cs -->
> This configuration object (reference type) permanently lives inside objects which require styling. It is recommended to use this object as an init-only property.

```csharp
public class MarkerStyle : IHasLine, IHasFill, IHasOutline
public bool IsVisible { get, set; }
public MarkerShape Shape { get, set; }
// Diameter of the marker (in pixels)
public float Size { get, set; }
public Color MarkerColor { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public FillStyle FillStyle { get, set; }
public Color FillColor { get, set; }
public Color FillHatchColor { get, set; }
public IHatch? FillHatch { get, set; }
public IMarker? CustomRenderer { get, set; }
public bool FillOutline { get, set; }
public LineStyle Outline { get, set; }
public LineStyle OutlineStyle { get, set; }
public float OutlineWidth { get, set; }
public LinePattern OutlinePattern { get, set; }
public Color OutlineColor { get, set; }
public FillStyle Fill { get, set; }
public MarkerStyle()
public MarkerStyle(MarkerShape shape, float size) : this(shape, size, Colors.Gray)
public MarkerStyle(MarkerShape shape, float size, Color color)
public static MarkerStyle Default
public static MarkerStyle None
public void Render(RenderPack rp, Pixel px)
public void Render(SKCanvas canvas, Pixel px, Paint paint)
```

### `public readonly struct MeasuredText`
<!-- Primitives\MeasuredText.cs -->

```csharp
public readonly struct MeasuredText
// Size of the entire multiline label in pixels. Width is the largest value returned by paint.MeasureText(). Height is the line height multiplied by the number of lines.
public PixelSize Size { get, init; }
// Vertical spacing between each line. This is the value returned by GetFontMetrics().
public float LineHeight { get, init; }
// Width of each line of text in pixel units.
public float[] LineWidths { get, init; }
// Recommended vertical offset when calling SKCanvas.DrawText(). See https://github.com/ScottPlot/ScottPlot/issues/3700 for details.
public required float VerticalOffset { get, init; }
// Distance below the baseline the rendered font may occupy.
public required float Bottom { get, init; }
// Width of the entire text. Equals the length of the widest line.
public float Width
// Height of the entire text.
public float Height
// Return a rectangle representing the bounding box of the entire text with the alignment point centered at the origin.
public PixelRect Rect(Alignment alignment)
```

### `public class MinMaxCache`
<!-- DataSources\MinMaxCache.cs -->

```csharp
public class MinMaxCache
public int CachePeriod { get; }
public MinMaxCache(IReadOnlyList<double> data, int cachePeriod = 1000)
public SignalRangeY GetMinMax(int start, int end)
```

### `public class MultiAxisLimits(Plot plot)`
<!-- Primitives\MultiAxisLimits.cs -->
> Stores the for all axes on the plot and has methods that can be used to recall them at a future point in time.

```csharp
public class MultiAxisLimits(Plot plot)
public readonly Plot Plot = plot
// Set all axis limits to their original ranges
public void Recall()
```

### `public class Multiplot : IMultiplot`
<!-- Multiplot.cs -->

```csharp
public class Multiplot : IMultiplot
public MultiplotSharedAxisManager SharedAxes { get; }
public SubplotCollection Subplots { get; }
public MultiplotLayoutSnapshot LastRender { get; }
public List<IMultiplotPreRenderAction> PreRenderActions { get, set; }
public IMultiplotLayout Layout { get, set; }
public Multiplot() : this(new Plot())
public Multiplot(Plot plot)
public void Render(SKCanvas canvas, PixelRect figureRect)
```

### `public class MultiplotLayoutSnapshot`
<!-- Primitives\MultiplotLayoutSnapshot.cs -->

```csharp
public class MultiplotLayoutSnapshot
public void Remember(Plot plot, PixelRect subplotRect)
public PixelRect? GetLastRenderRectangle(Plot plot)
public void Forget(Plot plot)
public void Reset()
// Return the plot beneath the given pixel according to the last render. Returns null if no render occurred or the pixel is not over a plot.
public Plot? GetPlotAtPixel(Pixel pixel)
```

### `public class MultiplotSharedAxisManager : IMultiplotPreRenderAction`
<!-- MultiplotSharedAxisManager.cs -->

```csharp
public class MultiplotSharedAxisManager : IMultiplotPreRenderAction
// Link horizontal axis limits of the given collection of plots so when one changes they all change in unison
public void ShareX(IEnumerable<Plot> plots)
// Link vertical axis limits of the given collection of plots so when one changes they all change in unison
public void ShareY(IEnumerable<Plot> plots)
public void UpdateSharedPlotAxisLimits()
public void Invoke()
```

### `public class MutableCoordinateLine`
<!-- Primitives\MutableCoordinateLine.cs -->

```csharp
public class MutableCoordinateLine
public double X1 { get, set; }
public double X2 { get, set; }
public double Y1 { get, set; }
public double Y2 { get, set; }
public Coordinates Point1 { get, set; }
public Coordinates Point2 { get, set; }
public CoordinateLine CoordinateLine
public double XMin
public double XMax
public double YMin
public double YMax
public AxisLimits AxisLimits
public void Update(CoordinateLine line)
```

### `public static class NumericConversion`
<!-- NumericConversion.cs -->
> This class contains type-specific methods to convert between generic values and doubles optimized for performance using platform-specific features. See discussion in https://github.com/ScottPlot/ScottPlot/pull/1927

```csharp
public static class NumericConversion
public static double[] GenericToDoubleArray<T>(T[] values)
public static double[] GenericToDoubleArray<T>(IEnumerable<T> values)
// Returns the double value of a using a conversion technique optimized for the platform.
public static double GenericToDouble<T>(ref T value)
public static Coordinates GenericToCoordinates<T1, T2>(ref T1 x, ref T2 y)
public static Coordinates[] GenericToCoordinates<T1, T2>(IEnumerable<T1> xs, IEnumerable<T2> ys)
// Returns the double value of the at position in using a conversion technique optimized for the platform.
public static double GenericToDouble<T>(IReadOnlyList<T> list, int i)
// Returns the double value of the at position in using a conversion technique optimized for the platform.
public static double GenericToDouble<T>(T[] array, int i)
// Creates a for a given double using a conversion technique optimized for the platform.
public static void DoubleToGeneric<T>(double value, out T v)
public static T DoubleToGeneric<T>(double value)
public static T[] DoubleToGeneric<T>(this double[] input) [扩展方法]
public static T[] ToGenericArray<T>(this double[] input) [扩展方法]
public static byte AddBytes(byte a, byte b)
public static byte Multiply(byte a, byte b)
public static byte SubtractBytes(byte a, byte b)
public static bool LessThanOrEqualBytes(byte a, byte b)
public static Func<T, T, T> CreateAddFunction<T>()
public static Func<T, T, T> CreateMultFunction<T>()
public static Func<T, T, T> CreateSubtractFunction<T>()
public static Func<T, T, bool> CreateLessThanOrEqualFunction<T>()
public static T Clamp<T>(T input, T min, T max) where T : IComparable
public static sbyte Clamp(sbyte value, sbyte min, sbyte max)
public static byte Clamp(byte value, byte min, byte max)
public static short Clamp(short value, short min, short max)
public static ushort Clamp(ushort value, ushort min, ushort max)
public static int Clamp(int value, int min, int max)
public static uint Clamp(uint value, uint min, uint max)
public static long Clamp(long value, long min, long max)
public static ulong Clamp(ulong value, ulong min, ulong max)
public static float Clamp(float value, float min, float max)
public static double Clamp(double value, double min, double max)
public static decimal Clamp(decimal value, decimal min, decimal max)
public static bool AreReal(double x, double y)
public static bool IsReal(double x)
public static bool IsReal(float x)
// Convert a number that can be plotted on a numeric axis into a DateTime
public static DateTime ToDateTime(double value)
// Convert a DateTime into a number that can be plotted on a numeric axis
public static double ToNumber(DateTime value)
public static double IncrementLargeDouble(double value)
public static double DecrementLargeDouble(double value)
```

### `public struct OHLC`
<!-- Primitives\OHLC.cs -->

```csharp
public struct OHLC
public double Open { get, set; }
public double High { get, set; }
public double Low { get, set; }
public double Close { get, set; }
public DateTime DateTime { get, set; }
public TimeSpan TimeSpan { get, set; }
public OHLC(double open, double high, double low, double close) : this(open, high, low, close, DateTime.MinValue, TimeSpan.FromDays(1))
public OHLC(double open, double high, double low, double close, DateTime start, TimeSpan span)
public readonly OHLC Clone()
public readonly OHLC WithOpen(double price)
public readonly OHLC WithHigh(double price)
public readonly OHLC WithLow(double price)
public readonly OHLC WithClose(double price)
public readonly OHLC WithDate(DateTime dateTime)
public readonly OHLC WithTimeSpan(TimeSpan timeSpan)
public readonly OHLC ShiftedBy(TimeSpan timeSpan)
public readonly OHLC ShiftedBy(double delta)
```

### `public enum Orientation { Horizontal, Vertical }`
<!-- Primitives\Orientation.cs -->

```csharp
public enum Orientation { Horizontal, Vertical }
成员: Horizontal, Vertical
```

### `public class Paint : IDisposable`
<!-- Primitives\Paint.cs -->

```csharp
public class Paint : IDisposable
public Color Color { get, set; }
public bool IsStroke { get, set; }
public float StrokeWidth { get, set; }
public bool IsAntialias { get, set; }
public float StrokeMiter { get, set; }
public float TextSize { get, set; }
public float FontSpacing { get; }
public HorizontalAlignment TextAlign { set; }
public bool SubpixelText { get, set; }
public bool Bold { get, set; }
public ResizeFilter ResizeFilter { set; }
public SKPaint SKPaint { get, set; }
public SKFont SKFont { get, set; }
public SKColor SKColor { get, set; }
public SKTextAlign SKTextAlign { get, set; }
public SKTypeface SKTypeface { get, set; }
public SKShader? SKShader { get, set; }
public SKPathEffect SKPathEffect { get, set; }
public SKStrokeCap SKStrokeCap { get, set; }
public SKStrokeJoin SKStrokeJoin { get, set; }
public SKSamplingOptions SKSamplingOptions { get, set; }
public SKPaintStyle SKPaintStyle { get, set; }
public static Paint NewDisposablePaint()
public void Dispose()
public PixelRect MeasureText(string str)
public (float lineHeight, SKFontMetrics metrics) GetFontMetrics()
```

### `public static class Palette`
<!-- Primitives\Palette.cs -->

```csharp
public static class Palette
public static IPalette Default { get, set; }
// Create a custom palette from an array of colors
public static IPalette FromColors(string[] hexColors)
// Create a custom palette from an array of colors
public static IPalette FromColors(Color[] colors)
// Return an array containing every available palette
public static IPalette[] GetPalettes()
```

### `public class PieSlice : LabelStyleProperties, IHasLegendText, IHasLabel`
<!-- Primitives\PieSlice.cs -->

```csharp
public class PieSlice : LabelStyleProperties, IHasLegendText, IHasLabel
public string Label { get, set; }
public string LegendText { get, set; }
public double Value { get, set; }
public FillStyle Fill { get, set; }
public override LabelStyle LabelStyle { get, set; }
public Color FillColor { get, set; }
public PieSlice() : this(default, default, string.Empty)
public PieSlice(double value, Color color) : this(value, color, string.Empty)
public PieSlice(double value, Color color, string label)
```

### `public struct Pixel : IEquatable<Pixel>`
<!-- Primitives\Pixel.cs -->
> Represents an X/Y location on screen in pixel units. Pixels in screen units are distinct from with axis units. Pixels use precision, whereas use precision.

```csharp
public struct Pixel : IEquatable<Pixel>
// Horizontal position on the screen in pixel units. Larger numbers are farther right on the screen.
public float X
// Vertical position on the screen in pixel units. Larger numbers are lower on the screen.
public float Y
// Create a pixel, casting values into ones with precision
public Pixel(float x, float y)
// Create a pixel, casting values into ones with precision
public Pixel(double x, double y)
public override string ToString()
// Represents an invalid pixel location
public static Pixel NaN
public static Pixel Zero
// Convert the ScottPlot pixel to a SkiaSharp point
public SKPoint ToSKPoint()
public bool Equals(Pixel other)
public override bool Equals(object? obj)
public static bool operator ==(Pixel a, Pixel b)
public static bool operator !=(Pixel a, Pixel b)
public override int GetHashCode()
public static Pixel operator +(Pixel a, Pixel b)
public static Pixel operator -(Pixel a, Pixel b)
public static Pixel operator *(Pixel a, float b)
public static Pixel operator /(Pixel a, float b)
public readonly float DistanceFrom(Pixel px2)
public readonly Pixel WithOffset(float dX, float dY)
public readonly Pixel WithOffset(PixelOffset offset)
public readonly Pixel MovedRight(float dX)
public readonly Pixel MovedLeft(float dX)
public readonly Pixel MovedUp(float dY)
public readonly Pixel MovedDown(float dY)
public readonly Pixel Divide(float v)
public readonly Pixel Divide(float x, float y)
public readonly Pixel Multiply(float v)
public readonly Pixel Multiply(float x, float y)
```

### `public readonly struct PixelColumn`
<!-- Primitives\PixelColumn.cs -->
> This data structure describes a single vertical column of pixels that represents the Y span of an X range of data points.

```csharp
public readonly struct PixelColumn
public readonly float X
public readonly float Enter
public readonly float Exit
public readonly float Bottom
public readonly float Top
public bool HasData
public PixelColumn(float x, float enter, float exit, float bottom, float top)
public static PixelColumn WithoutData(float x)
public override string ToString()
```

### `public enum PixelFormat { Unknown = 0, Bgra8888, Rgba8888, }`
<!-- Primitives\Image.cs -->

```csharp
public enum PixelFormat { Unknown = 0, Bgra8888, Rgba8888, }
成员: Unknown, Bgra8888, Rgba8888
```

### `public readonly struct PixelLength`
<!-- Primitives\PixelLength.cs -->
> Represents a distance in pixel units

```csharp
public readonly struct PixelLength
public readonly float Length
public PixelLength(float length)
public static implicit operator PixelLength(float length)
public override string ToString()
```

### `public readonly struct PixelLine`
<!-- Primitives\PixelLine.cs -->
> Describes a straight line in pixel space

```csharp
public readonly struct PixelLine
public readonly float X1
public readonly float X2
public readonly float Y1
public readonly float Y2
public float XSpan
public float YSpan
public float Slope
public float SlopeRadians
public float SlopeDegrees
public float AngleRadians
public float AngleDegrees
public float YIntercept
public float Length
public float DeltaX
public float DeltaY
public Pixel Pixel1
public Pixel Pixel2
public Pixel Center
public PixelLine(float x1, float y1, float x2, float y2)
public PixelLine(Pixel px1, Pixel px2)
public override string ToString()
public PixelLine BackedUpBy(float distance)
public PixelLine WithDelta(float dx, float dy)
// Return the X position on the line at the given Y
public float X(float y = 0)
// Return the Y position on the line at the given X
public float Y(float x = 0)
```

### `public record struct PixelOffset(float X, float Y)`
<!-- Primitives\PixelOffset.cs -->
> Represents the distance from one pixel relative to another in pixel units. Increasing X offset moves a pixel to the right. Increasing Y offset moves a pixel downward.

```csharp
public record struct PixelOffset(float X, float Y)
public static PixelOffset Zero
public static PixelOffset NaN
public readonly PixelOffset WithY(float newY)
public readonly PixelOffset WithX(float newX)
```

### `public struct PixelPadding`
<!-- Primitives\PixelPadding.cs -->
> Represents the size (in pixels) of padding on all edges of a rectangle

```csharp
public struct PixelPadding
public float Left
public float Right
public float Bottom
public float Top
public float Horizontal
public float Vertical
public PixelPadding(float padding)
public PixelPadding(float x, float y)
public PixelPadding(float left, float right, float bottom, float top)
public PixelPadding(PixelSize figureSize, PixelRect dataArea)
public void Expand(float amount)
public void Contract(float amount)
public static PixelPadding Zero
```

### `public readonly struct PixelPath(Pixel[] pixels, bool close)`
<!-- Primitives\PixelPath.cs -->

```csharp
public readonly struct PixelPath(Pixel[] pixels, bool close)
public readonly Pixel[] Pixels = pixels
public readonly bool Close = close
public static PixelPath Closed(Pixel[] pixels)
public static PixelPath Open(Pixel[] pixels)
public static PixelPath Closed(IEnumerable<Pixel> pixels)
public static PixelPath Open(IEnumerable<Pixel> pixels)
```

### `public struct PixelRangeX(float x1, float x2)`
<!-- Primitives\PixelRangeX.cs -->
> Represents a range of pixels between two pixels on the horizontal axis. The value of will be SMALLER than the value of .

```csharp
public struct PixelRangeX(float x1, float x2)
public float Left { get, set; }
public float Right { get, set; }
public readonly float Span
public void Expand(float value)
public override readonly string ToString()
public readonly bool Contains(float position)
```

### `public struct PixelRangeY(float y1, float y2)`
<!-- Primitives\PixelRangeY.cs -->
> Represents a range of pixels between two pixels on the vertical axis used in Signal plots. The value of will be SMALLER than the value of .

```csharp
public struct PixelRangeY(float y1, float y2)
public float Top { get, set; }
public float Bottom { get, set; }
public readonly float Span
public void Expand(float value)
public override readonly string ToString()
public readonly bool Contains(float position)
```

### `public readonly struct PixelRect : IEquatable<PixelRect>`
<!-- Primitives\PixelRect.cs -->

```csharp
public readonly struct PixelRect : IEquatable<PixelRect>
public readonly float Left
public readonly float Right
public readonly float Bottom
public readonly float Top
public float HorizontalCenter
public float VerticalCenter
public float Width
public float Height
public bool HasArea
public Pixel TopLeft
public Pixel TopRight
public Pixel BottomLeft
public Pixel BottomRight
public Pixel LeftCenter
public Pixel RightCenter
public Pixel BottomCenter
public Pixel TopCenter
public Pixel Center
public PixelSize Size
public PixelLine BottomLine
public PixelLine TopLine
public PixelLine LeftLine
public PixelLine RightLine
public static PixelRect Zero
public static PixelRect NaN
// Create a rectangle from the bounding box of a circle centered at with radius
public PixelRect(Pixel center, float radius) : this(center.X - radius, center.X + radius, center.Y + radius, center.Y - radius)
// Create a rectangle with edges at the given pixel positions. This constructor will rectify the points so rectangles will always have positive area.
public PixelRect(Pixel corner1, Pixel corner2) : this(corner1.X, corner2.X, corner1.Y, corner2.Y)
// Create a rectangle representing pixels on a screen
public PixelRect(Pixel topLeftCorner, PixelSize size) : this(topLeftCorner.X, topLeftCorner.X + size.Width, topLeftCorner.Y, topLeftCorner.Y + size.Height)
// Create a rectangle representing pixels on a screen
public PixelRect(PixelOffset offset, PixelSize size) : this(offset.X, offset.X + size.Width, offset.Y, offset.Y + size.Height)
// Create a rectangle representing pixels on a screen
public PixelRect(Pixel topLeftCorner, float width, float height) : this(topLeftCorner.X, topLeftCorner.X + width, topLeftCorner.Y, topLeftCorner.Y + height)
// Create a rectangle representing pixels on a screen
public PixelRect(PixelSize size) : this(0, size.Width, size.Height, 0)
// Create a rectangle representing pixels on a screen
public PixelRect(float width, float height) : this(0, width, height, 0)
// Create a rectangle representing pixels on a screen
public PixelRect(PixelSize size, Pixel offset) : this(offset.X, size.Width, size.Height, offset.Y)
// Create a rectangle representing pixels on a screen
public PixelRect(PixelSize size, PixelOffset offset) : this(offset.X, size.Width, size.Height, offset.Y)
// Create a rectangle from the given edges. This constructor permits inverted rectangles with negative area.
public PixelRect(float left, float right, float bottom, float top)
// Create a pixel rectangle from two pixel ranges
public PixelRect(PixelRangeX xRange, PixelRangeY yRange)
public PixelRect(IEnumerable<Pixel> pixels)
public PixelRect WithPan(float x, float y)
public override string ToString()
public SkiaSharp.SKRect ToSKRect()
public PixelRect Contract(float delta)
public PixelRect Contract(float x, float y)
public PixelRect Contract(PixelPadding padding)
public PixelRect Expand(PixelRect other)
// Returns the intersection with another rectangle
public PixelRect Intersect(PixelRect other)
public PixelRect Expand(PixelPadding pad)
public PixelRect Expand(float delta)
public PixelRect ExpandX(float x)
public PixelRect ExpandY(float y)
public PixelRect WithDelta(float x, float y)
public PixelRect WithDelta(float x, float y, Alignment alignment)
public bool Equals(PixelRect other)
public override bool Equals(object? obj)
public static bool operator ==(PixelRect a, PixelRect b)
public static bool operator !=(PixelRect a, PixelRect b)
public override int GetHashCode()
public bool Contains(Pixel px)
public bool Contains(float x, float y)
public bool ContainsX(float x)
public bool ContainsY(float y)
public Pixel GetAlignedPixel(Alignment alignment)
public PixelRect WithOffset(PixelOffset offset)
// Return the position of this rectangle aligned inside a larger one
public PixelRect AlignedInside(PixelRect largerRect, Alignment alignment)
// Return the position of this rectangle aligned inside a larger one
public PixelRect AlignedInside(PixelRect largerRect, Alignment alignment, PixelPadding padding)
public PixelRect Fraction(FractionRect frac)
```

### `public static class PixelRectExtensions`
<!-- Primitives\PixelRect.cs -->

```csharp
public static class PixelRectExtensions
public static PixelRect ToPixelRect(this SKRect rect) [扩展方法]
public static PixelRect ToPixelRect(this SKRectI rect) [扩展方法]
```

### `public struct PixelSize : IEquatable<PixelSize>`
<!-- Primitives\PixelSize.cs -->

```csharp
public struct PixelSize : IEquatable<PixelSize>
public readonly float Width
public readonly float Height
public float Area
public float Diagonal
public PixelSize(float width, float height)
public PixelSize(double width, double height)
public override string ToString()
public static PixelSize Zero
public static PixelSize NaN
public static PixelSize Infinity
public PixelRect ToPixelRect()
public PixelRect ToPixelRect(Pixel pixel, Alignment alignment)
public bool Contains(PixelSize size)
public PixelSize Max(PixelSize rect2)
public bool Equals(PixelSize other)
public override bool Equals(object? obj)
public static bool operator ==(PixelSize a, PixelSize b)
public static bool operator !=(PixelSize a, PixelSize b)
public override int GetHashCode()
public PixelSize Expanded(PixelPadding pad)
public PixelSize Contracted(PixelPadding pad)
```

### `public static class Platform`
<!-- Primitives\Platform.cs -->

```csharp
public static class Platform
// Launch a web browser to a URL using a command appropriate for the operating system
public static void LaunchWebBrowser(string url)
public static void LaunchFile(string filePath)
```

### `public class Plot : IDisposable`
<!-- Plot.cs -->

```csharp
public class Plot : IDisposable
public List<IPlottable> PlottableList { get; }
public PlottableAdder Add { get; }
public RenderManager RenderManager { get; }
public RenderDetails LastRender
public LayoutManager Layout { get, set; }
// Style for the background of the entire figure
public BackgroundStyle FigureBackground = new() { Color = Colors.White }
// Style for the data area (the area within the axis frames)
public BackgroundStyle DataBackground = new() { Color = Colors.Transparent }
public LineStyle FigureBorder { get, set; }
public LineStyle DataBorder { get, set; }
public IZoomRectangle ZoomRectangle { get, set; }
public double ScaleFactor { get, set; }
public AxisManager Axes { get; }
public PlotStyler Style { get; }
public FontStyler Font { get; }
public Legend Legend { get, set; }
public DefaultGrid Grid
public IPlottable Benchmark { get, set; }
// This object is locked by the Render() methods. Logic that manipulates the plot (UI inputs or editing data) can lock this object to prevent rendering artifacts.
public object Sync { get; }
// In GUI environments this property holds a reference to the interactive plot control
public IPlotControl? PlotControl { get, set; }
public Plot()
public void Dispose()
// Return the location on the screen (pixel) for a location on the plot (coordinates) on the default axes. The figure size and layout referenced will be the one from the last render.
public Pixel GetPixel(Coordinates coordinates)
// Return the location on the screen (pixel) for a location on the plot (coordinates) on the given axes. The figure size and layout referenced will be the one from the last render.
public Pixel GetPixel(Coordinates coordinates, IXAxis xAxis, IYAxis yAxis)
// Return the coordinate for a specific pixel using measurements from the most recent render.
public Coordinates GetCoordinates(Pixel pixel, IXAxis? xAxis = null, IYAxis? yAxis = null)
// Return the coordinate for a specific pixel using measurements from the most recent render.
public Coordinates GetCoordinates(float x, float y, IXAxis? xAxis = null, IYAxis? yAxis = null)
// Return a coordinate rectangle centered at a pixel. Uses measurements from the most recent render. Center point pixel's x Center point pixel's y Radius in pixels The coordinate rectangle
public CoordinateRect GetCoordinateRect(float x, float y, float radius = 10, IXAxis? xAxis = null, IYAxis? yAxis = null)
// Return a coordinate rectangle centered at a pixel. Uses measurements from the most recent render. Center point pixel Radius in pixels The coordinate rectangle
public CoordinateRect GetCoordinateRect(Pixel pixel, float radius = 10, IXAxis? xAxis = null, IYAxis? yAxis = null)
// Return a coordinate rectangle centered at a coordinate pair with the radius specified in pixels. Uses measurements from the most recent render. Center point in coordinate units Radius in pixels The coordinate rectangle
public CoordinateRect GetCoordinateRect(Coordinates coordinates, float radius = 10, IXAxis? xAxis = null, IYAxis? yAxis = null)
// Get the axis under a given pixel
public IAxis? GetAxis(Pixel pixel)
// Get the panel under a given pixel
public IPanel? GetPanel(Pixel pixel, bool axesOnly)
public InteractiveHandle? GetInteractiveHandle(float xPixel, float yPixel, float radius = 10, IXAxis? xAxis = null, IYAxis? yAxis = null)
public EventHandler<InteractiveHandle?>? HandleHoverChanged { get, set; }
public EventHandler<InteractiveHandle>? HandlePressed { get, set; }
public EventHandler<InteractiveHandle>? HandleMoved { get, set; }
public EventHandler<InteractiveHandle>? HandleReleased { get, set; }
public void Render(int width = 400, int height = 300)
// Create a new image of the given dimensions, render the plot onto it, and return it.
public void RenderInMemory(int width = 400, int height = 300)
// Render onto an existing canvas with the given dimensions
public void Render(SKCanvas canvas, int width, int height)
// Render onto an existing canvas inside the given rectangle
public void Render(SKCanvas canvas, PixelRect rect)
// Render onto an existing canvas of a surface over the local clip bounds
public void Render(SKSurface surface)
public Image GetImage(int width, int height)
public string GetImageHtml(int width, int height)
// Render the plot and return an HTML img element containing a Base64-encoded PNG
public string GetPngHtml(int width, int height, string classContent = "", string styleContent = "")
// Render the plot and return a plain text SVG element suitable for insertion into HTML
public string GetSvgHtml(int width, int height)
public SavedImageInfo SaveJpeg(string filePath, int width, int height, int quality = 85)
public SavedImageInfo SavePng(string filePath, int width, int height)
public SavedImageInfo SaveBmp(string filePath, int width, int height)
public SavedImageInfo SaveWebp(string filePath, int width, int height, int quality = 85)
public SavedImageInfo SaveSvg(string filePath, int width, int height)
public string GetSvgXml(int width, int height)
public SavedImageInfo Save(string filePath, int width, int height)
public SavedImageInfo Save(string filePath, int width, int height, ImageFormat format, int quality = 85)
public byte[] GetImageBytes(int width, int height, ImageFormat format = ImageFormat.Bmp)
// Returns the content of the legend as a raster image
public Image GetLegendImage()
// Returns the content of the legend as SVG (vector) image
public string GetLegendSvgXml()
// Return contents of .
public IEnumerable<IPlottable> GetPlottables()
// Return all plottables in of the given type.
public IEnumerable<T> GetPlottables<T>() where T : IPlottable
// Remove the given plottable from the .
public void Remove(IPlottable plottable)
// Remove the given Panel from the .
public void Remove(IPanel panel)
// Remove the given Axis from the .
public void Remove(IAxis axis)
// Remove all items of a specific type from the .
public void Remove(Type plotType)
// Remove a all instances of a specific type from the .
public void Remove<T>() where T : IPlottable
// Remove all instances of a specific type from the that meet the criteraia.
public void Remove<T>(Func<T, bool> predicate) where T : IPlottable
// Move the indicated plottable to the end of the list so it is rendered last and appears above all other plottables.
public void MoveToTop(IPlottable plottable)
// Move the indicated plottable to the start of the list so it is rendered first and appears below all other plottables.
public void MoveToBottom(IPlottable plottable)
// Move the indicated plottable to the end of the list so it is rendered last
public void MoveToFront(IPlottable plottable)
// Move the indicated plottable to the start of the list so it is rendered first
public void MoveToBack(IPlottable plottable)
// Disable visibility for all axes and grids
public void HideAxesAndGrid()
// Enable visibility for all axes and grids
public void ShowAxesAndGrid()
// Disable visibility for all grids
public void HideGrid()
// Enable visibility for all grids
public void ShowGrid()
// Helper method for setting visibility of the
public Legend ShowLegend()
// Helper method for setting visibility of the and setting to the provided one.
public Legend ShowLegend(Alignment alignment)
// Helper method for setting the Legend's IsVisible, Alignment, and Orientation properties all at once.
public Legend ShowLegend(Alignment alignment, Orientation orientation)
// Helper method for displaying specific items in the legend
public Legend ShowLegend(IEnumerable<LegendItem> items, Alignment location = Alignment.LowerRight)
// Hide the default legend (inside the data area) and create a new legend panel placed on the edge of the figure outside the data area.
public Panels.LegendPanel ShowLegend(Edge edge)
// Helper method for setting visibility of the
public Legend HideLegend()
// Clears the list
public void Clear()
// Clear a all instances of a specific type from the .
public void Clear<T>() where T : IPlottable
// Shortcut to set text of the Axes.Title Label and enable its visibility. Reference properties of Axes.Title to customize size, color, font, etc.
public void Title(string? text = null, float? size = null)
// Shortcut to show or hide the title by setting Axes.Title.IsVisible. Reference properties of Axes.Title to customize size, color, font, etc.
public void Title(bool show)
// Shortcut to set text of the Label Assign properties of Label to customize size, color, font, etc.
public void XLabel(string label, float? size = null)
// Shortcut to set text of the Label Assign properties of Label to customize size, color, font, etc.
public void YLabel(string label, float? size = null)
public static DefaultGrid GetDefaultGrid()
// Return the current style settings for this plot
public PlotStyle GetStyle()
// Apply the given style settings to this plot
public void SetStyle(PlotStyle style)
// Apply the style settings from the given plot to this plot
public void SetStyle(Plot otherPlot)
public void Developer_ShowAxisDetails(bool enable = true)
```

### `public class PlotStyle`
<!-- Primitives\PlotStyle.cs -->
> This object holds many common plot style customizations and facilitates switching between styles or copying styles from one plot to another.

```csharp
public class PlotStyle
public IPalette? Palette { get, set; }
public Color? FigureBackgroundColor { get, set; }
public Color? DataBackgroundColor { get, set; }
public Color? AxisColor { get, set; }
public Color? GridMajorLineColor { get, set; }
public Color? LegendBackgroundColor { get, set; }
public Color? LegendFontColor { get, set; }
public Color? LegendOutlineColor { get, set; }
// Apply these style settings to the given plot
public void Apply(Plot plot)
// Return the styles represented by the given plot
public static PlotStyle FromPlot(Plot plot)
// Return a plot style with all values nulled except those that are different than the given style
public PlotStyle WhereDifferentFrom(PlotStyle other)
```

### `public class PlottableAdder(Plot plot)`
<!-- PlottableAdder.cs -->
> Helper methods to create plottable objects and add them to the plot

```csharp
public class PlottableAdder(Plot plot)
public Plot Plot { get; }
// Color set used for adding new plottables
public IPalette Palette { get, set; }
// Return the next color of the . Colors reset if is cleared.
public Color GetNextColor(bool incrementCounter = true)
public Annotation Annotation(string text, Alignment alignment = Alignment.UpperLeft)
public Ellipse AnnularEllipticalSector( Coordinates center, double outerRadiusX, double outerRadiusY, double innerRadiusX, double innerRadiusY, Angle startAngle, Angle sweepAngle, Angle? rotation = null)
public Ellipse AnnularEllipticalSector( int xCenter, int yCenter, double outerRadiusX, double outerRadiusY, double innerRadiusX, double innerRadiusY, Angle startAngle, Angle sweepAngle, Angle? rotation = null)
public Ellipse AnnularSector( Coordinates center, double outerRadius, double innerRadius, Angle startAngle, Angle sweepAngle, Angle? rotation = null)
public Ellipse AnnularSector( int xCenter, int yCenter, double outerRadius, double innerRadius, Angle startAngle, Angle sweepAngle, Angle? rotation = null)
public Ellipse Arc(Coordinates center, double radius, Angle startAngle, Angle sweepAngle)
public Ellipse Arc(double xCenter, double yCenter, double radius, Angle startAngle, Angle sweepAngle)
public Arrow Arrow(Coordinates arrowBase, Coordinates arrowTip)
public Arrow Arrow(double xBase, double yBase, double xTip, double yTip)
public Arrow Arrow(CoordinateLine line)
public Annotation BackgroundText(string text, Color? color = null, double size = 48)
public (Annotation line1, Annotation line2) BackgroundText(string line1, string line2, Color? color = null, double size1 = 48, double size2 = 24)
public BarPlot Bar(Bar bar)
public BarPlot Bar(double position, double value, double error = 0)
public BarPlot Bars(List<Bar> bars)
public BarPlot Bars(Bar[] bars)
public BarPlot Bars(double[] values)
public BarPlot Bars<T>(IEnumerable<double> positions, IEnumerable<T> values)
public BarPlot Bars(IEnumerable<double> positions, IEnumerable<double> values)
public BoxPlot Box(Box box)
public BoxPlot Boxes(IEnumerable<Box> boxes)
public Bracket Bracket(Coordinates point1, Coordinates point2, string? label = null)
public Bracket Bracket(double x1, double y1, double x2, double y2, string? label = null)
public Bracket Bracket(CoordinateLine line, string? label = null)
public Callout Callout(string text, double textX, double textY, double tipX, double tipY)
public Callout Callout(string text, Coordinates textLocation, Coordinates tipLocation)
public CandlestickPlot Candlestick(OHLC[] ohlcs)
public CandlestickPlot Candlestick(List<OHLC> ohlcs)
public Ellipse Circle(Coordinates center, double radius)
public Ellipse Circle(double xCenter, double yCenter, double radius)
public Ellipse CircleSector(Coordinates center, double radius, Angle startAngle, Angle sweepAngle)
public Ellipse CircleSector(int xCenter, int yCenter, int radius, Angle startAngle, Angle sweepAngle)
public ColorBar ColorBar(IHasColorAxis source, Edge edge = Edge.Right)
public ContourLines ContourLines(Coordinates3d[,] coordinates, int count = 10)
public ContourLines ContourLines(Coordinates3d[] coordinates, int count = 10)
public Coxcomb Coxcomb(IList<PieSlice> slices)
public Coxcomb Coxcomb(IEnumerable<double> values)
public Crosshair Crosshair(double x, double y)
public DataLogger DataLogger()
public DataLogger DataLogger(List<Coordinates> coordinates)
public DataStreamer DataStreamer(int points, double period = 1)
public DataStreamerXY DataStreamerXY(int capacity)
public Ellipse Ellipse(Coordinates center, double radiusX, double radiusY, Angle? rotation = null)
public Ellipse Ellipse(double xCenter, double yCenter, double radiusX, double radiusY, Angle? rotation = null)
public Ellipse EllipticalArc(Coordinates center, double radiusX, double radiusY, Angle startAngle, Angle sweepAngle, Angle? rotation = null)
public Ellipse EllipticalArc(double xCenter, double yCenter, double radiusX, double radiusY, Angle startAngle, Angle sweepAngle, Angle? rotation = null)
public Ellipse EllipticalSector(Coordinates center, double radiusX, double radiusY, Angle startAngle, Angle sweepAngle, Angle? rotation = null)
public Ellipse EllipticalSector(double xCenter, double yCenter, double radiusX, double radiusY, Angle startAngle, Angle sweepAngle, Angle? rotation = null)
public ErrorBar ErrorBar(IReadOnlyList<double> xs, IReadOnlyList<double> ys, IReadOnlyList<double> yErrors)
// Fill the vertical range between two Y points for each X point
public FillY FillY(double[] xs, double[] ys1, double[] ys2)
// Fill the vertical range between two Y points for each X point
public FillY FillY(Scatter scatter1, Scatter scatter2)
// Fill the vertical range between two Y points for each X point
public FillY FillY(ICollection<(double X, double Top, double Bottom)> data)
// Fill the vertical range between two Y points for each X point This overload uses a custom function to calculate X, Y1, and Y2 values
public FillY FillY<T>(ICollection<T> data, Func<T, (double X, double Top, double Bottom)> function)
public FunctionPlot Function(IFunctionSource functionSource)
public FunctionPlot Function(Func<double, double> func)
public Heatmap Heatmap(double[,] intensities)
public Heatmap Heatmap(Coordinates3d[,] values)
public HistogramBars Histogram(Histogram histogram, Color? color = null, bool disableBottomPadding = true)
public HorizontalLine HorizontalLine(double y, float width = 2, Color? color = null, LinePattern pattern = default)
public HorizontalSpan HorizontalSpan(double x1, double x2, Color? color = null)
public ImageMarker ImageMarker(Coordinates location, Image image, float scale = 1)
public ImageRect ImageRect(Image image, CoordinateRect rect)
public InteractiveHorizontalLine InteractiveHorizontalLine(double y)
public InteractiveHorizontalLineSegment InteractiveHorizontalLineSegment(double x1, double x2, double y)
public InteractiveHorizontalSpan InteractiveHorizontalSpan(double x1, double x2)
public InteractiveLineSegment InteractiveLineSegment(CoordinateLine line)
public InteractiveMarker InteractiveMarker(Coordinates point)
public InteractiveRectangle InteractiveRectangle(CoordinateRect rect)
public InteractiveTrendLine InteractiveTrendLine(CoordinateLine line)
public InteractiveVerticalLine InteractiveVerticalLine(double x)
public InteractiveVerticalLineSegment InteractiveVerticalLineSegment(double x, double y1, double y2)
public InteractiveVerticalSpan InteractiveVerticalSpan(double y1, double y2)
public Legend Legend()
public LinePlot Line(Coordinates start, Coordinates end)
public LinePlot Line(CoordinateLine line)
public LinePlot Line(double x1, double y1, double x2, double y2)
public LollipopPlot Lollipop(double[] values)
public LollipopPlot Lollipop(double[] values, double[] positions)
public LollipopPlot Lollipop(IEnumerable<Coordinates> coordinates)
public Marker Marker(double x, double y, MarkerShape shape = MarkerShape.FilledCircle, float size = 10, Color? color = null)
public Marker Marker(Coordinates location, MarkerShape shape = MarkerShape.FilledCircle, float size = 10, Color? color = null)
public Plottables.Markers Markers(double[] xs, double[] ys, MarkerShape shape = MarkerShape.FilledCircle, float size = 10, Color? color = null)
public Plottables.Markers Markers(Coordinates[] coordinates, MarkerShape shape = MarkerShape.FilledCircle, float size = 10, Color? color = null)
public Plottables.Markers Markers(List<Coordinates> coordinates, MarkerShape shape = MarkerShape.FilledCircle, float size = 10, Color? color = null)
public Plottables.Markers Markers<TX, TY>(TX[] xs, TY[] ys, MarkerShape shape = MarkerShape.FilledCircle, float size = 10, Color? color = null)
public Plottables.Markers Markers<TX, TY>(List<TX> xs, List<TY> ys, MarkerShape shape = MarkerShape.FilledCircle, float size = 10, Color? color = null)
public OhlcPlot OHLC(List<OHLC> ohlcs)
public Phasor Phasor()
public Phasor Phasor(IEnumerable<PolarCoordinates> points)
public Pie Pie(IList<PieSlice> slices)
public Pie Pie(IEnumerable<double> values)
public IPlottable Plottable(IPlottable plottable)
public PolarAxis PolarAxis(double radius = 1.0, double spokeLength = 1.1, int circleCount = 5, int spokeCount = 12)
public Polygon Polygon(Coordinates[] coordinates)
public Polygon Polygon<TX, TY>(IEnumerable<TX> xs, IEnumerable<TY> ys)
public PopulationSymbol Population(double[] values, double x = 0)
public Radar Radar()
public Radar Radar(double[] values)
public Radar Radar(double[,] values)
public Radar Radar(IEnumerable<IEnumerable<double>> series)
public RadialGaugePlot RadialGaugePlot(IEnumerable<double> values)
// Create a bar plot to represent a collection of named ranges
public BarPlot Ranges(List<(string name, CoordinateRange range)> ranges, Color? color = null, bool horizontal = false)
public Rectangle Rectangle(CoordinateRect rect)
public Rectangle Rectangle(double left, double right, double bottom, double top)
public ScaleBar ScaleBar(double width, double height)
public Scatter Scatter(IScatterSource source, Color? color = null)
public Scatter Scatter(double x, double y, Color? color = null)
public Scatter Scatter(double[] xs, double[] ys, Color? color = null)
public Scatter Scatter(Coordinates point, Color? color = null)
public Scatter Scatter(Coordinates[] coordinates, Color? color = null)
public Scatter Scatter(List<Coordinates> coordinates, Color? color = null)
public Scatter Scatter<T1, T2>(T1[] xs, T2[] ys, Color? color = null)
public Scatter Scatter<T1, T2>(List<T1> xs, List<T2> ys, Color? color = null)
public Scatter ScatterLine(IScatterSource source, Color? color = null)
public Scatter ScatterLine(double[] xs, double[] ys, Color? color = null)
public Scatter ScatterLine(Coordinates[] coordinates, Color? color = null)
public Scatter ScatterLine(List<Coordinates> coordinates, Color? color = null)
public Scatter ScatterLine<T1, T2>(T1[] xs, T2[] ys, Color? color = null)
public Scatter ScatterLine<T1, T2>(List<T1> xs, List<T2> ys, Color? color = null)
public Scatter ScatterPoints(IScatterSource source, Color? color = null)
public Scatter ScatterPoints(double[] xs, double[] ys, Color? color = null)
public Scatter ScatterPoints(Coordinates[] coordinates, Color? color = null)
public Scatter ScatterPoints(List<Coordinates> coordinates, Color? color = null)
public Scatter ScatterPoints<T1, T2>(T1[] xs, T2[] ys, Color? color = null)
public Scatter ScatterPoints<T1, T2>(List<T1> xs, List<T2> ys, Color? color = null)
public Signal Signal(ISignalSource source, Color? color = null)
public Signal Signal(double[] ys, double period = 1, Color? color = null)
public Signal Signal<T>(T[] ys, double period = 1, Color? color = null)
public Signal Signal<T>(IReadOnlyList<T> ys, double period = 1, Color? color = null)
public Signal SignalConst<T>(T[] ys, double period = 1, Color? color = null) where T : struct, IComparable
public SignalXY SignalXY(ISignalXYSource source, Color? color = null)
public SignalXY SignalXY(double[] xs, double[] ys, Color? color = null)
public SignalXY SignalXY<TX, TY>(TX[] xs, TY[] ys, Color? color = null)
public SignalXY SignalXY<TX, TY>(IReadOnlyList<TX> xs, IReadOnlyList<TY> ys, Color? color = null)
public SmithChartAxis SmithChartAxis()
// Place a stacked bar chart at a single position
public BarPlot[] StackedRanges(List<(string name, double[] edgeValues)> ranges, IPalette? palette = null, bool horizontal = false)
public Text Text(string text, Coordinates location)
public Text Text(string text, double x, double y)
public Tooltip Tooltip(Coordinates tipLocation, string text, Coordinates labelLocation)
public Tooltip Tooltip(double tipX, double tipY, string text, double labelX, double labelY)
public TriangularAxis TriangularAxis(bool clockwise = true, bool hideAxisAndGrid = true, bool useSquareAxisUnits = true)
public VectorField VectorField(IList<RootedCoordinateVector> vectors, Color? color = null)
public VerticalLine VerticalLine(double x, float width = 2, Color? color = null, LinePattern pattern = default)
public VerticalSpan VerticalSpan(double y1, double y2, Color? color = null)
```

### `public class PolarAxisCircle(double radius) : IHasLine`
<!-- Primitives\PolarAxisCircle.cs -->
> A polar axis tick describes the radius of a circle centered at the origin and includes the styling information required to render it

```csharp
public class PolarAxisCircle(double radius) : IHasLine
public double Radius { get, set; }
public Coordinates Origin { get, set; }
public Angle StartAngle { get, set; }
public Angle SweepAngle { get, set; }
public LabelStyle LabelStyle { get, set; }
public string LabelText { get, set; }
public Angle LabelAngle { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
```

### `public class PolarAxisSpoke(Angle angle, double length) : IHasLine`
<!-- Primitives\PolarAxisSpoke.cs -->
> A straight line extending outward from the origin

```csharp
public class PolarAxisSpoke(Angle angle, double length) : IHasLine
public Angle Angle { get, set; }
public double Length { get, set; }
public LabelStyle LabelStyle { get; }
public string? LabelText { get, set; }
public double LabelPaddingFraction { get, set; }
public double LabelLength
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
```

### `public struct PolarCoordinates(double radius, Angle angle)`
<!-- Primitives\PolarCoordinates.cs -->
> Represents a point in polar coordinate space

```csharp
public struct PolarCoordinates(double radius, Angle angle)
public double Radius { get, set; }
public Angle Angle { get, set; }
public PolarCoordinates WithRadius(double radius)
public PolarCoordinates WithAngle(Angle angle)
public PolarCoordinates WithAngleDegrees(double degrees)
public PolarCoordinates WithAngleRadians(double radians)
public override readonly string ToString()
public Coordinates CartesianCoordinates
public Coordinates ToCartesian()
public Coordinates ToCartesian(Coordinates origin)
public static PolarCoordinates FromCartesian(Coordinates pt)
public static PolarCoordinates FromCartesian(Coordinates pt, Coordinates origin)
```

### `public class Population`
<!-- Primitives\Population.cs -->

```csharp
public class Population
public IReadOnlyList<double> Values { get; }
public IReadOnlyList<double> SortedValues { get; }
public int Count { get; }
public double Min { get; }
public double Max { get; }
public double Mean { get; }
public double Variance { get; }
public double StandardDeviation { get; }
public double StandardError { get; }
public double Median { get; }
public Population(double[] values)
public double GetPercentile(double percentile)
```

### `public class RadarSeries : LabelStyleProperties, IHasLabel, IHasLegendText, IHasFill, IHasLine`
<!-- Primitives\RadarSeries.cs -->
> Defines values and styling information for displaying a single shape on a radar chart

```csharp
public class RadarSeries : LabelStyleProperties, IHasLabel, IHasLegendText, IHasFill, IHasLine
public IReadOnlyList<double> Values { get, set; }
public override LabelStyle LabelStyle { get, set; }
public string LegendText { get, set; }
public FillStyle FillStyle { get, set; }
public Color FillColor { get, set; }
public Color FillHatchColor { get, set; }
public IHatch? FillHatch { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
```

### `public enum RadialGaugeMode { /// <summary> /// Successive gauges start outward from the center but start at the same angle /// </summary> Stacked, /// <summary> /// Successive gauges start outward from the center and start at sequential angles /// </summary> Sequential, /// <summary> /// Gauges are all the same distance from the center but start at sequential angles /// </summary> SingleGauge }`
<!-- Primitives\RadialGaugeMode.cs -->

```csharp
public enum RadialGaugeMode { /// <summary> /// Successive gauges start outward from the center but start at the same angle /// </summary> Stacked, /// <summary> /// Successive gauges start outward from the center and start at sequential angles /// </summary> Sequential, /// <summary> /// Gauges are all the same distance from the center but start at sequential angles /// </summary> SingleGauge }
成员: Stacked, Sequential, SingleGauge
```

### `public class RandomDataGenerator`
<!-- RandomDataGenerator.cs -->

```csharp
public class RandomDataGenerator
// Create a random number generator. The seed is random by default, but could be fixed to the defined value
public RandomDataGenerator(int? seed = null)
public void Seed(int seed)
public static RandomDataGenerator Generate { get, set; }
// Return a uniformly random number between 0 (inclusive) and 1 (exclusive)
public double RandomNumber()
// Return a uniformly random number between 0 (inclusive) and (exclusive)
public double RandomNumber(double max)
// Return a uniformly random number between (inclusive) and (exclusive)
public double RandomNumber(double min, double max)
// Return a random number guaranteed not to be zero
public double RandomNonZeroNumber(double max = 1)
// Return a random integer up to the maximum integer size
public int RandomInteger()
// Return a random byte (0-255)
public byte RandomByte()
// Return a random byte between the given values (inclusive)
public byte RandomByte(byte min, byte max)
// Return a random integer between zero (inclusive) and (exclusive)
public int RandomInteger(int max)
// Return a random integer between (inclusive) and (exclusive)
public int RandomInteger(int min, int max)
// Return a number normally distributed around the given according to the standard deviation.
public double RandomNormalNumber(double mean = 0, double stdDev = 1)
// Mutate the given array by adding noise (± magnitude) and return it
public void AddNoiseInPlace(double[] values, double magnitude)
// Return a copy of the given data with random noise added (± magnitude)
public double[] AddNoise(double[] input, double magnitude)
// Uniformly distributed random numbers between 0 and 1 (multiplied by then added to ).
public double[] RandomSample(int count, double mult = 1, double offset = 0)
// Return a collection of numbers normally distributed around the given according to the standard deviation.
public double[] RandomNormalSample(int count, double mean = 0, double stdDev = 1)
// Sine wave with random frequency, amplitude, and phase
public double[] RandomSin(int count)
// A sequence of numbers that starts at and "walks" randomly from one point to the next, scaled by with an approximate slope of .
public double[] RandomWalk(int count, double mult = 1, double offset = 0, double slope = 0)
// Return a collection OHLCs representing random price action
public List<OHLC> RandomOHLCs(int count)
// Return a collection OHLCs representing random price action
public List<OHLC> RandomOHLCs(int count, DateTime start)
```

### `public readonly struct Range // TODO: evaluate if this can be replaced with more task-specific primitives`
<!-- Primitives\Range.cs -->
> Represents a range between any two finite values (inclusive)

```csharp
public readonly struct Range // TODO: evaluate if this can be replaced with more task-specific primitives
public double Min { get; }
public double Max { get; }
public Range(double min, double max)
public override string ToString()
// Returns the given value as a fraction of the difference between Min and Max. This is a min-max feature scaling.
public double Normalize(double value, bool clamp = false)
// Returns the given value clamped to the range (inclusive).
public double Clamp(double value)
public static Range GetRange(double[,] input)
public static Range GetRange(IEnumerable<double> input)
```

### `public readonly struct RenderDetails`
<!-- Primitives\RenderDetails.cs -->
> Details about a completed render

```csharp
public readonly struct RenderDetails
// Size of the plot image in pixel units
public readonly PixelRect FigureRect
// Size of the data area of the plot in pixel units
public readonly PixelRect DataRect
// Distance between the data area and the edge of the figure
public readonly PixelPadding Padding
// Total time required to render this image
public readonly TimeSpan Elapsed
// Time the render was completed
public readonly DateTime Timestamp
// Each step of the render and how long it took to execute
public readonly (string, TimeSpan)[] TimedActions
// Axis limits of the primary axes for this render
public readonly AxisLimits AxisLimits
// Axis limits of the primary axes for the previous render
public readonly AxisLimits PreviousAxisLimits
// Axis limits for every axis
public readonly Dictionary<IAxis, CoordinateRange> AxisLimitsByAxis
// Axis limits of all axes from the previous render
public readonly Dictionary<IAxis, CoordinateRange> PreviousAxisLimitsByAxis
// Indicates whether the axis view (coordinate units) of this render differs from the previous
public readonly bool AxisLimitsChanged { get; }
// Indicates whether the size (pixels) of this render differs from the previous
public readonly bool SizeChanged { get; }
// Arrangement of all panels
public readonly Layout Layout
// The number of total renders including this one
public readonly int Count
public double PxPerUnitX
public double PxPerUnitY
public double UnitsPerPxX
public double UnitsPerPxY
public RenderDetails(RenderPack rp, (string, TimeSpan)[] actionTimes, RenderDetails lastRender)
// Search the for the specified and calculate the pixels per unit
public bool TryGetPixelPerUnitX(IXAxis? axis, out double value)
// Search the for the specified and calculate the pixels per unit
public bool TryGetPixelPerUnitY(IYAxis? axis, out double value)
// Search the for the specified and calculate the pixels per unit
public bool TryGetUnitPerPixelX(IXAxis? axis, out double value)
// Search the for the specified and calculate the pixels per unit
public bool TryGetUnitPerPixelY(IYAxis? axis, out double value)
```

### `public class RenderPack(Plot plot, PixelRect figureRect, SKCanvas canvas) : IDisposable`
<!-- RenderPack.cs -->
> This object pairs a Plot with pixel/canvas information and is passed throughout the render system to provide screen and canvas information to methods performing rendering.

```csharp
public class RenderPack(Plot plot, PixelRect figureRect, SKCanvas canvas) : IDisposable
public SKCanvas Canvas { get; }
public CanvasState CanvasState { get; }
public Paint Paint { get; }
public PixelRect FigureRect { get; }
public PixelRect ScaledFigureRect { get, set; }
public PixelRect DataRect { get, set; }
public Layout Layout { get, set; }
public Plot Plot { get; }
public TimeSpan Elapsed
public void Dispose()
```

### `public enum ResizeFilter { NearestNeighbor, Bilinear, Bicubic, }`
<!-- Primitives\ResizeFilter.cs -->

```csharp
public enum ResizeFilter { NearestNeighbor, Bilinear, Bicubic, }
成员: NearestNeighbor, Bilinear, Bicubic
```

### `public struct RootedCoordinateVector(Coordinates point, Vector2 vector)`
<!-- Primitives\RootedCoordinateVector.cs -->
> Represents a vector at a point in coordinate space

```csharp
public struct RootedCoordinateVector(Coordinates point, Vector2 vector)
public Coordinates Point { get, set; }
public Vector2 Vector { get, set; }
// Angle of the vector in radians
public readonly float Angle
// Length of the vector squared in coordinate units
public readonly float MagnitudeSquared
// Length of the vector in coordinate units
public readonly float Magnitude
```

### `public struct RootedPixelVector(Pixel point, Vector2 vector)`
<!-- Primitives\RootedPixelVector.cs -->
> Represents a vector at a point in pixel space

```csharp
public struct RootedPixelVector(Pixel point, Vector2 vector)
public Pixel Point { get, set; }
public Vector2 Vector { get, set; }
// Angle of the vector in radians
public readonly float Angle
// Length of the vector squared in pixel units
public readonly float MagnitudeSquared
// Length of the vector in pixel units
public readonly float Magnitude
```

### `public static class SampleData`
<!-- SampleData.cs -->
> Sample data used for testing

```csharp
public static class SampleData
// The first 100 prime numbers
public static readonly double[] FirstHundredPrimes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, }
// The Mona Lisa represented as as a 2D array (65 x 100) of grayscale values from 0 (dark) to 255 (bright)
public static double[,] MonaLisa()
public static double DunningKrugerCurve(double x)
public static double[] MaleHeights(int count = 1234)
public static double[] FemaleHeights(int count = 1234)
public static double[] Faithful { get, set; }
```

### `public class SampleImages`
<!-- SampleImages.cs -->

```csharp
public class SampleImages
public static Image MonaLisa()
public static Image ScottPlotLogo(int width = 256, int height = 256)
public static Image NoiseGrayscale(int width, int height, int seed = 0)
public static Image NoisyText(string text, int width, int height)
```

### `public class SavedImageInfo(string path, int fileSize)`
<!-- Primitives\SavedImageInfo.cs -->

```csharp
public class SavedImageInfo(string path, int fileSize)
public string Path { get; }
public int FileSize { get; }
public override string ToString()
public SavedImageInfo WithRenderDetails(RenderDetails renderDetails)
public void LaunchFile()
public void ConsoleWritePath()
public void LaunchInBrowser(double refresh = 3)
```

### `public class SubplotCollection`
<!-- Primitives\SubplotCollection.cs -->
> Logic that manages a collection of subplots with logic that can perform custom actions when subplots are added or removed.

```csharp
public class SubplotCollection
public Action<List<Plot>> PlotAddedAction = CopyStyleOntoLastPlot
public int Count
public void Add(Plot plot)
public void Remove(Plot plot)
public void RemoveAt(int index)
public Plot GetPlot(int index)
public Plot[] GetPlots()
public static void CopyStyleOntoLastPlot(List<Plot> plots)
```

### `public readonly struct Tick`
<!-- Primitives\Tick.cs -->

```csharp
public readonly struct Tick
public readonly double Position
public readonly string Label
public readonly bool IsMajor
public Tick(double position, string label)
public Tick(double position, string label, bool isMajor)
public static Tick Major(double position, string label)
public static Tick Minor(double position)
```

### `public class TickMarkStyle`
<!-- Primitives\TickMarkStyle.cs -->

```csharp
public class TickMarkStyle
public float Length
public float Width
public bool Hairline
public Color Color
public bool AntiAlias
public LinePattern Pattern = LinePattern.Solid
public void Render(SKCanvas canvas, Paint paint, PixelLine pxLine)
public void ApplyToPaint(Paint paint)
```

### `public class TriangularAxisCornerLabel`
<!-- Primitives\TriangularAxisCornerLabel.cs -->
> Represents a label at a corner of the triangular plot triangle and includes styling information.

```csharp
public class TriangularAxisCornerLabel
public Coordinates Position { get, set; }
public LabelStyle LabelStyle { get; }
public string? LabelText { get, set; }
public TriangularAxisCornerLabel(Coordinates position, string labelText)
```

### `public class TriangularAxisEdge`
<!-- Primitives\TriangularAxisEdge.cs -->

```csharp
public class TriangularAxisEdge
public CoordinateLine Line { get; }
public Coordinates Start
public Coordinates End
public List<(Coordinates Point, string Label)> Ticks { get; }
public LineStyle EdgeLineStyle { get, set; }
public TickMarkStyle TickMarkStyle { get, set; }
public LabelStyle TickLabelStyle { get, set; }
public LabelStyle LabelStyle { get, set; }
public PixelOffset TickOffset { get, set; }
public static readonly double MaxY = Math.Sqrt(3) / 2
public static readonly AxisLimits AxisLimits = new(0, 1, 0, MaxY)
public string LabelText { get, set; }
public void Title(string title)
public void Title(string title, Color color)
public void Color(Color color)
public static TriangularAxisEdge Left(bool clockwise = true)
public static TriangularAxisEdge Right(bool clockwise = true)
public static TriangularAxisEdge Bottom(bool clockwise = true)
public TriangularAxisEdge(CoordinateLine line)
// Return the point along this axis a given fraction between 0 and 1
public Coordinates GetCoordinates(double fraction)
```

### `public static class Version`
<!-- Version.cs -->

```csharp
public static class Version
public static int Major
public static int Minor
public static int Build
// Version formatted like "1.2.3-beta"
public static string VersionString { get, set; }
// Version formatted like "ScottPlot 1.2.3-beta"
public static string LongString { get, set; }
// Throws an exception if this version of ScottPlot does not match the expected major version
public static void ShouldBe(int major)
// Throws an exception if this version of ScottPlot does not match the expected major and minor versions
public static void ShouldBe(int major, int minor)
// Throws an exception if this version of ScottPlot does not match the exact one given
public static void ShouldBe(int major, int minor, int build)
```

### `public enum VerticalAlignment { Bottom, Middle, Top, }`
<!-- Primitives\VerticalAlignment.cs -->

```csharp
public enum VerticalAlignment { Bottom, Middle, Top, }
成员: Bottom, Middle, Top
```

## ScottPlot.AxisPanels

### `public abstract class AxisBase : LabelStyleProperties`
<!-- AxisPanels\AxisBase.cs -->

```csharp
public abstract class AxisBase : LabelStyleProperties
public bool IsVisible { get, set; }
public abstract Edge Edge { get; }
public virtual CoordinateRangeMutable Range { get, set; }
public float MinimumSize { get, set; }
public float MaximumSize { get, set; }
public float SizeWhenNoData { get, set; }
public PixelPadding EmptyLabelPadding { get, set; }
public PixelPadding PaddingBetweenTickAndAxisLabels { get, set; }
public PixelPadding PaddingOutsideAxisLabels { get, set; }
// Controls whether labels should be clipped to the boundaries of the data area
public bool ClipLabel { get, set; }
public double Min { get, set; }
public double Max { get, set; }
public override string ToString()
public virtual ITickGenerator TickGenerator { get, set; }
public LabelStyle Label
public override LabelStyle LabelStyle { get, set; }
public bool ShowDebugInformation { get, set; }
public LineStyle FrameLineStyle { get; }
public TickMarkStyle MajorTickStyle { get, set; }
public TickMarkStyle MinorTickStyle { get, set; }
public LabelStyle TickLabelStyle { get, set; }
// Apply a single color to all axis components: label, tick labels, tick marks, and frame
public void Color(Color color)
// Draw a line along the edge of an axis on the side of the data area
public static void DrawFrame(RenderPack rp, PixelRect panelRect, Edge edge, LineStyle lineStyle)
public static void DrawTicks(RenderPack rp, LabelStyle label, PixelRect panelRect, IEnumerable<Tick> ticks, IAxis axis, TickMarkStyle majorStyle, TickMarkStyle minorStyle)
// Replace the with a pre-loaded with the given ticks.
public void SetTicks(double[] xs, string[] labels)
```

### `public class BottomAxis : XAxisBase, IXAxis`
<!-- AxisPanels\BottomAxis.cs -->

```csharp
public class BottomAxis : XAxisBase, IXAxis
public override Edge Edge
public BottomAxis()
```

### `public class DateTimeXAxis : XAxisBase, IXAxis`
<!-- AxisPanels\DateTimeXAxis.cs -->

```csharp
public class DateTimeXAxis : XAxisBase, IXAxis
public override Edge Edge { get; }
public override ITickGenerator TickGenerator { get, set; }
public IEnumerable<double> ConvertToCoordinateSpace(IEnumerable<DateTime> dates)
```

### `public class LeftAxis : YAxisBase, IYAxis`
<!-- AxisPanels\LeftAxis.cs -->

```csharp
public class LeftAxis : YAxisBase, IYAxis
public override Edge Edge { get; }
public LeftAxis()
```

### `public sealed class MirroredXAxis : XAxisBase, IXAxis`
<!-- AxisPanels\MirroredXAxis.cs -->

```csharp
public sealed class MirroredXAxis : XAxisBase, IXAxis
public override Edge Edge
public override CoordinateRangeMutable Range
public MirroredXAxis(IXAxis axis, Edge? edge)
```

### `public sealed class MirroredYAxis : YAxisBase, IYAxis`
<!-- AxisPanels\MirroredYAxis.cs -->

```csharp
public sealed class MirroredYAxis : YAxisBase, IYAxis
public override Edge Edge
public override CoordinateRangeMutable Range
public MirroredYAxis(IYAxis axis, Edge? edge)
```

### `public class RightAxis : YAxisBase, IYAxis`
<!-- AxisPanels\RightAxis.cs -->

```csharp
public class RightAxis : YAxisBase, IYAxis
public override Edge Edge { get; }
public RightAxis()
```

### `public class TopAxis : XAxisBase, IXAxis`
<!-- AxisPanels\TopAxis.cs -->

```csharp
public class TopAxis : XAxisBase, IXAxis
public override Edge Edge
public TopAxis()
```

### `public abstract class XAxisBase : AxisBase, IXAxis`
<!-- AxisPanels\XAxisBase.cs -->

```csharp
public abstract class XAxisBase : AxisBase, IXAxis
public double Width
public XAxisBase()
public virtual float Measure(Paint paint)
public float GetPixel(double position, PixelRect dataArea)
public double GetCoordinate(float pixel, PixelRect dataArea)
public PixelRect GetPanelRect(PixelRect dataRect, float size, float offset, Paint paint)
public virtual void Render(RenderPack rp, float size, float offset)
public double GetPixelDistance(double distance, PixelRect dataArea)
public double GetCoordinateDistance(float distance, PixelRect dataArea)
public void RegenerateTicks(PixelLength size, Paint paint)
```

### `public abstract class YAxisBase : AxisBase, IYAxis`
<!-- AxisPanels\YAxisBase.cs -->

```csharp
public abstract class YAxisBase : AxisBase, IYAxis
public double Height
public float GetPixel(double position, PixelRect dataArea)
public double GetCoordinate(float pixel, PixelRect dataArea)
public virtual float Measure(Paint paint)
public PixelRect GetPanelRect(PixelRect dataRect, float size, float offset, Paint paint)
public virtual void Render(RenderPack rp, float size, float offset)
public double GetPixelDistance(double distance, PixelRect dataArea)
public double GetCoordinateDistance(float distance, PixelRect dataArea)
public void RegenerateTicks(PixelLength size, Paint paint)
```

## ScottPlot.AxisPanels.Experimental

### `public class LeftAxisWithSubtitle : YAxisBase`
<!-- AxisPanels\Experimental\LeftAxisWithSubtitle.cs -->
> A simple custom Y axis which includes a subtitle/sub-label. Note that and are called whenever the plot needs to be rendered so be wary of heavy code that will slow down the rendering if you are using the chart in a user interface where there is zooming, panning, etc.

```csharp
public class LeftAxisWithSubtitle : YAxisBase
public string SubLabelText { get, set; }
public LabelStyle SubLabelStyle { get, set; }
public override Edge Edge
public LeftAxisWithSubtitle()
public override float Measure(Paint paint)
public override void Render(RenderPack rp, float size, float offset)
```

## ScottPlot.AxisRules

### `public class LockedBottom(IYAxis yAxis, double yMin) : IAxisRule`
<!-- AxisRules\LockedBottom.cs -->

```csharp
public class LockedBottom(IYAxis yAxis, double yMin) : IAxisRule
public readonly IYAxis YAxis = yAxis
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class LockedCenterX(IXAxis xAxis, double xCenter) : IAxisRule`
<!-- AxisRules\LockedCenterX.cs -->

```csharp
public class LockedCenterX(IXAxis xAxis, double xCenter) : IAxisRule
public readonly IXAxis XAxis = xAxis
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class LockedCenterY(IYAxis yAxis, double yCenter) : IAxisRule`
<!-- AxisRules\LockedCenterY.cs -->

```csharp
public class LockedCenterY(IYAxis yAxis, double yCenter) : IAxisRule
public readonly IYAxis YAxis = yAxis
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class LockedHorizontal(IXAxis xAxis, double xMin, double xMax) : IAxisRule`
<!-- AxisRules\LockedHorizontal.cs -->

```csharp
public class LockedHorizontal(IXAxis xAxis, double xMin, double xMax) : IAxisRule
public readonly IXAxis XAxis = xAxis
public double XMin = xMin
public double XMax = xMax
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class LockedLeft(IXAxis xAxis, double xMin) : IAxisRule`
<!-- AxisRules\LockedLeft.cs -->

```csharp
public class LockedLeft(IXAxis xAxis, double xMin) : IAxisRule
public readonly IXAxis XAxis = xAxis
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class LockedRight(IXAxis xAxis, double xMax) : IAxisRule`
<!-- AxisRules\LockedRight.cs -->

```csharp
public class LockedRight(IXAxis xAxis, double xMax) : IAxisRule
public readonly IXAxis XAxis = xAxis
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class LockedTop(IYAxis yAxis, double yMax) : IAxisRule`
<!-- AxisRules\LockedTop.cs -->

```csharp
public class LockedTop(IYAxis yAxis, double yMax) : IAxisRule
public readonly IYAxis YAxis = yAxis
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class LockedVertical(IYAxis yAxis, double yMin, double yMax) : IAxisRule`
<!-- AxisRules\LockedVertical.cs -->

```csharp
public class LockedVertical(IYAxis yAxis, double yMin, double yMax) : IAxisRule
public readonly IYAxis YAxis = yAxis
public double YMin = yMin
public double Max = yMax
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class MaximumBoundary(IXAxis xAxis, IYAxis yAxis, AxisLimits limits) : IAxisRule`
<!-- AxisRules\MaximumBoundary.cs -->

```csharp
public class MaximumBoundary(IXAxis xAxis, IYAxis yAxis, AxisLimits limits) : IAxisRule
public AxisLimits Limits { get, set; }
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class MaximumSpan(IXAxis xAxis, IYAxis yAxis, double xSpan, double ySpan) : IAxisRule`
<!-- AxisRules\MaximumSpan.cs -->

```csharp
public class MaximumSpan(IXAxis xAxis, IYAxis yAxis, double xSpan, double ySpan) : IAxisRule
public double XSpan = xSpan
public double YSpan = ySpan
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class MinimumBoundary(IXAxis xAxis, IYAxis yAxis, AxisLimits limits) : IAxisRule`
<!-- AxisRules\MinimumBoundary.cs -->

```csharp
public class MinimumBoundary(IXAxis xAxis, IYAxis yAxis, AxisLimits limits) : IAxisRule
public AxisLimits Limits { get, set; }
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class MinimumSpan(IXAxis xAxis, IYAxis yAxis, double xSpan, double ySpan) : IAxisRule`
<!-- AxisRules\MinimumSpan.cs -->

```csharp
public class MinimumSpan(IXAxis xAxis, IYAxis yAxis, double xSpan, double ySpan) : IAxisRule
public double XSpan = xSpan
public double YSpan = ySpan
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class SnapToTicksX(IXAxis xAxis) : IAxisRule`
<!-- AxisRules\SnapToTicksX.cs -->

```csharp
public class SnapToTicksX(IXAxis xAxis) : IAxisRule
public readonly IXAxis XAxis = xAxis
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class SnapToTicksY(IYAxis yAxis) : IAxisRule`
<!-- AxisRules\SnapToTicksY.cs -->

```csharp
public class SnapToTicksY(IYAxis yAxis) : IAxisRule
public readonly IYAxis YAxis = yAxis
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class SquarePreserveX(IXAxis xAxis, IYAxis yAxis) : IAxisRule`
<!-- AxisRules\SquarePreserveX.cs -->

```csharp
public class SquarePreserveX(IXAxis xAxis, IYAxis yAxis) : IAxisRule
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class SquarePreserveY(IXAxis xAxis, IYAxis yAxis) : IAxisRule`
<!-- AxisRules\SquarePreserveY.cs -->

```csharp
public class SquarePreserveY(IXAxis xAxis, IYAxis yAxis) : IAxisRule
public void Apply(RenderPack rp, bool beforeLayout)
```

### `public class SquareZoomOut(IXAxis xAxis, IYAxis yAxis) : IAxisRule`
<!-- AxisRules\SquareZoomOut.cs -->

```csharp
public class SquareZoomOut(IXAxis xAxis, IYAxis yAxis) : IAxisRule
public void Apply(RenderPack rp, bool beforeLayout)
```

## ScottPlot.Collections

### `public sealed class CircularBuffer<T> : IList<T>, ICollection<T>, IEnumerable<T>, IEnumerable`
<!-- Collections\CircularBuffer.cs -->
> The circular buffer starts with an empty list and grows to a maximum size. When the buffer is full, adding or inserting a new item removes the first item in the buffer.

```csharp
public sealed class CircularBuffer<T> : IList<T>, ICollection<T>, IEnumerable<T>, IEnumerable
public CircularBuffer(int capacity) : this(new List<T>(), capacity, start: 0, end: 0)
public int Capacity { get; }
public bool IsFull
public bool IsEmpty
public int Count
public bool IsReadOnly { get; }
public bool IsFixedSize { get; }
public object SyncRoot { get; }
public bool IsSynchronized { get; }
public int IndexOf(T item)
public void Insert(int index, T item)
public void RemoveAt(int index)
public bool Remove(T item)
public T this[int index]
public void Add(T item)
public void Clear()
public bool Contains(T item)
public void CopyTo(T[] array, int arrayIndex)
public T[] ToArray()
public IEnumerator<T> GetEnumerator()
public int BinarySearch(int index, int count, T item, IComparer<T> comparer)
```

## ScottPlot.Colormaps

### `public class Algae : IColormap`
<!-- Colormaps\Algae.cs -->

```csharp
public class Algae : IColormap
public string Name
public Color GetColor(double position)
public Algae()
```

### `public class Amp : IColormap`
<!-- Colormaps\Amp.cs -->

```csharp
public class Amp : IColormap
public string Name
public Color GetColor(double position)
public Amp()
```

### `public class Balance : IColormap`
<!-- Colormaps\Balance.cs -->

```csharp
public class Balance : IColormap
public string Name
public Color GetColor(double position)
public Balance()
```

### `public class Blues : IColormap`
<!-- Colormaps\Blues.cs -->

```csharp
public class Blues : IColormap
public string Name
public Color GetColor(double position)
public Blues()
```

### `public class Curl : IColormap`
<!-- Colormaps\Curl.cs -->

```csharp
public class Curl : IColormap
public string Name
public Color GetColor(double position)
public Curl()
```

### `public class Custom(Color[] colors, bool smooth = true) : IColormap`
<!-- Colormaps\Custom.cs -->
> A custom colormap created from a collection of colors

```csharp
public class Custom(Color[] colors, bool smooth = true) : IColormap
public string Name
public Color GetColor(double position)
```

### `public class CustomInterpolated : IColormap`
<!-- Colormaps\CustomInterpolated.cs -->
> A custom palette which smoothly blends across a collection of colors using linear interpolation

```csharp
public class CustomInterpolated : IColormap
public string Name
public CustomInterpolated(Color[] colors)
public Color GetColor(double position)
```

### `public class CustomPalette : IColormap`
<!-- Colormaps\CustomPalette.cs -->
> A palette of colors with "hard edges" (no interpolation between colors)

```csharp
public class CustomPalette : IColormap
public string Name { get; }
public CustomPalette(Color[] colors, string name = "custom")
public Color GetColor(double position)
```

### `public class Deep : IColormap`
<!-- Colormaps\Deep.cs -->

```csharp
public class Deep : IColormap
public string Name
public Color GetColor(double position)
public Deep()
```

### `public class Delta : IColormap`
<!-- Colormaps\Delta.cs -->

```csharp
public class Delta : IColormap
public string Name
public Color GetColor(double position)
public Delta()
```

### `public class Dense : IColormap`
<!-- Colormaps\Dense.cs -->

```csharp
public class Dense : IColormap
public string Name
public Color GetColor(double position)
public Dense()
```

### `public class Diff : IColormap`
<!-- Colormaps\Diff.cs -->

```csharp
public class Diff : IColormap
public string Name
public Color GetColor(double position)
public Diff()
```

### `public class Grayscale : IColormap`
<!-- Colormaps\Grayscale.cs -->

```csharp
public class Grayscale : IColormap
public string Name
public Color GetColor(double normalizedIntensity)
```

### `public class GrayscaleReversed : IColormap`
<!-- Colormaps\GrayscaleReversed.cs -->

```csharp
public class GrayscaleReversed : IColormap
public string Name
public Color GetColor(double normalizedIntensity)
```

### `public class Greens : IColormap`
<!-- Colormaps\Greens.cs -->

```csharp
public class Greens : IColormap
public string Name
public Color GetColor(double position)
public Greens()
```

### `public class Haline : IColormap`
<!-- Colormaps\Haline.cs -->

```csharp
public class Haline : IColormap
public string Name
public Color GetColor(double position)
public Haline()
```

### `public class Ice : IColormap`
<!-- Colormaps\Ice.cs -->

```csharp
public class Ice : IColormap
public string Name
public Color GetColor(double position)
public Ice()
```

### `public class Inferno : IColormap`
<!-- Colormaps\Inferno.cs -->

```csharp
public class Inferno : IColormap
public string Name
public Color GetColor(double position)
public Inferno()
```

### `public class Jet : IColormap`
<!-- Colormaps\Jet.cs -->

```csharp
public class Jet : IColormap
public string Name
public Color GetColor(double position)
public Jet()
```

### `public class Magma : IColormap`
<!-- Colormaps\Magma.cs -->

```csharp
public class Magma : IColormap
public string Name
public Color GetColor(double position)
public Magma()
```

### `public class Matter : IColormap`
<!-- Colormaps\Matter.cs -->

```csharp
public class Matter : IColormap
public string Name
public Color GetColor(double position)
public Matter()
```

### `public class MellowRainbow : IColormap`
<!-- Colormaps\MellowRainbow.cs -->
> A rainbow colormap inspired by Jet and Turbo but adapted by Scott Harden to have less dark edges (red or purple) and a more mellow center (darker yellow/green) for more even brightness perception when displayed using thin lines on a white background.

```csharp
public class MellowRainbow : IColormap
public string Name
public Color GetColor(double position)
public MellowRainbow()
```

### `public class Oxy : IColormap`
<!-- Colormaps\Oxy.cs -->

```csharp
public class Oxy : IColormap
public string Name
public Color GetColor(double position)
public Oxy()
```

### `public class Phase : IColormap`
<!-- Colormaps\Phase.cs -->

```csharp
public class Phase : IColormap
public string Name
public Color GetColor(double position)
public Phase()
```

### `public class Plasma : IColormap`
<!-- Colormaps\Plasma.cs -->

```csharp
public class Plasma : IColormap
public string Name
public Color GetColor(double position)
public Plasma()
```

### `public class Rain : IColormap`
<!-- Colormaps\Rain.cs -->

```csharp
public class Rain : IColormap
public string Name
public Color GetColor(double position)
public Rain()
```

### `public class Reversed(IColormap cmap) : IColormap`
<!-- Colormaps\Reversed.cs -->

```csharp
public class Reversed(IColormap cmap) : IColormap
public string Name
public Color GetColor(double position)
```

### `public class Solar : IColormap`
<!-- Colormaps\Solar.cs -->

```csharp
public class Solar : IColormap
public string Name
public Color GetColor(double position)
public Solar()
```

### `public class Speed : IColormap`
<!-- Colormaps\Speed.cs -->

```csharp
public class Speed : IColormap
public string Name
public Color GetColor(double position)
public Speed()
```

### `public class Tarn : IColormap`
<!-- Colormaps\Tarn.cs -->

```csharp
public class Tarn : IColormap
public string Name
public Color GetColor(double position)
public Tarn()
```

### `public class Tempo : IColormap`
<!-- Colormaps\Tempo.cs -->

```csharp
public class Tempo : IColormap
public string Name
public Color GetColor(double position)
public Tempo()
```

### `public class Thermal : IColormap`
<!-- Colormaps\Thermal.cs -->

```csharp
public class Thermal : IColormap
public string Name
public Color GetColor(double position)
public Thermal()
```

### `public class Topo : IColormap`
<!-- Colormaps\Topo.cs -->

```csharp
public class Topo : IColormap
public string Name
public Color GetColor(double position)
public Topo()
```

### `public class Turbid : IColormap`
<!-- Colormaps\Turbid.cs -->

```csharp
public class Turbid : IColormap
public string Name
public Color GetColor(double position)
public Turbid()
```

### `public class Turbo : IColormap`
<!-- Colormaps\Turbo.cs -->

```csharp
public class Turbo : IColormap
public string Name
public Color GetColor(double position)
public Turbo()
```

### `public class Viridis : IColormap`
<!-- Colormaps\Viridis.cs -->

```csharp
public class Viridis : IColormap
public string Name
public Color GetColor(double position)
public Viridis()
```

## System.Runtime.CompilerServices

### `public class CompilerFeatureRequiredAttribute : Attribute`
<!-- CompilerServices\CompilerServices.cs -->
> Allows required members in older .NET versions

```csharp
public class CompilerFeatureRequiredAttribute : Attribute
public CompilerFeatureRequiredAttribute(string _)
```

### `public class RequiredMemberAttribute : Attribute`
<!-- CompilerServices\CompilerServices.cs -->
> Allows required members in older .NET versions

```csharp
public class RequiredMemberAttribute : Attribute
```

## ScottPlot.DataGenerators

### `public class FinancialDataGenerator(int? seed = null)`
<!-- DataGenerators\FinancialDataGenerator.cs -->

```csharp
public class FinancialDataGenerator(int? seed = null)
public OHLC[] RandomWalk(int count)
public OHLC[] OHLCsByMinute(int count)
```

### `public class RandomWalker(int? seed = null, double firstValue = 0, double multiplier = 1)`
<!-- DataGenerators\RandomWalker.cs -->

```csharp
public class RandomWalker(int? seed = null, double firstValue = 0, double multiplier = 1)
public double Next()
public IEnumerable<double> Next(int count)
```

### `public class RandomWalker2D(int? seed = null)`
<!-- DataGenerators\RandomWalker2D.cs -->

```csharp
public class RandomWalker2D(int? seed = null)
public Coordinates Next()
public IEnumerable<Coordinates> Next(int count)
```

## ScottPlot.DataSources

### `public class CacheScatterLimitsDecorator(IScatterSource source) : IScatterSource, IGetNearest`
<!-- DataSources\ScatterSourceWithCachedLimits.cs -->

```csharp
public class CacheScatterLimitsDecorator(IScatterSource source) : IScatterSource, IGetNearest
public int MinRenderIndex { get, set; }
public int MaxRenderIndex { get, set; }
public AxisLimits GetLimits()
public CoordinateRange GetLimitsX()
public CoordinateRange GetLimitsY()
public DataPoint GetNearest(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public IReadOnlyList<Coordinates> GetScatterPoints()
```

### `public class CoordinateDataSource(IReadOnlyList<Coordinates> readOnlyList) : IDataSource`
<!-- DataSources\CoordinateDataSource.cs -->
> Helper class used when a source (such as ) does not implement

```csharp
public class CoordinateDataSource(IReadOnlyList<Coordinates> readOnlyList) : IDataSource
public double XOffset { get, set; }
public double YOffset { get, set; }
public double XScale { get, set; }
public double YScale { get, set; }
public bool PreferCoordinates
public int Length
public int MinRenderIndex { get, set; }
public int MaxRenderIndex { get, set; }
public Coordinates GetCoordinate(int index)
public Coordinates GetCoordinateScaled(int index)
public double GetX(int index)
public int GetXClosestIndex(Coordinates mouseLocation)
public double GetXScaled(int index)
public double GetY(int index)
public double GetYScaled(int index)
public bool IsSorted()
```

### `public class DataLoggerSource(List<Coordinates> coordinates)`
<!-- DataSources\DataLoggerSource.cs -->

```csharp
public class DataLoggerSource(List<Coordinates> coordinates)
public List<Coordinates> Coordinates { get; }
public double XOffset { get, set; }
public double YOffset { get, set; }
public double YScale { get, set; }
public bool HasNewData { get, set; }
public bool WasRendered { get, set; }
public void Add(Coordinates coordinates)
public void Clear()
public void OnRendered()
public CoordinateRange GetRangeX()
public CoordinateRange GetRangeY(CoordinateRange newRangeX)
public Pixel[] GetPixelsToDrawHorizontally(RenderPack rp, IAxes axes, ConnectStyle connectStyle)
public Pixel[] GetPixelsToDrawVertically(RenderPack rp, IAxes axes, ConnectStyle connectStyle)
// Get the index associated with the given X position
public int GetIndex(double x)
```

### `public class DataStreamerSource`
<!-- DataSources\DataStreamerSource.cs -->

```csharp
public class DataStreamerSource
// Fixed-length array used as a circular buffer to shift data in at the position defined by . Values in this array should not be modified externally if is enabled.
public double[] Data { get; }
// Index in where the next point will be added
public int NextIndex { get, set; }
// Index in holding the newest data point
public int NewestIndex { get, set; }
// Value of the most recently added data point
public double NewestPoint
// The number of visible data points to display
public int Length
// The total number of data points added
public int CountTotal { get, set; }
// Total of data points added the last time this plottable was rendered. This can be compared with to determine if a new render is required.
public int CountTotalOnLastRender { get, set; }
// Minimum value of all known data (not just the data in view)
public double DataMin { get, set; }
// Maximum value of all known data (not just the data in view)
public double DataMax { get, set; }
public double OffsetX { get, set; }
public double OffsetY { get, set; }
public double SamplePeriod { get, set; }
public DataStreamerSource(double[] data)
// Shift in a new Y value
public void Add(double value)
// Shift in a collection of new Y values
public void AddRange(IEnumerable<double> values)
// Clear the buffer by setting all Y points to the given value
public void Clear(double value = 0)
public AxisLimits GetAxisLimits(bool tight = true)
```

### `public class FastSignalSourceDouble : SignalSourceBase, ISignalSource, IDataSource`
<!-- DataSources\FastSignalSourceDouble.cs -->

```csharp
public class FastSignalSourceDouble : SignalSourceBase, ISignalSource, IDataSource
public override int Length
public FastSignalSourceDouble(IReadOnlyList<double> ys, double period, int cachePeriod = 1000)
public IReadOnlyList<double> GetYs()
public IEnumerable<double> GetYs(int i1, int i2)
public double GetY(int index)
public override SignalRangeY GetLimitsY(int firstIndex, int lastIndex)
public PixelColumn GetPixelColumn(IAxes axes, int xPixelIndex)
```

### `public class FunctionSource(Func<double, double> func) : IFunctionSource`
<!-- DataSources\FunctionSource.cs -->

```csharp
public class FunctionSource(Func<double, double> func) : IFunctionSource
public CoordinateRange RangeX { get, set; }
public Func<double, double> Function { get, set; }
public Func<CoordinateRange, CoordinateRange>? GetRangeYFunc { get, set; }
public double Get(double x)
public CoordinateRange GetRangeY(CoordinateRange xs)
```

### `public class OHLCSourceArray(OHLC[] prices) : OHLCSourceBase, IOHLCSource`
<!-- DataSources\OHLCSourceArray.cs -->

```csharp
public class OHLCSourceArray(OHLC[] prices) : OHLCSourceBase, IOHLCSource
public override IReadOnlyList<OHLC> GetOHLCs()
public override int Count
```

### `public abstract class OHLCSourceBase : IOHLCSource`
<!-- DataSources\OHLCSourceBase.cs -->

```csharp
public abstract class OHLCSourceBase : IOHLCSource
public abstract IReadOnlyList<OHLC> GetOHLCs()
public abstract int Count { get; }
public AxisLimits GetLimits()
public CoordinateRange GetLimitsX()
public CoordinateRange GetLimitsY()
public CoordinateRange GetPriceRange(int index1, int index2)
```

### `public class OHLCSourceList(List<OHLC> prices) : OHLCSourceBase, IOHLCSource`
<!-- DataSources\OHLCSourceList.cs -->

```csharp
public class OHLCSourceList(List<OHLC> prices) : OHLCSourceBase, IOHLCSource
public override IReadOnlyList<OHLC> GetOHLCs()
public override int Count
```

### `public class ScatterSourceCoordinatesArray(Coordinates[] coordinates) : IScatterSource, IDataSource, IGetNearest`
<!-- DataSources\ScatterSourceCoordinatesArray.cs -->
> This data source manages X/Y points as a collection of coordinates

```csharp
public class ScatterSourceCoordinatesArray(Coordinates[] coordinates) : IScatterSource, IDataSource, IGetNearest
public int MinRenderIndex { get, set; }
public int MaxRenderIndex { get, set; }
public IReadOnlyList<Coordinates> GetScatterPoints()
public AxisLimits GetLimits()
public CoordinateRange GetLimitsX()
public CoordinateRange GetLimitsY()
public DataPoint GetNearest(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
```

### `public class ScatterSourceCoordinatesList(List<Coordinates> coordinates) : IScatterSource, IDataSource, IGetNearest`
<!-- DataSources\ScatterSourceCoordinatesList.cs -->
> This data source manages X/Y points as a collection of coordinates

```csharp
public class ScatterSourceCoordinatesList(List<Coordinates> coordinates) : IScatterSource, IDataSource, IGetNearest
public int MinRenderIndex { get, set; }
public int MaxRenderIndex { get, set; }
public IReadOnlyList<Coordinates> GetScatterPoints()
public AxisLimits GetLimits()
public CoordinateRange GetLimitsX()
public CoordinateRange GetLimitsY()
public DataPoint GetNearest(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
```

### `public class ScatterSourceDoubleArray(double[] xs, double[] ys) : IScatterSource, IDataSource, IGetNearest`
<!-- DataSources\ScatterSourceDoubleArray.cs -->
> This data source manages X/Y points as separate X and Y collections

```csharp
public class ScatterSourceDoubleArray(double[] xs, double[] ys) : IScatterSource, IDataSource, IGetNearest
public int MinRenderIndex { get, set; }
public int MaxRenderIndex { get, set; }
public IReadOnlyList<Coordinates> GetScatterPoints()
public AxisLimits GetLimits()
public CoordinateRange GetLimitsX()
public CoordinateRange GetLimitsY()
public DataPoint GetNearest(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
```

### `public class ScatterSourceGenericArray<T1, T2>(T1[] xs, T2[] ys) : IScatterSource, IDataSource, IGetNearest`
<!-- DataSources\ScatterSourceGenericArray.cs -->
> This data source manages X/Y points as separate X and Y collections

```csharp
public class ScatterSourceGenericArray<T1, T2>(T1[] xs, T2[] ys) : IScatterSource, IDataSource, IGetNearest
public int MinRenderIndex { get, set; }
public int MaxRenderIndex { get, set; }
public IReadOnlyList<Coordinates> GetScatterPoints()
public AxisLimits GetLimits()
public CoordinateRange GetLimitsX()
public CoordinateRange GetLimitsY()
public DataPoint GetNearest(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
```

### `public class ScatterSourceGenericList<T1, T2>(List<T1> xs, List<T2> ys) : IScatterSource, IDataSource, IGetNearest`
<!-- DataSources\ScatterSourceGenericList.cs -->
> This data source manages X/Y points as separate X and Y collections

```csharp
public class ScatterSourceGenericList<T1, T2>(List<T1> xs, List<T2> ys) : IScatterSource, IDataSource, IGetNearest
public int MinRenderIndex { get, set; }
public int MaxRenderIndex { get, set; }
public IReadOnlyList<Coordinates> GetScatterPoints()
public AxisLimits GetLimits()
public CoordinateRange GetLimitsX()
public CoordinateRange GetLimitsY()
public DataPoint GetNearest(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
```

### `public class SegmentedTree<T> where T : struct, IComparable`
<!-- DataSources\SegmentedTree.cs -->

```csharp
public class SegmentedTree<T> where T : struct, IComparable
public bool TreesReady = false
public T[] SourceArray { get, set; }
public SegmentedTree()
public async Task SetSourceAsync(T[] data)
public void updateElement(int index, T newValue)
public void updateRange(int from, int to, T[] newData, int fromData = 0) // RangeUpdate
public void updateData(int from, T[] newData)
public void updateData(T[] newData)
public void UpdateTreesInBackground()
public void UpdateTrees()
public void MinMaxRangeQuery(int l, int r, out double lowestValue, out double highestValue)
```

### `public class SignalConstSource<T> : SignalSourceGenericArray<T> where T : struct, IComparable`
<!-- DataSources\SignalConstSource.cs -->

```csharp
public class SignalConstSource<T> : SignalSourceGenericArray<T> where T : struct, IComparable
public readonly SegmentedTree<T> SegmentedTree = new()
public SignalConstSource(T[] ys, double period) : base(ys, period)
public override SignalRangeY GetLimitsY(int firstIndex, int lastIndex)
```

### `public static class SignalInterpolation`
<!-- DataSources\SignalInterpolation.cs -->

```csharp
public static class SignalInterpolation
// If the point to the left of the graph is extremely far outside the data area, modify it using interpolation so it's closer to the data area to prevent render artifacts.
public static void InterpolateBeforeX(RenderPack rp, Pixel[] pixels, ConnectStyle connectStyle)
// If the point to the bottom of the graph is extremely far outside the data area, modify it using interpolation so it's closer to the data area to prevent render artifacts.
public static void InterpolateBeforeY(RenderPack rp, Pixel[] pixels, ConnectStyle connectStyle)
// If the point to the right of the graph is extremely far outside the data area, modify it using interpolation so it's closer to the data area to prevent render artifacts.
public static void InterpolateAfterX(RenderPack rp, Pixel[] pixels, ConnectStyle connectStyle)
// If the point to the top of the graph is extremely far outside the data area, modify it using interpolation so it's closer to the data area to prevent render artifacts.
public static void InterpolateAfterY(RenderPack rp, Pixel[] pixels, ConnectStyle connectStyle)
```

### `public readonly struct SignalRangeY`
<!-- DataSources\SignalRangeY.cs -->

```csharp
public readonly struct SignalRangeY
public double Min { get; }
public double Max { get; }
public SignalRangeY(double min, double max)
public override string ToString()
```

### `public abstract class SignalSourceBase`
<!-- DataSources\SignalSourceBase.cs -->

```csharp
public abstract class SignalSourceBase
public double Period { get, set; }
public abstract int Length { get; }
public int MinimumIndex { get, set; }
public int MaximumIndex { get, set; }
public int MinRenderIndex
public int MaxRenderIndex
public bool UsePixelOverlap { get; }
public double XOffset { get, set; }
public double YOffset { get, set; }
public double YScale { get, set; }
public int GetIndex(double x, bool visibleDataOnly)
public bool RangeContainsSignal(double xMin, double xMax)
public double GetX(int index)
public CoordinateRange GetLimitsX()
public CoordinateRange GetLimitsY()
public abstract SignalRangeY GetLimitsY(int firstIndex, int lastIndex)
public AxisLimits GetLimits()
```

### `public class SignalSourceDouble : SignalSourceBase, ISignalSource, IDataSource`
<!-- DataSources\SignalSourceDouble.cs -->

```csharp
public class SignalSourceDouble : SignalSourceBase, ISignalSource, IDataSource
public override int Length
public SignalSourceDouble(IReadOnlyList<double> ys, double period)
public IReadOnlyList<double> GetYs()
public IEnumerable<double> GetYs(int i1, int i2)
public double GetY(int index)
public override SignalRangeY GetLimitsY(int firstIndex, int lastIndex)
public PixelColumn GetPixelColumn(IAxes axes, int xPixelIndex)
```

### `public class SignalSourceGenericArray<T> : SignalSourceBase, ISignalSource, IDataSource`
<!-- DataSources\SignalSourceGenericArray.cs -->

```csharp
public class SignalSourceGenericArray<T> : SignalSourceBase, ISignalSource, IDataSource
public override int Length
public SignalSourceGenericArray(T[] ys, double period)
public IReadOnlyList<double> GetYs()
public IEnumerable<double> GetYs(int i1, int i2)
public double GetY(int index)
public override SignalRangeY GetLimitsY(int firstIndex, int lastIndex)
public PixelColumn GetPixelColumn(IAxes axes, int xPixelIndex)
```

### `public class SignalSourceGenericList<T> : SignalSourceBase, ISignalSource, IDataSource`
<!-- DataSources\SignalSourceGenericList.cs -->

```csharp
public class SignalSourceGenericList<T> : SignalSourceBase, ISignalSource, IDataSource
public override int Length
public SignalSourceGenericList(IReadOnlyList<T> ys, double period)
public IReadOnlyList<double> GetYs()
public IEnumerable<double> GetYs(int i1, int i2)
public double GetY(int index)
public override SignalRangeY GetLimitsY(int firstIndex, int lastIndex)
public PixelColumn GetPixelColumn(IAxes axes, int xPixelIndex)
```

### `public class SignalXYSourceDoubleArray : ISignalXYSource, IDataSource, IGetNearest`
<!-- DataSources\SignalXYSourceDoubleArray.cs -->

```csharp
public class SignalXYSourceDoubleArray : ISignalXYSource, IDataSource, IGetNearest
public int Count
public bool Rotated { get, set; }
public double XOffset { get, set; }
public double YOffset { get, set; }
public double YScale { get, set; }
public double XScale { get, set; }
public int MinimumIndex { get, set; }
public int MaximumIndex { get, set; }
public bool UsePixelOverlap { get; }
public SignalXYSourceDoubleArray(double[] xs, double[] ys)
public AxisLimits GetAxisLimits()
public IReadOnlyList<Pixel> GetPixelsToDraw(RenderPack rp, IAxes axes, ConnectStyle connectStyle)
public DataPoint GetNearest(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
```

### `public class SignalXYSourceGenericArray<TX, TY> : ISignalXYSource, IDataSource, IGetNearest`
<!-- DataSources\SignalXYSourceGenericArray.cs -->

```csharp
public class SignalXYSourceGenericArray<TX, TY> : ISignalXYSource, IDataSource, IGetNearest
public TX[] Xs { get, set; }
public TY[] Ys { get, set; }
public int Count
public bool Rotated { get, set; }
public double XOffset { get, set; }
public double YOffset { get, set; }
public double YScale { get, set; }
public double XScale { get, set; }
public int MinimumIndex { get, set; }
public int MaximumIndex { get, set; }
public bool UsePixelOverlap { get; }
public SignalXYSourceGenericArray(TX[] xs, TY[] ys)
public AxisLimits GetAxisLimits()
public IReadOnlyList<Pixel> GetPixelsToDraw(RenderPack rp, IAxes axes, ConnectStyle connectStyle)
public Pixel[] GetPixelsToDrawHorizontally(RenderPack rp, IAxes axes, ConnectStyle connectStyle)
public Pixel[] GetPixelsToDrawVertically(RenderPack rp, IAxes axes, ConnectStyle connectStyle)
// Return the vertical range covered by data between the given indices (inclusive)
public CoordinateRange GetRangeY(int index1, int index2)
// Get the index associated with the given X position
public int GetIndex(double x)
// Get the index associated with the given X position limited to the given range
public int GetIndex(double x, IndexRange indexRange)
// Given a pixel column, return the pixels to render its line. If the column contains no data, no pixels are returned. If the column contains one point, return that one pixel. If the column contains multiple points, return 4 pixels: enter, min, max, and exit
public IEnumerable<Pixel> GetColumnPixelsX(int pixelColumnIndex, IndexRange rng, RenderPack rp, IAxes axes)
// Given a pixel column, return the pixels to render its line. If the column contains no data, no pixels are returned. If the column contains one point, return that one pixel. If the column contains multiple points, return 4 pixels: enter, min, max, and exit
public IEnumerable<Pixel> GetColumnPixelsY(int pixelColumnIndex, IndexRange rng, RenderPack rp, IAxes axes)
public DataPoint GetNearest(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
```

### `public class SignalXYSourceGenericList<Tx, Ty> : ISignalXYSource, IDataSource, IGetNearest`
<!-- DataSources\SignalXYSourceGenericList.cs -->

```csharp
public class SignalXYSourceGenericList<Tx, Ty> : ISignalXYSource, IDataSource, IGetNearest
public int Count
public bool Rotated { get, set; }
public double XOffset { get, set; }
public double YOffset { get, set; }
public double YScale { get, set; }
public double XScale { get, set; }
public int MinimumIndex { get, set; }
public int MaximumIndex { get, set; }
public bool UsePixelOverlap { get; }
public SignalXYSourceGenericList(IReadOnlyList<Tx> xs, IReadOnlyList<Ty> ys)
public AxisLimits GetAxisLimits()
public IReadOnlyList<Pixel> GetPixelsToDraw(RenderPack rp, IAxes axes, ConnectStyle connectStyle)
public Pixel[] GetPixelsToDrawHorizontally(RenderPack rp, IAxes axes, ConnectStyle connectStyle)
public Pixel[] GetPixelsToDrawVertically(RenderPack rp, IAxes axes, ConnectStyle connectStyle)
// Return the vertical range covered by data between the given indices (inclusive)
public CoordinateRange GetRangeY(int index1, int index2)
// Get the index associated with the given X position
public int GetIndex(double x)
// Get the index associated with the given X position limited to the given range
public int GetIndex(double x, IndexRange indexRange)
// Given a pixel column, return the pixels to render its line. If the column contains no data, no pixels are returned. If the column contains one point, return that one pixel. If the column contains multiple points, return 4 pixels: enter, min, max, and exit
public IEnumerable<Pixel> GetColumnPixelsX(int pixelColumnIndex, IndexRange rng, RenderPack rp, IAxes axes)
// Given a pixel column, return the pixels to render its line. If the column contains no data, no pixels are returned. If the column contains one point, return that one pixel. If the column contains multiple points, return 4 pixels: enter, min, max, and exit
public IEnumerable<Pixel> GetColumnPixelsY(int pixelColumnIndex, IndexRange rng, RenderPack rp, IAxes axes)
public DataPoint GetNearest(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
```

### `public class VectorFieldDataSourceCoordinatesList(IList<RootedCoordinateVector> rootedVectors) : IVectorFieldSource, IDataSource, IGetNearest`
<!-- DataSources\VectorFieldDataSourceCoordinatesList.cs -->

```csharp
public class VectorFieldDataSourceCoordinatesList(IList<RootedCoordinateVector> rootedVectors) : IVectorFieldSource, IDataSource, IGetNearest
public int MinRenderIndex { get, set; }
public int MaxRenderIndex { get, set; }
public IReadOnlyList<RootedCoordinateVector> GetRootedVectors()
public AxisLimits GetLimits()
public CoordinateRange GetLimitsX()
public CoordinateRange GetLimitsY()
public DataPoint GetNearest(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
```

## ScottPlot.DataViews

### `public interface IDataStreamerView`
<!-- DataViews\IDataStreamerView.cs -->
> Contains logic for rendering fixed-length data in a streaming data logger.

```csharp
public interface IDataStreamerView
```

### `public class Scroll : IDataStreamerView`
<!-- DataViews\Scroll.cs -->

```csharp
public class Scroll : IDataStreamerView
public DataStreamer Streamer { get; }
public Scroll(DataStreamer streamer, bool newOnRight)
public void Render(RenderPack rp)
public IReadOnlyList<Pixel[]> GetSegments(RenderPack rp)
```

### `public class Wipe : IDataStreamerView`
<!-- DataViews\Wipe.cs -->

```csharp
public class Wipe : IDataStreamerView
public DataStreamer Streamer { get; }
public double BlankFraction { get, set; }
public Wipe(DataStreamer streamer, bool wipeRight)
public void Render(RenderPack rp)
public IReadOnlyList<Pixel[]> GetSegments(RenderPack rp)
```

## ScottPlot.Finance

### `public class BollingerBands`
<!-- Finance\BollingerBands.cs -->

```csharp
public class BollingerBands
public readonly double[] Means
public readonly double[] UpperValues
public readonly double[] LowerValues
public readonly DateTime[] DateTimes
public readonly double[] Dates
public BollingerBands(List<OHLC> ohlcs, int N, double sdCoeff = 2)
```

### `public class SimpleMovingAverage`
<!-- Finance\SimpleMovingAverage.cs -->

```csharp
public class SimpleMovingAverage
public readonly double[] Means
public readonly DateTime[] DateTimes
public readonly double[] Dates
public SimpleMovingAverage(IReadOnlyList<OHLC> ohlcs, int N)
```

## ScottPlot.FontResolvers

### `public class FileFontResolver(string name, string path, FontWeight weight, FontSlant slant, FontSpacing width) : IFontResolver`
<!-- FontResolvers\FileFontResolver.cs -->
> Font resolver that creates a typeface from a specified TTF file

```csharp
public class FileFontResolver(string name, string path, FontWeight weight, FontSlant slant, FontSpacing width) : IFontResolver
public FileFontResolver(string name, string path, bool bold, bool italic) : this(name, path, bold ? FontWeight.Bold : FontWeight.Normal, italic ? FontSlant.Italic : FontSlant.Upright, FontSpacing.Normal)
// Attempt to create the typeface using the given settings. Returns null if this resolver does not match the requested font.
public SKTypeface? CreateTypeface(string fontName, FontWeight weight, FontSlant slant, FontSpacing width)
public SKTypeface? CreateTypeface(string fontName, bool bold, bool italic)
public SKTypeface? CreateTypeface(string fontName, bool bold, bool italic, FontSpacing width = FontSpacing.Normal)
public override string ToString()
```

### `public class SystemFontResolver : IFontResolver`
<!-- FontResolvers\SystemFontResolver.cs -->

```csharp
public class SystemFontResolver : IFontResolver
public static string DefaultSystemFont()
public static SKTypeface CreateDefaultTypeface()
public SKTypeface? CreateTypeface(string fontName, FontWeight weight, FontSlant slant, FontSpacing width)
public SKTypeface? CreateTypeface(string fontName, bool bold, bool italic)
public SKTypeface? CreateTypeface(string fontName, bool bold, bool italic, FontSpacing width = FontSpacing.Normal)
```

## ScottPlot.Grids

### `public class DefaultGrid(IXAxis xAxis, IYAxis yAxis) : IGrid`
<!-- Grids\DefaultGrid.cs -->

```csharp
public class DefaultGrid(IXAxis xAxis, IYAxis yAxis) : IGrid
public bool IsVisible { get, set; }
public bool IsBeneathPlottables { get, set; }
public IXAxis XAxis { get, set; }
public IYAxis YAxis { get, set; }
public GridStyle XAxisStyle { get, set; }
public GridStyle YAxisStyle { get, set; }
public Color LineColor { set; }
public float LineWidth { set; }
public LinePattern LinePattern { set; }
public Color MajorLineColor { get, set; }
public Color MinorLineColor { set; }
public float MajorLineWidth { set; }
public float MinorLineWidth { set; }
public LinePattern MajorLinePattern { set; }
public void Render(RenderPack rp)
```

## ScottPlot.Hatches

### `public class Checker : IHatch`
<!-- Hatches\Checker.cs -->

```csharp
public class Checker : IHatch
public SKShader GetShader(Color backgroundColor, Color hatchColor, PixelRect rect)
```

### `public class Dots : IHatch`
<!-- Hatches\Dots.cs -->

```csharp
public class Dots : IHatch
public SKShader GetShader(Color backgroundColor, Color hatchColor, PixelRect rect)
```

### `public class Grid : IHatch`
<!-- Hatches\Grid.cs -->

```csharp
public class Grid : IHatch
public bool Rotate { get, set; }
public Grid(bool rotate = false)
public SKShader GetShader(Color backgroundColor, Color hatchColor, PixelRect rect)
```

### `public class Square : IHatch`
<!-- Hatches\Square.cs -->

```csharp
public class Square : IHatch
public SKShader GetShader(Color backgroundColor, Color hatchColor, PixelRect rect)
```

### `public enum StripeDirection { DiagonalUp, DiagonalDown, Horizontal, Vertical }`
<!-- Hatches\Striped.cs -->

```csharp
public enum StripeDirection { DiagonalUp, DiagonalDown, Horizontal, Vertical }
成员: DiagonalUp, DiagonalDown, Horizontal, Vertical
```

### `public class Striped : IHatch`
<!-- Hatches\Striped.cs -->

```csharp
public class Striped : IHatch
public Striped(StripeDirection stripeDirection = StripeDirection.DiagonalUp)
public StripeDirection StripeDirection { get, set; }
public SKShader GetShader(Color backgroundColor, Color hatchColor, PixelRect rect)
```

## ScottPlot.IO

### `public struct BitmapHeader`
<!-- IO\BitmapHeader.cs -->
> This struct holds values that define the first several bytes of a bitmap file.

```csharp
public struct BitmapHeader
public const int FileHeaderSize = 54
public readonly byte MagicNumberHighByte = (byte)'B'
public readonly byte MagicNumberLowByte = (byte)'M'
public readonly int Size
public readonly short Reserved1
public readonly short Reserved2
public readonly int Offset = FileHeaderSize
public readonly int BitmapInfoHeaderSize = 40
public readonly int Width
public readonly int Height
public readonly short ColorPlanes = 1
public readonly short BitsPerPixel = 32
public readonly int CompressionMethod = 0
public readonly int PixelSize = 0
public readonly int HorizontalResolution
public readonly int VerticalResolution
public readonly int ColorsInPalette
public readonly int ImportantColors
public BitmapHeader(int width, int height)
```

## ScottPlot.Interactivity

### `public interface IMouseAction : IUserAction`
<!-- Interactivity\IMouseAction.cs -->
> User actions that occur at a point in pixel space

```csharp
public interface IMouseAction : IUserAction
public Pixel Pixel { get; }
```

### `public interface IMouseButtonAction : IMouseAction`
<!-- Interactivity\IMouseButtonAction.cs -->
> Mouse actions that describe a button changing state

```csharp
public interface IMouseButtonAction : IMouseAction
public bool IsPressed { get; }
```

### `public interface IUserAction`
<!-- Interactivity\IUserAction.cs -->
> Describes something the uer did to interact with the plot

```csharp
public interface IUserAction
// Describes when the event happened. Useful for distinguishing single from double-clicks.
public DateTime DateTime { get, set; }
```

### `public interface IUserActionResponse`
<!-- Interactivity\IUserActionResponse.cs -->
> Describes a class that has logic to watch user actions and manipulate the plot accordingly.

```csharp
public interface IUserActionResponse
```

### `public readonly record struct Key`
<!-- Interactivity\Key.cs -->
> Represents a single key on a keyboard that may be pressed and held. Keys are tracked by and classes can see which keys are pressed when they are executed.

```csharp
public readonly record struct Key
// A name that uniquely identifies a specific key
public string Name { get; }
public Key(string name)
```

### `public class KeyboardState`
<!-- Interactivity\KeyboardState.cs -->
> Tracks which keyboard keys are currently pressed.

```csharp
public class KeyboardState
public int PressedKeyCount
public void Reset()
public void Add(Key key)
public void Remove(Key key)
public bool IsPressed(Key key)
public bool IsPressed(IEnumerable<Key> keys)
public bool IsPressed(string keyName)
public string[] GetPressedKeyNames
public override string ToString()
```

### `public static class MouseAxisManipulation`
<!-- Interactivity\MouseAxisManipulation.cs -->
> This class stores logic for changing axis limits according to mouse inputs in pixel units. Methods here are similar to those in except their inputs are all mouse events.

```csharp
public static class MouseAxisManipulation
public static void MouseWheelZoom(Plot plot, double fracX, double fracY, Pixel pixel, bool ChangeOpposingAxesTogether)
public static void DragPan(Plot plot, Pixel mouseDown, Pixel mouseNow, bool changeOpposingAxesTogether)
public static void DragZoom(Plot plot, Pixel mouseDown, Pixel mouseNow, bool changeOpposingAxesTogether)
public static void PlaceZoomRectangle(Plot plot, Pixel mouseDown, Pixel mouseNow)
public static void AutoScale(Plot plot, Pixel pixel, bool allParallelAxes)
```

### `public record struct MouseButton(string name)`
<!-- Interactivity\MouseButton.cs -->
> Represents a physical button on a mouse

```csharp
public record struct MouseButton(string name)
public string Name { get; }
```

### `public readonly record struct ResponseInfo`
<!-- Interactivity\ResponseInfo.cs -->
> Describes what may need to happen after a user action response has completed executing

```csharp
public readonly record struct ResponseInfo
// Request a render after all responses have finished executing
public bool RefreshNeeded { get, init; }
// If true, all other responses will not be executed until the response that returned this result returns a new result with this flag false.
public bool IsPrimary { get, init; }
public override string ToString()
public static ResponseInfo NoActionRequired
public static ResponseInfo Refresh
```

### `public static class StandardKeys`
<!-- Interactivity\StandardKeys.cs -->
> Structures for commonly used keys. Use these as a safer alternative to instantiating your own.

```csharp
public static class StandardKeys
public static readonly Key Alt = new("alt")
public static readonly Key Control = new("ctrl")
public static readonly Key Shift = new("shift")
public static readonly Key Down = new("down")
public static readonly Key Up = new("up")
public static readonly Key Left = new("left")
public static readonly Key Right = new("right")
public static readonly Key Unknown = new("unknown")
public static readonly Key A = new("a")
public static bool IsArrowKey(Key key)
```

### `public static class StandardMouseButtons`
<!-- Interactivity\StandardMouseButtons.cs -->
> Structures for commonly used mouse buttons. Use these as a safer alternative to instantiating your own.

```csharp
public static class StandardMouseButtons
public readonly static MouseButton Left = new("left")
public readonly static MouseButton Right = new("right")
public readonly static MouseButton Middle = new("middle")
public readonly static MouseButton Wheel = new("wheel")
```

### `public class UserInputProcessor`
<!-- Interactivity\UserInputProcessor.cs -->
> This class collects user inputs and performs responses to manipulate a Plot. Custom user input actions may be supplied, and the list of responses can be modified to achieve total control over interaction behavior.

```csharp
public class UserInputProcessor
// The plot this input processor will act on
public IPlotControl PlotControl { get; }
// Tracks which keys are currently pressed
public readonly KeyboardState KeyState = new()
// Controls whether new events are processed. Enabling this disables the older system.
public bool IsEnabled { get, set; }
// Enable processing of user input events.
public void Enable()
// Disable processing of user input events. Effectively makes this control non-interactive.
public void Disable()
// A list of user input responses that processes all incoming events in order. Users may manipulate this list to change the default behavior and add custom behaviors.
public readonly List<IUserActionResponse> UserActionResponses = []
public UserInputProcessor(IPlotControl plotControl)
// Remove all user input responses of the specified type
public void RemoveAll<T>() where T : IUserActionResponse
// Resets the user input responses to use the default interactivity settings
public void Reset()
// Default user actions that are in place when the event processor is constructed or reset.
public static List<IUserActionResponse> DefaultUserResponses()
// Helper method to enable or disable the default double-left-click benchmark behavior
public void DoubleLeftClickBenchmark(bool enable)
// Helper method to enable or disable the default left-click-drag pan behavior
public void LeftClickDragPan(bool enable, bool horizontal = true, bool vertical = true)
// Helper method to enable or disable the default left-click-drag pan behavior
public void RightClickDragZoom(bool enable, bool horizontal = true, bool vertical = true)
// Process a user input
public void Process(IUserAction userAction)
public Action<IPlotControl> LostFocusAction = (IPlotControl plotControl) => { ResetState(plotControl); plotControl.Refresh(); }
// Reset state of all user action responses to do things like abort mouse-down-drag actions or key press-and-hold actions
public static void ResetState(IPlotControl plotControl)
public void ProcessLostFocus()
```

## ScottPlot.Interactivity.UserActionResponses

### `public class DoubleClickBenchmark(MouseButton button) : DoubleClickResponse(button, ToggleBenchmarkVisibility)`
<!-- Interactivity\UserActionResponses\DoubleClickBenchmark.cs -->

```csharp
public class DoubleClickBenchmark(MouseButton button) : DoubleClickResponse(button, ToggleBenchmarkVisibility)
public static void ToggleBenchmarkVisibility(IPlotControl plotControl, Pixel pixel)
```

### `public class DoubleClickResponse(MouseButton button, Action<IPlotControl, Pixel> action) : IUserActionResponse`
<!-- Interactivity\UserActionResponses\DoubleClickResponse.cs -->

```csharp
public class DoubleClickResponse(MouseButton button, Action<IPlotControl, Pixel> action) : IUserActionResponse
// Which mouse button to watch for double-clicks.
public MouseButton MouseButton { get; }
// This action is invoked when a double-click occurs. Replace this action with your own logic to customize double-click behavior.
public Action<IPlotControl, Pixel> ResponseAction { get; }
// Consecutive clicks are only considered a double-click if the time between the first click mouse down and second click mouse up does not exceed this value.
public TimeSpan MaximumTimeBetweenClicks = TimeSpan.FromMilliseconds(500)
public void ResetState(IPlotControl plotControl)
public ResponseInfo Execute(IPlotControl plotControl, IUserAction userAction, KeyboardState keys)
```

### `public class KeyPressResponse(Key key, Action<IPlotControl, Pixel> action) : IUserActionResponse`
<!-- Interactivity\UserActionResponses\KeyPressResponse.cs -->

```csharp
public class KeyPressResponse(Key key, Action<IPlotControl, Pixel> action) : IUserActionResponse
public void ResetState(IPlotControl plotControl)
public ResponseInfo Execute(IPlotControl plotControl, IUserAction userAction, KeyboardState keys)
```

### `public class KeyboardAutoscale(Key key) : KeyPressResponse(key, AutoScale)`
<!-- Interactivity\UserActionResponses\KeyboardAutoscale.cs -->

```csharp
public class KeyboardAutoscale(Key key) : KeyPressResponse(key, AutoScale)
public static void AutoScale(IPlotControl plotControl, Pixel pixel)
```

### `public class KeyboardPanAndZoom : IUserActionResponse`
<!-- Interactivity\UserActionResponses\KeyboardPanAndZoom.cs -->

```csharp
public class KeyboardPanAndZoom : IUserActionResponse
public Key PanLeftKey { get, set; }
public Key PanRightKey { get, set; }
public Key PanDownKey { get, set; }
public Key PanUpKey { get, set; }
// When this key is held, pan actions will zoom instead
public Key ZoomModifierKey { get, set; }
// When this key is held, panning will occur in larger steps
public Key LargeStepKey { get, set; }
// When this key is held, panning will occur in single pixel steps
public Key FineStepKey { get, set; }
public float StepDistance { get, set; }
public float LargeStepDistance { get, set; }
public float FineStepDistance { get, set; }
public double DeltaZoomIn { get, set; }
public double DeltaZoomOut { get, set; }
public void ResetState(IPlotControl plotControl)
public ResponseInfo Execute(IPlotControl plotControl, IUserAction userInput, KeyboardState keys)
```

### `public class MouseDragPan(MouseButton button) : IUserActionResponse`
<!-- Interactivity\UserActionResponses\MouseDragPan.cs -->

```csharp
public class MouseDragPan(MouseButton button) : IUserActionResponse
// Which mouse button to watch for click-drag events
public MouseButton MouseButton { get; }
// Vertical panning is disabled if any of these keys are pressed
public List<Key> KeysThatLockY { get; }
// Horizontal panning is disabled if any of these keys are pressed
public List<Key> KeysThatLockX { get; }
// Vertical panning is disabled when this is set
public bool LockY { get, set; }
// Horizontal panning is disabled when this is set
public bool LockX { get, set; }
// If enabled, mouse interactions over a single axis will be applied to all axes with the same orientation.
public bool ChangeOpposingAxesTogether
public void ResetState(IPlotControl plotControl)
public ResponseInfo Execute(IPlotControl plotControl, IUserAction userInput, KeyboardState keys)
```

### `public class MouseDragZoom(MouseButton button) : IUserActionResponse`
<!-- Interactivity\UserActionResponses\MouseDragZoom.cs -->

```csharp
public class MouseDragZoom(MouseButton button) : IUserActionResponse
// Vertical panning is disabled if any of these keys are pressed
public List<Key> KeysThatLockY { get; }
// Horizontal panning is disabled if any of these keys are pressed
public List<Key> KeysThatLockX { get; }
// Vertical panning is disabled when this is set
public bool LockY { get, set; }
// Horizontal panning is disabled when this is set
public bool LockX { get, set; }
// Scale the horizontal mouse sensitivity by this value. Larger numbers result in more zooming for the same drag distance.
public double SensitivityX { get, set; }
// Scale the vertical mouse sensitivity by this value. Larger numbers result in more zooming for the same drag distance.
public double SensitivityY { get, set; }
// If enabled, mouse interactions over a single axis will be applied to all axes with the same orientation.
public bool ChangeOpposingAxesTogether
public void ResetState(IPlotControl plotControl)
public ResponseInfo Execute(IPlotControl plotControl, IUserAction userInput, KeyboardState keys)
```

### `public class MouseDragZoomRectangle(MouseButton button) : IUserActionResponse`
<!-- Interactivity\UserActionResponses\MouseDragZoomRectangle.cs -->
> Click-drag draws a rectangle over a plot which becomes the new field of view when released.

```csharp
public class MouseDragZoomRectangle(MouseButton button) : IUserActionResponse
// A zoom rectangle is started when this button is pressed and dragged with held down
public MouseButton SecondaryMouseButton { get, set; }
// A zoom rectangle is started when is pressed and dragged with this key held down
public Key SecondaryKey { get, set; }
// When held, horizontal axis limits will not be modified
public Key HorizontalLockKey { get, set; }
// When held, vertical axis limits will not be modified
public Key VerticalLockKey { get, set; }
public void ResetState(IPlotControl plotControl)
public ResponseInfo Execute(IPlotControl plotControl, IUserAction userAction, KeyboardState keys)
```

### `public class MouseInteractWithPlottables(MouseButton button) : IUserActionResponse`
<!-- Interactivity\UserActionResponses\MouseInteractWithPlottables.cs -->

```csharp
public class MouseInteractWithPlottables(MouseButton button) : IUserActionResponse
// Which mouse button to watch to engage with interactive plottables
public MouseButton MouseButton { get; }
public void ResetState(IPlotControl plotControl)
public ResponseInfo Execute(IPlotControl plotControl, IUserAction userInput, KeyboardState keys)
```

### `public class MouseWheelZoom(Key horizontalLockKey, Key verticalLockKey) : IUserActionResponse`
<!-- Interactivity\UserActionResponses\MouseWheelZoom.cs -->

```csharp
public class MouseWheelZoom(Key horizontalLockKey, Key verticalLockKey) : IUserActionResponse
// If enabled, when the mouse zooms while hovered over an axis only that axis will be changed.
public bool ZoomAxisUnderMouse { get, set; }
// If enabled with , all axes of the same direction will be changed together.
public bool LockParallelAxes { get, set; }
public void ResetState(IPlotControl plotControl)
// Fraction of the axis range to change when zooming in and out.
public double ZoomFraction { get, set; }
public ResponseInfo Execute(IPlotControl plotControl, IUserAction userInput, KeyboardState keys)
```

### `public class SingleClickAutoscale(MouseButton button) : SingleClickResponse(button, AutoScale)`
<!-- Interactivity\UserActionResponses\SingleClickAutoscale.cs -->

```csharp
public class SingleClickAutoscale(MouseButton button) : SingleClickResponse(button, AutoScale)
public static void AutoScale(IPlotControl plotControl, Pixel pixel)
```

### `public class SingleClickContextMenu(MouseButton button) : SingleClickResponse(button, LaunchContextMenu)`
<!-- Interactivity\UserActionResponses\SingleClickContextMenu.cs -->

```csharp
public class SingleClickContextMenu(MouseButton button) : SingleClickResponse(button, LaunchContextMenu)
public static void LaunchContextMenu(IPlotControl plotControl, Pixel pixel)
```

### `public class SingleClickResponse(MouseButton button, Action<IPlotControl, Pixel> action) : IUserActionResponse`
<!-- Interactivity\UserActionResponses\SingleClickResponse.cs -->

```csharp
public class SingleClickResponse(MouseButton button, Action<IPlotControl, Pixel> action) : IUserActionResponse
// Which mouse button to watch for single-click events
public MouseButton MouseButton { get; }
// This action is invoked when a single-click occurs.
public Action<IPlotControl, Pixel> ResponseAction { get; }
public void ResetState(IPlotControl plotControl)
public ResponseInfo Execute(IPlotControl plotControl, IUserAction userAction, KeyboardState keys)
```

## ScottPlot.Interactivity.UserActions

### `public record struct KeyDown(Key Key) : IUserAction`
<!-- Interactivity\UserActions\KeyDown.cs -->

```csharp
public record struct KeyDown(Key Key) : IUserAction
public readonly string Device
public readonly string Description
public DateTime DateTime { get, set; }
```

### `public record struct KeyUp(Key Key) : IUserAction`
<!-- Interactivity\UserActions\KeyUp.cs -->

```csharp
public record struct KeyUp(Key Key) : IUserAction
public readonly string Device
public readonly string Description
public DateTime DateTime { get, set; }
```

### `public record struct LeftMouseDown(Pixel Pixel) : IMouseButtonAction`
<!-- Interactivity\UserActions\LeftMouseDown.cs -->

```csharp
public record struct LeftMouseDown(Pixel Pixel) : IMouseButtonAction
public readonly MouseButton Button
public readonly bool IsPressed
public readonly string Device
public readonly string Description
public DateTime DateTime { get, set; }
```

### `public record struct LeftMouseUp(Pixel Pixel) : IMouseButtonAction`
<!-- Interactivity\UserActions\LeftMouseUp.cs -->

```csharp
public record struct LeftMouseUp(Pixel Pixel) : IMouseButtonAction
public readonly MouseButton Button
public readonly bool IsPressed
public readonly string Device
public readonly string Description
public DateTime DateTime { get, set; }
```

### `public record struct MiddleMouseDown(Pixel Pixel) : IMouseButtonAction`
<!-- Interactivity\UserActions\MiddleMouseDown.cs -->

```csharp
public record struct MiddleMouseDown(Pixel Pixel) : IMouseButtonAction
public readonly MouseButton Button
public readonly bool IsPressed
public readonly string Device
public readonly string Description
public DateTime DateTime { get, set; }
```

### `public record struct MiddleMouseUp(Pixel Pixel) : IMouseButtonAction`
<!-- Interactivity\UserActions\MiddleMouseUp.cs -->

```csharp
public record struct MiddleMouseUp(Pixel Pixel) : IMouseButtonAction
public readonly MouseButton Button
public readonly bool IsPressed
public readonly string Device
public readonly string Description
public DateTime DateTime { get, set; }
```

### `public record struct MouseMove(Pixel Pixel) : IMouseAction`
<!-- Interactivity\UserActions\MouseMove.cs -->

```csharp
public record struct MouseMove(Pixel Pixel) : IMouseAction
public readonly string Device
public readonly string Description
public DateTime DateTime { get, set; }
```

### `public record struct MouseWheelDown(Pixel Pixel) : IMouseButtonAction`
<!-- Interactivity\UserActions\MouseWheelDown.cs -->

```csharp
public record struct MouseWheelDown(Pixel Pixel) : IMouseButtonAction
public readonly MouseButton Button
public readonly bool IsPressed
public readonly string Device
public readonly string Description
public DateTime DateTime { get, set; }
```

### `public record struct MouseWheelUp(Pixel Pixel) : IMouseButtonAction`
<!-- Interactivity\UserActions\MouseWheelUp.cs -->

```csharp
public record struct MouseWheelUp(Pixel Pixel) : IMouseButtonAction
public readonly MouseButton Button
public readonly bool IsPressed
public readonly string Device
public readonly string Description
public DateTime DateTime { get, set; }
```

### `public record struct RightMouseDown(Pixel Pixel) : IMouseButtonAction`
<!-- Interactivity\UserActions\RightMouseDown.cs -->

```csharp
public record struct RightMouseDown(Pixel Pixel) : IMouseButtonAction
public readonly MouseButton Button
public readonly bool IsPressed
public readonly string Device
public readonly string Description
public DateTime DateTime { get, set; }
```

### `public record struct RightMouseUp(Pixel Pixel) : IMouseButtonAction`
<!-- Interactivity\UserActions\RightMouseUp.cs -->

```csharp
public record struct RightMouseUp(Pixel Pixel) : IMouseButtonAction
public readonly MouseButton Button
public readonly bool IsPressed
public readonly string Device
public readonly string Description
public DateTime DateTime { get, set; }
```

### `public record struct Unknown(string device, string? description) : IUserAction`
<!-- Interactivity\UserActions\Unknown.cs -->

```csharp
public record struct Unknown(string device, string? description) : IUserAction
public readonly string Device
public readonly string Description
public DateTime DateTime { get, set; }
```

## ScottPlot.LayoutEngines

### `public class Automatic : LayoutEngineBase, ILayoutEngine`
<!-- LayoutEngines\Automatic.cs -->
> Generate the layout by measuring all panels and adding enough padding around the data area to fit them all exactly.

```csharp
public class Automatic : LayoutEngineBase, ILayoutEngine
public float SizeForAxisPanelsWithoutData = 10
public Layout GetLayout(PixelRect figureRect, Plot plot, Paint paint)
```

### `public class FixedDataArea(PixelRect dataRect) : LayoutEngineBase, ILayoutEngine`
<!-- LayoutEngines\FixedDataArea.cs -->
> Generate a layout using a fixed rectangle for the data area

```csharp
public class FixedDataArea(PixelRect dataRect) : LayoutEngineBase, ILayoutEngine
public Layout GetLayout(PixelRect figureRect, Plot plot, Paint paint)
```

### `public class FixedPadding(PixelPadding padding) : LayoutEngineBase, ILayoutEngine`
<!-- LayoutEngines\FixedPadding.cs -->
> Generate layouts where the data area has a fixed padding from the edge of the figure

```csharp
public class FixedPadding(PixelPadding padding) : LayoutEngineBase, ILayoutEngine
public Layout GetLayout(PixelRect figureRect, Plot plot, Paint paint)
```

### `public class LayoutEngineBase`
<!-- LayoutEngines\LayoutEngineBase.cs -->

```csharp
public class LayoutEngineBase
```

### `public class MatchedDataRect(Plot referencePlot) : LayoutEngineBase, ILayoutEngine`
<!-- LayoutEngines\MatchedDataRect.cs -->
> Generate layouts that match layouts of another control

```csharp
public class MatchedDataRect(Plot referencePlot) : LayoutEngineBase, ILayoutEngine
public Layout GetLayout(PixelRect figureRect, Plot plot, Paint paint)
```

## ScottPlot.LegendLayouts

### `public class Wrapping : ILegendLayout`
<!-- LegendLayouts\Wrapping.cs -->

```csharp
public class Wrapping : ILegendLayout
public LegendLayout GetLayout(Legend legend, LegendItem[] items, PixelSize maxSize, Paint paint)
```

## ScottPlot.MultiplotLayouts

### `public class Columns : IMultiplotLayout`
<!-- MultiplotLayouts\Columns.cs -->

```csharp
public class Columns : IMultiplotLayout
public PixelRect[] GetSubplotRectangles(SubplotCollection subplots, PixelRect figureRect)
```

### `public class CustomGrid : IMultiplotLayout`
<!-- MultiplotLayouts\CustomGrid.cs -->

```csharp
public class CustomGrid : IMultiplotLayout
public PixelRect[] GetSubplotRectangles(SubplotCollection subplots, PixelRect figureRect)
public void Set(Plot plot, GridCell gridCell)
```

### `public class DraggableRows() : IMultiplotLayout`
<!-- MultiplotLayouts\DraggableRows.cs -->

```csharp
public class DraggableRows() : IMultiplotLayout
// The plot with this index will be resized automatically to occupy remaining space.
public int ExpandingPlotIndex { get, set; }
// Plots cannot be resized to be smaller than this number of pixels
public float MinimumHeight { get, set; }
// Allow resizing when the cursor is this many pixels away from a divider
public float SnapDistance { get, set; }
// Set the initial height for each plot. These heights will be modified automatically as dividers are moved or the plot is resized.
public void SetHeights(IEnumerable<float> heights)
// Resizes plots as necessary to place a divider at the given location
public void SetDivider(int index, float yPixel)
// Returns the index of the divider between two plots at the given pixel
public int? GetDivider(float yPixel)
public PixelRect[] GetSubplotRectangles(SubplotCollection subplots, PixelRect figureRect)
```

### `public class Grid(int rows, int columns) : IMultiplotLayout`
<!-- MultiplotLayouts\Grid.cs -->

```csharp
public class Grid(int rows, int columns) : IMultiplotLayout
public PixelRect[] GetSubplotRectangles(SubplotCollection subplots, PixelRect figureRect)
```

### `public class Rows : IMultiplotLayout`
<!-- MultiplotLayouts\Rows.cs -->

```csharp
public class Rows : IMultiplotLayout
public PixelRect[] GetSubplotRectangles(SubplotCollection subplots, PixelRect figureRect)
```

## ScottPlot.NamedColors

### `public abstract class NamedColorsBase : INamedColors`
<!-- NamedColors\NamedColorsBase.cs -->

```csharp
public abstract class NamedColorsBase : INamedColors
public Color[] GetAllColors()
```

### `public class WebColors : NamedColorsBase`
<!-- NamedColors\WebColors.cs -->
> Colors defined according to W3C standard keywords https://www.w3.org/wiki/CSS/Properties/color/keywords

```csharp
public class WebColors : NamedColorsBase
public static Color AliceBlue
public static Color AntiqueWhite
public static Color Aqua
public static Color Aquamarine
public static Color Azure
public static Color Beige
public static Color Bisque
public static Color Black
public static Color BlanchedAlmond
public static Color Blue
public static Color BlueViolet
public static Color Brown
public static Color BurlyWood
public static Color CadetBlue
public static Color Chartreuse
public static Color Chocolate
public static Color Coral
public static Color CornflowerBlue
public static Color Cornsilk
public static Color Crimson
public static Color Cyan
public static Color DarkBlue
public static Color DarkCyan
public static Color DarkGoldenRod
public static Color DarkGray
public static Color DarkGrey
public static Color DarkGreen
public static Color DarkKhaki
public static Color DarkMagenta
public static Color DarkOliveGreen
public static Color DarkOrange
public static Color DarkOrchid
public static Color DarkRed
public static Color DarkSalmon
public static Color DarkSeaGreen
public static Color DarkSlateBlue
public static Color DarkSlateGray
public static Color DarkSlateGrey
public static Color DarkTurquoise
public static Color DarkViolet
public static Color DeepPink
public static Color DeepSkyBlue
public static Color DimGray
public static Color DimGrey
public static Color DodgerBlue
public static Color FireBrick
public static Color FloralWhite
public static Color ForestGreen
public static Color Fuchsia
public static Color Gainsboro
public static Color GhostWhite
public static Color Gold
public static Color GoldenRod
public static Color Gray
public static Color Grey
public static Color Green
public static Color GreenYellow
public static Color HoneyDew
public static Color HotPink
public static Color IndianRed
public static Color Indigo
public static Color Ivory
public static Color Khaki
public static Color Lavender
public static Color LavenderBlush
public static Color LawnGreen
public static Color LemonChiffon
public static Color LightBlue
public static Color LightCoral
public static Color LightCyan
public static Color LightGoldenRodYellow
public static Color LightGray
public static Color LightGrey
public static Color LightGreen
public static Color LightPink
public static Color LightSalmon
public static Color LightSeaGreen
public static Color LightSkyBlue
public static Color LightSlateGray
public static Color LightSlateGrey
public static Color LightSteelBlue
public static Color LightYellow
public static Color Lime
public static Color LimeGreen
public static Color Linen
public static Color Magenta
public static Color Maroon
public static Color MediumAquaMarine
public static Color MediumBlue
public static Color MediumOrchid
public static Color MediumPurple
public static Color MediumSeaGreen
public static Color MediumSlateBlue
public static Color MediumSpringGreen
public static Color MediumTurquoise
public static Color MediumVioletRed
public static Color MidnightBlue
public static Color MintCream
public static Color MistyRose
public static Color Moccasin
public static Color NavajoWhite
public static Color Navy
public static Color OldLace
public static Color Olive
public static Color OliveDrab
public static Color Orange
public static Color OrangeRed
public static Color Orchid
public static Color PaleGoldenRod
public static Color PaleGreen
public static Color PaleTurquoise
public static Color PaleVioletRed
public static Color PapayaWhip
public static Color PeachPuff
public static Color Peru
public static Color Pink
public static Color Plum
public static Color PowderBlue
public static Color Purple
public static Color RebeccaPurple
public static Color Red
public static Color RosyBrown
public static Color RoyalBlue
public static Color SaddleBrown
public static Color Salmon
public static Color SandyBrown
public static Color SeaGreen
public static Color SeaShell
public static Color Sienna
public static Color Silver
public static Color SkyBlue
public static Color SlateBlue
public static Color SlateGray
public static Color SlateGrey
public static Color Snow
public static Color SpringGreen
public static Color SteelBlue
public static Color Tan
public static Color Teal
public static Color Thistle
public static Color Tomato
public static Color Turquoise
public static Color Violet
public static Color Wheat
public static Color White
public static Color WhiteSmoke
public static Color Yellow
public static Color YellowGreen
```

### `public class WindowsClassicColors : NamedColorsBase`
<!-- NamedColors\WindowsClassicColors.cs -->

```csharp
public class WindowsClassicColors : NamedColorsBase
public static Color ActiveBorder
public static Color ActiveCaption
public static Color AppWorkspace
public static Color Background
public static Color ButtonFace
public static Color ButtonHighlight
public static Color ButtonShadow
public static Color ButtonText
public static Color CaptionText
public static Color GrayText
public static Color Highlight
public static Color HighlightText
public static Color InactiveBorder
public static Color InactiveCaption
public static Color InactiveCaptionText
public static Color InfoBackground
public static Color InfoText
public static Color Menu
public static Color MenuText
public static Color Scrollbar
public static Color ThreeDDarkShadow
public static Color ThreeDFace
public static Color ThreeDHighlight
public static Color ThreeDLightShadow
public static Color ThreeDShadow
public static Color Window
public static Color WindowFrame
public static Color WindowText
```

### `public class WindowsStandardColors : NamedColorsBase`
<!-- NamedColors\WindowsStandardColors.cs -->

```csharp
public class WindowsStandardColors : NamedColorsBase
public static Color ActiveBorder
public static Color ActiveCaption
public static Color AppWorkspace
public static Color Background
public static Color ButtonFace
public static Color ButtonHighlight
public static Color ButtonShadow
public static Color ButtonText
public static Color CaptionText
public static Color GrayText
public static Color Highlight
public static Color HighlightText
public static Color InactiveBorder
public static Color InactiveCaption
public static Color InactiveCaptionText
public static Color InfoBackground
public static Color InfoText
public static Color Menu
public static Color MenuText
public static Color Scrollbar
public static Color ThreeDDarkShadow
public static Color ThreeDFace
public static Color ThreeDHighlight
public static Color ThreeDLightShadow
public static Color ThreeDShadow
public static Color Window
public static Color WindowFrame
public static Color WindowText
```

### `public class WindowsVistaColors : NamedColorsBase`
<!-- NamedColors\WindowsVistaColors.cs -->

```csharp
public class WindowsVistaColors : NamedColorsBase
public static Color ActiveBorder
public static Color ActiveCaption
public static Color AppWorkspace
public static Color Background
public static Color ButtonFace
public static Color ButtonHighlight
public static Color ButtonShadow
public static Color ButtonText
public static Color CaptionText
public static Color GrayText
public static Color Highlight
public static Color HighlightText
public static Color InactiveBorder
public static Color InactiveCaption
public static Color InactiveCaptionText
public static Color InfoBackground
public static Color InfoText
public static Color Menu
public static Color MenuText
public static Color Scrollbar
public static Color ThreeDDarkShadow
public static Color ThreeDFace
public static Color ThreeDHighlight
public static Color ThreeDLightShadow
public static Color ThreeDShadow
public static Color Window
public static Color WindowFrame
public static Color WindowText
```

### `public class XkcdColors : NamedColorsBase`
<!-- NamedColors\XkcdColors.cs -->
> Colors defined according to results of the xkcd color name survey https://xkcd.com/color/rgb/

```csharp
public class XkcdColors : NamedColorsBase
public static Color AcidGreen
public static Color Adobe
public static Color Algae
public static Color AlgaeGreen
public static Color AlmostBlack
public static Color Amber
public static Color Amethyst
public static Color Apple
public static Color AppleGreen
public static Color Apricot
public static Color Aqua
public static Color AquaBlue
public static Color AquaGreen
public static Color AquaMarine
public static Color Aquamarine
public static Color ArmyGreen
public static Color Asparagus
public static Color Aubergine
public static Color Auburn
public static Color Avocado
public static Color AvocadoGreen
public static Color Azul
public static Color Azure
public static Color BabyBlue
public static Color BabyGreen
public static Color BabyPink
public static Color BabyPoo
public static Color BabyPoop
public static Color BabyPoopGreen
public static Color BabyPukeGreen
public static Color BabyPurple
public static Color BabyShitBrown
public static Color BabyShitGreen
public static Color Banana
public static Color BananaYellow
public static Color BarbiePink
public static Color BarfGreen
public static Color Barney
public static Color BarneyPurple
public static Color BattleshipGrey
public static Color Beige
public static Color Berry
public static Color Bile
public static Color Black
public static Color Bland
public static Color Blood
public static Color BloodOrange
public static Color BloodRed
public static Color Blue
public static Color BlueBlue
public static Color BlueGreen
public static Color BlueGrey
public static Color BluePurple
public static Color BlueSlashGreen
public static Color BlueSlashGrey
public static Color BlueSlashPurple
public static Color BlueViolet
public static Color BlueWithAHintOfPurple
public static Color Blueberry
public static Color Bluegreen
public static Color Bluegrey
public static Color BlueyGreen
public static Color BlueyGrey
public static Color BlueyPurple
public static Color Bluish
public static Color BluishGreen
public static Color BluishGrey
public static Color BluishPurple
public static Color Blurple
public static Color Blush
public static Color BlushPink
public static Color Booger
public static Color BoogerGreen
public static Color Bordeaux
public static Color BoringGreen
public static Color BottleGreen
public static Color Brick
public static Color BrickOrange
public static Color BrickRed
public static Color BrightAqua
public static Color BrightBlue
public static Color BrightCyan
public static Color BrightGreen
public static Color BrightLavender
public static Color BrightLightBlue
public static Color BrightLightGreen
public static Color BrightLilac
public static Color BrightLime
public static Color BrightLimeGreen
public static Color BrightMagenta
public static Color BrightOlive
public static Color BrightOrange
public static Color BrightPink
public static Color BrightPurple
public static Color BrightRed
public static Color BrightSeaGreen
public static Color BrightSkyBlue
public static Color BrightTeal
public static Color BrightTurquoise
public static Color BrightViolet
public static Color BrightYellow
public static Color BrightYellowGreen
public static Color BritishRacingGreen
public static Color Bronze
public static Color Brown
public static Color BrownGreen
public static Color BrownGrey
public static Color BrownOrange
public static Color BrownRed
public static Color BrownYellow
public static Color Brownish
public static Color BrownishGreen
public static Color BrownishGrey
public static Color BrownishOrange
public static Color BrownishPink
public static Color BrownishPurple
public static Color BrownishRed
public static Color BrownishYellow
public static Color BrownyGreen
public static Color BrownyOrange
public static Color Bruise
public static Color BubbleGumPink
public static Color Bubblegum
public static Color BubblegumPink
public static Color Buff
public static Color Burgundy
public static Color BurntOrange
public static Color BurntRed
public static Color BurntSiena
public static Color BurntSienna
public static Color BurntUmber
public static Color BurntYellow
public static Color Burple
public static Color Butter
public static Color ButterYellow
public static Color Butterscotch
public static Color CadetBlue
public static Color Camel
public static Color Camo
public static Color CamoGreen
public static Color CamouflageGreen
public static Color Canary
public static Color CanaryYellow
public static Color CandyPink
public static Color Caramel
public static Color Carmine
public static Color Carnation
public static Color CarnationPink
public static Color CarolinaBlue
public static Color Celadon
public static Color Celery
public static Color Cement
public static Color Cerise
public static Color Cerulean
public static Color CeruleanBlue
public static Color Charcoal
public static Color CharcoalGrey
public static Color Chartreuse
public static Color Cherry
public static Color CherryRed
public static Color Chestnut
public static Color Chocolate
public static Color ChocolateBrown
public static Color Cinnamon
public static Color Claret
public static Color Clay
public static Color ClayBrown
public static Color ClearBlue
public static Color CloudyBlue
public static Color Cobalt
public static Color CobaltBlue
public static Color Cocoa
public static Color Coffee
public static Color CoolBlue
public static Color CoolGreen
public static Color CoolGrey
public static Color Copper
public static Color Coral
public static Color CoralPink
public static Color Cornflower
public static Color CornflowerBlue
public static Color Cranberry
public static Color Cream
public static Color Creme
public static Color Crimson
public static Color Custard
public static Color Cyan
public static Color Dandelion
public static Color Dark
public static Color DarkAqua
public static Color DarkAquamarine
public static Color DarkBeige
public static Color DarkBlue
public static Color DarkBlueGreen
public static Color DarkBlueGrey
public static Color DarkBrown
public static Color DarkCoral
public static Color DarkCream
public static Color DarkCyan
public static Color DarkForestGreen
public static Color DarkFuchsia
public static Color DarkGold
public static Color DarkGrassGreen
public static Color DarkGreen
public static Color DarkGreenBlue
public static Color DarkGrey
public static Color DarkGreyBlue
public static Color DarkHotPink
public static Color DarkIndigo
public static Color DarkKhaki
public static Color DarkLavender
public static Color DarkLilac
public static Color DarkLime
public static Color DarkLimeGreen
public static Color DarkMagenta
public static Color DarkMaroon
public static Color DarkMauve
public static Color DarkMint
public static Color DarkMintGreen
public static Color DarkMustard
public static Color DarkNavy
public static Color DarkNavyBlue
public static Color DarkOlive
public static Color DarkOliveGreen
public static Color DarkOrange
public static Color DarkPastelGreen
public static Color DarkPeach
public static Color DarkPeriwinkle
public static Color DarkPink
public static Color DarkPlum
public static Color DarkPurple
public static Color DarkRed
public static Color DarkRose
public static Color DarkRoyalBlue
public static Color DarkSage
public static Color DarkSalmon
public static Color DarkSand
public static Color DarkSeaGreen
public static Color DarkSeafoam
public static Color DarkSeafoamGreen
public static Color DarkSkyBlue
public static Color DarkSlateBlue
public static Color DarkTan
public static Color DarkTaupe
public static Color DarkTeal
public static Color DarkTurquoise
public static Color DarkViolet
public static Color DarkYellow
public static Color DarkYellowGreen
public static Color Darkblue
public static Color Darkgreen
public static Color DarkishBlue
public static Color DarkishGreen
public static Color DarkishPink
public static Color DarkishPurple
public static Color DarkishRed
public static Color DeepAqua
public static Color DeepBlue
public static Color DeepBrown
public static Color DeepGreen
public static Color DeepLavender
public static Color DeepLilac
public static Color DeepMagenta
public static Color DeepOrange
public static Color DeepPink
public static Color DeepPurple
public static Color DeepRed
public static Color DeepRose
public static Color DeepSeaBlue
public static Color DeepSkyBlue
public static Color DeepTeal
public static Color DeepTurquoise
public static Color DeepViolet
public static Color Denim
public static Color DenimBlue
public static Color Desert
public static Color Diarrhea
public static Color Dirt
public static Color DirtBrown
public static Color DirtyBlue
public static Color DirtyGreen
public static Color DirtyOrange
public static Color DirtyPink
public static Color DirtyPurple
public static Color DirtyYellow
public static Color DodgerBlue
public static Color Drab
public static Color DrabGreen
public static Color DriedBlood
public static Color DuckEggBlue
public static Color DullBlue
public static Color DullBrown
public static Color DullGreen
public static Color DullOrange
public static Color DullPink
public static Color DullPurple
public static Color DullRed
public static Color DullTeal
public static Color DullYellow
public static Color Dusk
public static Color DuskBlue
public static Color DuskyBlue
public static Color DuskyPink
public static Color DuskyPurple
public static Color DuskyRose
public static Color Dust
public static Color DustyBlue
public static Color DustyGreen
public static Color DustyLavender
public static Color DustyOrange
public static Color DustyPink
public static Color DustyPurple
public static Color DustyRed
public static Color DustyRose
public static Color DustyTeal
public static Color Earth
public static Color EasterGreen
public static Color EasterPurple
public static Color Ecru
public static Color EggShell
public static Color Eggplant
public static Color EggplantPurple
public static Color Eggshell
public static Color EggshellBlue
public static Color ElectricBlue
public static Color ElectricGreen
public static Color ElectricLime
public static Color ElectricPink
public static Color ElectricPurple
public static Color Emerald
public static Color EmeraldGreen
public static Color Evergreen
public static Color FadedBlue
public static Color FadedGreen
public static Color FadedOrange
public static Color FadedPink
public static Color FadedPurple
public static Color FadedRed
public static Color FadedYellow
public static Color Fawn
public static Color Fern
public static Color FernGreen
public static Color FireEngineRed
public static Color FlatBlue
public static Color FlatGreen
public static Color FluorescentGreen
public static Color FluroGreen
public static Color FoamGreen
public static Color Forest
public static Color ForestGreen
public static Color ForrestGreen
public static Color FrenchBlue
public static Color FreshGreen
public static Color FrogGreen
public static Color Fuchsia
public static Color Gold
public static Color Golden
public static Color GoldenBrown
public static Color GoldenRod
public static Color GoldenYellow
public static Color Goldenrod
public static Color Grape
public static Color GrapePurple
public static Color Grapefruit
public static Color Grass
public static Color GrassGreen
public static Color GrassyGreen
public static Color Green
public static Color GreenApple
public static Color GreenBlue
public static Color GreenBrown
public static Color GreenGrey
public static Color GreenSlashBlue
public static Color GreenSlashYellow
public static Color GreenTeal
public static Color GreenYellow
public static Color Greenblue
public static Color Greenish
public static Color GreenishBeige
public static Color GreenishBlue
public static Color GreenishBrown
public static Color GreenishCyan
public static Color GreenishGrey
public static Color GreenishTan
public static Color GreenishTeal
public static Color GreenishTurquoise
public static Color GreenishYellow
public static Color GreenyBlue
public static Color GreenyBrown
public static Color GreenyGrey
public static Color GreenyYellow
public static Color Grey
public static Color GreyBlue
public static Color GreyBrown
public static Color GreyGreen
public static Color GreyPink
public static Color GreyPurple
public static Color GreySlashBlue
public static Color GreySlashGreen
public static Color GreyTeal
public static Color Greyblue
public static Color Greyish
public static Color GreyishBlue
public static Color GreyishBrown
public static Color GreyishGreen
public static Color GreyishPink
public static Color GreyishPurple
public static Color GreyishTeal
public static Color GrossGreen
public static Color Gunmetal
public static Color Hazel
public static Color Heather
public static Color Heliotrope
public static Color HighlighterGreen
public static Color HospitalGreen
public static Color HotGreen
public static Color HotMagenta
public static Color HotPink
public static Color HotPurple
public static Color HunterGreen
public static Color Ice
public static Color IceBlue
public static Color IckyGreen
public static Color IndianRed
public static Color Indigo
public static Color IndigoBlue
public static Color Iris
public static Color IrishGreen
public static Color Ivory
public static Color Jade
public static Color JadeGreen
public static Color JungleGreen
public static Color KelleyGreen
public static Color KellyGreen
public static Color KermitGreen
public static Color KeyLime
public static Color Khaki
public static Color KhakiGreen
public static Color Kiwi
public static Color KiwiGreen
public static Color Lavender
public static Color LavenderBlue
public static Color LavenderPink
public static Color LawnGreen
public static Color Leaf
public static Color LeafGreen
public static Color LeafyGreen
public static Color Leather
public static Color Lemon
public static Color LemonGreen
public static Color LemonLime
public static Color LemonYellow
public static Color Lichen
public static Color LightAqua
public static Color LightAquamarine
public static Color LightBeige
public static Color LightBlue
public static Color LightBlueGreen
public static Color LightBlueGrey
public static Color LightBluishGreen
public static Color LightBrightGreen
public static Color LightBrown
public static Color LightBurgundy
public static Color LightCyan
public static Color LightEggplant
public static Color LightForestGreen
public static Color LightGold
public static Color LightGrassGreen
public static Color LightGreen
public static Color LightGreenBlue
public static Color LightGreenishBlue
public static Color LightGrey
public static Color LightGreyBlue
public static Color LightGreyGreen
public static Color LightIndigo
public static Color LightKhaki
public static Color LightLavendar
public static Color LightLavender
public static Color LightLightBlue
public static Color LightLightGreen
public static Color LightLilac
public static Color LightLime
public static Color LightLimeGreen
public static Color LightMagenta
public static Color LightMaroon
public static Color LightMauve
public static Color LightMint
public static Color LightMintGreen
public static Color LightMossGreen
public static Color LightMustard
public static Color LightNavy
public static Color LightNavyBlue
public static Color LightNeonGreen
public static Color LightOlive
public static Color LightOliveGreen
public static Color LightOrange
public static Color LightPastelGreen
public static Color LightPeaGreen
public static Color LightPeach
public static Color LightPeriwinkle
public static Color LightPink
public static Color LightPlum
public static Color LightPurple
public static Color LightRed
public static Color LightRose
public static Color LightRoyalBlue
public static Color LightSage
public static Color LightSalmon
public static Color LightSeaGreen
public static Color LightSeafoam
public static Color LightSeafoamGreen
public static Color LightSkyBlue
public static Color LightTan
public static Color LightTeal
public static Color LightTurquoise
public static Color LightUrple
public static Color LightViolet
public static Color LightYellow
public static Color LightYellowGreen
public static Color LightYellowishGreen
public static Color Lightblue
public static Color LighterGreen
public static Color LighterPurple
public static Color Lightgreen
public static Color LightishBlue
public static Color LightishGreen
public static Color LightishPurple
public static Color LightishRed
public static Color Lilac
public static Color Liliac
public static Color Lime
public static Color LimeGreen
public static Color LimeYellow
public static Color Lipstick
public static Color LipstickRed
public static Color MacaroniAndCheese
public static Color Magenta
public static Color Mahogany
public static Color Maize
public static Color Mango
public static Color Manilla
public static Color Marigold
public static Color Marine
public static Color MarineBlue
public static Color Maroon
public static Color Mauve
public static Color MediumBlue
public static Color MediumBrown
public static Color MediumGreen
public static Color MediumGrey
public static Color MediumPink
public static Color MediumPurple
public static Color Melon
public static Color Merlot
public static Color MetallicBlue
public static Color MidBlue
public static Color MidGreen
public static Color Midnight
public static Color MidnightBlue
public static Color MidnightPurple
public static Color MilitaryGreen
public static Color MilkChocolate
public static Color Mint
public static Color MintGreen
public static Color MintyGreen
public static Color Mocha
public static Color Moss
public static Color MossGreen
public static Color MossyGreen
public static Color Mud
public static Color MudBrown
public static Color MudGreen
public static Color MuddyBrown
public static Color MuddyGreen
public static Color MuddyYellow
public static Color Mulberry
public static Color MurkyGreen
public static Color Mushroom
public static Color Mustard
public static Color MustardBrown
public static Color MustardGreen
public static Color MustardYellow
public static Color MutedBlue
public static Color MutedGreen
public static Color MutedPink
public static Color MutedPurple
public static Color NastyGreen
public static Color Navy
public static Color NavyBlue
public static Color NavyGreen
public static Color NeonBlue
public static Color NeonGreen
public static Color NeonPink
public static Color NeonPurple
public static Color NeonRed
public static Color NeonYellow
public static Color NiceBlue
public static Color NightBlue
public static Color Ocean
public static Color OceanBlue
public static Color OceanGreen
public static Color Ocher
public static Color Ochre
public static Color Ocre
public static Color OffBlue
public static Color OffGreen
public static Color OffWhite
public static Color OffYellow
public static Color OldPink
public static Color OldRose
public static Color Olive
public static Color OliveBrown
public static Color OliveDrab
public static Color OliveGreen
public static Color OliveYellow
public static Color Orange
public static Color OrangeBrown
public static Color OrangePink
public static Color OrangeRed
public static Color OrangeYellow
public static Color Orangeish
public static Color Orangered
public static Color OrangeyBrown
public static Color OrangeyRed
public static Color OrangeyYellow
public static Color Orangish
public static Color OrangishBrown
public static Color OrangishRed
public static Color Orchid
public static Color Pale
public static Color PaleAqua
public static Color PaleBlue
public static Color PaleBrown
public static Color PaleCyan
public static Color PaleGold
public static Color PaleGreen
public static Color PaleGrey
public static Color PaleLavender
public static Color PaleLightGreen
public static Color PaleLilac
public static Color PaleLime
public static Color PaleLimeGreen
public static Color PaleMagenta
public static Color PaleMauve
public static Color PaleOlive
public static Color PaleOliveGreen
public static Color PaleOrange
public static Color PalePeach
public static Color PalePink
public static Color PalePurple
public static Color PaleRed
public static Color PaleRose
public static Color PaleSalmon
public static Color PaleSkyBlue
public static Color PaleTeal
public static Color PaleTurquoise
public static Color PaleViolet
public static Color PaleYellow
public static Color Parchment
public static Color PastelBlue
public static Color PastelGreen
public static Color PastelOrange
public static Color PastelPink
public static Color PastelPurple
public static Color PastelRed
public static Color PastelYellow
public static Color Pea
public static Color PeaGreen
public static Color PeaSoup
public static Color PeaSoupGreen
public static Color Peach
public static Color PeachyPink
public static Color PeacockBlue
public static Color Pear
public static Color Periwinkle
public static Color PeriwinkleBlue
public static Color Perrywinkle
public static Color Petrol
public static Color PigPink
public static Color Pine
public static Color PineGreen
public static Color Pink
public static Color PinkPurple
public static Color PinkRed
public static Color PinkSlashPurple
public static Color Pinkish
public static Color PinkishBrown
public static Color PinkishGrey
public static Color PinkishOrange
public static Color PinkishPurple
public static Color PinkishRed
public static Color PinkishTan
public static Color Pinky
public static Color PinkyPurple
public static Color PinkyRed
public static Color PissYellow
public static Color Pistachio
public static Color Plum
public static Color PlumPurple
public static Color PoisonGreen
public static Color Poo
public static Color PooBrown
public static Color Poop
public static Color PoopBrown
public static Color PoopGreen
public static Color PowderBlue
public static Color PowderPink
public static Color PrimaryBlue
public static Color PrussianBlue
public static Color Puce
public static Color Puke
public static Color PukeBrown
public static Color PukeGreen
public static Color PukeYellow
public static Color Pumpkin
public static Color PumpkinOrange
public static Color PureBlue
public static Color Purple
public static Color PurpleBlue
public static Color PurpleBrown
public static Color PurpleGrey
public static Color PurplePink
public static Color PurpleRed
public static Color PurpleSlashBlue
public static Color PurpleSlashPink
public static Color Purpleish
public static Color PurpleishBlue
public static Color PurpleishPink
public static Color Purpley
public static Color PurpleyBlue
public static Color PurpleyGrey
public static Color PurpleyPink
public static Color Purplish
public static Color PurplishBlue
public static Color PurplishBrown
public static Color PurplishGrey
public static Color PurplishPink
public static Color PurplishRed
public static Color Purply
public static Color PurplyBlue
public static Color PurplyPink
public static Color Putty
public static Color RacingGreen
public static Color RadioactiveGreen
public static Color Raspberry
public static Color RawSienna
public static Color RawUmber
public static Color ReallyLightBlue
public static Color Red
public static Color RedBrown
public static Color RedOrange
public static Color RedPink
public static Color RedPurple
public static Color RedViolet
public static Color RedWine
public static Color Reddish
public static Color ReddishBrown
public static Color ReddishGrey
public static Color ReddishOrange
public static Color ReddishPink
public static Color ReddishPurple
public static Color ReddyBrown
public static Color RichBlue
public static Color RichPurple
public static Color RobinEggBlue
public static Color RobinsEgg
public static Color RobinsEggBlue
public static Color Rosa
public static Color Rose
public static Color RosePink
public static Color RoseRed
public static Color RosyPink
public static Color Rouge
public static Color Royal
public static Color RoyalBlue
public static Color RoyalPurple
public static Color Ruby
public static Color Russet
public static Color Rust
public static Color RustBrown
public static Color RustOrange
public static Color RustRed
public static Color RustyOrange
public static Color RustyRed
public static Color Saffron
public static Color Sage
public static Color SageGreen
public static Color Salmon
public static Color SalmonPink
public static Color Sand
public static Color SandBrown
public static Color SandYellow
public static Color Sandstone
public static Color Sandy
public static Color SandyBrown
public static Color SandyYellow
public static Color SapGreen
public static Color Sapphire
public static Color Scarlet
public static Color Sea
public static Color SeaBlue
public static Color SeaGreen
public static Color Seafoam
public static Color SeafoamBlue
public static Color SeafoamGreen
public static Color Seaweed
public static Color SeaweedGreen
public static Color Sepia
public static Color Shamrock
public static Color ShamrockGreen
public static Color Shit
public static Color ShitBrown
public static Color ShitGreen
public static Color ShockingPink
public static Color SickGreen
public static Color SicklyGreen
public static Color SicklyYellow
public static Color Sienna
public static Color Silver
public static Color Sky
public static Color SkyBlue
public static Color Slate
public static Color SlateBlue
public static Color SlateGreen
public static Color SlateGrey
public static Color SlimeGreen
public static Color Snot
public static Color SnotGreen
public static Color SoftBlue
public static Color SoftGreen
public static Color SoftPink
public static Color SoftPurple
public static Color Spearmint
public static Color SpringGreen
public static Color Spruce
public static Color Squash
public static Color Steel
public static Color SteelBlue
public static Color SteelGrey
public static Color Stone
public static Color StormyBlue
public static Color Straw
public static Color Strawberry
public static Color StrongBlue
public static Color StrongPink
public static Color SunYellow
public static Color Sunflower
public static Color SunflowerYellow
public static Color SunnyYellow
public static Color SunshineYellow
public static Color Swamp
public static Color SwampGreen
public static Color Tan
public static Color TanBrown
public static Color TanGreen
public static Color Tangerine
public static Color Taupe
public static Color Tea
public static Color TeaGreen
public static Color Teal
public static Color TealBlue
public static Color TealGreen
public static Color Tealish
public static Color TealishGreen
public static Color TerraCotta
public static Color Terracota
public static Color Terracotta
public static Color TiffanyBlue
public static Color Tomato
public static Color TomatoRed
public static Color Topaz
public static Color Toupe
public static Color ToxicGreen
public static Color TreeGreen
public static Color TrueBlue
public static Color TrueGreen
public static Color Turquoise
public static Color TurquoiseBlue
public static Color TurquoiseGreen
public static Color TurtleGreen
public static Color Twilight
public static Color TwilightBlue
public static Color UglyBlue
public static Color UglyBrown
public static Color UglyGreen
public static Color UglyPink
public static Color UglyPurple
public static Color UglyYellow
public static Color Ultramarine
public static Color UltramarineBlue
public static Color Umber
public static Color Velvet
public static Color Vermillion
public static Color VeryDarkBlue
public static Color VeryDarkBrown
public static Color VeryDarkGreen
public static Color VeryDarkPurple
public static Color VeryLightBlue
public static Color VeryLightBrown
public static Color VeryLightGreen
public static Color VeryLightPink
public static Color VeryLightPurple
public static Color VeryPaleBlue
public static Color VeryPaleGreen
public static Color VibrantBlue
public static Color VibrantGreen
public static Color VibrantPurple
public static Color Violet
public static Color VioletBlue
public static Color VioletPink
public static Color VioletRed
public static Color Viridian
public static Color VividBlue
public static Color VividGreen
public static Color VividPurple
public static Color Vomit
public static Color VomitGreen
public static Color VomitYellow
public static Color WarmBlue
public static Color WarmBrown
public static Color WarmGrey
public static Color WarmPink
public static Color WarmPurple
public static Color WashedOutGreen
public static Color WaterBlue
public static Color Watermelon
public static Color WeirdGreen
public static Color Wheat
public static Color White
public static Color WindowsBlue
public static Color Wine
public static Color WineRed
public static Color Wintergreen
public static Color Wisteria
public static Color Yellow
public static Color YellowBrown
public static Color YellowGreen
public static Color YellowOchre
public static Color YellowOrange
public static Color YellowSlashGreen
public static Color YellowTan
public static Color Yellowgreen
public static Color Yellowish
public static Color YellowishBrown
public static Color YellowishGreen
public static Color YellowishOrange
public static Color YellowishTan
public static Color YellowyBrown
public static Color YellowyGreen
```

## ScottPlot.Palettes

### `public class Amber : IPalette`
<!-- Palettes\Amber.cs -->

```csharp
public class Amber : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class Aurora : IPalette`
<!-- Palettes\Aurora.cs -->

```csharp
public class Aurora : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class Building : IPalette`
<!-- Palettes\Building.cs -->

```csharp
public class Building : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class Category10 : IPalette`
<!-- Palettes\Category10.cs -->

```csharp
public class Category10 : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class Category20 : IPalette`
<!-- Palettes\Category20.cs -->

```csharp
public class Category20 : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class ColorblindFriendly : IPalette`
<!-- Palettes\ColorblindFriendly.cs -->

```csharp
public class ColorblindFriendly : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class ColorblindFriendlyDark : IPalette`
<!-- Palettes\ColorblindFriendlyDark.cs -->
> Inverted version of which is useful for plots with dark backgrounds

```csharp
public class ColorblindFriendlyDark : IPalette
public string Name
public string Description
public Color[] Colors
public Color GetColor(int index)
```

### `public class Custom : IPalette`
<!-- Palettes\Custom.cs -->

```csharp
public class Custom : IPalette
public Color[] Colors { get; }
public string Name { get; }
public string Description { get; }
public Custom(IEnumerable<Color> colors, string? name, string? description = null)
public Custom(string[] hex, string? name = null, string? description = null) : this(Color.FromHex(hex), name, description)
public Color GetColor(int index)
```

### `public class Dark : IPalette`
<!-- Palettes\Dark.cs -->

```csharp
public class Dark : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class DarkPastel : IPalette`
<!-- Palettes\DarkPastel.cs -->

```csharp
public class DarkPastel : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class Frost : IPalette`
<!-- Palettes\Frost.cs -->

```csharp
public class Frost : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class LightOcean : IPalette`
<!-- Palettes\LightOcean.cs -->

```csharp
public class LightOcean : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class LightSpectrum : IPalette`
<!-- Palettes\LightSpectrum.cs -->

```csharp
public class LightSpectrum : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class Microcharts : IPalette`
<!-- Palettes\Microcharts.cs -->

```csharp
public class Microcharts : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class Nero : IPalette`
<!-- Palettes\Nero.cs -->

```csharp
public class Nero : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class Nord : IPalette`
<!-- Palettes\Nord.cs -->

```csharp
public class Nord : IPalette
public string Name { get; }
public string Description
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class Normal : IPalette`
<!-- Palettes\Normal.cs -->

```csharp
public class Normal : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class OneHalf : IPalette`
<!-- Palettes\OneHalf.cs -->

```csharp
public class OneHalf : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class OneHalfDark : IPalette`
<!-- Palettes\OneHalfDark.cs -->

```csharp
public class OneHalfDark : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class PastelWheel : IPalette`
<!-- Palettes\PastelWheel.cs -->

```csharp
public class PastelWheel : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class Penumbra : IPalette`
<!-- Palettes\Penumbra.cs -->

```csharp
public class Penumbra : IPalette
public string Name { get; }
public string Description
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class PolarNight : IPalette`
<!-- Palettes\PolarNight.cs -->

```csharp
public class PolarNight : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class Redness : IPalette`
<!-- Palettes\Redness.cs -->

```csharp
public class Redness : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class SnowStorm : IPalette`
<!-- Palettes\SnowStorm.cs -->

```csharp
public class SnowStorm : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class SummerSplash : IPalette`
<!-- Palettes\SummerSplash.cs -->

```csharp
public class SummerSplash : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

### `public class Tsitsulin : IPalette`
<!-- Palettes\Tsitsulin.cs -->

```csharp
public class Tsitsulin : IPalette
public string Name { get; }
public string Description { get; }
public Color[] Colors { get; }
public Color GetColor(int index)
```

## ScottPlot.Panels

### `public class ColorBar(IHasColorAxis source, Edge edge = Edge.Right) : IPanel`
<!-- Panels\ColorBar.cs -->
> An axis panel which displays a colormap and range of values

```csharp
public class ColorBar(IHasColorAxis source, Edge edge = Edge.Right) : IPanel
public bool IsVisible { get, set; }
public IHasColorAxis Source { get, set; }
public Edge Edge { get, set; }
// Axis (spine, ticks, label, etc) for the colorbar
public IAxis Axis { get, set; }
// Thickness of the colorbar image (in pixels)
public float Width { get, set; }
// Title for the colorbar, displayed outside the ticks.
public string Label { get, set; }
// Title for the colorbar, displayed outside the ticks.
public LabelStyle LabelStyle
public bool ShowDebugInformation { get, set; }
public float MinimumSize { get, set; }
public float MaximumSize { get, set; }
public float Measure(Paint paint)
// Return a rectangle encapsulating the colormap bitmap plus the axis and ticks.
public PixelRect GetPanelRect(PixelRect dataRect, float size, float offset, Paint paint)
public void Render(RenderPack rp, float size, float offset)
```

### `public class LegendPanel(Legend legend) : PanelBase`
<!-- Panels\LegendPanel.cs -->

```csharp
public class LegendPanel(Legend legend) : PanelBase
public Legend Legend { get; }
public Alignment Alignment { get, set; }
public PixelPadding Padding { get, set; }
public override float Measure(Paint paint)
public override void Render(RenderPack rp, float size, float offset)
```

### `public abstract class PanelBase : IPanel`
<!-- Panels\PanelBase.cs -->

```csharp
public abstract class PanelBase : IPanel
public bool IsVisible { get, set; }
public Edge Edge { get, set; }
public bool ShowDebugInformation { get, set; }
public float MinimumSize { get, set; }
public float MaximumSize { get, set; }
public abstract float Measure(Paint paint)
public abstract void Render(RenderPack rp, float size, float offset)
public PixelRect GetPanelRect(PixelRect dataRect, float size, float offset, Paint paint)
```

### `public class TitlePanel : IPanel`
<!-- Panels\TitlePanel.cs -->

```csharp
public class TitlePanel : IPanel
public bool IsVisible { get, set; }
public Edge Edge
public bool ShowDebugInformation { get, set; }
public float MinimumSize { get, set; }
public float MaximumSize { get, set; }
// Enable this to center the panel using the full width of the figure rather than centering it over the width of the data area.
public bool FullFigureCenter { get, set; }
public TitlePanel()
public LabelStyle Label { get; }
// Extra space to add above the title text so the title does not touch the edge of the image
public float VerticalPadding = 10
public PixelRect GetPanelRect(PixelRect dataRect, float size, float offset, Paint paint)
public float Measure(Paint paint)
public void Render(RenderPack rp, float size, float offset)
```

## ScottPlot.PathStrategies

### `public static class Arrows // TODO: use an interface to let users inject custom logic`
<!-- PathStrategies\Arrows.cs -->

```csharp
public static class Arrows // TODO: use an interface to let users inject custom logic
public static SKPath GetPath(IEnumerable<RootedPixelVector> vectors, ArrowStyle style, float maxBladeWidth = float.PositiveInfinity)
```

### `public class CubicSpline : IPathStrategy`
<!-- PathStrategies\CubicSpline.cs -->
> Connect points with Catmull-Rom cubic splines, see https://doi.org/10.1007/s42979-021-00770-x NaN values will be skipped, producing a gap in the path.

```csharp
public class CubicSpline : IPathStrategy
public double Tension { get, set; }
public SKPath GetPath(IEnumerable<Pixel> pixels)
```

### `public class QuadHalfPoint : IPathStrategy`
<!-- PathStrategies\QuadHalfPoint.cs -->
> Connect points with curved lines which ease into and out of the midpoint between each pair. This strategy does not "overshoot" points in the Y direction.

```csharp
public class QuadHalfPoint : IPathStrategy
public SKPath GetPath(IEnumerable<Pixel> pixels)
```

### `public class Straight : IPathStrategy`
<!-- PathStrategies\Straight.cs -->
> Connect points with straight lines. NaN values will be skipped, producing a gap in the path.

```csharp
public class Straight : IPathStrategy
public SKPath GetPath(IEnumerable<Pixel> pixels)
```

## ScottPlot.PlotStyles

### `public class Dark : PlotStyle`
<!-- PlotStyles\Dark.cs -->

```csharp
public class Dark : PlotStyle
public Dark()
```

### `public class Light : PlotStyle`
<!-- PlotStyles\Light.cs -->

```csharp
public class Light : PlotStyle
public Light()
```

## ScottPlot.Plottables

### `public class Annotation : LabelStyleProperties, IPlottable, IHasLabel`
<!-- Plottables\Annotation.cs -->

```csharp
public class Annotation : LabelStyleProperties, IPlottable, IHasLabel
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public override LabelStyle LabelStyle { get, set; }
public LabelStyle Label { get, set; }
public string Text { get, set; }
public Alignment Alignment { get, set; }
public PixelOffset PixelOffset { get, set; }
public float OffsetX { get, set; }
public float OffsetY { get, set; }
// The annotation will be placed inside this fractional portion of the data area according to and
public FractionRect FractionRect { get, set; }
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class Arrow : IPlottable, IHasArrow, IHasLegendText`
<!-- Plottables\Arrow.cs -->

```csharp
public class Arrow : IPlottable, IHasArrow, IHasLegendText
public Coordinates Base { get, set; }
public Coordinates Tip { get, set; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public string LegendText { get, set; }
public ArrowStyle ArrowStyle { get, set; }
public Color ArrowLineColor { get, set; }
public float ArrowLineWidth { get, set; }
public Color ArrowFillColor { get, set; }
public float ArrowMinimumLength { get, set; }
public float ArrowMaximumLength { get, set; }
public float ArrowOffset { get, set; }
public ArrowAnchor ArrowAnchor { get, set; }
public float ArrowWidth { get, set; }
public float ArrowheadAxisLength { get, set; }
public float ArrowheadLength { get, set; }
public float ArrowheadWidth { get, set; }
public string Label { get, set; }
public Color ArrowColor { get, set; }
public Color Color { get, set; }
public float Offset { get, set; }
public float MinimumLength { get, set; }
public float LineWidth { get, set; }
public LineStyle LineStyle { get, set; }
public AxisLimits GetAxisLimits()
public IArrowShape ArrowShape { get, set; }
public virtual void Render(RenderPack rp)
```

### `public abstract class AxisLine : LabelStyleProperties, IPlottable, IRenderLast, IHasLine, IHasLegendText`
<!-- Plottables\AxisLine.cs -->

```csharp
public abstract class AxisLine : LabelStyleProperties, IPlottable, IRenderLast, IHasLine, IHasLegendText
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public override LabelStyle LabelStyle { get, set; }
public string Text { get, set; }
public string LegendText { get, set; }
public Alignment? ManualLabelAlignment { get, set; }
public Alignment? TextAlignment { get, set; }
public LabelStyle Label { get, set; }
public float FontSize { get, set; }
public bool FontBold { get, set; }
public string FontName { get, set; }
public Color FontColor { get, set; }
public Color TextColor { get, set; }
public Color TextBackgroundColor { get, set; }
public float TextRotation { get, set; }
public float TextSize { get, set; }
public bool LabelOppositeAxis { get, set; }
public bool IsDraggable { get, set; }
public bool ExcludeFromLegend { get, set; }
public bool EnableAutoscale { get, set; }
public Color Color { get, set; }
public double Position { get, set; }
public IEnumerable<LegendItem> LegendItems { get; }
public abstract bool IsUnderMouse(CoordinateRect rect)
public abstract AxisLimits GetAxisLimits()
public abstract void Render(RenderPack rp)
public abstract void RenderLast(RenderPack rp)
```

### `public abstract class AxisSpan : IPlottable, IHasLine, IHasFill, IHasLegendText`
<!-- Plottables\AxisSpan.cs -->

```csharp
public abstract class AxisSpan : IPlottable, IHasLine, IHasFill, IHasLegendText
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public LabelStyle Label { get, set; }
public string LegendText { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public FillStyle FillStyle { get, set; }
public Color FillColor { get, set; }
public Color FillHatchColor { get, set; }
public IHatch? FillHatch { get, set; }
public IEnumerable<LegendItem> LegendItems
public bool EnableAutoscale { get, set; }
public abstract AxisLimits GetAxisLimits()
public abstract void Render(RenderPack rp)
public bool IsDraggable { get, set; }
public bool IsResizable { get, set; }
public abstract AxisSpanUnderMouse? UnderMouse(CoordinateRect rect)
public bool IsUnderMouse(CoordinateRect rect)
public abstract void DragTo(AxisSpanUnderMouse start, Coordinates mouseNow)
```

### `public class BarPlot : IPlottable, IHasLegendText, IRenderLast`
<!-- Plottables\BarPlot.cs -->
> Holds a collection of individually styled bars

```csharp
public class BarPlot : IPlottable, IHasLegendText, IRenderLast
public string Label { get, set; }
public string LegendText { get, set; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public List<Bar> Bars { get; }
public bool LabelsOnTop { set; }
public LabelStyle ValueLabelStyle { get, set; }
// Text displayed above each bar, typically containing string representation of the value. This label is displayed below the bar for negative bars.
public string ValueLabel { get, set; }
// Apply a fill color to all bars
public Color Color { set; }
// Define orientation for all bars
public bool Horizontal { set; }
public BarPlot(List<Bar> bars)
public IEnumerable<LegendItem> LegendItems { get; }
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
public virtual void RenderLast(RenderPack rp)
```

### `public class Benchmark : LabelStyleProperties, IPlottable`
<!-- Plottables\Benchmark.cs -->

```csharp
public class Benchmark : LabelStyleProperties, IPlottable
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public override LabelStyle LabelStyle { get, set; }
public virtual void Render(RenderPack rp)
```

### `public class BoxPlot : IPlottable, IHasLegendText`
<!-- Plottables\BoxPlot.cs -->
> Displays 1 or more boxes all styled the same

```csharp
public class BoxPlot : IPlottable, IHasLegendText
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public string Label { get, set; }
public string LegendText { get, set; }
public IEnumerable<LegendItem> LegendItems
public readonly List<Box> Boxes = []
public Color FillColor { set; }
public Color LineColor { set; }
public float LineWidth { set; }
public Color StrokeColor { set; }
public float StrokeWidth { set; }
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class Bracket : IPlottable`
<!-- Plottables\Bracket.cs -->

```csharp
public class Bracket : IPlottable
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public Coordinates Point1 { get, set; }
public Coordinates Point2 { get, set; }
// Controls whether the tip of the bracket is counter-clockwise from the line formed by the bracket base.
public bool LabelCounterClockwise { get, set; }
// Size of the small lines (in pixels) placed the edges of the bracket and between the center of the bracket and the label
public float EdgeLength = 5
// Text displayed near the center of the bracket
public string Text { get, set; }
public LineStyle LineStyle { get, set; }
public LabelStyle LabelStyle { get, set; }
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class Callout : LabelStyleProperties, IPlottable, IHasArrow, IHasLabel`
<!-- Plottables\Callout.cs -->

```csharp
public class Callout : LabelStyleProperties, IPlottable, IHasArrow, IHasLabel
public Text LabelPlottable { get; }
public Arrow ArrowPlottable { get; }
public override LabelStyle LabelStyle { get, set; }
public string Text { get, set; }
public ArrowStyle ArrowStyle { get, set; }
public Color ArrowLineColor { get, set; }
public float ArrowLineWidth { get, set; }
public Color ArrowFillColor { get, set; }
public float ArrowMinimumLength { get, set; }
public float ArrowMaximumLength { get, set; }
public float ArrowOffset { get, set; }
public ArrowAnchor ArrowAnchor { get, set; }
public float ArrowWidth { get, set; }
public float ArrowheadAxisLength { get, set; }
public float ArrowheadLength { get, set; }
public float ArrowheadWidth { get, set; }
public Color ArrowColor { get, set; }
public Color TextColor { get, set; }
public bool Bold { get, set; }
public float FontSize { get, set; }
public Color TextBorderColor { get, set; }
public float TextBorderWidth { get, set; }
public Color TextBackgroundColor { get, set; }
public Coordinates TextCoordinates { get, set; }
public Pixel TextPixel { get, set; }
public Coordinates TipCoordinates { get, set; }
public Pixel TipPixel { get, set; }
public PixelRect LastRenderRect
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
// Calculates the attachment point on the label based on the closest distance from the given pixel location.
public Coordinates CalculateClosestAttachPoint(Paint paint)
public virtual void Render(RenderPack rp)
```

### `public class CandlestickPlot(IOHLCSource data) : IPlottable`
<!-- Plottables\CandlestickPlot.cs -->

```csharp
public class CandlestickPlot(IOHLCSource data) : IPlottable
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IOHLCSource Data { get; }
// X position of candles is sourced from the OHLC's DateTime by default. If this option is enabled, X position will be an ascending integers starting at 0 with no gaps.
public bool Sequential { get, set; }
// Fractional width of the candle symbol relative to its time span
public double SymbolWidth = .8
public LineStyle RisingLineStyle { get; }
public LineStyle FallingLineStyle { get; }
public FillStyle RisingFillStyle { get; }
public FillStyle FallingFillStyle { get; }
public Color RisingColor { set; }
public Color FallingColor { set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public CoordinateRange GetPriceRangeInView()
public (int index, OHLC ohlc)? GetOhlcNearX(double x)
public virtual void Render(RenderPack rp)
```

### `public class ContourLines : IPlottable, IHasLine`
<!-- Plottables\ContourLines.cs -->

```csharp
public class ContourLines : IPlottable, IHasLine
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public List<ContourLine> Lines { get, set; }
public LineStyle LineStyle { get, set; }
public LabelStyle LabelStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public IColormap? Colormap { get, set; }
public double MinZ { get, set; }
public double MaxZ { get, set; }
// If defined, contour lines will be drawn at this height and will be ignored.
public int ContourLineCount = 10
// If defined, contour lines will be drawn at this height and will be ignored.
public double[]? ContourLineLevels = null
// Update contour lines from arbitrarily placed data points.
public void Update(IEnumerable<Coordinates3d> coordinates)
// Update contour lines from a rectangular grid of coordinates
public void Update(Coordinates3d[,] coordinateGrid)
public virtual void Render(RenderPack rp)
```

### `public class Coxcomb : PieBase`
<!-- Plottables\Coxcomb.cs -->

```csharp
public class Coxcomb : PieBase
public IStarAxis StarAxis { get, set; }
public Coxcomb(IList<PieSlice> slices)
public override AxisLimits GetAxisLimits()
public override void Render(RenderPack rp)
```

### `public class Crosshair : IPlottable, IRenderLast, IHasMarker`
<!-- Plottables\Crosshair.cs -->

```csharp
public class Crosshair : IPlottable, IRenderLast, IHasMarker
public HorizontalLine HorizontalLine { get; }
public VerticalLine VerticalLine { get; }
public Coordinates Position { get, set; }
public double X { get, set; }
public double Y { get, set; }
public float FontSize { set; }
public bool FontBold { set; }
public string FontName { set; }
public Color TextColor { set; }
public Color TextBackgroundColor { set; }
public Color LineColor { set; }
public float LineWidth { set; }
public LinePattern LinePattern { set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
public LineStyle LineStyle { get, set; }
public Color FontColor
public bool EnableAutoscale { get, set; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
public void RenderLast(RenderPack rp)
```

### `public class DataLogger(List<Coordinates>? coordinates = null) : IPlottable, IManagesAxisLimits, IHasLine, IHasMarker, IHasLegendText`
<!-- Plottables\DataLogger.cs -->

```csharp
public class DataLogger(List<Coordinates>? coordinates = null) : IPlottable, IManagesAxisLimits, IHasLine, IHasMarker, IHasLegendText
public DataLoggerSource Data { get; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IAxisLimitManager AxisManager { get, set; }
public bool Rotated { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
public bool HasNewData
public bool InvertX { get, set; }
public bool InvertY { get, set; }
// The style of lines to use when connecting points.
public ConnectStyle ConnectStyle { get, set; }
public Color Color { get, set; }
public double Period { get, set; }
public string Label { get, set; }
public string LegendText { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
// Get the data point nearest to the given mouse location.
public DataPoint GetNearest(Coordinates mouseLocation, PixelRect dataRect, float maxDistance = 15)
// Get the data point nearest to the given mouse location (only considering X values).
public DataPoint GetNearestX(Coordinates mouseLocation, PixelRect dataRect, float maxDistance = 15)
public virtual void Render(RenderPack rp)
public void Add(Coordinates coordinates)
public void Add(double x, double y)
public void Add(double y)
public void Add(IEnumerable<double> ys)
public void Add(double[] xs, double[] ys)
public void Add(Coordinates[] coordinates)
public void Clear()
public void UpdateAxisLimits(Plot plot)
public bool ManageAxisLimits { get, set; }
// Automatically expand the axis as needed to ensure the full dataset is visible before each render.
public void ViewFull()
// Automatically adjust the axis limits to track the newest data as it comes in. The axis limits will appear to "jump" when new data runs off the screen.
public void ViewJump(double width = 1000, double paddingFraction = .5)
// Automatically adjust the axis limits to track the newest data as it comes in. The axis limits will appear to "slide" continuously as new data is added.
public void ViewSlide(double width = 1000)
```

### `public class DataStreamer : IPlottable, IManagesAxisLimits, IHasLine, IHasLegendText, IHasMarker`
<!-- Plottables\DataStreamer.cs -->

```csharp
public class DataStreamer : IPlottable, IManagesAxisLimits, IHasLine, IHasLegendText, IHasMarker
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public string Label { get, set; }
public string LegendText { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
public bool FillY { get, set; }
public double FillYValue { get, set; }
public Color FillYAboveColor { get, set; }
public Color FillYBelowColor { get, set; }
public Color FillYColor { get, set; }
public Color Color { get, set; }
public DataStreamerSource Data { get, set; }
public int Count
public int CountTotal
public double Period { get, set; }
// Returns true if data has been added since the last render
public bool HasNewData
// If enabled, axis limits will be adjusted automatically if new data runs off the screen.
public bool ManageAxisLimits { get, set; }
public bool ContinuouslyAutoscale { get, set; }
// Logic for displaying the fixed-length Y values in
public DataViews.IDataStreamerView Renderer { get, set; }
public DataStreamer(Plot plot, double[] data)
// Shift in a new Y value
public void Add(double value)
public void Add(double[] ys)
// Shift in a collection of new Y values
public void AddRange(IEnumerable<double> values)
// Clear the buffer by setting all Y points to the given value
public void Clear(double value = 0)
// Display the data using a view where new data overlaps old data from left to right.
public void ViewWipeRight(double blankFraction = 0)
// Display the data using a view where new data overlaps old data from right to left.
public void ViewWipeLeft()
// Display the data using a view that continuously shifts data to the left, placing the newest data on the right.
public void ViewScrollLeft()
// Display the data using a view that continuously shifts data to the right, placing the newest data on the left.
public void ViewScrollRight()
// Display the data using a custom rendering function
public void ViewCustom(DataViews.IDataStreamerView view)
public AxisLimits GetAxisLimits()
public void UpdateAxisLimits(Plot plot)
public virtual void Render(RenderPack rp)
```

### `public class DataStreamerXY(int capacity) : IPlottable, IManagesAxisLimits, IHasLine, IHasLegendText, IHasMarker`
<!-- Plottables\DataStreamerXY.cs -->

```csharp
public class DataStreamerXY(int capacity) : IPlottable, IManagesAxisLimits, IHasLine, IHasLegendText, IHasMarker
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public string LegendText { get, set; }
public bool ManageAxisLimits { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
public Color Color { get, set; }
public AxisLimits GetAxisLimits()
public void UpdateAxisLimits(Plot plot)
public void Add(double x, double y)
public void Add(DateTime x, double y)
public void Add(Coordinates point)
public virtual void Render(RenderPack rp)
```

### `public class DraggablePlottableDecorator : HittablePlottableDecorator`
<!-- Plottables\DraggablePlottableDecorator.cs -->

```csharp
public class DraggablePlottableDecorator : HittablePlottableDecorator
public DraggablePlottableDecorator(IPlottable plottable) : base(plottable)
public void StartDrag(Coordinates start)
public void DragTo(Coordinates to)
```

### `public class Ellipse : IPlottable, IHasLine, IHasFill, IHasLegendText`
<!-- Plottables\Ellipse.cs -->

```csharp
public class Ellipse : IPlottable, IHasLine, IHasFill, IHasLegendText
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public FillStyle FillStyle { get, set; }
public Color FillColor { get, set; }
public Color FillHatchColor { get, set; }
public IHatch? FillHatch { get, set; }
public string Label { get, set; }
public string LegendText { get, set; }
public Coordinates Center = Coordinates.Origin
// Horizontal radius (axis units)
public double RadiusX { get, set; }
// Horizontal radius (axis units)
public double RadiusY { get, set; }
// Horizontal inner annular radius (axis units)
public double InnerRadiusX { get, set; }
// Horizontal inner annular radius (axis units)
public double InnerRadiusY { get, set; }
// Rotation of the ellipse (degrees)
public Angle Rotation { get, set; }
public bool IsAnnulus
// if false, it is an elliptical arc If true, it is an elliptical sector;
public bool IsSector { get, set; }
// Start angle of elliptical arc or elliptical sector (degrees)
public Angle StartAngle { get, set; }
// Sweep angle of elliptical arc or elliptical sector (degrees)
public Angle SweepAngle { get, set; }
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class ErrorBar : IPlottable, IHasLine, IHasLegendText`
<!-- Plottables\ErrorBar.cs -->

```csharp
public class ErrorBar : IPlottable, IHasLine, IHasLegendText
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IReadOnlyList<double> Xs { get, set; }
public IReadOnlyList<double> Ys { get, set; }
public IReadOnlyList<double>? XErrorPositive { get, set; }
public IReadOnlyList<double>? XErrorNegative { get, set; }
public IReadOnlyList<double>? YErrorPositive { get, set; }
public IReadOnlyList<double>? YErrorNegative { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public float CapSize { get, set; }
public Color Color { get, set; }
public ErrorBar(IReadOnlyList<double> xs, IReadOnlyList<double> ys, IReadOnlyList<double>? xErrorsPositive, IReadOnlyList<double>? xErrorsNegative, IReadOnlyList<double>? yErrorsPositive, IReadOnlyList<double>? yErrorsNegative)
public IEnumerable<LegendItem> LegendItems
public string Label { get, set; }
public string LegendText { get, set; }
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class FillY : IPlottable, IHasLine, IHasFill, IHasMarker, IHasLegendText`
<!-- Plottables\FillY.cs -->

```csharp
public class FillY : IPlottable, IHasLine, IHasFill, IHasMarker, IHasLegendText
public string Label { get, set; }
public string LegendText { get, set; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public FillStyle FillStyle { get, set; }
public Color FillColor { get, set; }
public Color FillHatchColor { get, set; }
public IHatch? FillHatch { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
// Creates an empty RangePlot plot, call SetDataSource() to set the coordinates.
public FillY()
// Creates a RangePlot plot from two scatter plots.
public FillY(Scatter scatter1, Scatter scatter2)
public void SetDataSource(ICollection<(double X, double Top, double Bottom)> items)
public void SetDataSource<T>(ICollection<T> items, Func<T, (double X, double Top, double Bottom)> coordinateSolver)
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class FinancialTimeAxis(DateTime[] dateTimes) : IPlottable`
<!-- Plottables\FinancialTimeAxis.cs -->
> This plottable renders date tick labels for financial charts where data is displayed sequentially along the horizontal axis despite DateTimes not being evenly spaced (e.g., data may include gaps)

```csharp
public class FinancialTimeAxis(DateTime[] dateTimes) : IPlottable
public DateTime[] DateTimes { get, set; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public LabelStyle LabelStyle { get, set; }
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class FloatingAxis : IPlottable`
<!-- Plottables\FloatingAxis.cs -->
> This plottable renders an axis line, ticks, and tick labels inside the data area

```csharp
public class FloatingAxis : IPlottable
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public bool IsVertical { get; }
public ITickGenerator TickGenerator { get; }
public double Position = 0.5
public FloatingAxis(IXAxis axis)
public FloatingAxis(IYAxis axis)
public virtual void Render(RenderPack rp)
public void RenderVerticalAxis(RenderPack rp)
public void RenderHorizontalAxis(RenderPack rp)
```

### `public class FunctionPlot(IFunctionSource source) : IPlottable, IHasLine, IHasLegendText`
<!-- Plottables\FunctionPlot.cs -->

```csharp
public class FunctionPlot(IFunctionSource source) : IPlottable, IHasLine, IHasLegendText
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public string Label { get, set; }
public string LegendText { get, set; }
public double GetY(double x)
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public double MinX { get, set; }
public double MaxX { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class Heatmap(double[,] intensities) : IPlottable, IHasColorAxis`
<!-- Plottables\Heatmap.cs -->

```csharp
public class Heatmap(double[,] intensities) : IPlottable, IHasColorAxis
// Data values for the heatmap. must be called after changing this array or editing its values.
public double[,] Intensities { get, set; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IColormap Colormap { get, set; }
public Alignment CellAlignment { get, set; }
public CoordinateRect? Extent { get, set; }
// If defined, the heatmap will be rendered within the edges of this rectangle.
public CoordinateRect? Rectangle { set; }
// If defined, the this rectangle sets the axis boundaries of heatmap data. Note that the actual heatmap area is 1 cell larger than this rectangle.
public CoordinateRect? Position { get, set; }
public bool FlipVertically { get, set; }
public bool FlipHorizontally { get, set; }
public bool FlipColumns { get, set; }
public bool FlipRows { get, set; }
public bool Smooth { get, set; }
// Actual extent of the heatmap bitmap after alignment has been applied
public CoordinateRect GetAlignedExtent()
// Width of a single cell from the heatmap (in coordinate units)
public double CellWidth { get, set; }
// Height of a single cell from the heatmap (in coordinate units)
public double CellHeight { get, set; }
// Defines what color will be used to fill cells containing NaN.
public Color NaNCellColor { get, set; }
// If present, this array defines transparency for each cell in the heatmap. Values range from 0 (transparent) through 255 (opaque).
public byte[,]? AlphaMap { get, set; }
// Controls the opacity of the entire heatmap from 0 (transparent) to 1 (opaque)
public double Opacity { get, set; }
// Change this to customize how heatmap values are rendered
public IRenderStrategy RenderStrategy { get, set; }
// Regenerate the image using the present settings and data in
public void Update()
public AxisLimits GetAxisLimits()
// Return the position in the array beneath the given point
public (int x, int y) GetIndexes(Coordinates coordinates)
// Return the value of the cell beneath the given point. Returns NaN if the point is outside the heatmap area.
public double GetValue(Coordinates coordinates)
public IEnumerable<LegendItem> LegendItems
public Range GetRange()
// Range of values spanned by the data the last time it was updated
public Range DataRange { get, set; }
// If supplied, the colormap will span this range of values
public Range? ManualRange { get, set; }
public virtual void Render(RenderPack rp)
```

### `public interface IRenderStrategy`（嵌套于 Heatmap）

```csharp
public interface IRenderStrategy
```

### `public static class RenderStrategies`（嵌套于 Heatmap）

```csharp
public static class RenderStrategies
```

### `public class HistogramBars : IPlottable`
<!-- Plottables\HistogramBars.cs -->

```csharp
public class HistogramBars : IPlottable
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public Bar[] Bars { get, set; }
public LabelStyle LabelStyle { get, set; }
public double BarWidthFraction { set; }
public HistogramBars(Histogram histogram)
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class HittablePlottableDecorator : IPlottable, IDisposable`
<!-- Plottables\HittablePlottableDecorator.cs -->
> This class wraps an to give it a pixel-based hit detection map that can be used for mouse interaction

```csharp
public class HittablePlottableDecorator : IPlottable, IDisposable
public IPlottable Source { get; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public HittablePlottableDecorator(IPlottable plottable)
// Returns true if the plottable is within pixels of the given
public bool IsHit(Pixel pixel, float radius)
public virtual void Render(RenderPack rp)
public void Dispose()
```

### `public class HorizontalLine : AxisLine`
<!-- Plottables\HorizontalLine.cs -->
> A line at a defined Y position that spans the entire horizontal space of the data area

```csharp
public class HorizontalLine : AxisLine
public double Y { get, set; }
public double Minimum { get, set; }
public double Maximum { get, set; }
public HorizontalLine()
public override bool IsUnderMouse(CoordinateRect rect)
public override AxisLimits GetAxisLimits()
public override void Render(RenderPack rp)
public override void RenderLast(RenderPack rp)
```

### `public class HorizontalSpan : AxisSpan, IPlottable`
<!-- Plottables\HorizontalSpan.cs -->
> A horizontal span marks the full vertical range between two horizontal values

```csharp
public class HorizontalSpan : AxisSpan, IPlottable
public double X1 { get, set; }
public double X2 { get, set; }
public CoordinateRange XRange
public double Left { get, set; }
public double Right { get, set; }
public override AxisLimits GetAxisLimits()
public override void Render(RenderPack rp)
public override AxisSpanUnderMouse? UnderMouse(CoordinateRect rect)
public override void DragTo(AxisSpanUnderMouse spanUnderMouse, Coordinates mouseNow)
```

### `public class ImageMarker : IPlottable`
<!-- Plottables\ImageMarker.cs -->

```csharp
public class ImageMarker : IPlottable
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public ScottPlot.Image? Image { get, set; }
public Coordinates Location { get, set; }
public float Scale { get, set; }
public bool AntiAlias { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class ImageRect() : IPlottable`
<!-- Plottables\ImageRect.cs -->

```csharp
public class ImageRect() : IPlottable
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public Image? Image { get, set; }
public CoordinateRect Rect { get, set; }
public bool AntiAlias { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class IsoLines : IPlottable, IHasLine`
<!-- Plottables\IsoLines.cs -->

```csharp
public class IsoLines : IPlottable, IHasLine
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public LabelStyle TickLabelStyle = new()
public bool RotateLabels { get, set; }
public readonly List<(double, string)> ManualPositions = []
public Func<double, string> TickLabelFormatter = DefaultTickFormatter
public bool ExteriorTickLabels { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public static string DefaultTickFormatter(double yIntercept)
public virtual void Render(RenderPack rp)
```

### `public class LinePlot : IPlottable, IHasLine, IHasMarker, IHasLegendText`
<!-- Plottables\LinePlot.cs -->

```csharp
public class LinePlot : IPlottable, IHasLine, IHasMarker, IHasLegendText
public Coordinates Start { get, set; }
public Coordinates End { get, set; }
public CoordinateLine Line { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
public string Label { get, set; }
public string LegendText { get, set; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public bool LineOnTop { get, set; }
public bool MarkersOnTop { get, set; }
public Color Color { get, set; }
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class LollipopPlot : IPlottable, IHasLine, IHasMarker, IGetNearest`
<!-- Plottables\LollipopPlot.cs -->

```csharp
public class LollipopPlot : IPlottable, IHasLine, IHasMarker, IGetNearest
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public string LegendText { get, set; }
public IEnumerable<LegendItem> LegendItems
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
public Color Color { get, set; }
public IEnumerable<Coordinates> Coordinates { get, set; }
public Orientation Orientation { get, set; }
public double BaseValue { get, set; }
public LollipopPlot(IEnumerable<Coordinates> coordinates)
public AxisLimits GetAxisLimits()
public DataPoint GetNearest(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public virtual void Render(RenderPack rp)
```

### `public class Marker : IPlottable, IHasMarker, IHasLegendText`
<!-- Plottables\Marker.cs -->

```csharp
public class Marker : IPlottable, IHasMarker, IHasLegendText
public double X { get, set; }
public double Y { get, set; }
public Coordinates Location { get, set; }
public Coordinates Position { get, set; }
public Coordinates Coordinates { get, set; }
public string Label { get, set; }
public string LegendText { get, set; }
public bool IsVisible { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
public float Size { get, set; }
public float LineWidth { set; }
public MarkerShape Shape { get, set; }
public Color Color { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class Markers(IScatterSource data) : IPlottable, IHasMarker, IHasLegendText`
<!-- Plottables\Markers.cs -->

```csharp
public class Markers(IScatterSource data) : IPlottable, IHasMarker, IHasLegendText
public string Label { get, set; }
public string LegendText { get, set; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
public IScatterSource Data { get; }
public Color Color { get, set; }
public IColormap? Colormap { get, set; }
public AxisLimits GetAxisLimits()
public IEnumerable<LegendItem> LegendItems
public virtual void Render(RenderPack rp)
```

### `public class OhlcPlot(IOHLCSource data) : IPlottable`
<!-- Plottables\OHLCPlot.cs -->

```csharp
public class OhlcPlot(IOHLCSource data) : IPlottable
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
// X position of each symbol is sourced from the OHLC's DateTime by default. If this option is enabled, X position will be an ascending integers starting at 0 with no gaps.
public bool Sequential { get, set; }
// Fractional width of the OHLC symbol relative to its time span
public double SymbolWidth = .8
public LineStyle RisingStyle { get; }
public LineStyle FallingStyle { get; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class Phasor : IPlottable, IHasArrow, IHasLegendText`
<!-- Plottables\Phasor.cs -->
> A Phasor plot marks a collection of points in polar space using an arrow with its base centered at the origin.

```csharp
public class Phasor : IPlottable, IHasArrow, IHasLegendText
// A collection of points in polar space
public List<PolarCoordinates> Points { get; }
// If populated, will be labeled with these strings
public List<string> Labels { get; }
// Style for arrow labels defined in
public LabelStyle LabelStyle { get; }
// Additional padding given to accommodate spoke labels
public double PaddingFraction { get, set; }
// Additional padding given to accommodate labels
public double PaddingArc { get, set; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public string LegendText { get, set; }
public ArrowStyle ArrowStyle { get, set; }
public Color ArrowLineColor { get, set; }
public float ArrowLineWidth { get, set; }
public Color ArrowFillColor { get, set; }
public float ArrowMinimumLength { get, set; }
public float ArrowMaximumLength { get, set; }
public float ArrowOffset { get, set; }
public ArrowAnchor ArrowAnchor { get, set; }
public float ArrowWidth { get, set; }
public float ArrowheadAxisLength { get, set; }
public float ArrowheadLength { get, set; }
public float ArrowheadWidth { get, set; }
public IArrowShape ArrowShape { get, set; }
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class Pie : PieBase`
<!-- Plottables\Pie.cs -->

```csharp
public class Pie : PieBase
public double Radius { get, set; }
public double ExplodeFraction { get, set; }
public double DonutFraction { get, set; }
public Pie(IList<PieSlice> slices)
public override AxisLimits GetAxisLimits()
public override void Render(RenderPack rp)
```

### `public abstract class PieBase : IPlottable, IManagesAxisLimits, IHasLine`
<!-- Plottables\PieBase.cs -->

```csharp
public abstract class PieBase : IPlottable, IManagesAxisLimits, IHasLine
public IAxes Axes { get, set; }
public bool IsVisible { get, set; }
public Angle Rotation { get, set; }
public IEnumerable<LegendItem> LegendItems
public Color LineColor { get, set; }
public LinePattern LinePattern { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public double Padding { get, set; }
public double SliceLabelDistance { get, set; }
public IList<PieSlice> Slices { get, set; }
// Enable this to modify the axis limits at render time to achieve "square axes" where the units/px values are equal for horizontal and vertical axes, allowing circles to always appear as circles instead of ellipses.
public bool ManageAxisLimits { get, set; }
public virtual void UpdateAxisLimits(Plot plot)
public abstract AxisLimits GetAxisLimits()
public abstract void Render(RenderPack rp)
```

### `public class PolarAxis : IPlottable, IManagesAxisLimits, IHasFill`
<!-- Plottables\PolarAxis.cs -->
> A polar axes uses spoke lines and circles to describe a polar coordinate system where points are represented by a radius and angle. This class draws a polar axes and has options to customize spokes and circles.

```csharp
public class PolarAxis : IPlottable, IManagesAxisLimits, IHasFill
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
// Spokes are straight lines that extend outward from the origin
public List<PolarAxisSpoke> Spokes { get; }
// Radial positions describing concentric circles centered on the origin
public List<PolarAxisCircle> Circles { get; }
// This value will be added to all angles, effectively rotating the polar axis. The default origin angle (0 degrees) is right in 2D Axis space. The direction of rotation is defined by .
public Angle Rotation { get, set; }
// Determines whether angles ascend clockwise or counter-clockwise relative to the origin. The origin can be effectively changed by setting .
public bool Clockwise { get, set; }
// If enabled, radial ticks will be drawn using straight lines connecting intersections circles and spokes
public bool StraightLines { get, set; }
// Enable this to modify the axis limits at render time to achieve "square axes" where the units/px values are equal for horizontal and vertical axes, allowing circles to always appear as circles instead of ellipses.
public bool ManageAxisLimits { get, set; }
public FillStyle FillStyle { get, set; }
public Color FillColor { get, set; }
public Color FillHatchColor { get, set; }
public IHatch? FillHatch { get, set; }
// Create ticks (circles) evenly spaced between 0 and
public void SetCircles(double maximumRadius, int count)
// Clear existing circles and add new ones at the defined positions.
public void SetCircles(double[] positions)
// Clear existing circles and add new ones at the defined positions with the given labels.
public void SetCircles(double[] positions, string[] labels)
// Replace existing spokes with a new set evenly spaced around the circle.
public void SetSpokes(int count, double length, bool degreeLabels = true)
// Replace existing spokes with new ones placed at the specified angles
public void SetSpokes(Angle[] angles, double length, string[] labels)
public void SetSpokes(string[] labels, double length, bool clockwise = true)
// Replace existing spokes with new ones that have the given labels evenly spaced around the circle
public void SetSpokes(string[] labels, double length)
// Return the X/Y position of a point defined in polar space
public Coordinates GetCoordinates(double radius, double degrees)
// Return the X/Y position of a point defined in polar space
public Coordinates GetCoordinates(double radius, Angle angle)
// Return the X/Y position of a point defined in polar space
public Coordinates GetCoordinates(PolarCoordinates point)
public Coordinates[] GetCoordinates(IReadOnlyList<double> values, bool clockwise = false)
// Return coordinates for the given radius values assuming one value per spoke.
public Coordinates[] GetCoordinates(IReadOnlyList<double> radiusValues)
public AxisLimits GetAxisLimits()
public virtual void UpdateAxisLimits(Plot plot)
public virtual void Render(RenderPack rp)
public void RegenerateCircles(int count = 3)
public void RegenerateSpokes(int count = 5)
public void RegenerateSpokes(string[] labels)
```

### `public class Polygon : IPlottable, IHasLine, IHasFill, IHasMarker, IHasLegendText`
<!-- Plottables\Polygon.cs -->
> A polygon is a collection of X/Y points that are all connected to form a closed shape. Polygons can be optionally filled with a color or a gradient.

```csharp
public class Polygon : IPlottable, IHasLine, IHasFill, IHasMarker, IHasLegendText
public static Polygon Empty
public bool IsEmpty { get, set; }
public Coordinates[] Coordinates { get, set; }
public string Label { get, set; }
public string LegendText { get, set; }
public bool IsVisible { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public FillStyle FillStyle { get, set; }
public Color FillColor { get, set; }
public Color FillHatchColor { get, set; }
public IHatch? FillHatch { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
public int PointCount { get; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
// Creates a new polygon.
public Polygon(Coordinates[] coords)
public override string ToString()
public void UpdateCoordinates(Coordinates[] newCoordinates)
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class PopulationSymbol(Population population) : IPlottable`
<!-- Plottables\PopulationSymbol.cs -->

```csharp
public class PopulationSymbol(Population population) : IPlottable
public Population Population { get; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public double X { get, set; }
public double Width { get, set; }
public double MarkerWidthFraction = 0.8
public HorizontalAlignment MarkerAlignment { get, set; }
public double BarWidthFraction = .9
public HorizontalAlignment BarAlignment { get, set; }
public HorizontalAlignment BoxAlignment { get, set; }
public AxisLimits GetAxisLimits()
public Bar Bar { get, set; }
public Box Box { get, set; }
public Marker Marker { get, set; }
public Func<Box, Population, Population> BoxValueConfig { get, set; }
public virtual void Render(RenderPack rp)
public static Population BoxValueConfigurator_MeanStdErrStDev(Box box, Population pop)
public static Population BoxValueConfigurator_MedianQuantileExtrema(Box box, Population pop)
```

### `public class Radar() : IPlottable, IManagesAxisLimits`
<!-- Plottables\Radar.cs -->

```csharp
public class Radar() : IPlottable, IManagesAxisLimits
// The polar axis drawn beneath each radar series polygon
public PolarAxis PolarAxis { get, set; }
// A collection of RadarSeries, each of which hold a set of values and the styling information that controls how the shape is rendered
public List<RadarSeries> Series { get; }
// Enable this to modify the axis limits at render time to achieve "square axes" where the units/px values are equal for horizontal and vertical axes, allowing circles to always appear as circles instead of ellipses.
public bool ManageAxisLimits { get, set; }
public virtual void UpdateAxisLimits(Plot plot)
public bool IsVisible { get, set; }
// If enabled, the Polar axis will be drawn above any .
public bool IsAxisAboveData { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class RadialGaugePlot : IPlottable`
<!-- Plottables\RadialGaugePlot.cs -->
> A radial gauge chart is a graphical method of displaying scalar data in the form of a chart made of circular gauges so that each scalar is represented by each gauge.

```csharp
public class RadialGaugePlot : IPlottable
public IAxes Axes { get, set; }
// This array holds the original levels passed-in by the user. These levels are used to calculate radial gauge positions on every render.
public double[] Levels { get, set; }
// Number of gauges.
public int GaugeCount
// Maximum size (degrees) for the gauge. 180 is a semicircle and 360 is a full circle.
public double MaximumAngle { get, set; }
// Controls whether the backgrounds of the gauges are full circles or stop at the maximum angle.
public bool CircularBackground { get, set; }
// Labels that appear in the legend for each gauge. Number of labels must equal number of gauges. May be null if gauges are not to appear in the legend.
public string[]? Labels { get, set; }
// Colors for each gauge. Number of colors must equal number of gauges.
public Color[] Colors { get, set; }
// Describes how transparent the unfilled background of each gauge is (0 to 1). The larger the number the darker the background becomes.
public double BackgroundTransparencyFraction { get, set; }
// Indicates whether gauges fill clockwise as levels increase. If false, gauges will fill counter-clockwise (anti-clockwise).
public bool Clockwise { get, set; }
// Determines whether the gauges are drawn stacked (dafault value), sequentially, or as a single gauge (ressembling a pie plot).
public RadialGaugeMode GaugeMode { get, set; }
// Controls whether gauges will be dwan inside-out (true) or outside-in (false)
public bool OrderInsideOut { get, set; }
// Defines where the gauge label is written on the gage as a fraction of its length. Low values place the label near the base and high values place the label at its tip.
public double LabelPositionFraction { get, set; }
// Angle (degrees) at which the gauges start. 270° for North (default value), 0° for East, 90° for South, 180° for West, etc. Expected values in the range [0°-360°], otherwise unexpected side-effects might happen.
public float StartingAngle { get, set; }
// The empty space between gauges as a fraction of the gauge width.
public double SpaceFraction { get, set; }
// Size of the gague label text as a fraction of the gauge width.
public double FontSizeFraction { get, set; }
// Describes labels drawn on each gauge.
public readonly FontStyle Font = new()
// Controls if value labels are shown inside the gauges.
public bool ShowLevels { get, set; }
// String formatter to use for converting gauge levels to text
public string LevelTextFormat { get, set; }
// Style of the tip of the gauge
public SkiaSharp.SKStrokeCap EndCap { get, set; }
// Style of the base of the gauge
public SkiaSharp.SKStrokeCap StartCap { get, set; }
public bool IsVisible { get, set; }
public int XAxisIndex { get, set; }
public int YAxisIndex { get, set; }
public RadialGaugePlot(double[] levels, Color[] colors)
public override string ToString()
// Replace gauge levels with new ones.
public void Update(double[] levels, Color[]? colors = null)
public void ValidateData(bool deep = false)
public IEnumerable<LegendItem> LegendItems { get; }
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class Rectangle : IPlottable, IHasLine, IHasFill, IHasLegendText`
<!-- Plottables\Rectangle.cs -->

```csharp
public class Rectangle : IPlottable, IHasLine, IHasFill, IHasLegendText
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public FillStyle FillStyle { get, set; }
public Color FillColor { get, set; }
public Color FillHatchColor { get, set; }
public IHatch? FillHatch { get, set; }
public string Label { get, set; }
public string LegendText { get, set; }
public double X1 { get, set; }
public double X2 { get, set; }
public double Y1 { get, set; }
public double Y2 { get, set; }
public CoordinateRect CoordinateRect { get, set; }
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class ScaleBar : IPlottable, IHasLine`
<!-- Plottables\ScaleBar.cs -->

```csharp
public class ScaleBar : IPlottable, IHasLine
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
// Distance of the corner of the scalebar from the corner of the data area
public PixelPadding EdgePadding { get, set; }
// Padding to add between labels and scalebar lines
public PixelPadding LabelPadding { get, set; }
public double Width { get, set; }
public double Height { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public LabelStyle XLabelStyle { get, set; }
public LabelStyle YLabelStyle { get, set; }
public string XLabel { get, set; }
public string YLabel { get, set; }
public virtual void Render(RenderPack rp)
```

### `public class Scatter(IScatterSource data) : IPlottable, IHasLine, IHasMarker, IHasLegendText, IDataSource, IGetNearest`
<!-- Plottables\Scatter.cs -->

```csharp
public class Scatter(IScatterSource data) : IPlottable, IHasLine, IHasMarker, IHasLegendText, IDataSource, IGetNearest
public string Label { get, set; }
public string LegendText { get, set; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public int MinRenderIndex { get, set; }
public int MaxRenderIndex { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
public IScatterSource Data { get; }
public bool FillY { get, set; }
public bool FillYBelow { get, set; }
public bool FillYAbove { get, set; }
public double FillYValue { get, set; }
public Color FillYAboveColor { get, set; }
public Color FillYBelowColor { get, set; }
public Color FillYColor { get, set; }
public List<AxisGradientColorPosition> ColorPositions { get, set; }
public AxisGradientDirection AxisGradientDirection { get, set; }
public double OffsetX { get, set; }
public double OffsetY { get, set; }
public double ScaleX { get, set; }
public double ScaleY { get, set; }
// The style of lines to use when connecting points.
public ConnectStyle ConnectStyle = ConnectStyle.Straight
// Controls whether points are connected by smooth or straight lines
public bool Smooth { set; }
// Setting this value enables and sets the curve tension. Low tensions tend to "overshoot" data points. High tensions begin to approach connecting points with straight lines.
public double SmoothTension { get, set; }
// Strategy to use for generating the path used to connect points
public IPathStrategy PathStrategy { get, set; }
public Color Color { get, set; }
public AxisLimits GetAxisLimits()
public IEnumerable<LegendItem> LegendItems
public virtual void Render(RenderPack rp)
// Convert scatter plot points (connected by diagonal lines) to step plot points (connected by right angles) by inserting an extra point between each of the original data points to result in L-shaped steps.
public static IReadOnlyList<Pixel> GetStepDisplayPixels(IReadOnlyList<Pixel> pixels, bool right)
public DataPoint GetNearest(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
// Returns an optimized to work with when having to iterate across the collection of points
public IDataSource GetIDataSource()
```

### `public class Signal(ISignalSource data) : IPlottable, IHasLine, IHasMarker, IHasLegendText, IGetNearest`
<!-- Plottables\Signal.cs -->

```csharp
public class Signal(ISignalSource data) : IPlottable, IHasLine, IHasMarker, IHasLegendText, IGetNearest
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public ISignalSource Data { get, set; }
public string Label { get, set; }
public string LegendText { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public int MinRenderIndex { get, set; }
public int MaxRenderIndex { get, set; }
// Maximum size of the marker (in pixels) to display at each data point when the plot is zoomed far in.
public float MaximumMarkerSize { get, set; }
// Setting this flag causes lines to be drawn between every visible point (similar to scatter plots) to improve anti-aliasing in static images. Setting this will decrease performance for large datasets and is not recommended for interactive environments.
public bool AlwaysUseLowDensityMode { get, set; }
public Color Color { get, set; }
public AxisLimits GetAxisLimits()
public IEnumerable<LegendItem> LegendItems { get; }
public virtual void Render(RenderPack rp)
public DataPoint GetNearest(Coordinates location, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates location, RenderDetails renderInfo, float maxDistance = 15)
```

### `public class SignalConst<T>(SignalConstSource<T> data) : Signal(data), IPlottable, IHasLine, IHasMarker, IHasLegendText where T : struct, IComparable`
<!-- Plottables\SignalConst.cs -->

```csharp
public class SignalConst<T>(SignalConstSource<T> data) : Signal(data), IPlottable, IHasLine, IHasMarker, IHasLegendText where T : struct, IComparable
```

### `public class SignalXY(ISignalXYSource dataSource) : IPlottable, IHasLine, IHasMarker, IHasLegendText, IGetNearest`
<!-- Plottables\SignalXY.cs -->

```csharp
public class SignalXY(ISignalXYSource dataSource) : IPlottable, IHasLine, IHasMarker, IHasLegendText, IGetNearest
public ISignalXYSource Data { get, set; }
public bool IsVisible { get, set; }
public int XAxisIndex { get, set; }
public int YAxisIndex { get, set; }
public IAxes Axes { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public MarkerShape MarkerShape { get, set; }
public float MarkerSize { get, set; }
public Color MarkerFillColor { get, set; }
public Color MarkerLineColor { get, set; }
public Color MarkerColor { get, set; }
public float MarkerLineWidth { get, set; }
// The style of lines to use when connecting points.
public ConnectStyle ConnectStyle { get, set; }
public int MinRenderIndex { get, set; }
public int MaxRenderIndex { get, set; }
public Color Color { get, set; }
public string Label { get, set; }
public string LegendText { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public DataPoint GetNearest(Coordinates location, RenderDetails renderInfo, float maxDistance = 15)
public DataPoint GetNearestX(Coordinates location, RenderDetails renderInfo, float maxDistance = 15)
public virtual void Render(RenderPack rp)
```

### `public class SmithChartAxis : IPlottable, IManagesAxisLimits`
<!-- Plottables\SmithChartAxis.cs -->
> A polar axes uses spoke lines and circles to describe a polar coordinate system where points are represented by a radius and angle. This class draws a polar axes and has options to customize spokes and circles.

```csharp
public class SmithChartAxis : IPlottable, IManagesAxisLimits
public static Coordinates CalculateGamma(Coordinates normalizedImpedance)
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
// Concentric circular tick lines
public List<RealTick> RealTicks { get; }
// Curves extending from the right side of the outer circle to various points around its circumference
public List<ImaginaryTick> ImaginaryTicks { get; }
// Rotates the axis clockwise from its default position (where 0 points right)
public Angle Rotation { get, set; }
// Enable this to modify the axis limits at render time to achieve "square axes" where the units/px values are equal for horizontal and vertical axes, allowing circles to always appear as circles instead of ellipses.
public bool ManageAxisLimits { get, set; }
// Default style of the curved lines extending from the right edge to points around the circumference of the chart outline
public LineStyle RealLineStyle { get, set; }
// Default style of the concentric circular axis lines
public LineStyle Imaginary { get, set; }
public LabelStyle LabelStyle { get; }
public string? LabelText { get, set; }
// Distance to offset label text
public double LabelPaddingFraction { get, set; }
public static IEnumerable<Coordinates> FindIntersectionPoints( Coordinates pt1, double r1, Coordinates pt2, double r2)
public RealTick AddRealTick(double value)
public ImaginaryTick AddImaginaryTick(double value)
// Return the X/Y position of a point defined in polar space
public Coordinates GetCoordinates(double radius, Angle angle)
// Return the X/Y position of a point defined in polar space
public Coordinates GetCoordinates(PolarCoordinates point)
// Return the X/Y position of the given impedance
public Coordinates GetCoordinates(double resistance, double reactance)
public AxisLimits GetAxisLimits()
public virtual void UpdateAxisLimits(Plot plot)
public virtual void Render(RenderPack rp)
```

### `public sealed class RealTick : PolarAxisCircle`（嵌套于 SmithChartAxis）

```csharp
public sealed class RealTick : PolarAxisCircle
public double Re { get, set; }
public RealTick(double Re) : base(Math.Abs(1 / (1 + Re)))
public AxisLimits GetAxisLimits()
```

### `public sealed class ImaginaryTick : PolarAxisCircle`（嵌套于 SmithChartAxis）

```csharp
public sealed class ImaginaryTick : PolarAxisCircle
public double Lm { get, set; }
public IReadOnlyList<Coordinates> Points { get; }
public ImaginaryTick( double Lm, Coordinates center = default, double radius = 1) : base(Math.Abs(1 / Lm))
// Calculate the angle of the target point relative to the center of the circle.
public static Angle GetAngle(Coordinates point, Coordinates center)
// Calculates a point on a specified angle base.
public static Coordinates GetPointOnCircle( Coordinates center, double radius, Angle angle)
public AxisLimits GetAxisLimits()
```

### `public class TINPlot : IPlottable`
<!-- Plottables\TINPlot.cs -->

```csharp
public class TINPlot : IPlottable
public string LegendText { get, set; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public AxisLimits GetAxisLimits()
public IEnumerable<LegendItem> LegendItems
public double ContourLineInterval { get, set; }
public TINPlot(IEnumerable<Coordinates3d> coordinates)
public void Update(IEnumerable<Coordinates3d> coordinates)
public MarkerStyle MarkerStyle { get, set; }
public LineStyle NetworkLineStyle { get, set; }
public MarkerStyle VoronoiMarkerStyle { get, set; }
public LineStyle VoronoiLineStyle { get, set; }
public LineStyle ContourLineStyle { get, set; }
public virtual void Render(RenderPack rp)
```

### `public class Text : LabelStyleProperties, IPlottable`
<!-- Plottables\Text.cs -->

```csharp
public class Text : LabelStyleProperties, IPlottable
public Coordinates Location { get, set; }
public float OffsetX { get, set; }
public float OffsetY { get, set; }
public override LabelStyle LabelStyle { get, set; }
public Alignment Alignment { get, set; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public readonly LabelStyle Label = null!
public Color Color { get, set; }
public Color FontColor { get, set; }
public Color BackgroundColor { get, set; }
public Color BackColor { get, set; }
public Color BorderColor { get, set; }
public float BorderWidth { get, set; }
public float Padding { set; }
public float Size { get, set; }
public float FontSize { get, set; }
public bool Bold { get, set; }
public float Rotation { get, set; }
public string FontName { get, set; }
public float? LineSpacing { get, set; }
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class TickModifierLabel : IPlottable`
<!-- Plottables\TickModifierLabel.cs -->
> This plottable contains logic to modify tick labels to display them using scientific notation with a multiplier displaed as text placed just outside the corner of the data area.

```csharp
public class TickModifierLabel : IPlottable
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public LabelStyle LabelStyle { get; }
// The axis this tick modifier will modify tick labels for
public IAxis Axis { get; }
// This logic determines where the text will be placed relative to the data area
public Func<PixelRect, Pixel> GetTextPixel { get, set; }
// This logic determines how to display the exponent as a string
public Func<int, string> LabelFormatter { get, set; }
public TickModifierLabel(IAxis axis)
public virtual void UpdateTickLabels()
public virtual void Render(RenderPack rp)
```

### `public class Tooltip : LabelStyleProperties, IPlottable, IHasLine, IHasFill`
<!-- Plottables\Tooltip.cs -->
> A tooltip displays a text bubble pointing to a specific location in X/Y space. The position of the bubble moves according to the axis limits to best display the text in the data area.

```csharp
public class Tooltip : LabelStyleProperties, IPlottable, IHasLine, IHasFill
// Location in coordinate space where the text of the tooltip will be displayed
public Coordinates LabelLocation { get, set; }
// Location in coordinate space of the tip of the tail
public Coordinates TipLocation { get, set; }
// Fractional size of the tail where it attaches to the tooltip body
public double TailWidthPercentage { get, set; }
// Distance (in pixels) of empty space between all sides of the label and the edge of the tooltip body
public float Padding { get, set; }
public override LabelStyle LabelStyle { get, set; }
public LineStyle LineStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public FillStyle FillStyle { get, set; }
public Color FillColor { get, set; }
public Color FillHatchColor { get, set; }
public IHatch? FillHatch { get, set; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public virtual void Render(RenderPack rp)
```

### `public class TriangularAxis(bool clockwise) : IPlottable`
<!-- Plottables\TriangularAxis.cs -->
> This plot type places a triangular axis on the plot and has methods to convert between triangular and Cartesian coordinates.

```csharp
public class TriangularAxis(bool clockwise) : IPlottable
public bool Clockwise { get; }
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public double Padding { get, set; }
public AxisLimits GetAxisLimits()
public FillStyle FillStyle { get, set; }
public LineStyle GridLineStyle { get, set; }
public TriangularAxisEdge Left { get; }
public TriangularAxisEdge Right { get; }
public TriangularAxisEdge Bottom { get; }
// Return coordinates for a point on the triangle for a fractional distance (0 through 1, inclusive) along the bottom and left axes.
public Coordinates GetCoordinates(double bottomFraction, double leftFraction)
// Converts ternary coordinates (bottom, left, right) to Cartesian coordinates (X, Y)
public Coordinates GetCoordinates(double bottomFraction, double leftFraction, double rightFraction)
public virtual void Render(RenderPack rp)
```

### `public class VectorField(IVectorFieldSource source) : IPlottable, IHasArrow, IHasLegendText`
<!-- Plottables\VectorField.cs -->

```csharp
public class VectorField(IVectorFieldSource source) : IPlottable, IHasArrow, IHasLegendText
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public string Label { get, set; }
public string LegendText { get, set; }
public ArrowStyle ArrowStyle { get, set; }
public Color ArrowLineColor { get, set; }
public float ArrowLineWidth { get, set; }
public Color ArrowFillColor { get, set; }
public float ArrowMinimumLength { get, set; }
public float ArrowMaximumLength { get, set; }
public float ArrowOffset { get, set; }
public ArrowAnchor ArrowAnchor { get, set; }
public float ArrowWidth { get, set; }
public float ArrowheadAxisLength { get, set; }
public float ArrowheadLength { get, set; }
public float ArrowheadWidth { get, set; }
public IColormap? Colormap { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
// Length (in pixels) of the longest arrow
public float MaximumArrowLength { get, set; }
public virtual void Render(RenderPack rp)
```

### `public class VerticalLine : AxisLine`
<!-- Plottables\VerticalLine.cs -->
> A line at a defined X position that spans the entire vertical space of the data area

```csharp
public class VerticalLine : AxisLine
public double X { get, set; }
public double Minimum { get, set; }
public double Maximum { get, set; }
public VerticalLine()
public override bool IsUnderMouse(CoordinateRect rect)
public override AxisLimits GetAxisLimits()
public override void Render(RenderPack rp)
public override void RenderLast(RenderPack rp)
```

### `public class VerticalSpan : AxisSpan, IPlottable`
<!-- Plottables\VerticalSpan.cs -->
> A vertical span marks the full horizontal range between two vertical values

```csharp
public class VerticalSpan : AxisSpan, IPlottable
public double Y1 { get, set; }
public double Y2 { get, set; }
public CoordinateRange YRange
public double Bottom { get, set; }
public double Top { get, set; }
public override AxisLimits GetAxisLimits()
public override void Render(RenderPack rp)
public override AxisSpanUnderMouse? UnderMouse(CoordinateRect rect)
public override void DragTo(AxisSpanUnderMouse spanUnderMouse, Coordinates mouseNow)
```

### `public class ZoomRectangle(Plot plot) : IZoomRectangle`
<!-- Plottables\ZoomRectangle.cs -->
> The shaded region on the plot when the user middle-click-drags to zoom

```csharp
public class ZoomRectangle(Plot plot) : IZoomRectangle
public bool IsVisible { get, set; }
public FillStyle FillStyle { get, set; }
public LineStyle LineStyle { get, set; }
public Pixel MouseDown { get, set; }
public Pixel MouseUp { get, set; }
public bool HorizontalSpan { get, set; }
public bool VerticalSpan { get, set; }
public Plot Plot { get; }
public void Apply(IXAxis xAxis)
public void Apply(IYAxis yAxis)
public void Render(RenderPack rp)
```

## ScottPlot.Plottables.Interactive

### `public class InteractiveHorizontalLine : IPlottable, IHasInteractiveHandles`
<!-- Plottables\Interactive\InteractiveHorizontalLine.cs -->

```csharp
public class InteractiveHorizontalLine : IPlottable, IHasInteractiveHandles
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public Cursor Cursor { get, set; }
public LineStyle LineStyle { get; }
public double Y { get, set; }
public AxisLimits GetAxisLimits()
public InteractiveHandle? GetHandle(CoordinateRect rect)
public virtual void MoveHandle(InteractiveHandle handle, Coordinates point)
public virtual void PressHandle(InteractiveHandle handle)
public virtual void ReleaseHandle(InteractiveHandle handle)
public virtual void Render(RenderPack rp)
```

### `public class InteractiveHorizontalLineSegment : IPlottable, IHasInteractiveHandles`
<!-- Plottables\Interactive\InteractiveHorizontalLineSegment.cs -->

```csharp
public class InteractiveHorizontalLineSegment : IPlottable, IHasInteractiveHandles
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public LineStyle LineStyle { get; }
public float HandleLength { get, set; }
public double Y { get, set; }
public double X1 { get, set; }
public double X2 { get, set; }
public double XMin
public double XMax
public AxisLimits GetAxisLimits()
public InteractiveHandle? GetHandle(CoordinateRect rect)
public virtual void MoveHandle(InteractiveHandle handle, Coordinates point)
public virtual void PressHandle(InteractiveHandle handle)
public virtual void ReleaseHandle(InteractiveHandle handle)
public virtual void Render(RenderPack rp)
```

### `public class InteractiveHorizontalSpan : IPlottable, IHasInteractiveHandles`
<!-- Plottables\Interactive\InteractiveHorizontalSpan.cs -->

```csharp
public class InteractiveHorizontalSpan : IPlottable, IHasInteractiveHandles
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public Cursor EdgeCursor { get, set; }
public Cursor BodyCursor { get, set; }
public LineStyle LineStyle { get; }
public FillStyle FillStyle { get; }
public double X1 { get, set; }
public double X2 { get, set; }
public double XMin
public double XMax
public AxisLimits GetAxisLimits()
public InteractiveHandle? GetHandle(CoordinateRect rect)
public virtual void MoveHandle(InteractiveHandle handle, Coordinates point)
public virtual void PressHandle(InteractiveHandle handle)
public virtual void ReleaseHandle(InteractiveHandle handle)
public virtual void Render(RenderPack rp)
```

### `public class InteractiveLineSegment : IPlottable, IHasInteractiveHandles`
<!-- Plottables\Interactive\InteractiveLineSegment.cs -->
> A straight line between two points

```csharp
public class InteractiveLineSegment : IPlottable, IHasInteractiveHandles
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public Cursor Cursor { get, set; }
public CoordinateLine Line { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public LineStyle LineStyle { get; }
public MarkerStyle StartMarkerStyle { get; }
public MarkerStyle EndMarkerStyle { get; }
public InteractiveHandle? GetHandle(CoordinateRect rect)
public Color Color { set; }
public virtual void PressHandle(InteractiveHandle handle)
public virtual void ReleaseHandle(InteractiveHandle handle)
public virtual void MoveHandle(InteractiveHandle handle, Coordinates point)
public virtual void Render(RenderPack rp)
```

### `public class InteractiveMarker : IPlottable, IHasInteractiveHandles`
<!-- Plottables\Interactive\InteractiveMarker.cs -->

```csharp
public class InteractiveMarker : IPlottable, IHasInteractiveHandles
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public Cursor Cursor { get, set; }
public MarkerStyle MarkerStyle { get, set; }
public IEnumerable<LegendItem> LegendItems
public double X
public double Y
public Coordinates Point { get, set; }
public AxisLimits GetAxisLimits()
public InteractiveHandle? GetHandle(CoordinateRect rect)
public virtual void MoveHandle(InteractiveHandle handle, Coordinates point)
public virtual void PressHandle(InteractiveHandle handle)
public virtual void ReleaseHandle(InteractiveHandle handle)
public virtual void Render(RenderPack rp)
```

### `public class InteractiveRectangle : IPlottable, IHasInteractiveHandles`
<!-- Plottables\Interactive\InteractiveRectangle.cs -->

```csharp
public class InteractiveRectangle : IPlottable, IHasInteractiveHandles
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public LineStyle LineStyle { get; }
public FillStyle FillStyle { get; }
public double X1 { get, set; }
public double X2 { get, set; }
public double Y1 { get, set; }
public double Y2 { get, set; }
public double XMin
public double XMax
public double YMin
public double YMax
public CoordinateRect Rect { get, set; }
public AxisLimits GetAxisLimits()
public InteractiveHandle? GetHandle(CoordinateRect rect)
public virtual void MoveHandle(InteractiveHandle handle, Coordinates point)
public virtual void PressHandle(InteractiveHandle handle)
public virtual void ReleaseHandle(InteractiveHandle handle)
public virtual void Render(RenderPack rp)
```

### `public class InteractiveTrendLine : IPlottable, IHasInteractiveHandles`
<!-- Plottables\Interactive\InteractiveTrendLine.cs -->
> An infinite line defined by two points that extends infinitely in both directions

```csharp
public class InteractiveTrendLine : IPlottable, IHasInteractiveHandles
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public Cursor Cursor { get, set; }
public CoordinateLine Line { get, set; }
public IEnumerable<LegendItem> LegendItems
public AxisLimits GetAxisLimits()
public LineStyle LineStyle { get; }
public MarkerStyle StartMarkerStyle { get; }
public MarkerStyle EndMarkerStyle { get; }
public InteractiveHandle? GetHandle(CoordinateRect rect)
public Color Color { set; }
public virtual void PressHandle(InteractiveHandle handle)
public virtual void ReleaseHandle(InteractiveHandle handle)
public virtual void MoveHandle(InteractiveHandle handle, Coordinates point)
public virtual void Render(RenderPack rp)
```

### `public class InteractiveVerticalLine : LabelStyleProperties, IPlottable, IRenderLast, IHasInteractiveHandles, IHasLine, IHasLegendText`
<!-- Plottables\Interactive\InteractiveVerticalLine.cs -->

```csharp
public class InteractiveVerticalLine : LabelStyleProperties, IPlottable, IRenderLast, IHasInteractiveHandles, IHasLine, IHasLegendText
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public Cursor Cursor { get, set; }
public LineStyle LineStyle { get, set; }
public bool LabelOppositeAxis { get, set; }
public double X { get, set; }
public override LabelStyle LabelStyle { get, set; }
public float LineWidth { get, set; }
public LinePattern LinePattern { get, set; }
public Color LineColor { get, set; }
public string LegendText { get, set; }
public string Text { get, set; }
public AxisLimits GetAxisLimits()
public InteractiveHandle? GetHandle(CoordinateRect rect)
public virtual void MoveHandle(InteractiveHandle handle, Coordinates point)
public virtual void PressHandle(InteractiveHandle handle)
public virtual void ReleaseHandle(InteractiveHandle handle)
public virtual void Render(RenderPack rp)
public void RenderLast(RenderPack rp)
public InteractiveVerticalLine()
```

### `public class InteractiveVerticalLineSegment : IPlottable, IHasInteractiveHandles`
<!-- Plottables\Interactive\InteractiveVerticalLineSegment.cs -->

```csharp
public class InteractiveVerticalLineSegment : IPlottable, IHasInteractiveHandles
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public LineStyle LineStyle { get; }
public float HandleLength { get, set; }
public double X { get, set; }
public double Y1 { get, set; }
public double Y2 { get, set; }
public double YMin
public double YMax
public AxisLimits GetAxisLimits()
public InteractiveHandle? GetHandle(CoordinateRect rect)
public virtual void MoveHandle(InteractiveHandle handle, Coordinates point)
public virtual void PressHandle(InteractiveHandle handle)
public virtual void ReleaseHandle(InteractiveHandle handle)
public virtual void Render(RenderPack rp)
```

### `public class InteractiveVerticalSpan : IPlottable, IHasInteractiveHandles`
<!-- Plottables\Interactive\InteractiveVerticalSpan.cs -->

```csharp
public class InteractiveVerticalSpan : IPlottable, IHasInteractiveHandles
public bool IsVisible { get, set; }
public IAxes Axes { get, set; }
public IEnumerable<LegendItem> LegendItems
public Cursor EdgeCursor { get, set; }
public Cursor BodyCursor { get, set; }
public LineStyle LineStyle { get; }
public FillStyle FillStyle { get; }
public double Y1 { get, set; }
public double Y2 { get, set; }
public double YMin
public double YMax
public AxisLimits GetAxisLimits()
public InteractiveHandle? GetHandle(CoordinateRect rect)
public virtual void MoveHandle(InteractiveHandle handle, Coordinates point)
public virtual void PressHandle(InteractiveHandle handle)
public virtual void ReleaseHandle(InteractiveHandle handle)
public virtual void Render(RenderPack rp)
```

## ScottPlot.Plottables.Interactive.SubplotPreRenderActions

### `public class SharedVerticalLine : IMultiplotPreRenderAction`
<!-- Plottables\Interactive\SubplotPreRenderActions\SharedVerticalLine.cs -->
> Demonstrates how to link multiple InteractiveVerticalLine objects so they move together.

```csharp
public class SharedVerticalLine : IMultiplotPreRenderAction
public SharedVerticalLine(params InteractiveVerticalLine[] lines)
public void Invoke()
```

## ScottPlot.Rendering.RenderActions

### `public class ApplyAxisRulesAfterLayout : IRenderAction`
<!-- Rendering\RenderActions\ApplyAxisRulesAfterLayout.cs -->

```csharp
public class ApplyAxisRulesAfterLayout : IRenderAction
public void Render(RenderPack rp)
```

### `public class ApplyAxisRulesBeforeLayout : IRenderAction`
<!-- Rendering\RenderActions\ApplyAxisRulesBeforeLayout.cs -->

```csharp
public class ApplyAxisRulesBeforeLayout : IRenderAction
public void Render(RenderPack rp)
```

### `public class AutoScaleUnsetAxes : IRenderAction`
<!-- Rendering\RenderActions\AutoScaleUnsetAxes.cs -->

```csharp
public class AutoScaleUnsetAxes : IRenderAction
public void Render(RenderPack rp)
```

### `public class CalculateLayout : IRenderAction`
<!-- Rendering\RenderActions\CalculateLayout.cs -->

```csharp
public class CalculateLayout : IRenderAction
public void Render(RenderPack rp)
```

### `public class ClearCanvas : IRenderAction`
<!-- Rendering\RenderActions\ClearCanvas.cs -->

```csharp
public class ClearCanvas : IRenderAction
public void Render(RenderPack rp)
```

### `public class ContinuouslyAutoscale : IRenderAction`
<!-- Rendering\RenderActions\ContinuouslyAutoscale.cs -->

```csharp
public class ContinuouslyAutoscale : IRenderAction
public void Render(RenderPack rp)
```

### `public class ExecutePlottableAxisManagers : IRenderAction`
<!-- Rendering\RenderActions\ExecutePlottableAxisManagers.cs -->

```csharp
public class ExecutePlottableAxisManagers : IRenderAction
public void Render(RenderPack rp)
```

### `public class PreRenderLock : IRenderAction`
<!-- Rendering\RenderActions\PreRenderLock.cs -->

```csharp
public class PreRenderLock : IRenderAction
public void Render(RenderPack rp)
```

### `public class RegenerateTicks : IRenderAction`
<!-- Rendering\RenderActions\RegenerateTicks.cs -->

```csharp
public class RegenerateTicks : IRenderAction
public void Render(RenderPack rp)
```

### `public class RenderBenchmark : IRenderAction`
<!-- Rendering\RenderActions\RenderBenchmark.cs -->

```csharp
public class RenderBenchmark : IRenderAction
public void Render(RenderPack rp)
```

### `public class RenderBorders : IRenderAction`
<!-- Rendering\RenderActions\RenderBorders.cs -->

```csharp
public class RenderBorders : IRenderAction
public void Render(RenderPack rp)
```

### `public class RenderDataBackground : IRenderAction`
<!-- Rendering\RenderActions\RenderDataBackground.cs -->

```csharp
public class RenderDataBackground : IRenderAction
public void Render(RenderPack rp)
```

### `public class RenderFigureBackground : IRenderAction`
<!-- Rendering\RenderActions\RenderFigureBackground.cs -->

```csharp
public class RenderFigureBackground : IRenderAction
public void Render(RenderPack rp)
```

### `public class RenderGridsAbovePlottables : IRenderAction`
<!-- Rendering\RenderActions\RenderGridsAbovePlottables.cs -->

```csharp
public class RenderGridsAbovePlottables : IRenderAction
public void Render(RenderPack rp)
```

### `public class RenderGridsBelowPlottables : IRenderAction`
<!-- Rendering\RenderActions\RenderGridsBelowPlottables.cs -->

```csharp
public class RenderGridsBelowPlottables : IRenderAction
public void Render(RenderPack rp)
```

### `public class RenderLegends : IRenderAction`
<!-- Rendering\RenderActions\RenderLegends.cs -->

```csharp
public class RenderLegends : IRenderAction
public void Render(RenderPack rp)
```

### `public class RenderPanels : IRenderAction`
<!-- Rendering\RenderActions\RenderPanels.cs -->

```csharp
public class RenderPanels : IRenderAction
public void Render(RenderPack rp)
```

### `public class RenderPlottables : IRenderAction`
<!-- Rendering\RenderActions\RenderPlottables.cs -->

```csharp
public class RenderPlottables : IRenderAction
public void Render(RenderPack rp)
```

### `public class RenderPlottablesLast : IRenderAction`
<!-- Rendering\RenderActions\RenderPlottablesLast.cs -->

```csharp
public class RenderPlottablesLast : IRenderAction
public void Render(RenderPack rp)
```

### `public class RenderStartingEvent : IRenderAction`
<!-- Rendering\RenderActions\RenderStartingEvent.cs -->

```csharp
public class RenderStartingEvent : IRenderAction
public void Render(RenderPack rp)
```

### `public class RenderZoomRectangle : IRenderAction`
<!-- Rendering\RenderActions\RenderZoomRectangle.cs -->

```csharp
public class RenderZoomRectangle : IRenderAction
public void Render(RenderPack rp)
```

### `public class ReplaceNullAxesWithDefaults : IRenderAction`
<!-- Rendering\RenderActions\ReplaceNullAxesWithDefaults.cs -->

```csharp
public class ReplaceNullAxesWithDefaults : IRenderAction
public void Render(RenderPack rp)
```

### `public class RestoreGLState : IRenderAction`
<!-- Rendering\RenderActions\RestoreGLState.cs -->

```csharp
public class RestoreGLState : IRenderAction
public void Render(RenderPack rp)
```

### `public class StoreGLState : IRenderAction`
<!-- Rendering\RenderActions\StoreGLState.cs -->

```csharp
public class StoreGLState : IRenderAction
public void Render(RenderPack rp)
```

### `public class SyncGLPlottables : IRenderAction`
<!-- Rendering\RenderActions\SyncGLPlottables.cs -->

```csharp
public class SyncGLPlottables : IRenderAction
public void Render(RenderPack rp)
```

## ScottPlot.Rendering

### `public class RenderManager(Plot plot)`
<!-- Rendering\RenderManager.cs -->

```csharp
public class RenderManager(Plot plot)
// This list of actions is performed in sequence to render a plot. It may be modified externally to inject custom functionality.
public List<IRenderAction> RenderActions { get; }
// Information about the previous render
public RenderDetails LastRender { get, set; }
// These events are invoked before any render action. Users can add blocking code to this event to ensure processes that modify plottables are complete before rendering begins. Alternatively, lock the object.
public EventHandler PreRenderLock { get, set; }
// This event is invoked just before each render, after axis limits are determined, tick labels are measured, and data area has been decided
public EventHandler<RenderPack> RenderStarting { get, set; }
// This event is invoked after each render
public EventHandler<RenderDetails> RenderFinished { get, set; }
// This event a render where the figure size (in pixels) changed from the previous render
public EventHandler<RenderDetails> SizeChanged { get, set; }
// This event is invoked during a render where the axis limits (in coordinate units) changed from the previous render This event occurs after render actions are performed.
public EventHandler<RenderDetails> AxisLimitsChanged { get, set; }
// Prevents from being invoked in situations that may cause infinite loops
public bool DisableAxisLimitsChangedEventOnNextRender { get, set; }
// Indicates whether this plot is in the process of executing a render
public bool IsRendering { get, set; }
// If false, any calls to Render() return immediately
public bool EnableRendering { get, set; }
public bool EnableEvents { get, set; }
public bool ClearCanvasBeforeEachRender { get, set; }
// Total number of renders completed
public int RenderCount { get, set; }
// Remove all render actions of the given type
public void Remove<T>() where T : IRenderAction
public void Render(SKCanvas canvas, PixelRect rect)
public void ForgetLastRender()
```

## ScottPlot.Reporting

### `public class HtmlReport() : PlotCollection`
<!-- Reporting\HtmlReport.cs -->

```csharp
public class HtmlReport() : PlotCollection
public string Title { get, set; }
public string Description { get, set; }
public int DefaultPlotWidth { get, set; }
public int DefaultPlotHeight { get, set; }
public string Template { get, set; }
public new void Add(Plot plot, string? title = null, string? description = null)
public void AddHeading(string text, int level = 1)
public void AddParagraph(string text)
public void AddHtml(string html)
public void AddPlotPng(Plot plot, string title, string description)
public void AddPlotPng(Plot plot, string title, string description, int width, int height)
public void AddPlotSvg(Plot plot, string title, string description)
public void AddPlotSvg(Plot plot, string title, string description, int width, int height)
public void AddPageBreak()
public string GetHtml()
public void SaveAs(string filePath)
```

### `public class PlotCollection`
<!-- Reporting\PlotCollection.cs -->

```csharp
public class PlotCollection
public List<PlotFigure> Figures { get; }
public void Add(Plot plot, string? title = null, string? description = null)
```

### `public record PlotFigure(Plot Plot, string Title, string Description)`
<!-- Reporting\PlotFigure.cs -->

```csharp
public record PlotFigure(Plot Plot, string Title, string Description)
```

## ScottPlot.StarAxes

### `public class CircularStarAxis : SpokedStarAxis`
<!-- StarAxes\CircularStarAxis.cs -->

```csharp
public class CircularStarAxis : SpokedStarAxis
public override LineStyle LineStyle { get, set; }
public override void Render(RenderPack rp, IAxes axes, double maxSpokeLength, int numSpokes, float rotationDegrees)
```

### `public class PolygonalStarAxis : SpokedStarAxis`
<!-- StarAxes\PolygonalStarAxis.cs -->

```csharp
public class PolygonalStarAxis : SpokedStarAxis
public override LineStyle LineStyle { get, set; }
public override void Render(RenderPack rp, IAxes axes, double maxSpokeLength, int numSpokes, float rotationDegrees)
```

### `public abstract class SpokedStarAxis : IStarAxis`
<!-- StarAxes\SpokedStarAxis.cs -->

```csharp
public abstract class SpokedStarAxis : IStarAxis
public abstract LineStyle LineStyle { get, set; }
public abstract void Render(RenderPack rp, IAxes axes, double maxSpokeLength, int numSpokes, float rotationDegrees = 0)
public virtual void RenderSpokes(RenderPack rp, IAxes axes, double spokeLength, int numSpokes, float rotationDegrees = 0)
```

## ScottPlot.Statistics

### `public static class Descriptive`
<!-- Statistics\Descriptive.cs -->

```csharp
public static class Descriptive
// Return the sample sum.
public static double Sum(double[] values)
// Return the sample sum.
public static double Sum<T>(IReadOnlyList<T> values)
// Return the sample mean.
public static double Mean(double[] values)
// Return the sample median.
public static double Median(double[] values)
// Return the median of a sorted sample.
public static double SortedMedian(IReadOnlyList<double> sortedValues)
// Return the percentile of a sorted sample.
public static double SortedPercentile(IReadOnlyList<double> sortedValues, double percentile)
// Return the percentile of a sample.
public static double Percentile(IReadOnlyList<double> values, double percentile)
// Return the sample mean.
public static double Mean<T>(IEnumerable<T> values)
// Return the sample variance (second moment about the mean) of data. Input must contain at least two values. Use this function when your data is a sample from a population. To calculate the variance from the entire population use .
public static double Variance(double[] values)
// Return the sample variance (second moment about the mean) of data. Input must contain at least two values. Use this function to calculate the variance from the entire population. To estimate the variance from a sample, use .
public static double Variance<T>(IReadOnlyList<T> values)
// Return the sample variance (second moment about the mean) of data. Input must contain at least two values. Use this function to calculate the variance from the entire population. To estimate the variance from a sample, use .
public static double VarianceP(double[] values)
// Return the sample variance (second moment about the mean) of data. Input must contain at least two values. Use this function to calculate the variance from the entire population. To estimate the variance from a sample, use .
public static double VarianceP<T>(IReadOnlyList<T> values)
// Return the sample standard deviation (the square root of the sample variance).
public static double StandardDeviation(double[] values)
// Return the sample standard deviation (the square root of the sample variance).
public static double StandardDeviation<T>(IEnumerable<T> values)
// Return the population standard deviation (the square root of the population variance). See VarianceP() for more information.
public static double StandardDeviationP(double[] values)
// Return the population standard deviation (the square root of the population variance). See VarianceP() for more information.
public static double StandardDeviationP<T>(IEnumerable<T> values)
// Standard error of the mean.
public static double StandardError<T>(IReadOnlyList<T> values)
public static IReadOnlyList<double> RemoveNaN<T>(IReadOnlyList<T> values)
public static double[] RemoveNaN(double[] values)
// Return the sample mean. NaN values are ignored. Returns NaN if all values are NaN.
public static double NanMean<T>(IReadOnlyList<T> values)
// Return the sample variance (second moment about the mean) of data. Input must contain at least two values. NaN values are ignored. Use this function when your data is a sample from a population. To calculate the variance from the entire population use .
public static double NanVariance<T>(IReadOnlyList<T> values)
// Return the sample variance (second moment about the mean) of data. Input must contain at least two values. NaN values are ignored. Use this function when your data is a sample from a population. To calculate the variance from the entire population use .
public static double NanVarianceP<T>(IReadOnlyList<T> values)
// Return the sample standard deviation (the square root of the sample variance). NaN values are ignored.
public static double NanStandardDeviation<T>(IReadOnlyList<T> values)
// Return the population standard deviation (the square root of the sample variance). NaN values are ignored.
public static double NanStandardDeviationP<T>(IReadOnlyList<T> values)
// Standard error of the mean. NaN values are ignored.
public static double NanStandardError<T>(IReadOnlyList<T> values)
// Transpose a multidimensional (not jagged) array
public static double[,] ArrayTranspose(double[,] matrix)
// Extracts a row or column from a 2D array
public static double[] ArrayToVector(double[,] values, uint? row = 0, uint? column = null)
public static double NanMean(double[,] values, uint row = 0, uint? column = null)
public static double NanVariance<T>(double[,] values, uint row = 0, uint? column = null)
public static double NanVarianceP<T>(double[,] values, uint row = 0, uint? column = null)
public static double NanStandardDeviation<T>(double[,] values, uint row = 0, uint? column = null)
public static double NanStandardDeviationP<T>(double[,] values, uint row = 0, uint? column = null)
public static double NanStandardError<T>(double[,] values, uint row = 0, uint? column = null)
public static double[] VerticalSlice(double[,] values, int columnIndex)
public static double[] VerticalMean(double[,] values)
public static double[] VerticalNanMean(double[,] values)
public static double[] VerticalStandardDeviation(double[,] values)
public static double[] VerticalNanStandardDeviation(double[,] values)
public static double[] VerticalStandardError(double[,] values)
public static double[] VerticalNanStandardError(double[,] values)
```

### `public class Histogram`
<!-- Statistics\Histogram.cs -->
> A histogram that accumulates the number of values observed in a continuous range of evenly-sized, user defined bins

```csharp
public class Histogram
// Number of values in each bin
public int[] Counts { get; }
// Lower edge of each bin
public double[] Bins { get; }
// Lower edge of each bin plus a final value representing the upper edge of the last bin
public double[] Edges { get; }
// Size of the first bin (distance between the first pair of bin edges)
public double FirstBinSize
// If enabled, values below or above the bin range will be accumulated in the lowest or highest bin
public bool IncludeOutliers { get, set; }
// A collection of bins of size where the first bin's left edge is and the last bin's left edge is
public static Histogram WithBinSize(double binSize, double firstBin, double lastBin)
// A collection of bins of size starting from the smallest value in and increasing to include the largest value in
public static Histogram WithBinSize(double binSize, IEnumerable<double> values)
// A collection of evenly sized bins. is the lower edge of the first bin. is the lower edge of the last bin.
public static Histogram WithBinCount(int count, double minValue, double maxValue)
// A collection of evenly sized bins spaced to include the full range of
public static Histogram WithBinCount(int count, IEnumerable<double> values)
public void Clear()
public void Add(double value)
public void AddRange(IEnumerable<double> values)
// Return counts normalized so the sum of all values equals 1
public double[] GetProbability(double scale = 1)
// Return the probability of each bin scaled so the peak is
public double[] GetNormalized(double maxValue = 1)
// Return the cumulative sum of all counts. Each value is the number of counts in that bin plus all bins below it.
public int[] GetCumulativeCounts()
// Return the cumulative probability histogram. Each value is the fraction of counts in that bin plus all bins below it.
public double[] GetCumulativeProbability(double scale = 1.0)
```

### `public enum KdeBandWidthRule { Scotts }`
<!-- Statistics\KernelDensity.cs -->

```csharp
public enum KdeBandWidthRule { Scotts }
成员: Scotts
```

### `public enum KdeKernel { Epanechnikov, Gaussian, Uniform, Triangular }`
<!-- Statistics\KernelDensity.cs -->

```csharp
public enum KdeKernel { Epanechnikov, Gaussian, Uniform, Triangular }
成员: Epanechnikov, Gaussian, Uniform, Triangular
```

### `public static class KernelDensity`
<!-- Statistics\KernelDensity.cs -->

```csharp
public static class KernelDensity
public static double Estimate(double x, IReadOnlyList<double> values, Func<double, double> kernel, double bandwidth)
public static IEnumerable<double> Estimate(IEnumerable<double> xs, IReadOnlyList<double> values, Func<double, double> kernel, double bandwidth)
public static double Estimate(double x, IReadOnlyList<double> values, KdeKernel kernel = KdeKernel.Epanechnikov, KdeBandWidthRule bandwidthRule = KdeBandWidthRule.Scotts)
public static IEnumerable<double> Estimate(IEnumerable<double> xs, IReadOnlyList<double> values, KdeKernel kernel = KdeKernel.Epanechnikov, KdeBandWidthRule bandwidthRule = KdeBandWidthRule.Scotts)
```

### `public readonly struct LinearRegression`
<!-- Statistics\LinearRegression.cs -->

```csharp
public readonly struct LinearRegression
public readonly double Slope
public readonly double Offset
public readonly double Rsquared
public string Formula
public string FormulaWithRSquared
// Calculate the linear regression from a collection of X/Y coordinates
public LinearRegression(Coordinates[] coordinates)
// Calculate the linear regression from a collection of X/Y coordinates
public LinearRegression(IEnumerable<Coordinates> coordinates)
// Calculate the linear regression a paired collection of X and Y points
public LinearRegression(double[] xs, double[] ys)
// Calculate the linear regression from a collection of evenly-spaced Y values
public LinearRegression(double[] ys, double firstX = 0, double xSpacing = 1)
// Return the Y point of the regression line for the given X position
public double GetValue(double x)
// Return the Y points of the regression line for the given X positions
public double[] GetValues(double[] xs)
```

### `public class ProbabilityDensity`
<!-- Statistics\ProbabilityDensity.cs -->
> Represents a Gaussian distribution of probabilities for a normal distributed population.

```csharp
public class ProbabilityDensity
public readonly double Mean
public readonly double StDev
public ProbabilityDensity(IEnumerable<double> values) : this(Descriptive.Mean(values), Descriptive.StandardDeviation(values))
public ProbabilityDensity(double mean, double stDev)
public double GetY(double x, double scale = 1)
public double[] GetYs(double[] xs, double scale = 1)
```

### `public static class Series`
<!-- Statistics\Series.cs -->

```csharp
public static class Series
// Return a moving window average of the given data. If original length is true, data will be padded with NaN.
public static double[] MovingAverage(double[] values, int window, bool preserveLength = false)
// Return a moving window standard deviation of the given data. If original length is true, data will be padded with NaN.
public static double[] SimpleMovingStandardDeviation(double[] values, int window, bool preserveLength = false)
```

## ScottPlot.Statistics.Tests

### `public class UnpairedTTest`
<!-- Statistics\Tests\UnpairedTTest.cs -->

```csharp
public class UnpairedTTest
public Population Population1 { get; }
public Population Population2 { get; }
// T statistic
public double T { get; }
// Degrees of freedom
public int DF { get; }
public double P { get; }
public UnpairedTTest(Population pop1, Population pop2)
public static double Gauss(double z)
```

## ScottPlot.Stylers

### `public class FontStyler(Plot plot)`
<!-- Stylers\FontStyler.cs -->
> Helper methods for setting fonts to all components of a plot

```csharp
public class FontStyler(Plot plot)
// Apply the given font name to common plot components. Also sets the default font name so this font will be used for plot objects added in the future.
public SKTypeface? Set(string fontName, FontWeight weight = FontWeight.Normal, FontSlant slant = FontSlant.Upright, FontSpacing spacing = FontSpacing.Normal)
// Detects the best font to apply to every label in the plot based on the characters the they contain. If the best font for a label cannot be detected, the font last defined by will be used.
public void Automatic()
```

### `public class PlotStyler()`
<!-- Stylers\PlotStyler.cs -->

```csharp
public class PlotStyler()
public void Background(Color figure, Color data)
public void ColorAxes(Color color)
public void ColorLegend(Color background, Color foreground, Color border)
public void AxisFrame(float left, float right, float bottom, float top)
public void SetFont(string fontName)
public void SetBestFonts()
public void DarkMode()
```

## ScottPlot.Testing

### `public class DuplicateIdentifier<T>(string title)`
<!-- Testing\DuplicateIdentifier.cs -->
> Helper class to detect for duplicate items in complex collections and display helpful error messages to the console the facilitate debugging.

```csharp
public class DuplicateIdentifier<T>(string title)
public void Add(string id, T thing)
public void ShouldHaveNoDuplicates()
```

### `public class ImageDiff`
<!-- Testing\ImageDiff.cs -->
> Compare two raster images to identify and quantify differences

```csharp
public class ImageDiff
public double NumberOfDifferentPixels { get; }
public double PercentOfDifferencePixels { get; }
public double TotalDifference { get; }
public double MaxDifference { get; }
public Image? DifferenceImage { get; }
public ImageDiff(Image img1, Image img2, bool saveDiffImage = true)
```

### `public static class MD5Hasher`
<!-- Testing\MD5Hasher.cs -->

```csharp
public static class MD5Hasher
public static string GetHash(string input)
```

### `public class MockPlotControl : IPlotControl`
<!-- Testing\MockPlotControl.cs -->
> A plot control that renders in-memory and has functionality useful for testing interactivity.

```csharp
public class MockPlotControl : IPlotControl
public int Width { get, set; }
public int Height { get, set; }
public Pixel Center
public Plot Plot { get, set; }
public IMultiplot Multiplot { get, set; }
public GRContext? GRContext
public UserInputProcessor UserInputProcessor { get; }
public IPlotMenu? Menu // TODO: mock menu { get, set; }
public MockPlotControl()
public float DisplayScale { get, set; }
public float DetectDisplayScale()
public int RefreshCount { get, set; }
public void Refresh()
public void Reset()
public void Reset(Plot plot)
public int ContextMenuLaunchCount { get, set; }
public void ShowContextMenu(Pixel position)
public void ScrollWheelUp(Pixel pixel)
public void ScrollWheelDown(Pixel pixel)
public void PressShift()
public void ReleaseShift()
public void PressCtrl()
public void ReleaseCtrl()
public void PressAlt()
public void ReleaseAlt()
public void TapRightArrow()
public void TapLeftArrow()
public void TapUpArrow()
public void TapDownArrow()
public void PressKey(Key key)
public void ReleaseKey(Key key)
public void TapKey(Key key)
public void MoveMouse(Pixel px)
public void LeftMouseDown(Pixel px)
public void LeftMouseUp(Pixel px)
public void LeftClick(Pixel px)
public void LeftClickDrag(Pixel px1, Pixel px2)
public void RightMouseDown(Pixel px)
public void RightMouseUp(Pixel px)
public void RightClick(Pixel px)
public void RightClickDrag(Pixel px1, Pixel px2)
public void MiddleMouseDown(Pixel px)
public void MiddleMouseUp(Pixel px)
public void MiddleClick(Pixel px)
public void MiddleClickDrag(Pixel px1, Pixel px2)
public void SetCursor(Cursor cursor)
```

## ScottPlot.TickGenerators

### `public class DateTimeAutomatic : IDateTimeTickGenerator`
<!-- TickGenerators\DateTimeAutomatic.cs -->

```csharp
public class DateTimeAutomatic : IDateTimeTickGenerator
// If assigned, this function will be used to create tick labels
public Func<DateTime, string>? LabelFormatter { get, set; }
public ITimeUnit? TimeUnit { get, set; }
public Tick[] Ticks { get, set; }
public int MaxTickCount { get, set; }
public void Regenerate(CoordinateRange range, Edge edge, PixelLength size, Paint paint, LabelStyle labelStyle)
public IEnumerable<double> ConvertToCoordinateSpace(IEnumerable<DateTime> dates)
```

### `public class DateTimeFixedInterval : IDateTimeTickGenerator`
<!-- TickGenerators\DateTimeFixedInterval.cs -->

```csharp
public class DateTimeFixedInterval : IDateTimeTickGenerator
// The time unit to use for major ticks
public ITimeUnit Interval { get, set; }
// The number of units between major ticks (e.g. major ticks every 7 s)
public int IntervalsPerTick { get, set; }
// The time unit to use for minor ticks. If null, no minor ticks are generated.
public ITimeUnit? MinorInterval { get, set; }
// The number of units between minor ticks.
public int MinorIntervalsPerTick { get, set; }
// An optional function to override where the intervals for ticks start. The DateTime argument provided is the start range of the axis (i.e. ).
public Func<DateTime, DateTime>? GetIntervalStartFunc { get, set; }
// If assigned, this function will be used to create tick labels
public Func<DateTime, string>? LabelFormatter { get, set; }
// Creates a new generator.
public DateTimeFixedInterval(ITimeUnit interval, int intervalsPerTick = 1, ITimeUnit? minorInterval = null, int minorIntervalsPerTick = 1, Func<DateTime, DateTime>? getIntervalStartFunc = null)
public Tick[] Ticks { get, set; }
public int MaxTickCount { get, set; }
public IEnumerable<double> ConvertToCoordinateSpace(IEnumerable<DateTime> dates)
public void Regenerate(CoordinateRange range, Edge edge, PixelLength size, Paint paint, LabelStyle labelStyle)
```

### `public class DateTimeManual : ITickGenerator`
<!-- TickGenerators\DateTimeManual.cs -->

```csharp
public class DateTimeManual : ITickGenerator
public Tick[] Ticks { get, set; }
public int MaxTickCount { get, set; }
public DateTimeManual()
public DateTimeManual(Tick[] ticks)
public DateTimeManual(DateTime[] positions, string[] labels)
public void Regenerate(CoordinateRange range, Edge edge, PixelLength size, Paint paint, LabelStyle labelStyle)
public void Add(Tick tick)
public void AddMajor(DateTime position, string label)
public void AddMinor(DateTime position)
```

### `public class DecimalTickSpacingCalculator`
<!-- TickGenerators\DecimalTickSpacingCalculator.cs -->

```csharp
public class DecimalTickSpacingCalculator
public int MaximumTickCount { get, set; }
public double[] GenerateTickPositions(CoordinateRange range, PixelLength axisLength, PixelLength maxLabelLength)
```

### `public class EmptyTickGenerator : ITickGenerator`
<!-- TickGenerators\EmptyTickGenerator.cs -->

```csharp
public class EmptyTickGenerator : ITickGenerator
public Tick[] Ticks { get, set; }
public int MaxTickCount { get, set; }
public EmptyTickGenerator()
public void Regenerate(CoordinateRange range, Edge edge, PixelLength size, Paint paint, LabelStyle labelStyle)
```

### `public class EvenlySpacedMinorTickGenerator(double minorTickPerMajorTick) : IMinorTickGenerator`
<!-- TickGenerators\EvenlySpacedMinorTickGenerator.cs -->

```csharp
public class EvenlySpacedMinorTickGenerator(double minorTickPerMajorTick) : IMinorTickGenerator
public double MinorTicksPerMajorTick { get, set; }
public IEnumerable<double> GetMinorTicks(double[] majorTicks, CoordinateRange visibleRange)
```

### `public class FinancialTickGenerator(DateTime[] dates) : ITickGenerator`
<!-- TickGenerators\FinancialTickGenerator.cs -->
> Experimental tick generator designed for displaying financial time series data where values are evenly spaced visually despite having DateTimes which may contain gaps.

```csharp
public class FinancialTickGenerator(DateTime[] dates) : ITickGenerator
public Tick[] Ticks { get, set; }
public int MaxTickCount { get, set; }
public void Regenerate(CoordinateRange range, Edge edge, PixelLength size, Paint paint, LabelStyle labelStyle)
```

### `public interface IDateTimeTickGenerator : ITickGenerator`
<!-- TickGenerators\IDateTimeTickGenerator.cs -->

```csharp
public interface IDateTimeTickGenerator : ITickGenerator
```

### `public interface ITimeUnit`
<!-- TickGenerators\ITimeUnit.cs -->

```csharp
public interface ITimeUnit
// An array of integers that serve as good divisors to subdivide this time unit
public IReadOnlyList<int> Divisors { get; }
// Returns the format string used to display tick labels of this time unit. https://learn.microsoft.com/en-us/dotnet/api/system.datetime.tostring
public string GetDateTimeFormatString()
// Return the DateTime N units relative to this one
public DateTime Next(DateTime dateTime, int increment = 1)
// Minimum span this time unit can represent. To represent spans smaller than this, try the next smaller unit.
public TimeSpan MinSize { get; }
// Return a given date "snapped" back to the nearest nice tick position. Use this to find a good tick position for a given DateTime.
public DateTime Snap(DateTime dateTime)
```

### `public class LabelFormatters`
<!-- TickGenerators\LabelFormatters.cs -->
> A collection of methods which contain logic for choosing how a value is representing with text

```csharp
public class LabelFormatters
public static string Numeric(double value)
```

### `public class LogDecadeMinorTickGenerator : IMinorTickGenerator`
<!-- TickGenerators\LogDecadeMinorTickGenerator.cs -->

```csharp
public class LogDecadeMinorTickGenerator : IMinorTickGenerator
public int TicksPerDecade { get, set; }
public IEnumerable<double> GetMinorTicks(double[] majorPositions, CoordinateRange visibleRange)
```

### `public class LogMinorTickGenerator : IMinorTickGenerator`
<!-- TickGenerators\LogMinorTickGenerator.cs -->

```csharp
public class LogMinorTickGenerator : IMinorTickGenerator
public int Divisions { get, set; }
public IEnumerable<double> GetMinorTicks(double[] majorPositions, CoordinateRange visibleRange)
```

### `public class NumericAutomatic : ITickGenerator`
<!-- TickGenerators\NumericAutomatic.cs -->

```csharp
public class NumericAutomatic : ITickGenerator
public Tick[] Ticks { get, set; }
public int MaxTickCount { get, set; }
public bool IntegerTicksOnly { get, set; }
public Func<double, string> LabelFormatter { get, set; }
public IMinorTickGenerator MinorTickGenerator { get, set; }
public DecimalTickSpacingCalculator TickSpacingCalculator = new()
public float MinimumTickSpacing { get, set; }
public double TickDensity { get, set; }
public int? TargetTickCount = null
public void Regenerate(CoordinateRange range, Edge edge, PixelLength size, Paint paint, LabelStyle labelStyle)
```

### `public class NumericFixedInterval(double interval = 1) : ITickGenerator`
<!-- TickGenerators\NumericFixedInterval.cs -->

```csharp
public class NumericFixedInterval(double interval = 1) : ITickGenerator
public double Interval { get, set; }
public Func<double, string> LabelFormatter { get, set; }
public Tick[] Ticks { get, set; }
public int MaxTickCount { get, set; }
public void Regenerate(CoordinateRange range, Edge edge, PixelLength size, Paint paint, LabelStyle labelStyle)
```

### `public class NumericManual : ITickGenerator`
<!-- TickGenerators\NumericManual.cs -->

```csharp
public class NumericManual : ITickGenerator
public Tick[] Ticks { get, set; }
public int MaxTickCount { get, set; }
public NumericManual()
public NumericManual(Tick[] ticks)
public NumericManual(double[] positions, string[] labels)
public void Regenerate(CoordinateRange range, Edge edge, PixelLength size, Paint paint, LabelStyle labelStyle)
public void Add(Tick tick)
public void AddMajor(double position, string label)
public void AddMinor(double position)
```

## ScottPlot.TickGenerators.Financial

### `public class EveryNthUnit : IFinancialTickGenerator`
<!-- TickGenerators\Financial\EveryNthUnit.cs -->

```csharp
public class EveryNthUnit : IFinancialTickGenerator
public EveryNthUnit(int placeEveryNthUnit, int startIndex)
public List<(int, string)> GetTicks(DateTime[] DateTimes, int minIndexInView, int maxIndexInView)
```

### `public class Months : IFinancialTickGenerator`
<!-- TickGenerators\Financial\Months.cs -->

```csharp
public class Months : IFinancialTickGenerator
public List<(int, string)> GetTicks(DateTime[] DateTimes, int minIndexInView, int maxIndexInView)
```

### `public class MonthsAndMondays : IFinancialTickGenerator`
<!-- TickGenerators\Financial\MonthsAndMondays.cs -->

```csharp
public class MonthsAndMondays : IFinancialTickGenerator
public List<(int, string)> GetTicks(DateTime[] DateTimes, int minIndexInView, int maxIndexInView)
```

### `public class None : IFinancialTickGenerator`
<!-- TickGenerators\Financial\None.cs -->

```csharp
public class None : IFinancialTickGenerator
public List<(int, string)> GetTicks(DateTime[] DateTimes, int minIndexInView, int maxIndexInView)
```

### `public class Years : IFinancialTickGenerator`
<!-- TickGenerators\Financial\Years.cs -->

```csharp
public class Years : IFinancialTickGenerator
public List<(int, string)> GetTicks(DateTime[] DateTimes, int minIndexInView, int maxIndexInView)
```

## ScottPlot.TickGenerators.TimeUnits

### `public class Centisecond : ITimeUnit`
<!-- TickGenerators\TimeUnits\Centisecond.cs -->

```csharp
public class Centisecond : ITimeUnit
public IReadOnlyList<int> Divisors
public TimeSpan MinSize
public DateTime Snap(DateTime dt)
public string GetDateTimeFormatString()
public DateTime Next(DateTime dateTime, int increment = 1)
```

### `public class Day : ITimeUnit`
<!-- TickGenerators\TimeUnits\Day.cs -->

```csharp
public class Day : ITimeUnit
public IReadOnlyList<int> Divisors
public TimeSpan MinSize
public DateTime Snap(DateTime dt)
public string GetDateTimeFormatString()
public DateTime Next(DateTime dateTime, int increment = 1)
```

### `public class Decisecond : ITimeUnit`
<!-- TickGenerators\TimeUnits\Decisecond.cs -->

```csharp
public class Decisecond : ITimeUnit
public IReadOnlyList<int> Divisors
public TimeSpan MinSize
public DateTime Snap(DateTime dt)
public string GetDateTimeFormatString()
public DateTime Next(DateTime dateTime, int increment = 1)
```

### `public class Hour : ITimeUnit`
<!-- TickGenerators\TimeUnits\Hour.cs -->

```csharp
public class Hour : ITimeUnit
public IReadOnlyList<int> Divisors
public TimeSpan MinSize
public DateTime Snap(DateTime dt)
public string GetDateTimeFormatString()
public DateTime Next(DateTime dateTime, int increment = 1)
```

### `public class Millisecond : ITimeUnit`
<!-- TickGenerators\TimeUnits\Millisecond.cs -->

```csharp
public class Millisecond : ITimeUnit
public IReadOnlyList<int> Divisors
public TimeSpan MinSize
public DateTime Snap(DateTime dt)
public string GetDateTimeFormatString()
public DateTime Next(DateTime dateTime, int increment = 1)
```

### `public class Minute : ITimeUnit`
<!-- TickGenerators\TimeUnits\Minute.cs -->

```csharp
public class Minute : ITimeUnit
public IReadOnlyList<int> Divisors
public TimeSpan MinSize
public DateTime Snap(DateTime dt)
public string GetDateTimeFormatString()
public DateTime Next(DateTime dateTime, int increment = 1)
```

### `public class Month : ITimeUnit`
<!-- TickGenerators\TimeUnits\Month.cs -->

```csharp
public class Month : ITimeUnit
public IReadOnlyList<int> Divisors
public TimeSpan MinSize
public DateTime Snap(DateTime dt)
public string GetDateTimeFormatString()
public DateTime Next(DateTime dateTime, int increment = 1)
```

### `public class Second : ITimeUnit`
<!-- TickGenerators\TimeUnits\Second.cs -->

```csharp
public class Second : ITimeUnit
public IReadOnlyList<int> Divisors
public TimeSpan MinSize
public DateTime Snap(DateTime dt)
public string GetDateTimeFormatString()
public DateTime Next(DateTime dateTime, int increment = 1)
```

### `public class Year : ITimeUnit`
<!-- TickGenerators\TimeUnits\Year.cs -->

```csharp
public class Year : ITimeUnit
public IReadOnlyList<int> Divisors
public TimeSpan MinSize
public DateTime Snap(DateTime dt)
public string GetDateTimeFormatString()
public DateTime Next(DateTime dateTime, int increment = 1)
```

## ScottPlot.Triangulation

### `public class Delaunator`
<!-- Triangulation\Delaunator.cs -->

```csharp
public class Delaunator
// One value per half-edge, containing the point index of where a given half edge starts.
public int[] Triangles { get, set; }
// One value per half-edge, containing the opposite half-edge in the adjacent triangle, or -1 if there is no adjacent triangle
public int[] HalfEdges { get, set; }
// The initial points Delaunator was constructed with.
public Coordinates3d[] Points { get, set; }
// A list of point indices that traverses the hull of the points.
public int[] Hull { get, set; }
// Delaunator triangulation is an efficient algorithm for computing the Delaunay triangulation of a set of points, which connects points to form triangles with the property that no point lies inside the circumcircle of any triangle.
public Delaunator(Coordinates3d[] points)
public IEnumerable<Triangle3D> GetTriangles()
public IEnumerable<Edge3D> GetEdges()
public IEnumerable<Edge3D> GetVoronoEdges(Func<int, Coordinates3d>? triangleVerticeSelector = null)
public IEnumerable<Edge3D> GetVoronoEdgesBasedOnCircumCenter()
public IEnumerable<Edge3D> GetVoronoEdgesBasedOnCentroids()
public IEnumerable<VoronoiCell> GetVoronoiCells(Func<int, Coordinates3d>? triangleVerticeSelector = null)
public IEnumerable<VoronoiCell> GetVoronoiCellsBasedOnCircumcenters()
public IEnumerable<VoronoiCell> GetVoronoiCellsBasedOnCentroids()
public IEnumerable<Edge3D> GetHullEdges()
public Coordinates3d[] GetHullPoints()
public Coordinates3d[] GetTrianglePoints(int t)
public Coordinates3d[] GetRelaxedPoints()
public IEnumerable<Edge3D> GetEdgesOfTriangle(int t)
public static IEnumerable<Edge3D> CreateHull(IEnumerable<Coordinates3d> points)
public Coordinates3d GetTriangleCircumcenter(int t)
public Coordinates3d GetCentroid(int t)
public static Coordinates3d GetCircumcenter(Coordinates3d a, Coordinates3d b, Coordinates3d c)
public static Coordinates3d GetCentroid(Coordinates3d[] points)
// Returns the half-edges that share a start point with the given half edge, in order.
public IEnumerable<int> EdgesAroundPoint(int start)
// Returns the three point indices of a given triangle id.
public IEnumerable<int> PointsOfTriangle(int t)
// Returns the triangle ids adjacent to the given triangle id. Will return up to three values.
public IEnumerable<int> TrianglesAdjacentToTriangle(int t)
public static int NextHalfedge(int e)
public static int PreviousHalfedge(int e)
// Returns the three half-edges of a given triangle id.
public static int[] EdgesOfTriangle(int t)
// Returns the triangle id of a given half-edge.
public static int TriangleOfEdge(int e)
```

### `public record struct Edge3D(int Index, Coordinates3d P, Coordinates3d Q)`
<!-- Triangulation\Delaunator.cs -->

```csharp
public record struct Edge3D(int Index, Coordinates3d P, Coordinates3d Q)
public readonly Coordinates PCoordinates
public readonly Coordinates QCoordinates
public readonly CoordinateLine CoordinateLine
```

### `public class EdgeLine`
<!-- Triangulation\RectangularGridPrimitives.cs -->

```csharp
public class EdgeLine
public IEdge first { get; }
public IEdge second { get; }
public int CellID { get, set; }
public EdgeLine(IEdge first, IEdge second, int cellId)
```

### `public class EdgeLinePair : EdgeLine`
<!-- Triangulation\RectangularGridPrimitives.cs -->

```csharp
public class EdgeLinePair : EdgeLine
public IEdge first1 { get; }
public IEdge second1 { get; }
public EdgeLinePair(IEdge first, IEdge second, IEdge first1, IEdge second1, int cellId) : base(first, second, cellId)
```

### `public class HorizontalEdge : IEdge`
<!-- Triangulation\RectangularGridPrimitives.cs -->

```csharp
public class HorizontalEdge : IEdge
public Vertex First { get; }
public HorizontalEdge(Vertex first)
public override bool Equals(object? obj)
public override int GetHashCode()
public Coordinates Interpolate(Coordinates3d[,] coordinateGrid, double Z)
```

### `public interface IEdge`
<!-- Triangulation\RectangularGridPrimitives.cs -->

```csharp
public interface IEdge
```

### `public static class RectangularGrid`
<!-- Triangulation\RectangularGrid.cs -->

```csharp
public static class RectangularGrid
public static List<ContourLine> GetContourLines(Coordinates3d[,] coordinateGrid, double[] zs, bool fixContourDirections = true)
public static List<ContourLine> FixContourDirections(List<ContourLine> contours)
```

### `public record struct Triangle3D(int Index, IEnumerable<Coordinates3d> Points)`
<!-- Triangulation\Delaunator.cs -->

```csharp
public record struct Triangle3D(int Index, IEnumerable<Coordinates3d> Points)
public readonly double MinZ
public readonly double MaxZ
public readonly Coordinates[] Points2d
public readonly CoordinatePath Path
```

### `public class TriangulatedIrregularNetwork`
<!-- Triangulation\TriangulatedIrregularNetwork.cs -->

```csharp
public class TriangulatedIrregularNetwork
public AxisLimits3d AxisLimits { get, set; }
public Coordinates3d[] Points3D { get, set; }
public double MinZ { get, set; }
public double MaxZ { get, set; }
public TriangulatedIrregularNetwork(IEnumerable<Coordinates3d> coordinates)
public void Update(IEnumerable<Coordinates3d> coordinates)
public double[] GetZsByCount(int count)
public double[] GetZsByInterval(double interval)
public CoordinateLine[] GetLines()
public CoordinatePath[] GetCells()
public ContourLine[] GetContourLines(double[] zs)
```

### `public record Vertex(int i, int j)`
<!-- Triangulation\RectangularGridPrimitives.cs -->

```csharp
public record Vertex(int i, int j)
```

### `public class VerticalEdge : IEdge`
<!-- Triangulation\RectangularGridPrimitives.cs -->

```csharp
public class VerticalEdge : IEdge
public Vertex First { get; }
public VerticalEdge(Vertex first)
public override bool Equals(object? obj)
public override int GetHashCode()
public Coordinates Interpolate(Coordinates3d[,] coordinateGrid, double Z)
```

### `public record struct VoronoiCell(int Index, Coordinates3d[] Points)`
<!-- Triangulation\Delaunator.cs -->

```csharp
public record struct VoronoiCell(int Index, Coordinates3d[] Points)
public readonly Coordinates[] Points2d
public readonly CoordinatePath Path
```
