# ScottPlot 5 数据源系统深度剖析

> 约占核心库 1/13 · Scatter / Signal / OHLC / 实时流 四大体系

---

## 数据流视角

```
用户数据 (double[] / List<T> / IDataSource<T>)
  → PlottableAdder 自动包装为对应的 ISource 实现
  → IXXXSource（本章主角）
      Scatter:  GetScatterPoints() → Coordinates[]（ZipView 惰性视图，零拷贝）
      Signal:   GetPixelColumns() → SegmentedTree 降采样 → 每像素列画 min→max
  → IPlottable.Data（→ 06-plottables）

导出链路: plot.SavePng() → GetImage(800,600) → RenderManager.Render() → Encode
                                  ↑ 与交互渲染共用同一管道
```

---

## 一、总览：数据源分类

```
┌──────────────────────────────────────────────────────────────────┐
│                    DataSources 层全景                              │
├──────────────────────┬────────────────────┬─────────────────────┤
│ IScatterSource       │ ISignalSource      │ IOHLCSource         │
│ 离散XY散点数据       │ 等间距大数据        │ 金融K线数据          │
├──────────────────────┼────────────────────┼─────────────────────┤
│ 实时数据流           │ 优化引擎            │ 辅助                │
│ DataLogger/Streamer  │ SegmentedTree      │ Function, Vector... │
│                      │ MinMaxCache        │ CoordinateData...   │
│                      │ SignalInterpolation│                     │
└──────────────────────┴────────────────────┴─────────────────────┘
```

---

## 二、IScatterSource 系列（离散 XY 数据）

### 2.1 接口定义

```
IScatterSource               ← 核心接口
├── IReadOnlyList<Coordinates> GetScatterPoints()
├── DataPoint GetNearest(Coordinates, RenderDetails, maxDistance)
├── DataPoint GetNearestX(Coordinates, RenderDetails, maxDistance)
├── CoordinateRange GetLimitsX() / GetLimitsY()
├── AxisLimits GetLimits()
└── int MinRenderIndex / MaxRenderIndex    ← 支持部分渲染
```

### 2.2 5 种实现对照

| 实现类 | 内部存储 | 适用场景 | PreferCoordinates |
|---|---|---|---|
| `ScatterSourceDoubleArray` | `double[] Xs, Ys` | 通用双数组 | false (ZipView 懒合并) |
| `ScatterSourceCoordinatesArray` | `Coordinates[]` | 预设坐标数组 | true (直接返回) |
| `ScatterSourceCoordinatesList` | `List<Coordinates>` | 动态增删 | true |
| `ScatterSourceGenericArray<T>` | `T[]` (泛型) | 自定义类型数据 | false |
| `ScatterSourceGenericList<T>` | `List<T>` (泛型) | 自定义类型+动态 | false |

### 2.3 ZipView 懒合并技术

```csharp
// ScatterSourceDoubleArray 的核心：不预先分配 Coordinates 数组
public IReadOnlyList<Coordinates> GetScatterPoints()
{
    return Xs.ZipView(Ys, (x, y) => new Coordinates(x, y))
             .SkipView(MinRenderIndex)
             .TakeView(this.GetRenderIndexCount());
}
```

`ZipView` 是 ScottPlot 内部的 LINQ 扩展，**惰性求值**——`GetScatterPoints()` 返回的是 `IReadOnlyList` 视图而非完整拷贝，只在 `foreach` 遍历时才逐个创建 `Coordinates` 实例。这避免了百万级数据的 O(n) 内存复制。

### 2.4 最近点查询（GetNearest）

```csharp
// ScatterSourceDoubleArray 委托给 DataSourceUtilities 的智能查询
public DataPoint GetNearest(Coordinates mouseLocation, RenderDetails renderInfo, float maxDistance = 15)
    => DataSourceUtilities.GetNearestSmart(this, mouseLocation, renderInfo, maxDistance);
```

`GetNearestSmart` 根据 **renderInfo 中的像素缩放因子**，将 `maxDistance`(px) 转换为坐标距离阈值，遍历可见范围内的点找到最近者，避免扫描全部数据。

### 2.5 CacheScatterLimitsDecorator（装饰器模式，可选）

```csharp
// 文件: DataSources/ScatterSourceWithCachedLimits.cs（文件名与类名不一致，注意）
public class CacheScatterLimitsDecorator(IScatterSource source) : IScatterSource
{
    private AxisLimits? _axisLimits = null;
    // 首次调用计算，后续直接返回缓存（GetLimitsX/Y 同理）
    public AxisLimits GetLimits() => _axisLimits ??= _source.GetLimits();
}
```

