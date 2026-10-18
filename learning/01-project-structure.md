# ScottPlot 5 项目结构导航

> 职责：源码地图 — 解决方案全景 + 核心库目录速查<br/>深度分析见各分层文档（02-07）· 2026-10-18

---

## 一、解决方案全景

```
Solution 'ScottPlot5'
├── 📄 ScottPlot                          → ScottPlot5/ScottPlot.csproj
├── 📁 Controls/ (8)  WinForms·WPF·Avalonia·Blazor·Maui·WinUI·Eto·OpenGL
├── 📄 ScottPlot Cookbook                  → ScottPlot5 Cookbook/
├── 📁 Demo/ (4)       WinForms·WPF·Avalonia·Blazor
├── 📄 ScottPlot Unit Tests               → ScottPlot5 Tests/Unit Tests/
├── 📁 Advanced Tests/ (2)  Benchmark·Graphical Test Runner
├── 📁 Sandbox/ (12)    不参与常规 Build
├── 📁 Dev/              引入 CHANGELOG.md 到 VS
├── 📄 .editorconfig
└── 📄 Key.snk
```

| VS 文件夹 | 项目数 | 用途 |
|----------|--------|------|
| Controls/ | 8 | 跨平台 GUI 控件，发布为独立 NuGet 包 |
| Demo/ | 4 | 演示程序 |
| Advanced Tests/ | 2 | 性能测试 + 图形化测试运行器 |
| Sandbox/ | 12 | 开发调试用沙盒，不参与 Build |
| *(根级)* | 3 | 核心库 + Cookbook + 单元测试 |

---

## 二、核心库 `ScottPlot5/` 内部结构

### 2.1 根目录文件

| 文件 | 职责 |
|---|---|
| `Plot.cs` | 用户主入口 |
| `PlottableAdder.cs` | `Plot.Add.Scatter()` 等工厂方法集合 |
| `RenderPack.cs` | 单次渲染上下文 |
| `AxisManager.cs` | 多轴管理 |
| `LayoutManager.cs` | 布局计算 |
| `Multiplot.cs` / `MultiplotSharedAxisManager.cs` | 多图容器 |
| `Drawing.cs` | SkiaSharp 绘图封装 |
| `Generate.cs` / `SampleData.cs` / `SampleImages.cs` | 数据生成器 |
| `Fonts.cs` / `FontExtensions.cs` | 字体管理 |
| `ImageOperations.cs` / `DataOperations.cs` | 图像/数据操作工具 |
| `DataSourceUtilities.cs` / `BinarySearchComparer.cs` / `GenericComparer.cs` / `NumericConversion.cs` | 数据辅助工具 |
| `RandomDataGenerator.cs` | 随机数据（测试用） |
| `Version.cs` / `Usings.cs` | 版本号 / 全局 using |

### 2.2 子目录速查

| 目录 | 定位 | 详见 |
|---|---|---|
| Primitives/ | 原子数据结构（坐标/颜色/样式/几何） | [02](02-primitives.md) |
| Interfaces/ | 核心接口（策略模式插入点） | [02](02-primitives.md) |
| DataSources/ | 数据源实现（Scatter/Signal/OHLC/实时流） | [03](03-datasources.md) |
| Plottables/ | 可绘制物（根 + Interactive） | [04](04-plottables.md) |
| Rendering/ | 渲染管道（1 Manager + 25 Actions） | [05](05-rendering.md) |
| Interactivity/ | 交互系统 | [06](06-interactivity.md) |
| TickGenerators/ | 刻度生成（Numeric/DateTime/Financial/Log） | — |
| LayoutEngines/ | 5 种布局引擎 | — |
| AxisPanels/ | 轴面板（Bottom/Left/Top/Right 等） | — |
| AxisRules/ | 轴约束规则（Lock/Max/Min/SnapToTicks 等） | — |
| AxisLimitManagers/ | 实时轴范围（Full/Slide/FixedWidth） | — |
| AutoScalers/ | 自动缩放策略 | — |
| Panels/ | 图表面板（标题/图例/ColorBar） | — |
| Grids/ | 网格线 | — |
| Markers/ | 预设标记形状 | [02](02-primitives.md) |
| ArrowShapes/ | 箭头形状 | [02](02-primitives.md) |
| Colormaps/ | 科学配色方案 | [02](02-primitives.md) |
| Palettes/ | 分类调色板 | [02](02-primitives.md) |
| PathStrategies/ | 连线策略（直线/样条/阶梯） | — |
| Statistics/ | 统计计算（直方图/线性回归/核密度） | — |
| Finance/ | 金融指标（Bollinger/移动平均） | — |
| Hatches/ | 图案填充 | — |
| DataGenerators/ | 实时数据生成 | — |
| DataViews/ | 数据流视图 | — |
| FontResolvers/ | 字体解析 | — |
| Collections/ | CircularBuffer | — |
| MultiplotLayouts/ | 多图布局 | — |
| NamedColors/ | 命名颜色集 | — |
| PlotStyles/ | 图表样式 | — |
| Reporting/ | 报表生成 | — |
| StarAxes/ | 极坐标/星形轴 | — |
| Stylers/ | 样式应用器 | — |
| Testing/ | 测试辅助 | — |
| Triangulation/ | 三角剖分 | — |

---

## 三、跨平台控件

> 详见 [07-controls.md](07-controls.md)

| 项目 | NuGet 包 |
|---|---|
| ScottPlot.WinForms | ScottPlot.WinForms |
| ScottPlot.WPF | ScottPlot.WPF |
| ScottPlot.Avalonia | ScottPlot.Avalonia |
| ScottPlot.Blazor | ScottPlot.Blazor |
| ScottPlot.Eto | ScottPlot.Eto |
| ScottPlot.Maui | ScottPlot.Maui |
| ScottPlot.WinUI | ScottPlot.WinUI |
| ScottPlot.OpenGL | ScottPlot.OpenGL (GPU 加速扩展) |

---

## 四、单元测试结构

```
Unit Tests/
├── UnitTests/PrimitiveTests/         ← 原子类型测试
├── UnitTests/TickGenerators/         ← 刻度生成器测试
├── RenderTests/
│   ├── Figure/                       ← 整图对比测试
│   ├── Plottable/                    ← 各 Plottable 渲染测试
│   ├── AutoScale/Layout/Legend/...   ← 子系统测试
├── InteractivityTests/
│   ├── UserInputActionTests/
│   └── KeyboardStateTests
├── CodeTests/                        ← 代码规范检查
├── FontTests/                        ← 字体检测
├── Statistics/                       ← 统计算法测试
└── TestImages/                       ← 测试图片资源
```