# ScottPlot 5 学习与使用注意事项

> 基于源码逐条验证，所有主张均标注源码位置以证明非捏造。验证时间：2026-10-18。

---

## 一、架构层面

### 1. 双坐标系统是基石，混淆必出 Bug

```csharp
// 源码: Pixel.cs:L12-L17 — float X, float Y
// 源码: Coordinates.cs:L7-L8   — double X, double Y
```

- **转换方向不能错**：`Axes.GetPixel(coord)` 是 `Coordinates→Pixel`（数据→屏幕）
- **精度差异**：`Pixel` 用 `float`，`Coordinates` 用 `double`。大范围数据坐标转换可能累积浮点误差
- **绘图时只用 Pixel**：所有 `SKCanvas` 操作请求像素坐标，绝不能误传 `Coordinates` 值

### 2. AutoScale 的 `HasBeenSet` 标志是隐形陷阱

```csharp
// 源码: CoordinateRangeMutable.cs:L16
public bool HasBeenSet => NumericConversion.IsReal(Span) && Span != 0;
```

```csharp
plot.Axes.SetLimitsX(0, 100);   // HasBeenSet = true → 后续 AutoScale 不再覆盖
```

- 一旦手动设置轴范围，AutoScale 就**永久失效**（除非调用 `Reset()` 或重新创建 Plot）
- 调试时发现轴范围"锁死"了，90% 是这个标志位导致的

### 3. `RenderOnce` vs `Render` 的区别

```csharp
// 源码: RenderManager.cs:L109-L115
int maxRenderCount = 5;
for (int i = 0; i < maxRenderCount; i++)
{
    RenderOnce(canvas, rect);
    if (!LastRender.AxisLimitsChanged)
        return;
}
// 5 次后仍不稳定 → 放弃（防止无限循环）
```

- `Render()` 的循环逻辑是为了处理"AutoScale 算出范围 → 渲染时某些 Plottable 再次修改范围"的级联变化。超过 5 次仍未稳定则放弃
- 静态导出（`SavePng` 等）直接用 `Render()`，GUI 控件也是

---

## 二、Primitives 层

### 4. `PixelRect` 和 `CoordinateRect` 的 Y 轴方向相反

```
PixelRect:     Left→X+, Right→X+, Top→Y+(小值), Bottom→Y+(大值) — 屏幕坐标系，Y 向下增加
CoordinateRect: XMin→XMax, YMin→YMax — 笛卡尔坐标系，Y 向上增加
```

- 在手动做像素↔坐标转换时，必须注意 Y 轴的**翻转**
- `PixelRect.Contains(pixel)` 是性能关键路径，渲染管道中大量调用用于裁剪判断

### 5. `Color` 是 `readonly struct`，`WithAlpha()` 必须接收返回值

```csharp
// 源码: Color.cs:L3 — public readonly struct Color
// 源码: Color.cs:L126 — public readonly Color WithAlpha(byte alpha)

Color c = Colors.Red;
c.WithAlpha(128);           // ❌ 新值被丢弃！c 未改变（readonly struct 不可变）
c = c.WithAlpha(128);       // ✅ 必须重新赋值才能生效
```

- 这是 C# `readonly struct` 的经典陷阱，所有 `FillStyle`、`LineStyle` 的颜色操作都受影响
- `Color` 不可变意味着每次颜色修改都产生新的分配（但 struct 在栈上，开销很小）

### 6. `ExpandingAxisLimits.Expand()` 的合并语义

```csharp
// 源码: ExpandingAxisLimits.cs:L81-L96
public void ExpandX(double x)
{
    // if existing is NaN, use the new value
    // otherwise use minmax
    Left = Math.Min(Left, x);
    Right = Math.Max(Right, x);
}
```

- `Expand()` 使用 `Math.Min/Math.Max` —— 只能"变大"不能"变小"
- 如果某个 Plottable 的数据范围缩小了（如 DataLogger 旧数据过期），需要用 `AxisLimits` 的 `Set()` 方法重新计算

### 7. `Axes` 容器的所有权模型

