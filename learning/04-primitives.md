# ScottPlot 5 Primitives 层架构剖析

> 约占核心库 1/6 · 以 class 和 struct 为主体 · 辅以少量 enum 与 interface

---

## 数据流视角

```
用户数据 (double[] xs, ys / Coordinates[])
  → ScatterSourceDoubleArray / ScatterSourceCoordinatesArray (→ 05-datasources)
  → Scatter.Render():
      Coordinates[] → Axes.GetPixel() → Pixel[]
      → MarkerStyle.Render() / LineStyle.Apply() → SKCanvas
                                                ↑ 本章主角：所有样式、坐标、颜色类型
```

---

## 一、总览：Primitives 层分类

Primitives 是 ScottPlot 的**原子层**，所有高级组件(Plottable、RenderManager、AxisManager)都构建其上。按声明形式以 class 和 struct 为主体，辅以少量 enum 与 interface。

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Primitives 层全景                                  │
├───────────────┬──────────────┬──────────────┬──────────────────────┤
│ 坐标/几何     │ 样式系统     │ 颜色系统     │ 轴与范围             │
├───────────────┼──────────────┼──────────────┼──────────────────────┤
│ 数据承载      │ 布局/对齐   │ 图例         │ 渲染元数据            │
├───────────────┼──────────────┼──────────────┼──────────────────────┤
│ 交互/事件     │ 特效         │ 统计         │ 其他                  │
└───────────────┴──────────────┴──────────────┴──────────────────────┘
```

---

## 二、坐标与几何系统（最基础）

ScottPlot 维护两套并行的坐标体系，核心转换发生在渲染时。

### 2.1 两坐标系对照

```
        坐标空间 (Coordinate Space)         像素空间 (Pixel Space)
        ──────────────────────────          ─────────────────────
单位:   double (双精度)                     float (单精度)
用途:   数据逻辑位置                         屏幕绘制位置
Y方向:  数学坐标系 (上大下小)               屏幕坐标系 (上小下大)
存储:   Coordinates {X,Y}                   Pixel {X,Y}
范围:   CoordinateRect / CoordinateRange    PixelRect
线段:   CoordinateLine                      PixelLine
```

### 2.2 核心几何类型关系图

```
double X, Y
    │
    ├── Coordinates (struct)        ← 坐标空间中的点
    │     │
    │     ├── CoordinateLine        ← 坐标空间线段 (Start→End)
    │     ├── CoordinateRect         ← 坐标空间矩形 (Left,Right,Bottom,Top)
    │     │     ├── AxisLimits (readonly struct) ← 轴范围（只读快照）
    │     │     │     └── ExpandingAxisLimits (class) ← 动态扩展的有状态限制
    │     │     └── CoordinateSize  ← 坐标空间尺寸
    │     └── CoordinateRange (struct) ← 一维坐标范围 [Value1, Value2]
    │           └── CoordinateRangeMutable (class) ← 可变的坐标范围
    │
float X, Y
    │
    ├── Pixel (struct)               ← 屏幕像素点
    │     │
    │     ├── PixelLine               ← 像素线段
    │     ├── PixelRect (struct)     ← 像素矩形 (Left,Right,Bottom,Top)
    │     │     └── 核心: HasArea, Width, Height, Center, Contains()
    │     ├── PixelOffset             ← 像素偏移量
    │     ├── PixelSize               ← 像素尺寸
    │     ├── PixelPadding            ← 像素内边距 (Left,Right,Bottom,Top)
    │     ├── PixelLength             ← 像素长度
    │     ├── PixelPath               ← 像素路径 (List<PixelLine>)
    │     ├── PixelColumn             ← 单列像素范围
    │     └── PixelRangeX / PixelRangeY ← 一维像素范围
    │
    └── IAxes → Axes (class)         ← 两轴转换器
            ├── GetPixel(Coordinates) → Pixel
            ├── GetCoordinates(Pixel) → Coordinates
            └── DataRect: PixelRect  ← 数据区（渲染前注入）
