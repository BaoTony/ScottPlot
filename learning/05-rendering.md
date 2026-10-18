# ScottPlot 5 渲染管道深度剖析

> 职责：渲染管道深度剖析 — 25 步 RenderAction 序列 · RenderPack 上下文 · 关键步骤源码

---

## 数据流视角

```
┌─────────────────────────────────────────────────────────────┐
│                     渲染管道架构                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  触发源:                                                     │
│  control.Refresh()  Plot.SavePng()  平台控件 Invalidate()    │
│        │                                                     │
│        ▼                                                     │
│  RenderManager.Render(SKCanvas, PixelRect)                  │
│        │                                                     │
│        ├─ 最多重试 5 次 (轴范围连续变化时自动重渲染)           │
│        │                                                     │
│        └─ RenderOnce(canvas, rect)                           │
│              │                                               │
│              ├─ using RenderPack rp = new(Plot, rect, canvas)│
│              │                                               │
│              ├─ foreach IRenderAction in RenderActions       │
│              │     rp.CanvasState.Save()                     │
│              │     action.Render(rp)   ← 执行当前步骤        │
│              │     rp.CanvasState.RestoreAll()               │
│              │                                               │
│              ├─ 构建 RenderDetails                           │
│              │                                               │
│              └─ 触发事件:                                    │
│                   RenderFinished → SizeChanged → AxisLimitsChanged │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**注意**：`Plot` 本身没有 `Refresh()` 方法——它是 `IPlotControl` 的成员。平台控件的 `Invalidate()` 只是触发重绘事件，最终仍走 `control.Refresh()`。

---

## 一、IRenderAction 接口

```csharp
public interface IRenderAction
{
    void Render(RenderPack rp);
}
```

**极其简洁**：一个方法，一个参数 `RenderPack`。所有复杂性被封装在 25 个具体实现中。

---

## 二、RenderPack — 单次渲染的上下文

```csharp
public class RenderPack(Plot plot, PixelRect figureRect, SKCanvas canvas) : IDisposable
{
    SKCanvas Canvas;               // SkiaSharp 绘图画布
    CanvasState CanvasState;       // 画布状态机 (Save/Restore/Clip/Translate)
    Paint Paint;                   // 可复用的 SKPaint
    PixelRect FigureRect;          // 图表总区域
    PixelRect ScaledFigureRect;    // 缩放后的图表区域
    PixelRect DataRect;            // 数据区域 (计算后)
    Layout Layout;                 // 布局结果 (各面板尺寸)
    Plot Plot;                     // 回到 Plot 引用
    TimeSpan Elapsed;              // 自创建以来的耗时
}
```

**生命周期**：每次 `RenderOnce()` 创建新的 `RenderPack`，在 `using` 块结束时 `Dispose()` 释放 `Paint`。

---

## 三、25 步渲染序列详解

```
序号  RenderAction                     核心职责                    输入         输出
───── ────────────────────────────── ───────────────────────── ─────────── ─────────────
 1    PreRenderLock                   触发锁事件(用户挂载)        —            Event
 2    ClearCanvas                     清空画布(含半透明背景补偿)   Canvas       清空
 3    ReplaceNullAxesWithDefaults     未绑轴的Plottable→默认轴    PlottableList 修正后的Axes
 4    AutoScaleUnsetAxes              ★ 自动计算未设范围的轴范围   PlottableList 轴范围
 5    ContinuouslyAutoscale           连续自动缩放(条件性)        杂项          轴范围
 6    ExecutePlottableAxisManagers    DataLogger等自动管理轴范围   PlottableList 轴范围
 7    ApplyAxisRulesBeforeLayout      应用布局前的轴规则           轴规则        轴范围修正
 8    CalculateLayout                 ★ 计算Figure/Data布局矩形   轴面板        Layout
 9    RenderFigureBackground          绘制图表背景(含渐变)        图区          背景色