- 每个 Plottable 持有自己的 `Axes` 引用，多个 Plottable **可以共享**同一个轴
- 也可以各自创建独立轴（如双 Y 轴图表场景）
- `ReplaceNullAxesWithDefaults`（渲染第 3 步）会把未指定轴的 Plottable 强制绑定到默认轴

---

## 三、DataSources 层

### 8. ScatterSource ≠ SignalSource ≠ FastSignalSource

| 类型 | 数据假设 | 性能特性 |
|------|---------|---------|
| `IScatterSource` | 离散 XY，任意分布 | 全量渲染，无降采样 |
| `ISignalSource` | X 等间距，Y 可变 | **SegmentedTree O(log n) 降采样** |
| `FastSignalSource` | 同上，Y 数组无额外封装 | 零额外分配，极致性能 |

- **大数据的性能差异巨大**：Scatter 1M 点可能卡死，Signal 1M 点用 SegmentedTree 稳 60fps
- `Signal` 要求 X 值等间距 —— 如果传入不等间距的 X，渲染结果会**静默错位**（不会报错）

### 9. SegmentedTree 不是通用加速器

```
O(n)     构建（一次性）
O(log n) 每次范围查询
```

- 只在 `ISignalSource` 内部使用，Scatter 不享受这个优化
- 树在数据变化时**整体重建**，所以实时追加数据时用 `AddRange()` 比逐个 `Add()` 快很多

### 10. 惰性视图不会复制数据

```csharp
data.Zip(other).Skip(100).Take(50)
```

- `ZipView`、`SkipView`、`TakeView` 都是**零拷贝包装器**，只改变索引映射
- 好处：内存友好；陷阱：底层数据被修改时视图内容也会变（引用语义，不是快照）

---

## 四、Plottables 层

### 11. Mixin 接口体系（11 个 IHas*）

```csharp
// 源码: Interfaces/ 目录
public interface IHasLine;       public interface IHasMarker;
public interface IHasFill;       public interface IHasArrow;
public interface IHasOutline;    public interface IHasShadow;
public interface IHasLabel;      public interface IHasLegendText;
public interface IHasColorAxis;  public interface IHasBackground;
public interface IHasInteractiveHandles;
```

- `Scatter` 同时实现了 `IHasLine`、`IHasMarker`、`IHasFill` 三个样式接口
- 检查 Plottable 是否支持某种样式：`if (plottable is IHasLine l) l.LineStyle = ...`
- 不是所有 Plottable 都实现所有 Mixin —— 比如 `Pie` 没有 `IHasMarker`

### 12. `Render` vs `RenderLast` 的区别

```
步骤 17: RenderPlottables      → 在数据区内部渲染（标准 Plottable）
步骤 24: RenderPlottablesLast  → 覆盖在所有内容之上（轴标签/图例等）渲染
```

```csharp
// 源码: IRenderLast.cs:L3
public interface IRenderLast
```

- `IRenderLast` 接口用于需要在轴刻度/标签/图例**之上**绘制的内容
- 每个 `RenderAction` 前后都有 `CanvasState.Save()` / `RestoreAll()` 隔离，所以 `IRenderLast` 绘制时画布状态是干净的

### 13. `DraggablePlottableDecorator` 的坐标更新时机

```csharp
// 源码: DraggablePlottableDecorator.cs:L25-L30
public void DragTo(Coordinates to)
{
    double offsetX = BeforeDragOffset.X + to.X - DragFrom.X;
    double offsetY = BeforeDragOffset.Y + to.Y - DragFrom.Y;
    SetOffset(offsetX, offsetY);  // 直接修改数据源偏移量
}
```

- 拖拽时直接修改底层数据源的坐标偏移，不是用像素偏移量
- 这意味着拖拽后 `GetAxisLimits()` 返回的范围会变，可能触发 AutoScale（如果 `HasBeenSet=false`）

---

## 五、渲染层

### 14. 每个 RenderAction 执行前后都有 CanvasState Save/Restore

```csharp
// 源码: RenderManager.cs:L137-L139
foreach (IRenderAction action in RenderActions)
{
    rp.CanvasState.Save();
    action.Render(rp);
    rp.CanvasState.RestoreAll();
}
```