```

### 2.3 Axes 转换器（核心桥梁）

```csharp
public class Axes : IAxes
{
    IXAxis  XAxis;   // ← 水平轴（实现坐标↔像素转换）
    IYAxis  YAxis;   // ← 垂直轴
    PixelRect DataRect; // ← 每次 Render 前由 RenderManager 注入

    // 核心 API
    Pixel     GetPixel(Coordinates coords);     // 坐标 → 像素
    Coordinates GetCoordinates(Pixel pixel);    // 像素 → 坐标
    float     GetPixelX(double x);              // 仅 X 转换
    float     GetPixelY(double y);              // 仅 Y 转换
    PixelRect GetPixelRect(CoordinateRect);     // 矩形整体转换
}
```

**每个 Plottable 都持有自己的 Axes 实例**，这意味着：
- 不同 Plottable 可绑定到不同坐标轴
- 多轴图自然支持（左Y轴 → 散点1，右Y轴 → 散点2）
- 轴范围在 autoscale 阶段由 AxisManager 统一计算

### 2.4 AxisLimits — 轴范围的三种形态

```csharp
// ① 只读快照（用于传递/比较）
AxisLimits limits = new(left, right, bottom, top);
// ② 动态扩展（autoscale 阶段累积计算）
ExpandingAxisLimits expanding = new();
expanding.Expand(5.0, 10.0, -2.0, 3.0);  // 自动扩展边界
expanding.Expand(coordinates);             // 含入点集
// ③ 转为只读
AxisLimits final = expanding.AxisLimits;
```

---

## 三、样式系统

### 3.1 样式类设计模式

所有样式类型共享统一模式：

```
Style Class (class, reference type)
├── 作为 Plottable 的属性字段（永久持有）
├── 聚合 SkiaSharp 原生对象 (SKPaint, SKStrokeCap...)
├── Clone() 方法支持拷贝
├── 包含 IsVisible 开关
├── ApplyToPaint() 应用到 SKPaint
└── Render() 直接绘制 (FillStyle, LabelStyle)

"init-only" 哲学: Plottable 持有自己的 Style 实例，
修改 style 属性会立即生效于下次渲染（无需重建 Plottable）。
```

### 3.2 样式类型矩阵

| 样式类 | 渲染目标 | 关键属性 | 对应接口 |
|---|---|---|---|
| `LineStyle` | 线条描边 | Width, Color, Pattern, Hairline, HandDrawn, Rounded | `IHasLine` |
| `FillStyle` | 区域填充 | Color, HatchColor, Hatch, AntiAlias | `IHasFill` |
| `MarkerStyle` | 数据标记 | Shape, Size, FillColor, LineColor, Outline, CustomRenderer | `IHasMarker` |
| `FontStyle` | 文字字体 | Name, Size, Weight, Slant, Color, Bold | — |
| `LabelStyle` | 文字标签 | Text, Alignment, Rotation, Background, Border, Shadow, Underline, Padding | `IHasLabel` |
| `PlotStyle` | 整体主题 | Palette, Colors (批量Set) | — |
| `BackgroundStyle` | 背景 | Color | `IHasBackground` |
| `GridStyle` | 网格线 | LineStyle (聚合) | — |
| `TickMarkStyle` | 刻度线 | Length, Width, Color, Direction | — |
| `ArrowStyle` | 箭头 | ArrowShape, ArrowAnchor, LineStyle | `IHasArrow` |

### 3.3 样式转发（Delegate Pattern）

Plottable 实现 `IHasLine` 等接口时，用**属性转发**暴露常用样式属性：

```csharp
public class Scatter : IPlottable, IHasLine, IHasMarker
{
    public LineStyle LineStyle { get; set; } = new() { Width = 1 };
    // 转发常用属性 —— 用户不用写 scatter.LineStyle.Width
    public float LineWidth { get => LineStyle.Width; set => LineStyle.Width = value; }
    public Color LineColor { get => LineStyle.Color; set => LineStyle.Color = value; }
    
