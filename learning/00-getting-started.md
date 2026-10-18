# ScottPlot 5 新手入门指南

> 基于源码研读 + 项目实战整理 · 2026-10-18

---

## 零、ScottPlot 5 是什么？

ScottPlot 5 是一个**跨平台 .NET 图表库**，支持 WinForms、WPF、Avalonia、Blazor、MAUI、WinUI 等。它的核心哲学是：

> **"让用户用最少的代码画出交互式图表"**

一行代码画散点图，三行代码自定义样式，开箱即支持鼠标拖拽/滚轮/缩放等交互。

```
Plot myPlot = new();
myPlot.Add.Scatter(xs, ys);
myPlot.SavePng("chart.png", 800, 600);
```

---

## 一、架构速览（30 秒理解全貌）

```
┌──────────────────────────────────────────────────────────┐
│  ScottPlot 5 分层架构                                     │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Layer 7: 控件层 (Controls)                               │
│  WinForms · WPF · Avalonia · Blazor · MAUI · WinUI · Eto │
│           │                                              │
│  Layer 6: 交互层 (Interactivity)                          │
│  UserInputProcessor → 响应器责任链（默认 10 个）→ 拖拽/缩放/平移 │
│           │                                              │
│  Layer 5: 渲染层 (Rendering)                              │
│  RenderManager → 25 步 RenderAction 管道 → SkiaSharp     │
│           │                                              │
│  Layer 4: Plottables 层                                  │
│  Scatter · Signal · Bar · Heatmap · Pie · ... 72 种     │
│           │                                              │
│  Layer 3: DataSources 层                                 │
│  IScatterSource · ISignalSource · SegmentedTree          │
│           │                                              │
│  Layer 2: Primitives 层                                  │
│  Coordinates · Pixel · Color · LineStyle · AxisLimits    │
│           │                                              │
│  Layer 1: 核心运行时                                      │
│  Plot · RenderManager · AxisManager · LayoutEngine       │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**你只需关心两个入口：**
- `Plot` — 创建图表、添加数据、自定义样式、保存图片
- `IPlotControl`（平台控件）— 在 UI 中显示交互式图表

---

## 二、核心概念

### 2.1 Plot：一切的中心

```csharp
Plot myPlot = new();

// Plot 内部结构：
// myPlot
//   ├── PlottableList       ← 你添加的图形在这
//   ├── Axes (Bottom/Left/Top/Right)
//   ├── RenderManager       ← 25 步渲染管道
//   ├── LayoutEngine        ← 自动排版
//   ├── Legend              ← 图例系统
//   └── PlotControl         ← 宿主控件引用
```

### 2.2 两大坐标系统（最易踩坑）

ScottPlot 维护**两套并行坐标**，是所有渲染的基础：

| | Coordinates | Pixel |
|---|---|---|
| **数据类型** | `double` | `float` |
| **用处** | 数据逻辑位置 | 屏幕绘制位置 |
| **Y 轴方向** | 向上增大（数学坐标系） | 向下增大（屏幕坐标系） |
| **结构体** | `Coordinates(X, Y)` | `Pixel(X, Y)` |

```csharp
// ✅ 正确
var pt = new Coordinates(5.0, 3.0);   // 数据空间
Pixel px = myPlot.Axes.GetPixel(pt);  // 转换为屏幕像素

// ❌ 错误：直接把 Coordinates 传给 SkiaSharp 的 DrawLine()
// SKCanvas 只接受 float 像素坐标！
```

### 2.3 Axes：坐标转换器

```csharp
myPlot.Axes.GetPixel(coord);      // 数据 → 像素
myPlot.Axes.GetCoordinate(pixel); // 像素 → 数据

myPlot.Axes.SetLimitsX(0, 100);   // 手动设定 X 轴范围
myPlot.Axes.AutoScale();          // 自动适配所有数据
```

**陷阱**：一旦手动调用 `SetLimitsX/Y()`，AutoScale 就永久失效了。如需恢复，必须调用 `myPlot.Axes.Reset()`。

### 2.4 Plottable：你画的每一个东西

Plottable 是"可绘制物"的抽象。每个 Plottable 都必须：

1. 知道自己的**数据源**
2. 知道自己的**坐标系**（`IAxes`）
3. 能计算**数据范围**（`GetAxisLimits()`）
4. 能把自己**画出来**（`Render(rp)`）

```csharp
// 所有 Plottable 的统一模式
class Scatter : IPlottable
{
    IScatterSource Data;        // 数据
    IAxes Axes;                 // 坐标系
    AxisLimits GetAxisLimits(); // 告诉 Plot 我的范围
    void Render(RenderPack rp); // 画自己
}
```

---

## 三、5 分钟快速上手

### 3.1 创建第一个图表

```csharp
using ScottPlot;

// 1. 创建 Plot
Plot myPlot = new();