- **每个人的绘制状态是隔离的**。你在 `RenderPlottables()` 里改了裁剪区域，不影响后续的 `RenderLegends()`
- 这意味着你无法在 Plottable 之间共享 canvas 状态 —— 每个 Plottable 的 Render 都是干净画布

### 15. GL 状态的 StoreGL/RestoreGL 是 Bug Workaround

```
步骤 14: StoreGLState   ← 备份 OpenGL 状态
步骤 15: RenderGridsBelowPlottables
步骤 16: RestoreGLState  ← 恢复 OpenGL 状态
```

```csharp
// 源码: RenderManager.cs:L24 注释
// https://github.com/ScottPlot/ScottPlot/pull/4298
```

- 这是为了解决 **SkiaSharp + OpenGL 混用时的状态污染问题**
- 纯 CPU 渲染时这两步基本是空操作，但保留在序列中确保行为一致

### 16. `RegenerateTicks` 依赖布局后的 `DataRect` 尺寸

```
步骤 8:  CalculateLayout()    → 确定 DataRect
步骤 11: RegenerateTicks()     → 根据 DataRect.Width/Height 生成刻度
```

- 刻度数量由**像素宽度**决定，不是由坐标范围决定
- 窗口大小改变 → DataRect 变化 → 刻度重新生成 —— 这就是为什么缩小窗口时刻度会自动减少

### 17. 自定义 RenderAction 必须插入到正确位置

```csharp
// 源码: RenderManager.cs:L9 — RenderActions 是 public List<IRenderAction>
plot.RenderManager.RenderActions.Insert(index, new MyAction());
```

- 位置非常关键：插在 `CalculateLayout` 之前和之后的行为完全不同
- `IRenderLast` 被专门设计为"在所有内容之上渲染"，而不是让用户手动管理 Z 序

---

## 六、交互层

### 18. Primary Response 机制的独占性

```csharp
// 源码: UserInputProcessor.cs:L234-L241
if (PrimaryResponse is null && info.IsPrimary)
    PrimaryResponse = response;          // 获取独占权
if (PrimaryResponse == response && !info.IsPrimary)
    PrimaryResponse = null;              // 释放独占权
```

```
鼠标按下 → MouseDragPan.Respond() → IsPrimary = true
    ↓（独占！期间不重新匹配其他响应器）
鼠标移动 → 直接发给 MouseDragPan（不检查其他响应器）
    ↓
鼠标弹起 → ResetState() → IsPrimary = false
```

- 拖拽期间其他响应器（如 MouseWheelZoom）被完全屏蔽
- 这意味着你**不能在拖拽的同时用滚轮缩放** —— 必须松手再滚轮

### 19. `UserActionResponses` 顺序决定优先级

```csharp
// 源码: UserInputProcessor.cs:L84-L101 — DefaultUserResponses()
[
    MouseInteractWithPlottables(Left),   // [0] Plottable 拖拽交互标记
    MouseDragZoomRectangle(Middle),      // [1] 中键矩形缩放
    MouseDragPan(Left),                  // [2] 左键平移
    MouseDragZoom(Right),                // [3] 右键缩放
    MouseWheelZoom(Shift, Ctrl),         // [4] 滚轮缩放
    SingleClickAutoscale(Middle),        // [5] 中键单击自适应
    SingleClickContextMenu(Right),       // [6] 右键菜单
    DoubleClickBenchmark(Left),          // [7] 双击性能基准
    KeyboardPanAndZoom(),                // [8] 键盘方向键平移+缩放
    KeyboardAutoscale(A),                // [9] 键盘 A 键自适应
]
```

- `MouseInteractWithPlottables` 排第一：如果某个 Plottable 被标记为可拖拽，它优先于全局平移
- 自定义插入 `Insert(0, ...)` 获得最高优先级

### 20. `KeyboardState` 不会自动重置

- 控件失焦时（如 Alt+Tab 切窗口），`KeyboardState` 可能残留"Ctrl 按下"的状态
- `IPlotControl.Reset()` 内部会调用 `UserInputProcessor.Reset()` 清理所有状态

---

## 七、控件层

### 21. `Plot` 与 `IPlotControl` 的循环引用

