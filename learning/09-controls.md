# ScottPlot 5 跨平台控件与多图系统

> 8 个控件包（7 套平台控件 + 1 个 GPU 扩展）· 55 个 .cs · ~3,000 行 · IPlotControl + IPlotMenu + IMultiplot

---

## 一、包体系总览

```
src/ScottPlot5/
├── ScottPlot5/                       → 核心库（NuGet: ScottPlot）
├── ScottPlot5 Tests/                 → 单元测试
├── ScottPlot5 Cookbook/              → Cookbook 示例
└── ScottPlot5 Controls/              → 跨平台控件仓库
    ├── ScottPlot.WinForms/          → NuGet: ScottPlot.WinForms
    ├── ScottPlot.WPF/               → NuGet: ScottPlot.WPF
    ├── ScottPlot.Avalonia/          → NuGet: ScottPlot.Avalonia
    ├── ScottPlot.Blazor/            → NuGet: ScottPlot.Blazor
    ├── ScottPlot.Maui/              → NuGet: ScottPlot.Maui
    ├── ScottPlot.WinUI/             → NuGet: ScottPlot.WinUI
    ├── ScottPlot.Eto/               → NuGet: ScottPlot.Eto
    └── ScottPlot.OpenGL/            → NuGet: ScottPlot.OpenGL  (GPU 加速扩展)
```

每个包只有 **3~9 个 .cs 源文件**（WinForms 9、WPF 7、Maui 9、其余 3~4），各平台代码高度对称。OpenGL 包额外有 17 个 .cs（含 GLPrograms Shader）。

---

## 二、统一抽象体系

### 2.1 IPlotControl — 控件统一接口

```csharp
public interface IPlotControl
{
    Plot Plot { get; }                             // 核心 Plot 对象
    IMultiplot Multiplot { get; set; }             // 多图管理器
    void Refresh();                                // 触发布局+渲染
    UserInputProcessor UserInputProcessor { get; } // 交互处理器
    IPlotMenu? Menu { get; set; }                  // 右键菜单
    void ShowContextMenu(Pixel position);          // 弹出菜单
    GRContext? GRContext { get; }                  // OpenGL 上下文（null = 不支持）
    float DisplayScale { get; set; }               // HiDPI 缩放系数
    float DetectDisplayScale();                    // 检测 DPI（开销大，勿频繁调用）
    void Reset();                                  // 释放当前 Plot 并新建
    void Reset(Plot plot);                         // 热替换 Plot 对象
    void SetCursor(Cursor cursor);                 // 应用平台光标
}
// 扩展方法: GetPlotAtPixel(pixel) → 经 Multiplot.LastRender 查找像素下的 Plot
```

**设计价值**：所有七套平台控件都实现这个接口（ScottPlot.OpenGL 不实现——它是 Plottable 扩展包），`UserInputProcessor` 和 `RenderManager` 只需依赖 `IPlotControl`，完全不知道自己在哪个平台运行。

### 2.2 IPlotMenu — 右键菜单统一接口

```csharp
public interface IPlotMenu
{
    List<ContextMenuItem> ContextMenuItems { get; }
    void Reset();
    void Clear();
    void Add(string Label, Action<Plot> action);
    void AddSeparator();
    void ShowContextMenu(Pixel pixel);
}
```

**标准菜单项**（WinForms/WPF/Avalonia/Maui/WinUI/Eto 一致）：
```
├── Save Image...          → 弹出保存文件对话框
├── Copy to Clipboard      → 复制位图到剪贴板
├── Autoscale              → 自动缩放轴范围
└── Open in New Window     → 在新窗口中打开（FormsPlotViewer/WpfPlotViewer）
```

Blazor 的菜单实现是空壳（浏览器环境不支持原生菜单）。

---

## 三、各平台控件对比

| 特性 | WinForms | WPF | Avalonia | Blazor | MAUI | WinUI | Eto |
|---|---|---|---|---|---|---|---|
| **基类** | `UserControl` | `Control` | `Control` | `ComponentBase` | `SKCanvasView` | `UserControl` | `Drawable` |
| **SkiaSharp 承载** | `TransparentSKControl` | `SKElement` | `ICustomDrawOp` | JS Canvas | `SKCanvasView` | `SKXamlCanvas` | `SKSurface` |
| **渲染方式** | OnPaintSurface | OnPaintSurface | DrawOp.Render | PaintSurface | OnPaintSurface | PaintSurface | OnPaint (bitmap) |
| **HiDPI** | DeviceDpi | VisualTreeHelper | RenderScaling | 1.0 (TODO) | 1.0 (固定) | XamlRoot.RasterizationScale | LogicalPixelSize |
| **设计时支持** | ✅ 替代视图 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **右键菜单** | FormsPlotMenu | WpfPlotMenu | AvaPlotMenu | 空壳 | MauiPlotMenu | WinUIPlotMenu | EtoPlotMenu |
| **触摸手势** | ❌ | ❌ | ❌ | ❌ | ✅ Pan/Pinch | ❌ | ❌ |
| **子控件封装** | FormsPlot/FormsPlotGL | WpfPlot/WpfPlotGL | AvaPlot | BlazorPlot/BlazorPlotGL | MauiPlot | WinUIPlot | EtoPlot |
| **TargetFrameworks** | net462+net8.0-windows+net10.0-windows | net462+net8.0-windows+net10.0-windows | net8.0+net10.0 | net8.0+net10.0 | net10.0+移动端 | net10.0 系列 | net8.0+net10.0 |