**重要事实**：该装饰器只是**可选的公共工具类**——核心库中没有任何地方实例化它，
`PlottableAdder` 创建 Scatter 时**不会自动包裹**：

```
PlottableAdder.Scatter(xs, ys)
  → source = new ScatterSourceDoubleArray(xs, ys)
  → new Scatter(source)          ← 直接传入，无自动装饰
```

若数据静态且 GetLimits() 被高频重复调用，可手动 `new CacheScatterLimitsDecorator(source)` 后传给 Scatter。

---

## 三、ISignalSource 系列（等间距大数据）

### 3.1 与 IScatterSource 的本质区别

```
IScatterSource                  ISignalSource
─────────────────────────────────────────────────
每个点都有独立 XY                只有 Y 值，X = index*Period + Offset
逐点渲染                         降采样渲染（每像素列只绘制 Min/Max）
内存占用: 每个点 16 字节          内存占用: 每个点 8 字节
适合 <10万点                    适合 >10万点 ~ 亿级
 nearest 查询是 O(n)              nearest 是 O(1) (X 由 index 直接计算)
```

### 3.2 接口定义与基类

```
ISignalSource 接口:
├── double Period { get; set; }        ← X 间隔
├── double XOffset { get; set; }       ← X 偏移（第0个点的X位置）
├── double YOffset { get; set; }       ← Y 偏移
├── double YScale { get; set; }         ← Y 缩放因子
├── int MinimumIndex / MaximumIndex     ← 可见范围
├── IReadOnlyList<double> GetYs()
├── double GetY(int index)
├── PixelColumn GetPixelColumn(IAxes axes, int xPixelIndex)
└── SignalRangeY GetLimitsY(int first, int last)

SignalSourceBase (abstract):
  提供 Period/XOffset/YOffset 公共实现 + GetIndex()/GetX() 通用算法
```

### 3.3 实现矩阵

| 实现类 | 基类 | 内部数据 | 使用优化 |
|---|---|---|---|
| `SignalSourceDouble` | `SignalSourceBase` | `double[]` | SegmentedTree |
| `FastSignalSourceDouble` | `SignalSourceBase` | `IReadOnlyList<double>` | MinMaxCache |
| `SignalSourceGenericArray<T>` | — | `T[]` | SegmentedTree\<T\> |
| `SignalSourceGenericList<T>` | — | `List<T>` | SegmentedTree\<T\> |
| `SignalConstSource<T>` | `SignalSourceGenericArray<T>` | `T[]`（数值类型） | SegmentedTree（静态大数据，配合 SignalConst\<T\>） |
| `SignalXYSourceDoubleArray` | — | `double[] Xs, double[] Ys` | 不等间距但大数据 |
| `SignalXYSourceGenericArray<T>` | — | `T[]` | 不等间距大数据 |
| `SignalXYSourceGenericList<T>` | — | `List<T>` | 不等间距+动态 |

### 3.4 GetPixelColumn — 每像素列的降采样

```csharp
// FastSignalSourceDouble.GetPixelColumn
public PixelColumn GetPixelColumn(IAxes axes, int xPixelIndex)
{
    float xPixel = axes.DataRect.Left + xPixelIndex;
    double xRangeMin = axes.GetCoordinateX(xPixel);
    float xUnitsPerPixel = (float)(axes.XAxis.Width / axes.DataRect.Width);
    double xRangeMax = xRangeMin + xUnitsPerPixel;

    int i1 = GetIndex(xRangeMin, true);
    int i2 = GetIndex(xRangeMax, true);

    // 查询 SegmentedTree/MinMaxCache 获取该区间 [i1,i2] 的 min/max
    SignalRangeY range = GetLimitsY(i1, i2);

    return new PixelColumn(xPixel, range.Min, range.Max);
}
```

**核心逻辑**：每屏幕像素列对应 X 轴上的一个微小范围，查询该范围内所有数据点的 min/max，只画一条竖线（min→max）+ 一个点（均值），实现**以像素为单位的降采样**。

---

## 四、SegmentedTree — 核心降采样引擎

### 4.1 数据结构

```
原始数组: [3, 1, 4, 1, 5, 9, 2, 6]
                   ↓ 填充到 2的幂 (n=8)
           ┌────────[1, 9]─────────┐ (root, index=1)
       ┌─[1, 4]─┐             ┌─[2, 6]─┐ (level 1, index=2,3)
    [1,3]    [1,4]        [5,9]    [2,6]  (level 2, index=4,5,6,7)
   3   1    4   1        5   9    2   6   (叶子=原始数据, index=8..15)

TreeMin[i] 存储子树的最小值, TreeMax[i] 存储子树的最大值
叶子层对齐: 原始索引 k → 树索引 n + k (n 是2的幂)
```