    public MarkerStyle MarkerStyle { get; set; } = new();
    public MarkerShape MarkerShape { get => MarkerStyle.Shape; set => MarkerStyle.Shape = value; }
    public float MarkerSize { get => MarkerStyle.Size; set => MarkerStyle.Size = value; }
}
```

**这解释了为什么 `scatter.LineWidth = 3` 等价于 `scatter.LineStyle.Width = 3`。**

### 3.4 LinePattern 系统

```csharp
public readonly struct LinePattern(float[] intervals, float phase, string name)
// intervals: [实线长度, 空白长度, 实线长度, 空白长度, ...]
// phase:     偏移起始位置

预设值:
  Solid         → []
  Dashed        → [10, 10]
  DenselyDashed → [6, 6]
  Dotted        → [3, 5]
  // 可自定义任意 Pattern
```

### 3.5 MarkerShape 枚举（26种预设形状）

```
None, FilledCircle, OpenCircle, FilledSquare, OpenSquare,
FilledTriangleUp/Down, OpenTriangleUp/Down, FilledDiamond, OpenDiamond,
Eks, Cross, VerticalBar, HorizontalBar, TriUp, TriDown, Asterisk, HashTag,
OpenCircleWithDot/Cross/Eks, CircleWithLineLeft/Right, TriangleWithLineLeft/Right
```

可通过 `IMarker` 接口实现自定义形状注册。

---

## 四、颜色系统

### 4.1 Color 结构体

```csharp
public readonly struct Color
{
    byte Red, Green, Blue, Alpha;     // 内部存储：RGBA32

    // 多种构造方式
    Color(byte r, byte g, byte b, byte a=255)
    Color(float r, float g, float b, float a=1)  // 0-1 标准
    Color(string hexCode)                         // "#FF0000"
    Color(uint argb)                              // 0xAARRGGBB
    Color(SKColor skColor)
    Color(System.Drawing.Color)

    // 关键方法
    Color WithAlpha(double alpha)     // 修改透明度 → 新Color
    Color MixedWith(Color other, double fraction)
    string ToHex()                    // → "#RRGGBB"
    Color Lighten(double) / Darken(double)
    SKColor ToSKColor()              // → SkiaSharp 互转
}
```

### 4.2 Colors 静态工厂

```csharp
public static class Colors
{
    // 161 个预设颜色 (W3C CSS 颜色名，实测 Primitives/Colors.cs 静态属性数)
    static Color Red => new(255, 0, 0);
    static Color Blue => new(0, 0, 255);
    static Color Transparent => new(0, 0, 0, 0);
    static Color White => new(255, 255, 255);
    static Color Black => new(0, 0, 0);
    // ...
    // 预设调色板快捷方式
    static Color C0, C1, C2, C3, C4, C5, C6, C7, C8, C9  // Category10
}
```

### 4.3 Colormap 系统（38种科学色图）

```
IColormap 接口:
  Color GetColor(double fraction)     // fraction ∈ [0,1] → Color
  string Name

38种 Colormap (位于 ScottPlot.Colormaps 命名空间):
├── 经典科学: Viridis, Plasma, Inferno, Magma, Turbo, Jet
├── 海洋学:   Haline, Thermal, Deep, Ice, Rain
├── 地形学:   Topo, Turbid, Solar, Delta, Phase
├── 灰度:     Grayscale, GrayscaleReversed
├── 装饰器:   Reversed, Inverted, InvertedHue
├── 其他:     Amp, Balance, Blues, Greens, Curl, Dense, Diff,
│              Matter, MellowRainbow, Oxy, Speed, Tarn, Tempo, Algae
└── 自定义:   Custom, CustomInterpolated, CustomPalette（共 38 个，含自定义基类）

Colormap 工厂方法:
  Colormap.FromColors(Color[], bool smooth)   → 自定义色图
  Colormap.GetColormaps()                     → 所有可用色图的数组
  Colormap.Default = new MellowRainbow()      ← 默认色图