// 2. 准备数据
double[] xs = { 1, 2, 3, 4, 5 };
double[] ys = { 2, 4, 6, 8, 10 };

// 3. 添加散点图
myPlot.Add.Scatter(xs, ys);

// 4. 保存为图片
myPlot.SavePng("my-first-chart.png", 800, 600);
```

### 3.2 常用图表类型一览

```csharp
// ═══ 散点与信号 ═══
myPlot.Add.Scatter(xs, ys);              // 散点图（离散 XY）
myPlot.Add.ScatterLine(xs, ys);          // 带连线的散点图
myPlot.Add.Signal(ys);                   // 等间距大数据（性能最优）
myPlot.Add.SignalConst(ys);              // 只读信号（内存最优）

// ═══ 柱状图 ═══
myPlot.Add.Bars(values);                 // 简单柱状图
myPlot.Add.Bar(bars);                    // 多系列柱状图

// ═══ 金融图表 ═══
myPlot.Add.Candlestick(ohlcs);           // K 线图
myPlot.Add.OHLC(ohlcs);                  // OHLC 棒线图

// ═══ 饼图与径向图 ═══
myPlot.Add.Pie(values);                  // 饼图
myPlot.Add.Coxcomb(values);              // 南丁格尔玫瑰图

// ═══ 热力图 ═══
myPlot.Add.Heatmap(intensities);         // 热力图
myPlot.Add.Image(imageData);             // 图像

// ═══ 函数图 ═══
myPlot.Add.Function(x => Math.Sin(x));   // 函数曲线

// ═══ 标注 ═══
myPlot.Add.Callout("Label", x, y);       // 标注
myPlot.Add.Text("Hello", x, y);          // 文字
myPlot.Add.Arrow(from, to);              // 箭头

// ═══ 直线与区域 ═══
myPlot.Add.VerticalLine(x);              // 垂直线
myPlot.Add.HorizontalLine(y);            // 水平线
myPlot.Add.Rectangle(rect);              // 矩形
myPlot.Add.Ellipse(center, rx, ry);      // 椭圆
```

### 3.3 自定义样式

```csharp
var sp = myPlot.Add.Scatter(xs, ys);

// 通过 IHasLine / IHasMarker / IHasFill 接口
sp.LineWidth = 3;
sp.LineColor = Colors.Red;
sp.LinePattern = LinePattern.Dashed;

sp.MarkerSize = 10;
sp.MarkerShape = MarkerShape.FilledCircle;
sp.MarkerColor = Colors.Blue;

sp.FillColor = Colors.Red.WithAlpha(0.3);  // 半透明填充

// 图例
sp.LegendText = "My Data";
myPlot.ShowLegend();
```

### 3.4 自定义轴

```csharp
// 范围
myPlot.Axes.SetLimitsX(-10, 10);
myPlot.Axes.SetLimitsY(0, 100);

// 标签
myPlot.Axes.Bottom.Label.Text = "Time (seconds)";
myPlot.Axes.Left.Label.Text = "Voltage (mV)";

// 标题
myPlot.Title("My Experiment Results");

// 网格
myPlot.Grid.MajorLineColor = Colors.Gray.WithAlpha(0.3);
myPlot.HideGrid();
```

---

## 四、交互系统速成

### 4.1 默认交互

ScottPlot 5 **开箱自带**以下交互：

| 操作 | 效果 |
|------|------|
| 左键拖拽 | 平移 |
| 右键拖拽 | 缩放 |
| 中键拖拽 | 矩形缩放 |
| 滚轮 | 缩放（±Ctrl 切换方向，±Shift 缩放 Y） |
| 中键单击 | 自动适配范围 |
| 右键单击 | 右键菜单 |
| 方向键 | 平移 |
| A 键 | 自动适配范围 |

### 4.2 自定义交互

```csharp
// 禁用某个交互
myPlot.UserInputProcessor.Remove<UserActionResponses.MouseDragPan>();

// 添加自定义响应器
myPlot.UserInputProcessor.UserActionResponses.Insert(0, new MyCustomResponse());