---

## 四、控件源码对比（对称性）

### WinForms

```csharp
public abstract class FormsPlotBase : UserControl, IPlotControl
{
    // 构造
    public FormsPlotBase() {
        Plot = new() { PlotControl = this };        // ①
        Multiplot = new Multiplot(Plot);            // ②
        DisplayScale = DetectDisplayScale();        // ③
        UserInputProcessor = new(this);             // ④
        Menu = new FormsPlotMenu(this);             // ⑤
    }
    // 事件 → 转发到 UserInputProcessor
    void SKElement_MouseDown(...) => UserInputProcessor.ProcessMouseDown(e);
    // 渲染 → OnPaintSurface 自动完成
}
```

### WPF

```csharp
public abstract class WpfPlotBase : Control, IPlotControl
{
    // 构造（同上，①②③④⑤）
    public WpfPlotBase() { /* ... */ }
    // 事件 → 转发到 UserInputProcessor（注意 WPF 需要 CaptureMouse）
    void SKElement_MouseDown(...) => {
        Keyboard.Focus(this);
        UserInputProcessor.ProcessMouseDown(element, e);
        (sender as UIElement)?.CaptureMouse();
    };
    // 渲染 → OnPaintSurface
}
```

### Avalonia（最特殊的渲染路径）

```csharp
public class AvaPlot : Control, IPlotControl
{
    // 构造（同上，①②③④⑤ + ClipToBounds + Focusable）
    public AvaPlot() { /* ... */ }

    // ★ 渲染：通过 ICustomDrawOperation + ISkiaSharpApiLeaseFeature
    private class CustomDrawOp : ICustomDrawOperation
    {
        public void Render(ImmediateDrawingContext context) {
            var lease = context.TryGetFeature<ISkiaSharpApiLeaseFeature>();
            using var lease = lease.Lease();
            lease.SkCanvas.SaveLayer();          // 独立图层
            Multiplot.Render(lease.SkCanvas, rect);
        }
    }
    public override void Render(DrawingContext context) {
        context.Custom(new CustomDrawOp(Bounds, Multiplot));
    }

    // ★ Refresh：通过 Dispatcher 异步调用
    public void Refresh() {
        Dispatcher.UIThread.InvokeAsync(InvalidateVisual, DispatcherPriority.Background);
    }
}
```

**Avalonia 的特殊性**：不走 `SKControl` 标准路径，而是通过 `ICustomDrawOperation` + `ISkiaSharpApiLeaseFeature` 直接获取 SkiaSharp 画布。这是因为它使用的是 Avalonia 自己的 SkiaSharp 后端，不是 SkiaSharp.Views。

### Blazor（Web 最特殊）

```csharp
public class BlazorPlotBase : ComponentBase, IPlotControl
{
    [Parameter] public string Style { get; set; }
    [Parameter] public bool EnableRenderLoop { get; set; }  // 自动刷新

    // 交互：Blazor 有独立的 JS 互操作路径
    public EventHandler<Pixel>? MouseMoved;
    public EventHandler<(Pixel, MouseButton)>? MouseButtonPressed;
    public EventHandler<(Pixel, MouseButton)>? MouseButtonReleased;
    public EventHandler<(Pixel, double)>? MouseWheelChanged;
    public EventHandler<Key>? KeyPressed;
    public EventHandler<Key>? KeyReleased;

    // 渲染：由 .razor 模板（BlazorPlot.razor）控制
    //   <SKCanvas @ref="SKCanvasElement" Width="800" Height="600"
    //             OnPaintSurface="OnPaintSurface"
    //             onwheel="MouseWheel" ... />
}
```

### MAUI（移动端优先）