```

### 4.4 Palette 系统（26种配色方案）

```
IPalette 接口:
  Color GetColor(int index)            // 循环取色
  int Count

26种 Palette (ScottPlot.Palettes):
  Amber, Aurora, Building, Category10, Category20, ColorblindFriendly,
  ColorblindFriendlyDark, Custom, Dark, DarkPastel, Frost, LightOcean,
  LightSpectrum, Microcharts, Nero, Nord, Normal, OneHalf, OneHalfDark,
  PastelWheel, Penumbra, PolarNight, Redness, SnowStorm, SummerSplash, Tsitsulin

使用: Plot.Add.Palette = new Palettes.Nord();
     → 每次 Add.Scatter() 自动取下一个颜色
```

### 4.5 Gradient 渐变色系统

```csharp
Gradient (类型: Linear / Radial / Sweep / TwoPointConical)
  ├── Alignment / Center / Radius 等布局参数
  ├── GradientType 枚举
  └── Color[] 色阶数组
```

---

## 五、图例系统

```
Legend (class)
├── IsVisible
├── Alignment         ← 图例在图表中的位置 (Alignment.UpperRight)
├── Location          ← 精细位置控制 (PixelOffset)
├── BackgroundColor, OutlineColor, FontColor
├── Orientation       ← Vertical / Horizontal
├── FixedLineWidth    ← 是否固定图例中线的宽度
├── AllowMultiline    ← 多列布局
├── GetItems()        ← 从所有 Plottable 收集 LegendItem
├── ILegendLayout     ← 布局策略（可自定义）
└── Render(RenderPack)

LegendItem (class) — 实现了 5 个样式接口（另继承 LabelStyleProperties）
├── IHasLine        → LineStyle
├── IHasMarker      → MarkerStyle
├── IHasFill        → FillStyle
├── IHasArrow       → ArrowStyle
└── IHasLabel       → LabelStyle
```

---

## 六、数据承载类型（Plottable 的构造块）

这些 struct/class 是 Plottable 构造方法接收的参数类型：

| 类型 | 用途 | Plottable（实际类名） |
|---|---|---|
| `Bar` | 单条柱 (Position, Value, Error...) | BarPlot |
| `BarSeries` | 柱状图系列 | BarPlot (多系列) |
| `Box` | 箱线图数据 (Min, Q1, Median, Q3, Max, Outliers) | BoxPlot |
| `OHLC` | K线数据 (Open, High, Low, Close, DateTime) | CandlestickPlot / OhlcPlot |
| `PieSlice` | 饼图片 (Value, Label, Color, ExplodedFraction) | Pie / Coxcomb |
| `DataPoint` | 带索引的数据点 (X, Y, Index) | 触摸/最近点查询结果 |
| `PolarCoordinates` | 极坐标点 (Radius, Angle) | Polar 系 Plottables |
| `RadarSeries` | 雷达图系列 | Radar |
| `Population` | 统计总体 (Values[]) | PopulationSymbol |
| `ContourLine` | 等值线 (List<Coordinates>) | ContourLines |
| `RootedCoordinateVector` | 带根点的矢量 | VectorField |

---

## 七、布局与对齐系统

```
Alignment (enum)
├── UpperLeft     UpperCenter     UpperRight
├── MiddleLeft    MiddleCenter    MiddleRight
└── LowerLeft     LowerCenter     LowerRight

Edge (enum)             ← 四边: Left, Right, Bottom, Top
Location (class)        ← 精确坐标+对齐（注意：是引用类型，非 struct）
LocationUnit (enum)     ← Unspecified / Coordinates / Pixel

Layout (readonly struct) ← 布局计算结果快照（Primitives/Layout.cs）
  ├── FigureRect        ← 图表总区域
  ├── DataRect          ← 数据绘制区
  ├── PanelSizes        ← 各面板占用空间 (轴标签/标题/刻度)
  └── PanelOffsets      ← 各面板相对数据区边缘的偏移

