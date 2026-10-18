# ScottPlot 5 新手入门

> 跨平台 .NET 图表库 · WinForms / WPF / Avalonia / Blazor / MAUI / WinUI · 2026-10-18

---

## 一、这是什么？

ScottPlot 5 是一个 .NET 图表库。核心哲学：**用最少的代码画出交互式图表**。

```csharp
Plot myPlot = new();
myPlot.Add.Scatter(xs, ys);
myPlot.SavePng("chart.png", 800, 600);
```

---

## 二、30 秒理解架构

```
┌──────────────────────────────────────────────────────────────┐
│                     ScottPlot 5 分层架构                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  控件层     WinForms · WPF · Avalonia · Blazor · MAUI · ...  │
│    ↑                                                         │
│  交互层     UserInputProcessor → 响应器责任链 → 拖拽/缩放/平移 │
│    ↑                                                         │
│  渲染层     RenderManager → 25 步管道 → SkiaSharp             │
│    ↑                                                         │
│  Plottable  Scatter · Signal · Bar · Heatmap · Pie · ...     │
│    ↑                                                         │
│  DataSource IScatterSource · ISignalSource · SegmentedTree   │
│    ↑                                                         │
│  Primitives Coordinates · Pixel · Color · LineStyle · Axes   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

你只需关心两个入口：`Plot` — 创建图表、添加数据、保存图片；`IPlotControl` — 在 UI 中显示交互式图表。

**五条核心链路**（各层详析文档开头均有数据流视角）：

| 链路 | 路径 | 详析 |
|---|---|---|
| 数据源 | 用户数据 → IXXXSource → 坐标推算 | [05](05-datasources.md) |
| 构造 | Plot.Add.XXX() → PlottableAdder → PlottableList | [06](06-plottables.md) |
| 渲染 | Refresh() → RenderManager → 25 步 → SKCanvas | [07](07-rendering.md) |
| 交互 | 鼠标/键盘 → UserInputProcessor → 响应器 → Refresh | [08](08-interactivity.md) |
| 导出 | SavePng() → GetImage() → Render → Encode | [05](05-datasources.md) |

---

## 三、核心概念

### 3.1 两大坐标系统（最易踩坑）

ScottPlot 维护两套并行坐标：

| | Coordinates | Pixel |
|---|---|---|
| 数据类型 | `double` | `float` |
| 用途 | 数据逻辑位置 | 屏幕绘制位置 |
| Y 轴 | 向上增大（数学坐标系） | 向下增大（屏幕坐标系） |

```csharp
var pt = new Coordinates(5.0, 3.0);   // 数据空间
Pixel px = myPlot.Axes.GetPixel(pt);  // 坐标→像素
// 警告：SKCanvas 只接受 float 像素坐标！
```

### 3.2 Axes：坐标转换器

```csharp
myPlot.Axes.GetPixel(coord);      // 数据 → 像素
myPlot.Axes.SetLimitsX(0, 100);   // 手动设定范围（之后 AutoScale 失效）
myPlot.Axes.AutoScale();          // 自动适配所有数据
```

### 3.3 Plottable：你画的每一个东西

每个 Plottable 遵循统一模式：

```csharp
class Scatter : IPlottable, IHasLine, IHasMarker
{
    IScatterSource Data;         // 数据源
    IAxes Axes;                  // 坐标系
    AxisLimits GetAxisLimits();  // 告诉 Plot 我的范围
    void Render(RenderPack rp);  // 画自己
    // 样式能力通过 IHasLine / IHasMarker 等接口按需组合
}
```

---

## 四、5 分钟上手

### 4.1 第一个图表

```csharp
using ScottPlot;