10    ApplyAxisRulesAfterLayout       布局后应用轴规则             轴规则        轴范围修正
11    RegenerateTicks                 ★ 重新生成所有轴的刻度      DataRect      Tick[]
12    RenderStartingEvent             触发渲染开始事件             —            Event
13    RenderDataBackground            绘制数据区背景               数据区        背景色
14    StoreGLState                    备份 OpenGL 状态             GL           状态快照
15    RenderGridsBelowPlottables      绘制下层网格线               轴刻度        网格
16    RestoreGLState                  恢复 OpenGL 状态             GL           状态恢复
17    RenderPlottables                ★★★ 绘制所有可见Plottable   PlottableList 图表
18    RenderGridsAbovePlottables      绘制上层网格线               轴刻度        网格
19    RenderLegends                   绘制图例                     LegendItem[] 图例
20    RenderPanels                    绘制面板(轴标签、标题等)     面板列表      标签
21    RenderBorders                   绘制图表边框                 轴            边框
22    RenderZoomRectangle             绘制缩放矩形                 ZoomRect      矩形
23    SyncGLPlottables                GPU Plottable 同步            GL           同步
24    RenderPlottablesLast            ★ IRenderLast Plottable     PlottableList 上层图表
25    RenderBenchmark                 绘制性能基准信息             计时数据      文本
```

**注意**：步骤 14-16 的 StoreGL/RestoreGL 是为了解决 [SkiaSharp + OpenGL 混用的 bug](https://github.com/ScottPlot/ScottPlot/pull/4298)，非 GL 场景可以忽略。

---

## 四、关键 RenderAction 深入

### 4.1 AutoScaleUnsetAxes（步骤4）

```csharp
public void Render(RenderPack rp)
{
    var visible = rp.Plot.PlottableList.Where(x => x.IsVisible);

    if (visible.Any())
    {
        // 有数据 → 根据 Plottable 的数据范围自动缩放
        foreach (var plottable in rp.Plot.PlottableList)
        {
            bool xNeedScale = !plottable.Axes.XAxis.Range.HasBeenSet;
            bool yNeedScale = !plottable.Axes.YAxis.Range.HasBeenSet;
            if (xNeedScale || yNeedScale)
                plot.Axes.AutoScale(plottable.Axes.XAxis, plottable.Axes.YAxis, ...);
        }
    }
    else
    {
        // 无可见数据 → 仅对未手动设置范围的底/左轴应用默认范围 [-10, 10]
        if (!plot.Axes.Bottom.Range.HasBeenSet)
            plot.Axes.SetLimitsX(AxisLimits.Default);

        if (!plot.Axes.Left.Range.HasBeenSet)
            plot.Axes.SetLimitsY(AxisLimits.Default);
    }
}
```

**决策逻辑**：只有用户未手动设置范围的轴才自动缩放。一旦调用 `plot.Axes.SetLimitsX(0, 100)`，`HasBeenSet = true`，后续 AutoScale 不再覆盖。

### 4.2 CalculateLayout（步骤8）

```
FigureRect (画布总区域)
    │
    ├─────────────────────────────────────────────────────
    │  布局引擎 (LayoutEngine) 测量各面板:
    │
    │  panel |   MeasuredSize  |  方向
    │  ──────┼─────────────────┼──────
    │  标题   |   30 px (高度)   |  上
    │  X轴标签 |   40 px (高度)  |  下
    │  Y轴标签 |   60 px (宽度)  |  左
    │  Y轴2标签|    0 px        |  右
    │  图例   |  150 px (宽度)  |  右
    │  颜色轴  |   80 px (宽度)  |  右
    │
    │  结果:
    │  DataRect = FigureRect - panel sizes
    │     → PixelRect(60, FigureWidth-230, 30, FigureHeight-40)
    └──────────────────────────────────────────────────────
```

**Layout** 结果包含（`readonly struct`，定义于 [Layout.cs](file:///d:/dev/store/ScottPlot/src/ScottPlot5/ScottPlot5/Primitives/Layout.cs#L3)）：
```csharp
public readonly struct Layout
{
    PixelRect FigureRect;                     // 计算布局时的图表区域
    PixelRect DataRect;                       // 数据绘制区域
    Dictionary<IPanel, float> PanelSizes;     // 各面板尺寸（垂直于数据区边缘）
    Dictionary<IPanel, float> PanelOffsets;   // 各面板距数据区边缘的偏移
}
```

### 4.3 RegenerateTicks（步骤11）

```csharp
public void Render(RenderPack rp)
{
    // 收集所有被 Plottable 使用的X轴（去重）
    var xAxesWithData = rp.Plot.PlottableList.Select(x => x.Axes.XAxis).Distinct();
    foreach (IXAxis xAxis in xAxesWithData)
        xAxis.RegenerateTicks(rp.DataRect.Width, rp.Paint);  // 像素宽度决定了刻度数量

    // 同理处理 Y 轴
    var yAxesWithData = rp.Plot.PlottableList.Select(x => x.Axes.YAxis).Distinct();
    foreach (IYAxis yAxis in yAxesWithData)
        yAxis.RegenerateTicks(rp.DataRect.Height, rp.Paint);
}
```

**关键**：刻度数量由 `DataRect.Width/Height` 决定 —— 屏幕宽度 300px 和 1200px 生成的刻度数是不同的。

### 4.4 RenderPlottables（步骤17）— 核心渲染

```csharp
public void Render(RenderPack rp)
{
    foreach (IPlottable plottable in visiblePlottables)
    {
        plottable.Axes.DataRect = rp.DataRect;  // ← 注入数据区到每个 Plottable

        rp.CanvasState.Save();

        if (plottable is IPlottableGL plottableGL)
        {
            plottableGL.Render(rp);              // OpenGL 路径（不裁剪）
        }
        else
        {
            rp.CanvasState.Clip(rp.DataRect);   // 标准路径（裁剪到数据区）
            plottable.Render(rp);
        }

        rp.CanvasState.DisableClipping();
    }
}
```

**CanvasState.Save/RestoreAll 保证了每个 Plottable 的绘制状态完全隔离**——A 的变换不会影响 B。

### 4.5 ContinuouslyAutoscale（步骤5）

```
条件: 仅当 plot.Axes.ContinuouslyAutoscale 为 true 时启用
行为: 调用 plot.Axes.ContinuousAutoscaleAction.Invoke(rp) 调整轴范围，使所有数据始终可见
场景: 实时数据流、动画
```

---

## 五、自动重渲染机制

```csharp
public void Render(SKCanvas canvas, PixelRect rect)
{
    int maxRenderCount = 5;
    for (int i = 0; i < maxRenderCount; i++)
    {
        RenderOnce(canvas, rect);
        if (!LastRender.AxisLimitsChanged)
            return;  // 轴范围稳定 → 结束
    }
    // 5次后仍然不稳定 → 放弃（防止无限循环）
}
```

**为什么需要重渲染？**：第一遍渲染时轴范围可能由 AutoScale 决定，但某些 Plottable 需要知道轴范围才能决定渲染内容（如 `DataLogger`），这可能导致轴范围在渲染中再次变化。重渲染直到范围稳定。

---

## 六、事件系统

```
RenderManager 事件:
├── PreRenderLock            → 渲染前触发 (用户可加锁/同步)
├── RenderStarting           → 布局+刻度生成后触发
├── RenderFinished           → 每次渲染完成后触发
├── SizeChanged              → 画布尺寸变化时触发
└── AxisLimitsChanged        → 轴范围变化时触发

