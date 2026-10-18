# ScottPlot 5 交互系统与跨平台控件架构

> Interactivity: 25 个文件 · Controls: 8个包 56 个文件 · ~7,000 行

---

## 一、交互系统架构

```
┌──────────────────────────────────────────────────────────────┐
│                    交互系统数据流                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  平台控件 (WinForms/WPF/Avalonia/...)                        │
│    │ 捕获原生事件: MouseDown, MouseMove, MouseWheel, KeyDown  │
│    │                                                          │
│    ▼                                                          │
│  UserInputProcessor (统一入口)                                │
│    │ ① 将平台事件 → IUserAction (平台无关)                    │
│    │ ② 遍历 UserActionResponses[] 依次尝试匹配                │
│    │ ③ 第一个匹配的响应器执行 → 可能修改 Plot → Refresh()     │
│    │                                                          │
│    ▼                                                          │
│  IUserActionResponse[] (可插拔响应器列表)                      │
│    ├── MouseDragPan           ← 左键拖拽平移                  │
│    ├── MouseDragZoom          ← 右键拖拽缩放                  │
│    ├── MouseDragZoomRectangle ← 中键拖拽矩形缩放               │
│    ├── MouseWheelZoom         ← 滚轮缩放 (±Shift/Ctrl)       │
│    ├── MouseInteractWithPlottables ← 拖拽交互标记              │
│    ├── SingleClickAutoscale   ← 中键单击自动缩放               │
│    ├── SingleClickContextMenu ← 右键单击菜单                   │
│    ├── DoubleClickBenchmark   ← 双击性能面板                  │
│    ├── KeyboardPanAndZoom     ← 方向键平移缩放                │
│    └── KeyboardAutoscale      ← A键自动缩放                   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 二、核心类型关系

```
IUserAction               ← "用户做了什么"（接口）
├── IMouseAction          ← 鼠标相关操作
│     ├── LeftMouseDown, LeftMouseUp
│     ├── RightMouseDown, RightMouseUp
│     ├── MiddleMouseUp, MiddleMouseDown
│     ├── MouseMove
│     └── MouseWheelUp, MouseWheelDown
├── KeyDown, KeyUp        ← 键盘按/放
└── Unknown               ← 未知操作

IUserActionResponse       ← "如何响应用户操作"（接口）
├── Execute(IPlotControl, IUserAction, KeyboardState) → ResponseInfo
└── ResetState(IPlotControl)

ResponseInfo (struct)     ← 响应结果
├── IsPrimary → 当前只有这个响应器生效（直到结果变化）
└── RefreshNeeded → 是否需要重新渲染

KeyboardState             ← 跟踪当前按下的键
    └── IsPressed(Key), IsShift, IsCtrl, IsAlt

MouseButton               ← 鼠标按钮抽象
    └── ButtonName, IsLeft, IsRight, IsMiddle

Key                       ← 键盘按键抽象
    └── KeyName, IsShift, IsCtrl, IsAlt
```

---

## 三、事件响应机制（以 MouseDragPan 为例）

```
1. 鼠标按下
   UserInputProcessor.ProcessMouseDown(e)
     → 封装成 LeftMouseDown 的 IUserAction
     → 遍历 UserActionResponses:
       MouseInteractWithPlottables → 检查是否在交互标记上 → 不是
       MouseDragZoomRectangle     → 中键触发 → 不匹配
       MouseDragPan               → 左键触发 → ★ 匹配！
         ResponseInfo { IsPrimary = true, RefreshNeeded = false }
         记录起始像素坐标

2. 鼠标移动
   UserInputProcessor.ProcessMouseMove(e)
     → 因为 MouseDragPan.IsPrimary → 直接调用它
     → 计算 Δx, Δy (像素位移)
     → 转为坐标位移: Δcoord = Δpixel × (coordRange / pixelRange)
     → Plot.Axes.Pan(Δx, Δy)     ← 修改轴范围
     → ResponseInfo { RefreshNeeded = true }
     → PlotControl.Refresh()     ← 触发重新渲染