// 完全禁用交互
myPlot.UserInputProcessor.UserActionResponses.Clear();
```

### 4.3 初级响应独占机制

拖拽期间其他响应器被屏蔽，松手后才能用滚轮。这是设计行为，不是 bug。

---

## 五、跨平台使用

所有平台控件都实现 `IPlotControl`，用法完全一致：**拿到 `control.Plot` 添加内容，改完调 `control.Refresh()`**。

| 平台 | 控件 | 引用方式 |
|---|---|---|
| WinForms | `FormsPlot` | 拖入窗体或 `new FormsPlot()` |
| WPF | `WpfPlot` | `<ScottPlot:WpfPlot Name="MyWpfPlot" />` |
| Avalonia | `AvaPlot` | `<ScottPlot:AvaPlot Name="MyAvaPlot" />` |
| Blazor | `BlazorPlot` | `<BlazorPlot @ref="MyBlazorPlot" />` |

```csharp
// 通用模式（各平台相同）
control.Plot.Add.Scatter(xs, ys);  // 添加数据
control.Refresh();                 // 刷新显示
control.Reset(new Plot());         // 替换整个 Plot
```

> 8 套控件的内部实现对比（渲染路径、HiDPI、触摸手势）：见
> [learning/09-controls.md](./09-controls.md)。

---

## 六、常见陷阱

> 完整的 15 条陷阱清单（含源码证据与踩坑概率评级）：见
> [10-usage-caveats.md](10-usage-caveats.md)。此处仅列新手最高频的 5 条。

### 🥇 陷阱 1：忘记 Refresh()

```csharp
// ❌ 数据变了，图没变
myPlot.Add.Scatter(xs, ys);
xs[0] = 999;  // 修改了原始数据

// ✅ 必须手动触发重绘
myPlot.Refresh();  // GUI 模式
```

### 其余 4 条高频陷阱（速览）

| 陷阱 | 一句话 | 详见 |
|---|---|---|
| `Color.WithAlpha()` 不接收返回值 | `Color` 是 readonly struct，必须 `c = c.WithAlpha(...)` 重新赋值 | caveats §5 |
| `SetLimits` 后 AutoScale 失效 | `HasBeenSet=true` 后自动缩放永久失效，需 `Reset()` | caveats §2 |
| 大数据用错类型 | 百万点用 `Add.Signal()`（SegmentedTree 降采样），别用 `Add.Scatter()` | caveats §8 |
| 混淆 Coordinates 和 Pixel | `Coordinates` 是 double 数据坐标，`Pixel` 是 float 屏幕坐标，别传错 | caveats §1/§4 |

---

## 七、学习路径建议

```
第 1 天：快速上手
├── 读本文
├── 跑通 3.1 第一个图表
└── 浏览 3.2 图表类型列表，每个试一遍

第 2 天：深入定制
├── 学习 3.3 样式系统（颜色、线型、标记、填充）
├── 学习 3.4 轴系统（范围、标签、标题、网格）
└── 阅读 learning/04-primitives.md

第 3 天：理解架构
├── 学习陷阱 4：大数据降采样（Signal vs Scatter）
├── 阅读 learning/05-datasources.md
└── 阅读 learning/07-rendering.md（25 步渲染管道）

第 4 天：交互与控件
├── 学习 4 交互系统
├── 阅读 learning/08-interactivity.md
└── 阅读 learning/09-controls.md

第 5 天：动手项目
├── 做一个小项目（实时数据监控、科学图示、金融图表）
├── 尝试自定义 Plottable
└── 阅读 learning/06-plottables.md
```

---

## 八、速查卡片

```
┌──────────────────────────────────────────────────────────┐
│                ScottPlot 5 速查卡片                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  创建 Plot       new Plot()                              │
│  添加散点        plot.Add.Scatter(xs, ys)                 │
│  添加信号        plot.Add.Signal(ys)                     │
│  添加柱状图      plot.Add.Bars(values)                    │
│  添加函数        plot.Add.Function(x => Math.Sin(x))      │
│  添加垂直线      plot.Add.VerticalLine(x)                 │
│                                                          │
│  设置轴范围      plot.Axes.SetLimitsX(0, 100)             │
│  自动轴范围      plot.Axes.AutoScale()                    │
│  设置标题        plot.Title("Title")                      │
│  显示图例        plot.ShowLegend()                        │
│                                                          │
│  保存图片        plot.SavePng("chart.png", 800, 600)      │
│  保存 SVG        plot.SaveSvg("chart.svg", 800, 600)      │
│                                                          │
│  修改线色        plottable.LineColor = Colors.Red         │
│  修改线宽        plottable.LineWidth = 3                 │
│  修改标记        plottable.MarkerShape = FilledCircle     │
│                                                          │
│  刷新 GUI        plotControl.Refresh()                    │
│  静态渲染        plot.Render()                            │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## 九、推荐资源

| 资源 | 用途 |
|------|------|
| [ScottPlot Cookbook](https://scottplot.net/cookbook/5.0/) | 500+ 带截图的示例代码 |
| [API 文档](https://scottplot.net/api/5.0/) | 完整 API 参考 |
| [learning/ 学习笔记](../../learning/) | 项目架构深度剖析（本文档所在目录） |
| [02-project-structure.md](02-project-structure.md) | 源码目录导航，快速定位代码位置 |
| [GitHub 仓库](https://github.com/ScottPlot/ScottPlot) | 源码 + Issues + Discussion |
| [RenderManager.cs](../../src/ScottPlot5/ScottPlot5/Rendering/RenderManager.cs) | 25 步渲染序列唯一真相源 |