### 4.2 MinMaxRangeQuery — O(log n) 范围查询

```csharp
public void MinMaxRangeQuery(int l, int r, out double lowest, out double highest)
{
    // 算法: 从 l,r 向上遍历线段树
    // 1. 处理底部不成对节点 (单个叶子)
    if ((l & 1) == 1) // l是右子节点 → 单独处理
    if ((r & 1) != 1) // r是左子节点 → 单独处理

    // 2. 上移到树层
    l = (l + n + 1) / 2;
    r = (r + n - 1) / 2;

    // 3. 逐层向上，遇到完整覆盖的子树直接用 TreeMin/TreeMax
    while (l <= r)
    {
        if ((l & 1) == 1) { min = Min(min, TreeMin[l]); max = Max(max, TreeMax[l]); }
        if ((r & 1) != 1) { min = Min(min, TreeMin[r]); max = Max(max, TreeMax[r]); }
        l = (l + 1) / 2;
        r = (r - 1) / 2;
    }
}
// 复杂度: O(log n)，最多访问 2*log₂(n) 个树节点
```

### 4.3 渲染性能公式

```
屏幕宽度 W 像素，数据 N 个点，每像素调用 MinMaxRangeQuery

总复杂度: W * O(log N) = O(W log N)

例子:
  N=1,000,000, W=800
  800 * log₂(1,000,000) = 800 * 20 = 16,000 次节点访问
  对比全量遍历: 1,000,000 次节点访问
  加速比: 62.5x
```

### 4.4 SegmentedTree vs MinMaxCache

```
SegmentedTree<T>                    MinMaxCache
─────────────────────────────────   ──────────────────────
通用泛型 (任意 IComparable<T>)      仅 double[]
O(n) 构建线段树                      O(n/cachePeriod) 构建缓存 (支持并行)
O(log n) 单点更新                    不支持单点更新
O(log n) 区间查询                    O(1) 缓存命中, O(cachePeriod) cache miss
内存: 2*2^ceil(log₂(N))            内存: 2*N/cachePeriod
适合静态/低频更新大数据               适合频繁更新的 Signal 数据 (FastSignalSourceDouble)
```

---

## 五、实时数据系统

### 5.1 DataLoggerSource — 追加模式

```csharp
class DataLoggerSource(List<Coordinates> coordinates)
{
    void Add(Coordinates coords)     // 追加新点（要求 X 递增）
    void Clear()                     // 清空所有数据
    void OnRendered()                // 标记"已渲染"，清除 HasNewData 标志

    // 渲染判断: HasNewData → 需要重新渲染
    //            WasRendered → 已渲染过 (用于首次渲染检测)
}
```

**使用场景**：持续采集数据，每次追加 N 个点 → 渲染最新数据。

### 5.2 DataStreamerSource — 环形缓冲区

```csharp
class DataStreamerSource(double[] data)  // data: 固定长度缓冲区
{
    double[] Data;                   // 固定长度环形缓冲区
    int NextIndex;                   // 下次写入位置
    int NewestIndex;                 // 最新数据位置
    int CountTotal;                  // 总共添加的点数
    double DataMin, DataMax;         // 所有历史数据的 min/max

    void Add(double value)           // 写入环形缓冲区 (不回退)
    void AddRange(IEnumerable<double>)

    // 渲染: 总是渲染整个缓冲区（最新 N 个点）
    // 轴范围: 自动跟踪 DataMin/DataMax
}
```

**使用场景**：实时信号监测，只要最近 N 个数据点，旧数据自动覆盖。

### 5.3 关键对比

| | DataLoggerSource | DataStreamerSource |
|---|---|---|
| 缓冲区模型 | 无限增长 List | 固定长度环形数组 |
| 内存占用 | 随时间增长 | 恒定 |
| X轴范围 | 动态收缩 (只看部分) | 自动跟踪全局 min/max |
| 适用场景 | 持续采集+偶尔回看 | 实时波形显示 |

---

## 六、IOHLCSource 系列（金融数据）

### 6.1 接口与基类

