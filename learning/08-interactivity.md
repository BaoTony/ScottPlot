# ScottPlot 5 交互系统架构剖析

> 25 个文件 · UserInputProcessor + 12 个 IUserActionResponse · ~3,500 行

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

## 五、ResponseInfo 状态机

```csharp
public struct ResponseInfo
{
    public bool IsPrimary;       // 只有当前响应器生效（独占模式）
    public bool RefreshNeeded;   // 是否需要重新渲染
}
```

**IsPrimary 生命周期**：
```
非 Primary 状态
    │
    │ 鼠标按下：匹配到 MouseDragPan
    ▼
IsPrimary = true    ← 独占！所有后续事件只发给此响应器
    │
    │ 持续收到 MouseMove 事件
    │ → 直接处理，不重新匹配
    ▼
鼠标弹起：ResetState()
IsPrimary = false   ← 释放独占权
    │
    ▼
非 Primary 状态（下一次事件重新匹配）
```

---

## 六、KeyboardState — 按键跟踪

```csharp
class KeyboardState
{
    void Press(Key key);             // 标记按下
    void Release(Key key);           // 标记释放
    void Reset();                    // 清空所有状态
    bool IsPressed(Key key);         // 某键是否按下
    bool IsShift { get; }            // Shift 键
    bool IsCtrl { get; }             // Ctrl 键
    bool IsAlt { get; }              // Alt 键
}
```

**用途**：`MouseWheelZoom` 根据 `IsCtrl` 决定是缩放 X 轴还是 Y 轴或 XY 同时缩放。

---

## 七、自定义交互响应器

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

## 八、关键设计洞察

1. **命令模式 (IUserAction)**：平台事件被封装为平台无关的 `IUserAction` 对象，`UserInputProcessor` 不依赖任何具体平台类型（WinForms/PointerPressed/MouseEventArgs 全被屏蔽）。

2. **责任链模式 (IUserActionResponse[])**：响应器按列表顺序依次尝试匹配，先到先得。`MouseInteractWithPlottables` 排在 `MouseDragPan` 之前，确保拖拽交互标记优先于全图平移。

3. **Primary Response 独占机制**：类似模态对话框——当 `MouseDragPan` 正在拖拽时，`IsPrimary=true` 阻止其他响应器处理中间事件，只有拖拽结束时才释放。这避免了"拖拽平移时误触发滚轮缩放"。

4. **默认顺序的精心编排**：`MouseDragZoomRectangle(Middle)` 第二、`MouseDragPan(Left)` 第三——中键比左键优先，`SingleClickAutoscale(Middle)` 在点击类第一位——都比拖拽类靠后，确保拖拽优先于单击。

5. **键盘修饰键的灵活组合**：`MouseWheelZoom(Shift, Ctrl)` 表示默认滚轮行为被 Shift+滚轮和 Ctrl+滚轮覆盖，从而支持分别缩放 X/Y 轴。

6. **状态重置的安全性**：`UserInputProcessor.Reset()` 遍历所有响应器调用 `ResetState()`，清理所有活跃的拖拽/按键状态，防止失焦后残留状态导致下次交互行为异常。