3. 鼠标弹起
   UserInputProcessor.ProcessMouseUp(e)
     → MouseDragPan.IsPrimary → 完成
     → ResponseInfo { IsPrimary = false }  ← 释放独占权
```

---

## 四、UserInputProcessor 完整 API

```csharp
class UserInputProcessor
{
    // 基础控制
    void Enable() / Disable()   // 启用/禁用交互
    void Reset()                // 恢复到默认响应器列表

    // 响应器管理
    List<IUserActionResponse> UserActionResponses  // 自定义列表
    void RemoveAll<T>()         // 移除指定类型的响应器

    // 常用快捷配置
    void LeftClickDragPan(bool enable)           // 启用/禁用左键拖拽平移
    void RightClickDragZoom(bool enable)         // 启用/禁用右键拖拽缩放
    void DoubleLeftClickBenchmark(bool enable)   // 启用/禁用双击性能面板

    // 平台事件统一处理
    void ProcessMouseDown(e) / ProcessMouseUp(e)
    void ProcessMouseMove(e)
    void ProcessMouseWheel(e)
    void ProcessKeyDown(e) / ProcessKeyUp(e)
}
```

**默认响应器注册顺序**（先匹配先生效）：
```csharp
// 拖拽类 (高优先级)
MouseInteractWithPlottables(Left)    // 交互标记拖拽
MouseDragZoomRectangle(Middle)       // 矩形缩放
MouseDragPan(Left)                   // 平移
MouseDragZoom(Right)                 // 缩放

// 点击类
MouseWheelZoom(Shift, Ctrl)
SingleClickAutoscale(Middle)
SingleClickContextMenu(Right)
DoubleClickBenchmark(Left)

// 键盘类
KeyboardPanAndZoom()
KeyboardAutoscale(A)
```

---

## 五、跨平台控件架构

### 5.1 统一接口：IPlotControl

```csharp
public interface IPlotControl
{
    Plot Plot { get; }                  // 核心 Plot 对象
    IMultiplot Multiplot { get; set; }  // 多图支持
    void Refresh();                     // 触发布局+渲染
    UserInputProcessor UserInputProcessor { get; }
    IPlotMenu? Menu { get; set; }       // 右键菜单
    GRContext? GRContext { get; }       // OpenGL 上下文
    float DisplayScale { get; set; }    // 高分屏缩放
}
```

### 5.2 8 平台实现

| 平台 | 控件类 | NuGet 包 | 渲染方式 | 特殊处理 |
|---|---|---|---|---|
| **WinForms** | `FormsPlot` | `ScottPlot.WinForms` | SKControl (SkiaSharp.Views) | 设计时替代视图 |
| **WPF** | `WpfPlot` | `ScottPlot.WPF` | SKElement (SkiaSharp.Views) | 自定义 Measure/Arrange |
| **Avalonia** | `AvaPlot` | `ScottPlot.Avalonia` | ICustomDrawOperation | ClipToBounds + Focusable |
| **Blazor** | `BlazorPlot` | `ScottPlot.Blazor` | SKCanvas (JS interop) | 静态文件 + JS互操作 |
| **MAUI** | `MauiPlot` | `ScottPlot.Maui` | SKCanvasView | Handler 模式 |
| **WinUI** | `WinUIPlot` | `ScottPlot.WinUI` | SKXamlCanvas | WinUI 3 原生 |
| **Eto** | `EtoPlot` | `ScottPlot.Eto` | SKControl | 跨平台 GUI 框架 |
| **OpenGL** | `FormsPlotGL` | `ScottPlot.OpenGL` | GLControl | GPU 硬件加速 |

### 5.3 控件通用模式（以 WinForms 为例）

```csharp
// ① 构造函数：创建 Plot + UserInputProcessor + Menu
public FormsPlotBase()
{
    Plot = new() { PlotControl = this };   // Plot 反向引用控件
    Multiplot = new Multiplot(Plot);
    DisplayScale = DetectDisplayScale();
    UserInputProcessor = new(this);        // 绑定到自身
    Menu = new FormsPlotMenu(this);
}

// ② 事件处理：转发到 UserInputProcessor
void SKElement_MouseDown(sender, MouseEventArgs e)
{
    UserInputProcessor.ProcessMouseDown(e);   // → 交互系统
    base.OnMouseDown(e);                      // → WinForms 基类
}