```csharp
public class MauiPlot : SKCanvasView, IPlotControl
{
    public MauiPlot() {
        // ... ①②③④⑤

        if (DeviceInfo.Idiom == DeviceIdiom.Desktop) {
            // 桌面 → 触摸事件（鼠标模拟）
            Touch += MauiPlot_Touch;
        } else {
            // 移动端 → 手势识别器
            GestureRecognizers.Add(new PinchGestureRecognizer());   // 双指缩放
            GestureRecognizers.Add(new PanGestureRecognizer());      // 平移
            GestureRecognizers.Add(new TapGestureRecognizer());      // 双击 = 捏合点缩放
        }
    }
}
```

### WinUI（Windows 原生 3）

```csharp
public class WinUIPlot : UserControl, IPlotControl
{
    private readonly SKXamlCanvas _canvas = CreateRenderTarget();

    public WinUIPlot() {
        // ... ①②③④⑤
        Background = new SolidColorBrush(Colors.White);
        _canvas.PaintSurface += OnPaintSurface;      // 渲染
        _canvas.PointerWheelChanged += ...;          // 交互
        Content = _canvas;                            // 将 Canvas 设为唯一子控件
    }

    // ★ HiDPI 动态同步
    private void WinUIPlot_Loaded(...) {
        XamlRoot.Changed += (s, e) => DetectDisplayScale();  // DPI 变化时重检
        Plot.ScaleFactor = XamlRoot.RasterizationScale;
    }
}
```

### Eto（最特殊的渲染方式）

```csharp
public class EtoPlot : Drawable, IPlotControl
{
    // Eto 不支持 SKCanvas 直接绘制
    // 需要手动走：SKSurface → SKImage → SKPixmap → byte[] → Eto.Bitmap
    protected override void OnPaint(PaintEventArgs args) {
        using var surface = SKSurface.Create(imageInfo);       // ① 离屏渲染
        Multiplot.Render(surface.Canvas, rect);

        SKImage img = surface.Snapshot();                     // ② 截图
        SKPixmap pixels = img.ToRasterImage().PeekPixels();
        byte[] bytes = pixels.GetPixelSpan().ToArray();

        var bmp = new Bitmap(width, height, ...);             // ③ 转为 Eto Bitmap
        Marshal.Copy(bytes, 0, data.Data, bytes.Length);
        args.Graphics.DrawImage(bmp, 0, 0);                   // ④ 绘制到 Eto 画布
    }
}
```

---

## 五、OpenGL 包

```csharp
// ScottPlot.OpenGL 提供的扩展方法
public static ScatterGL ScatterGL(this PlottableAdder add,
    IPlotControl control, double[] xs, double[] ys)
{
    // 内部创建 ScatterSourceDoubleArray + IScatterSource
    // PlottableGL 类型要求 IPlotControl 提供 GRContext
    // 用于 GPU 硬件加速渲染大量散点
}

// 使用条件：
// ① 控件提供 GL 上下文 (GRContext != null)
// ② 控件须用 GL 变体: FormsPlotGL (WinForms) / WpfPlotGL (WPF) / BlazorPlotGL (Blazor)
//    (另有 ScatterGLCustom 扩展, 同样位于 ScottPlot.OpenGL)
```

**架构位置**：OpenGL 包位于 `ScottPlot5 Controls/` 下，但它不实现 `IPlotControl`，而是作为 `PlottableAdder` 的扩展方法，为 `IPlotControl` 添加 GPU 加速的 Plottable。

---

## 六、IMultiplot 多图系统

```csharp
public interface IMultiplot
{
    SubplotCollection Subplots { get; }               // 子图集合
    IMultiplotLayout Layout { get; set; }              // 布局策略
    MultiplotLayoutSnapshot LastRender { get; }        // 上次渲染快照
    MultiplotSharedAxisManager SharedAxes { get; }     // 共享轴管理
    List<IMultiplotPreRenderAction> PreRenderActions { get; }
    void Render(SKCanvas canvas, PixelRect figureRect); // 渲染入口
}
```

### 渲染流程

```
Multiplot.Render(canvas, figureRect)
    │
    ├─ SharedAxes.UpdateSharedPlotAxisLimits()
    │     → 遍历配置：哪些子图共享 X/Y 轴
    │     → 将主图的轴范围复制到从图
    │
    ├─ PreRenderActions.Invoke()
    │     → 用户注册的渲染前钩子
    │
    ├─ canvas.Clear()
    │
    ├─ Layout.GetSubplotRectangles(Subplots, figureRect)
    │     → 布局策略 (Rows ← 默认, Grid, Columns, CustomGrid)
    │     → 返回 PixelRect[] 分配给每个子图
    │
    └─ foreach plot in Subplots:
          plot.RenderManager.ClearCanvasBeforeEachRender = false
          plot.Render(canvas, subplotRectangle)
          LastRender.Remember(plot, rectangle)  // 记录位置供点击检测
```

