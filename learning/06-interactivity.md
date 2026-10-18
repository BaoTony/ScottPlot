# ScottPlot 5 交互系统架构剖析

> UserInputProcessor + 13 个响应器（默认注册 10 个）· IPlotControl 无关平台

---

## 数据流视角

```
鼠标/键盘事件（平台控件捕获）
  → UserInputProcessor.ProcessXXX()     ← 封装为 IUserAction（平台无关）
  → 遍历 UserActionResponses[] 责任链    ← 第一个匹配者独占（IsPrimary）
  → 修改 Plot 状态（Axes.Pan / SetLimits）
  → PlotControl.Refresh()               ← 触发 25 步渲染管道（05-rendering）
```

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
│  UserActionResponses[] (可插拔响应器列表, 默认注册 10/13)      │
│    ├── MouseInteractWithPlottables ← 左键拖拽交互标记 (优先)   │
│    ├── MouseDragZoomRectangle ← 中键拖拽矩形缩放               │
│    ├── MouseDragPan           ← 左键拖拽平移                  │
│    ├── MouseDragZoom          ← 右键拖拽缩放                  │
│    ├── MouseWheelZoom         ← 滚轮缩放 (Shift/Ctrl 锁轴)    │
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

ResponseInfo (readonly record struct) ← 响应结果
├── RefreshNeeded → 是否需要重新渲染
├── IsPrimary → 当前只有这个响应器生效（直到结果变化）
└── 静态快捷值: NoActionRequired / Refresh

KeyboardState             ← 跟踪当前按下的键 (内部 HashSet<string>)
    └── Add(Key), Remove(Key), Reset(), IsPressed(Key/键集合/键名)

MouseButton (record struct) ← 鼠标按钮抽象
    └── Name (StandardMouseButtons 提供 Left/Right/Middle 实例)

Key (readonly record struct) ← 键盘按键抽象
    └── Name (StandardKeys 提供 Shift/Control/A 等实例)
```

---

## 三、事件响应机制（以 MouseDragPan 为例）

```
1. 鼠标按下
   平台扩展方法 ProcessMouseDown(e)  (如 WpfPlotExtensions)
     → 封装成 UserActions.LeftMouseDown
     → UserInputProcessor.Process(action) 遍历 UserActionResponses:
       MouseInteractWithPlottables → 检查是否在交互标记上 → 不是
       MouseDragZoomRectangle     → 中键触发 → 不匹配
       MouseDragPan               → 左键触发 → ★ 匹配！
         记录起始像素坐标 (MouseDownPixel) 与当前轴范围 (RememberedLimits)
         返回 NoActionRequired    ← 注意: 按下时并不抢占 Primary

2. 鼠标移动
   ProcessMouseMove(e) → UserActions.MouseMove
     → MouseDragPan 检测到拖拽中 (RememberedLimits 非空)
     → 位移 < 5px 忽略 (为单击/双击事件留余地)
     → 先 Recall() 还原轴范围, 再经 MouseAxisManipulation.DragPan()
       按像素位移应用平移
     → ResponseInfo { IsPrimary = true, RefreshNeeded = true }
       ↑ 此刻才抢占 Primary, 之后其他响应器被跳过
     → Process() 末尾统一调用 PlotControl.Refresh()

3. 鼠标弹起
   ProcessMouseUp(e) → UserActions.LeftMouseUp
     → MouseDragPan 还原轴范围并应用最终位置, 返回 Refresh
     → 返回结果不含 IsPrimary → PrimaryResponse 清空  ← 释放独占权
```

---

## 四、UserInputProcessor 完整 API

```csharp
class UserInputProcessor
{
    // 基础控制
    void Enable() / Disable()   // 启用/禁用交互
    void Reset()                // 恢复默认响应器列表 (并清空按键状态)

    // 响应器管理
    List<IUserActionResponse> UserActionResponses  // 可插拔列表
    void RemoveAll<T>()         // 移除指定类型的响应器

    // 常用快捷配置
    void LeftClickDragPan(bool enable, bool horizontal = true, bool vertical = true)
    void RightClickDragZoom(bool enable, bool horizontal = true, bool vertical = true)
    void DoubleLeftClickBenchmark(bool enable)   // 启用/禁用双击性能面板

    // 核心入口 (平台无关)
    void Process(IUserAction userAction)  // 处理后按需 PlotControl.Refresh()
}
```

**注意**：`ProcessMouseDown / ProcessMouseMove / ProcessMouseWheel / ProcessKeyDown` 等方法**不在 UserInputProcessor 上**——它们是各平台的扩展方法（`WpfPlotExtensions`、`AvaPlotExtensions`、`EtoPlotExtensions`、`BlazorPlotExtensions`），负责把平台事件翻译成 `IUserAction` 后调用 `Process()`。

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
public readonly record struct ResponseInfo
{
    public bool IsPrimary { get; init; }       // 只有当前响应器生效（独占模式）
    public bool RefreshNeeded { get; init; }   // 是否需要重新渲染

    // 静态快捷值
    public static ResponseInfo NoActionRequired { get; }  // 不处理 → 继续下一个响应器
    public static ResponseInfo Refresh { get; }           // 需要重新渲染
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
    void Add(Key key);                   // 标记按下
    void Remove(Key key);                // 标记释放
    void Reset();                        // 清空所有状态
    bool IsPressed(Key key);             // 某键是否按下
    bool IsPressed(IEnumerable<Key> keys); // 任一键按下即 true
    bool IsPressed(string keyName);      // 按键名判断
    int PressedKeyCount { get; }         // 已按下键的数量
}
```

**注意**：内部是 `HashSet<string>`（按键名）。KeyboardState **没有** `IsShift/IsCtrl/IsAlt` 属性——响应器通过 `keys.IsPressed(StandardKeys.Shift)` 这类调用判断修饰键。`MouseWheelZoom` 的语义：按住 **Shift 锁定 X 轴**（只缩放 Y）、按住 **Ctrl 锁定 Y 轴**（只缩放 X），缩放步幅 `ZoomFraction` 默认 0.15。

---

## 七、自定义交互响应器

```csharp
class MyCustomResponse : IUserActionResponse
{
    public ResponseInfo Execute(IPlotControl control, IUserAction action, KeyboardState keys)
    {
        if (action is not RightMouseDown)
            return ResponseInfo.NoActionRequired;  // 不处理 → 继续下一个响应器

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

5. **键盘修饰键的灵活组合**：`MouseWheelZoom` 默认构造为 `MouseWheelZoom(StandardKeys.Shift, StandardKeys.Control)`——按住 Shift 锁定水平（只缩放 Y），按住 Ctrl 锁定垂直（只缩放 X），实现分轴缩放。

6. **状态重置的两层机制**：`Reset()` 是**重建默认响应器列表**并清空按键状态；真正遍历所有响应器调用 `ResetState()` 的是静态方法 `UserInputProcessor.ResetState(control)`——控件失焦时经 `LostFocusAction` 自动触发，清理活跃的拖拽/按键状态，防止残留状态导致下次交互行为异常。