Plot myPlot = new();
double[] xs = { 1, 2, 3, 4, 5 };
double[] ys = { 2, 4, 6, 8, 10 };
myPlot.Add.Scatter(xs, ys);
myPlot.SavePng("chart.png", 800, 600);
```

### 4.2 常用图表

```csharp
myPlot.Add.Scatter(xs, ys);             // 散点图
myPlot.Add.ScatterLine(xs, ys);         // 带连线
myPlot.Add.Signal(ys);                  // 等间距大数据（性能最优）
myPlot.Add.Bars(values);                // 柱状图
myPlot.Add.Candlestick(ohlcs);          // K 线图
myPlot.Add.Pie(values);                 // 饼图
myPlot.Add.Heatmap(intensities);        // 热力图
myPlot.Add.Function(x => Math.Sin(x));  // 函数曲线
myPlot.Add.VerticalLine(x);             // 垂直线
myPlot.Add.Callout("Label", x, y);      // 标注
myPlot.Add.Arrow(from, to);             // 箭头
```

### 4.3 自定义样式

```csharp
var sp = myPlot.Add.Scatter(xs, ys);
sp.LineWidth = 3;
sp.LineColor = Colors.Red;
sp.MarkerShape = MarkerShape.FilledCircle;
sp.FillColor = Colors.Red.WithAlpha(0.3);  // 半透明
sp.LegendText = "My Data";
myPlot.ShowLegend();
```

### 4.4 自定义轴

```csharp
myPlot.Axes.SetLimitsX(-10, 10);
myPlot.Axes.Bottom.Label.Text = "Time (s)";
myPlot.Title("Experiment Results");
myPlot.Grid.MajorLineColor = Colors.Gray.WithAlpha(0.3);
```

### 4.5 默认交互

| 操作 | 效果 |
|---|---|
| 左键拖拽 / 右键拖拽 | 平移 / 缩放 |
| 中键拖拽 | 矩形缩放 |
| 滚轮 | 缩放（±Ctrl 锁 X，±Shift 锁 Y） |
| 中键单击 / A 键 | 自动适配范围 |
| 右键单击 | 右键菜单 |
| 方向键 | 平移 |

---

## 五、新手高频陷阱（5 条速览）

1. **`Color.WithAlpha()` 必须接收返回值** — `Color` 是 readonly struct，`c = c.WithAlpha(128)` 才对。
2. **手动 `SetLimits` 后 AutoScale 永久失效** — 需调用 `myPlot.Axes.Reset()` 恢复。
3. **修改数据后必须手动 `Refresh()`** — `Plot` 没有数据变更检测机制。
4. **`PixelRect` 和 `CoordinateRect` 的 Y 轴方向相反** — 屏幕坐标 Y 向下，笛卡尔坐标 Y 向上。
5. **`SignalConst` 已标记为过时** — 新代码直接用 `Signal`。

> 全部 29 条陷阱：见 [10-usage-caveats.md](10-usage-caveats.md)。

---

## 六、搭建开发环境

**前置条件**：.NET SDK 10.0+。

```powershell
git clone https://github.com/ScottPlot/ScottPlot.git
cd ScottPlot/src/ScottPlot5
dotnet workload restore          # 安装 wasm/maui/android/ios 工作负载（首次 ~5 分钟）
dotnet build -c Release          # 全平台编译 ~57s
dotnet build ScottPlot5/ScottPlot.csproj  # 仅核心库 ~15s
```

**常见问题**：

| 问题 | 解决 |
|---|---|
| Android TFM 编译失败 (`XA5300`) | `dotnet build -c Release -f net10.0-windows` 跳过 |
| 工作负载缺失 (`NETSDK1138`) | `dotnet workload restore` |

---

## 七、下一步

按文件名编号 00 → 10 依次阅读即可。建议节奏：

| 阶段 | 文档 | 内容 |
|---|---|---|
| 导航 | [02-project-structure.md](02-project-structure.md) | 源码地图 |
| 分层（3 天） | [04](04-primitives.md) → [05](05-datasources.md) → [06](06-plottables.md) → [07](07-rendering.md) → [08](08-interactivity.md) → [09](09-controls.md) | 自底向上：原子层 → 控件层 |
| 全程 | [10-usage-caveats.md](10-usage-caveats.md) | 29 条陷阱，写代码前先过一遍 |