```
IOHLCSource:
├── int Count
├── IReadOnlyList<OHLC> GetOHLCs()
├── AxisLimits GetLimits()
├── CoordinateRange GetLimitsX() / GetLimitsY()
└── CoordinateRange GetPriceRange(int i1, int i2)  ← 可见区间价格范围

实现:
├── OHLCSourceBase       (abstract, 提供默认 GetLimitsX/Y 基于 DateTime)
├── OHLCSourceArray      (OHLC[] 数组)
└── OHLCSourceList       (List<OHLC> 列表)
```

### 6.2 OHLC 数据结构

```csharp
public struct OHLC
{
    double Open, High, Low, Close;
    DateTime DateTime;     ← X 轴用日期
    TimeSpan TimeSpan;
}
```

---

## 七、IDataSource 辅助接口

```csharp
interface IDataSource
{
    int Length { get; }
    bool PreferCoordinates { get; }     // true → 用 GetCoordinate(), false → 用 ZipView
    int GetXClosestIndex(Coordinates);
    Coordinates GetCoordinate(int index);
    Coordinates GetCoordinateScaled(int index);
    double GetX(int index), GetXScaled(int index);
    double GetY(int index), GetYScaled(int index);
    bool IsSorted();
}
```

所有 Scatter/Signal 源都实现 `IDataSource`，为 Plottable 提供统一的数据访问 API。

---

## 八、拓展方法：渲染索引控制

```csharp
// DataSourceUtilities.cs 中针对 IDataSource 的扩展方法:
this.GetRenderIndexCount()    → MaxRenderIndex - MinRenderIndex + 1
this.GetRenderIndexRange()    → IndexRange (MinRenderIndex, MaxRenderIndex)

// DataSources/ReadOnlyListExtensions.cs（internal）提供的惰性视图:
this.SelectView(selector)     → 投影视图 (不拷贝)
this.SkipView(n)              → IReadOnlyList 视图 (不拷贝)
this.TakeView(n)              → IReadOnlyList 视图 (不拷贝)
this.ZipView(other, selector) → 延迟 Zip 视图 (不拷贝)
```

**设计哲学**：所有 "View" 系列都是 `IReadOnlyList` 的 **惰性视图**（类似 LINQ 但返回 `IReadOnlyList`），避免大数组的内存复制。

---

## 九、数据源选择决策树

```
输入数据
  ├── 等间距? (X[i] = i * period + offset)
  │     ├── 是 → 用 ISignalSource
  │     │     ├── 静态数据 → SignalSourceDouble (带 SegmentedTree)
  │     │     ├── 静态大数组（数值类型） → SignalConst (内部 SignalConstSource + SegmentedTree)
  │     │     ├── 手动优化频繁更新的等间距序列 → FastSignalSourceDouble (带 MinMaxCache)
  │     │     └── 实时滑动窗口 → DataStreamerSource
  │     └── 否 → 用 IScatterSource
  │           ├── 已有 double[] xs, ys → ScatterSourceDoubleArray
  │           ├── 已有 Coordinates[]    → ScatterSourceCoordinatesArray
  │           └── 自定义类型 T[]        → ScatterSourceGenericArray<T>
  │
  ├── 金融OHLC? → IOHLCSource → OHLCSourceArray / OHLCSourceList
  ├── 持续累积采集? → DataLogger (DataLoggerSource，List 缓冲，与 Signal 源无关)
  ├── 向量/箭头? → VectorFieldDataSourceCoordinatesList (IVectorFieldSource)
  └── 函数/数学? → FunctionSource
```

---

## 十、关键设计洞察

1. **装饰器可选而非自动**：`CacheScatterLimitsDecorator` 随库提供（文件 ScatterSourceWithCachedLimits.cs），但 `PlottableAdder` **不会自动包裹**——核心库中没有实例化点。数据静态时可手动套用以缓存 GetLimits() 结果。

2. **惰性求值体系**：`ZipView` / `SkipView` / `TakeView` 构建了一个零拷贝的 `IReadOnlyList` 视图链，百万级数据的 `GetScatterPoints()` 不分配额外数组。

3. **双引擎互补**：静态数据用 `SegmentedTree`（构建一次，反复查询），动态数据用 `MinMaxCache`（无需重建，查询快但有缓存粒度折衷）。

4. **泛型线段树**：`SegmentedTree<T>` 用编译时 Lambda 表达式（`Expression.Lambda`）生成类型特化的 Min/Max 操作，避免泛型的虚调用开销，达到接近裸写的性能。

5. **实时数据独立封装**：`DataLogger` 和 `DataStreamer` 不实现标准 `IScatterSource`/`ISignalSource` 接口，而是拥有自己的 Source 类，因为它们有特殊的状态管理需求（HasNewData、环形缓冲等）。对应的 Plottable 直接理解这些 Source 类型。