### 使用方式

```csharp
// 方式1: 双图（AddPlot 是 IMultiplot 的扩展方法）
var mp = new Multiplot();
mp.AddPlot(plot1);
mp.AddPlot(plot2);
mp.Layout = new MultiplotLayouts.Rows();   // 上下排列（默认布局）

// 方式2: 2x2 网格
mp = new Multiplot() { Layout = new MultiplotLayouts.Grid(rows: 2, columns: 2) };

// 方式3: 共享轴
mp.SharedAxes.ShareX([plot1, plot2]);  // 两图共享X轴
```

---

## 七、控件生命周期

```
构造
  → Plot = new Plot { PlotControl = this }     // Plot 反向引用控件
  → Multiplot = new Multiplot(Plot)
  → UserInputProcessor = new(this)             // 绑定交互处理器
  → Menu = new XxxPlotMenu(this)               // 平台特定菜单
  → DisplayScale = DetectDisplayScale()        // 检测 DPI

运行时
  → Refresh()  ← 用户代码调用 / 交互响应调用
  → 平台 InvalidateVisual() / Invalidate()
  → 平台 OnPaint / OnPaintSurface
  → Multiplot.Render(canvas, rect)
  → RenderManager.Render(canvas, rect)         ← 25 步渲染管道

Reset(newPlot)  ← 热替换 Plot 对象
  → oldPlot = Plot; Plot = newPlot
  → oldPlot?.Dispose()                    // 释放旧 Plot
  → newPlot.PlotControl = this            // 更新反向引用
  → UserInputProcessor.Reset()            // 重建默认响应器列表
  → Multiplot.Reset(newPlot)
  // 注意: Reset 不主动调用 Refresh(), 由调用方决定何时重绘
```

---

## 八、各平台 HiDPI 检测方式

```csharp
// WinForms
float DetectDisplayScale() => DeviceDpi / 96f;        // 通过系统 DPI

// WPF
float DetectDisplayScale() {
    PresentationSource ps = PresentationSource.FromVisual(this);
    return (float)(ps?.CompositionTarget?.TransformToDevice.M11 ?? 1.0);
}

// Avalonia
float DetectDisplayScale() => (float)VisualRoot!.RenderScaling;

// WinUI
float DetectDisplayScale() => XamlRoot.RasterizationScale;

// Blazor: return 1.0f (TODO)
// Eto:    return LogicalPixelSize
// MAUI:   return 1.0f (固定)
```

检测到后统一写入 `Plot.ScaleFactorF`，RenderManager 在管道入口 `canvas.Scale(Plot.ScaleFactorF)` 缩放画布。

---

## 九、关键设计洞察

1. **抽象泄露的最小化**：每个控件仅 ~80 行核心代码，唯一平台相关的是事件订阅、HiDPI 检测、渲染承载。其余全部委托给 `UserInputProcessor` + `Multiplot` + `RenderManager`。

2. **双向引用模式**：`Plot.PlotControl = this` 在构造函数中建立双向引用，使得 Plottable（如 `DataLogger`）可以通过 `Plot.PlotControl.Refresh()` 触发重新渲染。这是一个刻意为之的循环引用，通过 `Dispose()` 链条解除。

3. **Avalonia 的独立渲染路径**：不走 SkiaSharp.Views，而是通过 `ISkiaSharpApiLeaseFeature` 直接从 Avalonia 的 SkiaSharp 后端获取画布。这避免了第三方依赖版本冲突。

4. **Eto 的"最重"渲染**：因为没有直接的 SKCanvas 承载，需要完整走 `SKSurface → Image → Pixmap → byte[] → Bitmap → Graphics` 流程，消耗最大。这是跨平台框架（Eto 封装 Gtk/WPF/WinForms）的限制。

5. **Blazor 的空菜单**：浏览器环境不支持原生右键菜单，`BlazorPlotMenu` 所有方法都是空操作。这体现了"即使不支持也实现接口"的设计选择，保持了类型一致性。

6. **MAUI 的手势适配**：桌面（Desktop idiom）和移动端使用完全不同的交互路径——桌面用 `SKTouchEventArgs`（模拟鼠标），移动端用 `PinchGestureRecognizer` + `PanGestureRecognizer`。`UserInputProcessor` 需要分别承载 `ProcessPanUpdated` 和 `ProcessPinchUpdated`。

7. **布局可插拔**：`IMultiplotLayout` 定义了布局策略接口，`Rows`（默认）、`Grid`、`Columns`、`CustomGrid` 都是实现。用户可以传入自定义布局器实现完全自由的子图排列。