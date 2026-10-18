# ScottPlot 5 学习笔记

> 基于对 `src/ScottPlot5/` 源码的逐层剖析（2026-10）。所有文档中的数字口径
> （文件数、枚举值数、响应器数等）均已对照源码核实。

## 目录约定

全部文档按**实际阅读顺序**编号（00-08），文件名即阅读顺序：

```
learning/
├── README.md                  ← 本文件（入口索引）
├── 00-getting-started.md      ← 从这开始：架构速览 + 5 分钟上手 + 搭建环境
├── 01-project-structure.md    ← 源码地图：目录速查
├── 02-primitives.md           ┐
├── 03-datasources.md          │
├── 04-plottables.md           │ 分层架构文档（自底向上：
├── 05-rendering.md            │ 原子层 → 数据源 → 图表 →
├── 06-interactivity.md        │ 渲染 → 交互 → 控件）
├── 07-controls.md             ┘
├── 08-usage-caveats.md        ← 全程伴随：29 条陷阱
├── archive/                   ← 历史材料
└── scripts/                   ← 统计脚本等辅助工具
```

## 阅读路径

**新手路径**（从零到理解全库）：按文件名编号 00 → 08 依次阅读。建议节奏：
第 1 天读 00-01（入门 + 源码地图），第 2 天读 02-04（Primitives → Plottables），
第 3 天读 05-07（渲染 → 控件），08 号陷阱文档全程伴随、写代码前先过一遍。

**按需查阅**：带着问题直接跳文档，见下方矩阵的"真相源"列。

## 文档职责与单一真相源矩阵

同一主题的内容只以一份文档为准（真相源），其他文档只链接、不复制：

| 主题 | 真相源 | 其他文档 |
|---|---|---|
| 新手入门 / API 速成 / 搭建环境 | `00-getting-started.md` | — |
| 目录树、物理路径、导航速查 | `01-project-structure.md` | — |
| 双坐标系、样式 Mixin、Colormaps/Palettes 清单 | `02-primitives.md` | 其余文档仅引用 |
| 数据源选型、SegmentedTree 降采样 | `03-datasources.md` | — |
| Plottable 分类矩阵与统一模板 | `04-plottables.md` | — |
| 25 步渲染序列、RenderPack 结构 | `05-rendering.md` | — |
| 交互责任链、默认响应器优先级 | `06-interactivity.md` | — |
| IPlotControl、平台控件对比、Multiplot | `07-controls.md` | — |
| 陷阱（29 条，含源码证据） | `08-usage-caveats.md` | 00 号文档仅留速览表 |

## 维护规则

1. **新增内容先查矩阵**：如果主题已有真相源，写进真相源文档，其他地方用链接。
2. **编号即阅读顺序**：新增文档按其在学习路径中的实际位置插入编号；若插入位置在
   中间，需整体重排编号并 grep 同步所有交叉引用（引用格式统一为 `learning/NN-*.md`）。
3. **数字口径以源码为准**：引用数量前先核对目录/枚举实际值（`scripts/scottplot5-stats.py` 可辅助统计）。
4. **每篇文档开头的一行职责声明**不得删除，它标注了该文档与矩阵的对应关系。
5. 若某个层未来需要多篇子笔记，可为该层单独建文件夹（如 `05-rendering/`），届时同步更新本 README 与矩阵。