事件在渲染管道中不打断流程，而是渲染完成后一次性触发。
```

---

## 七、OpenGL 支持路径

```
IPlottableGL 接口 (继承 IPlottable):
├── PlotControl    { get; }     ← 渲染时经它访问 GRContext (GPU 上下文)
├── GLFinish()                  ← 手动同步 GPU 渲染
├── StoreGLState()              ← 保存 OpenGL 状态
└── RestoreGLState()            ← 恢复 OpenGL 状态

支持 IPlottableGL 的 Plottable:
└── ScatterGL  (位于 ScottPlot.OpenGL 扩展包, 核心库无任何实现者)

GL 相关 RenderActions:
├── StoreGLState (14)  → 备份 GL 状态
├── RestoreGLState (16) → 恢复 GL 状态
└── SyncGLPlottables (23) → 同步 GPU 渲染
```

---

## 八、自定义渲染步骤

```csharp
// 方式1: 在指定位置插入自定义动作
plot.RenderManager.RenderActions.Insert(8, new MyCustomAction());

// 方式2: 移除某一步
plot.RenderManager.RenderActions.Remove<RenderBenchmark>();

// 方式3: 替换整个列表
plot.RenderManager.RenderActions.Clear();
plot.RenderManager.RenderActions.AddRange([...]);
```

---

## 九、性能计时与基准测试

每个 `RenderOnce` 调用都会记录每步的耗时：

```csharp
RenderDetails (readonly struct):
├── Elapsed: TimeSpan             ← 总渲染时间
├── TimedActions: (string, TimeSpan)[]  ← 每步耗时
│   e.g. [("PreRenderLock", 0ms), ("ClearCanvas", 0.5ms),
│          ("CalculateLayout", 2ms), ("RenderPlottables", 45ms), ...]
├── Count: int                    ← 渲染总次数 (含本次)
├── AxisLimitsChanged / SizeChanged: bool  ← 与上次渲染对比的变化标记
└── Layout / AxisLimitsByAxis     ← 布局结果与所有轴的范围快照
```

第 25 步的 `RenderBenchmark` 是独立的 RenderAction（在图像右上角绘制性能文字），不属于 RenderDetails。

---

## 十、关键设计洞察

1. **策略模式管道的极致实践**：`List<IRenderAction>` 是可插拔的渲染管道，每个步骤职责单一、可增删改。这是"开闭原则"在渲染系统中的完美体现。

2. **RenderPack 如同 HTTP Context**：每一次渲染都创建一个新的 `RenderPack`，携带所有必要的上下文信息（画布、布局、计时），在管道各步骤间流转。这类似于 ASP.NET 的 `HttpContext` 设计。

3. **CanvasState 是 SkiaSharp 的安全层**：SkiaSharp 的 `Save/Restore` 如果次数不配对会崩溃。ScottPlot 的 `CanvasState` 通过 `SaveLevels` 计数器跟踪调用层次，`RestoreAll()` 提供安全重置。

4. **Layout 计算是两阶段的**：步骤 8 计算布局→步骤 11 重新生成刻度。因为刻度标签的尺寸需要在 Layout 确定后才能精确计算（如轴标签文字宽度影响 DataRect 大小）。

5. **Z 序由 RenderAction 顺序决定**：先渲染的在下层。标准 Plottable 在步骤 17，`IRenderLast` Plottable 在步骤 24，网格线在 15/18 分上下两层。

6. **最多 5 次重试是防御性设计**：当 DataLogger 等自动管理轴范围的 Plottable 导致轴范围震荡时，最多重试 5 次后放弃，防止无限循环。这是一种实用的启发式限制。