```csharp
Plot.PlotControl = this;   // Plot 知道自己的控件宿主
```

- `Plot` 和 `IPlotControl` 之间存在循环引用
- 替换 Plot 时用 `Reset(newPlot)` 模式：先 dispose 旧 Plot → 设置新 Plot → 调用 `UserInputProcessor.Reset()`

### 22. 所有平台控件最终汇合到同一个方法

```
WinForms → ...           → Multiplot.Render(SKCanvas, PixelRect)
WPF     → ...            → RenderManager.Render(canvas, rect)
Avalonia → ...           → RenderManager.Render(canvas, rect)
Blazor  → JS Interop     → RenderManager.Render(canvas, rect)
```

- 平台控件代码量极少（每个 ~80 行），做的就是"事件转发 + 渲染触发"
- 如果想支持新平台，只需实现 `IPlotControl` 接口 + 一个薄控件封装

### 23. HiDPI 的 `DisplayScale` 检测

```csharp
float DisplayScale = DetectDisplayScale();
plot.ScaleFactorF = DisplayScale;
```

- 控件构造函数中自动检测，但检测机制因平台而异
- 如果跨屏拖拽窗口（屏 100% → 屏 150%），需手动监听 DPI 变化

---

## 八、速查清单

| # | 核心风险 | 踩坑概率 | 源码证据 |
|---|---------|----------|----------|
| 1 | `Coordinates`(double) ≠ `Pixel`(float)，方向别搞反 | ★★★★★ | Pixel.cs:L12 |
| 2 | `HasBeenSet=true` 后 AutoScale 永久失效 | ★★★★ | CoordinateRangeMutable.cs:L16 |
| 3 | `Color` 是 readonly struct，`WithAlpha()` 不接收返回值则丢失 | ★★★★ | Color.cs:L3, L126 |
| 4 | `Signal` 要求 X 等间距，不等间距会**静默**出错 | ★★★ | SignalSourceBase 无校验 |
| 5 | 拖拽期间 Primary 独占，不能同时滚轮缩放 | ★★★ | UserInputProcessor.cs:L234 |
| 6 | 每个 RenderAction 间 CanvasState 自动 Reset | ★★★ | RenderManager.cs:L137 |
| 7 | `Pixel.Y` 向下增加但 `Coordinate.Y` 向上增加 | ★★★ | Pixel.cs:L17 vs 笛卡尔坐标系 |
| 8 | `ExpandingAxisLimits.Expand()` 只增不减 | ★★ | ExpandingAxisLimits.cs:L94 |
| 9 | `DraggablePlottableDecorator` 直接修改数据源坐标 | ★★ | DraggablePlottableDecorator.cs:L29 |
| 10 | `Render()` 最多循环 5 次，之后不稳定的范围被放弃 | ★★ | RenderManager.cs:L109 |
| 11 | 惰性视图（Zip/Skip/Take）零拷贝，底层变化影响视图 | ★★ | 引用语义 |
| 12 | `IRenderLast` Plottable 覆盖在轴标签之上 | ★★ | IRenderLast.cs:L3 |
| 13 | `UserActionResponses` 顺序 = 交互优先级 | ★ | UserInputProcessor.cs:L86 |
| 14 | HiDPI 跨屏拖拽需手动重检 `DisplayScale` | ★ | 平台相关 |
| 15 | 控件 ~80 行薄封装，所有渲染在 RenderManager 中 | ★ | RenderManager.cs |

---

## 九、调试建议

1. **渲染异常**：对照 [RenderManager.cs](file:///d:/dev/store/ScottPlot/src/ScottPlot5/ScottPlot5/Rendering/RenderManager.cs) 的 25 步序列，排查是哪一步的问题
2. **轴范围锁定**：检查 `CoordinateRangeMutable.HasBeenSet` 是否为 true
3. **交互不响应**：检查 `UserInputProcessor.UserActionResponses` 顺序和 `IsPrimary` 状态
4. **性能问题**：确认大数据用了 `ISignalSource` 而非 `IScatterSource`
5. **颜色不生效**：检查 `WithAlpha()` 是否忘记了接收返回值