PixelPadding (struct)   ← 内边距 (Left, Right, Bottom, Top)
FractionRect (struct)   ← 百分比矩形 (0-1 归一化)
```

---

## 八、渲染元数据

```
RenderDetails (readonly struct)
├── FigureRect, DataRect, Padding   ← 渲染区域
├── Elapsed, TimedActions[]         ← 渲染耗时 (每步)
├── AxisLimits, PreviousAxisLimits  ← 轴范围 (用于检测变化)
├── AxisLimitsByAxis, PreviousAxisLimitsByAxis
│                                    ← 所有轴的范围 (Dictionary<IAxis, CoordinateRange>)
├── Layout                          ← 本次渲染的布局快照
├── SizeChanged                     ← 画布尺寸是否变化
├── AxisLimitsChanged               ← 轴范围是否变化
└── Count                           ← 渲染总计数（每次渲染 +1）

Tick (readonly struct)
├── Position (double)               ← 轴上的坐标位置
├── Label (string)                  ← 刻度标签文本
└── IsMajor (bool)                  ← 主刻度/次刻度

TickMarkStyle
├── Length, Width, Color, Direction

GridStyle
├── LineStyle (聚合LineStyle)
```

---

## 九、CanvasState — 画布状态机

```csharp
public class CanvasState(SKCanvas canvas)
{
    Save()          // canvas.Save() + 计数器
    Restore()       // canvas.Restore() + 校验 (Save/Restore 配对)
    RestoreAll()    // 重置到初始状态
    Translate()     // canvas.Translate()（float 与 Pixel 两个重载）
    RotateDegrees() / RotateRadians()   // canvas.Rotate()（按度/弧度两个重载族）
    Clip()          // canvas.ClipRect()
    DisableClipping()
}
```

**为什么需要？** SKCanvas 的 Save/Restore 是无状态的，ScottPlot 自己的 CanvasState 跟踪调用层次，防止 `Restore` 次数超过 `Save` 导致 SkiaSharp 崩溃。

---

## 十、样式接口 Mixin 体系总结

```
IHasLine      → { LineStyle, LineWidth, LineColor, LinePattern }
IHasMarker    → { MarkerStyle, MarkerShape, MarkerSize, MarkerFillColor, MarkerLineColor }
IHasFill      → { FillStyle, FillColor, FillHatchColor, FillHatch }
IHasLabel     → { LabelStyle, Text, FontSize, ForeColor, ... }
IHasLegendText→ { LegendText }
IHasArrow     → { ArrowStyle }
IHasOutline   → { OutlineStyle, OutlineWidth, OutlineColor, OutlinePattern }
IHasShadow    → { ShadowColor, ShadowOffset }
IHasBackground→ { BackgroundColor }
IHasColorAxis → { ColorAxis (热力图用) }

所有 Plottable 通过多重接口实现获得"即插即用"的样式能力。
Render 时通过 is/as 模式检查接口：
  if (plottable is IHasLine line)
      line.LineStyle.ApplyToPaint(paint);
```

---

## 十一、关键设计洞察

1. **struct vs class 的选择**：轻量不可变数据用 struct (`Coordinates`, `Pixel`, `LinePattern`, `CoordinateRange`, `Tick`)，有状态/需共享引用用 class (`LineStyle`, `MarkerStyle`, `Axes`)

2. **Double 与 Float 精度分野**：坐标计算用 double（用户数据精度），像素渲染用 float（SkiaSharp 精度），两者在 `Axes` 中完成收敛

3. **readonly struct 的防御性设计**：`AxisLimits`, `PixelRect`, `RenderDetails` 都是 `readonly struct`，防止在渲染管道中被意外修改

4. **ExpandingAxisLimits vs AxisLimits 的太极图**：前者是 mutable class（用于 autoscale 累积），后者是 immutable readonly struct（用于传递/比较快照）

5. **样式属性转发**：`scatter.LineWidth = 3` 是语法糖，实际修改 `scatter.LineStyle.Width`，这样用户无需深入样式对象层次

6. **LegendItem 是样式集大成者**：同时实现 6 个样式接口，是样式系统组合能力的完美展示