// ③ 渲染：平台 OnPaint → Refresh → RenderManager
protected override void OnPaint(PaintEventArgs e)
{
    // SkiaSharp SKControl 自动调用 OnPaintSurface
    // → Multiplot.Render(skCanvas, pixelRect)
    // → RenderManager.Render(canvas, rect)
}

// ④ 重置：支持更换 Plot 实例
void Reset(Plot newPlot)
{
    Plot = newPlot;
    UserInputProcessor.Reset();           // 重置交互状态
    Multiplot.Reset(newPlot);
    Refresh();
}
```

---

## 六、多平台渲染差异

```
WinForms / WPF:
  控件 → OnPaint → SKControl.Render → SkiaSharp SKCanvas
    → Multiplot.Render() → 遍历 Subplot → RenderManager.Render()

Avalonia:
  Control.Render(DrawingContext) → CustomDrawOp → ISkiaSharpApiLeaseFeature
    → lease.SkCanvas → Multiplot.Render()

Blazor (Web):
  JS Interop → HTML Canvas → SKCanvas WebGL
    → BlazorPlotBase.Render() → Multiplot.Render()

MAUI / WinUI:
  原生 Handler → SKCanvasView → OnPaintSurface
    → Multiplot.Render()

Eto:
  SKControl.OnPaint → EtoPlot.Refresh()
```

**关键差异**：所有平台最终都汇合到 `Multiplot.Render(SKCanvas, PixelRect)` 这一个方法，之后完全走相同的 `RenderManager` 管道。这就是 `IPlotControl` 抽象的价值。

---

## 七、高分屏（HiDPI）支持

```csharp
// 控件构造函数中自动检测
float DisplayScale = DetectDisplayScale();
// → 从 DeviceDpi 或系统 API 获取缩放系数
// → Plot.ScaleFactorF = DisplayScale
// → RenderManager.Render() 中: canvas.Scale(Plot.ScaleFactorF)
// → 所有文字/线条自动缩放，视觉效果在所有 DPI 下一致
```

---

## 八、自定义交互响应器

```csharp
class MyCustomResponse : IUserActionResponse
{
    public ResponseInfo Execute(IPlotControl control, IUserAction action, KeyboardState keys)
    {
        if (action is not RightMouseDown)
            return ResponseInfo.NoAction;  // 不处理 → 继续下一个响应器

        // 自定义行为
        control.Plot.Title("右键点击!");
        return ResponseInfo.Refresh;       // 需要重新渲染
    }

    public void ResetState(IPlotControl control) { }
}

// 注册
plotControl.UserInputProcessor.UserActionResponses.Insert(0, new MyCustomResponse());
```

---

## 九、关键设计洞察

1. **命令模式 (IUserAction)**：平台事件被封装为平台无关的 `IUserAction` 对象，`UserInputProcessor` 不依赖任何具体平台类型。

2. **责任链模式 (IUserActionResponse[])**：响应器按列表顺序依次尝试匹配，第一个 `IsPrimary` 的响应器获得独占权，直到下一个事件才释放。这确保了拖拽期间不会被其他响应器干扰。

3. **事件桥接的薄层设计**：每个控件只有 ~80 行核心代码，做的就是"捕获原生事件 → 传给 UserInputProcessor → Refresh()"，所有复杂度都在共享的交互系统中。

4. **DisplayScale 自动检测**：不同平台有不同的 DPI 检测机制（WinForms: DeviceDpi, WPF: VisualTreeHelper, Avalonia: RenderScaling），但最终统一为 `Plot.ScaleFactorF`。

5. **Reset 模式**：允许运行时更换整个 Plot 实例（用户可完全重建图表而无需销毁控件），同时 `UserInputProcessor.Reset()` 清理所有拖拽中状态，防止状态泄漏。

6. **Primary Response 机制**：类似模态对话框——当 `MouseDragPan` 正在拖拽时，`IsPrimary=true` 阻止其他响应器处理中间事件，只有拖拽结束时才释放。这避免了"拖拽平移时误触发滚轮缩放"。