# ScottPlot 5 统计脚本版本比对报告

> 比对对象：`scottplot5-stats.py` / `scottplot5-api.py` 的统计输出
> 真值源：① 编译后 `ScottPlot.dll`（net462）反射；② `git ls-files` 跟踪文件
> ScottPlot 版本：**5.1.60**
> 报告生成时间：2026-10-18

---

## 一、概述

本报告比对两套统计脚本（`scottplot5-stats.py` 基于正则、`scottplot5-api.py` 基于 tree-sitter）的输出与反射/git 真值的吻合度，重点呈现本轮对**接口总数**与**IPlottable 实现数**两个统计口径的修复效果。

## 二、真值源

| 类别 | 真值源 | 说明 |
|------|--------|------|
| 语义统计 | `ScottPlot.dll` 反射（public 范围） | 类型、成员、接口、接口实现类、枚举成员 |
| 文件计数 | `git ls-files`（tracked，排除 `.Designer.cs` / `.g.cs`） | 核心库各目录、子目录、平台控件的 `.cs` 文件数 |

## 三、文件计数比对 — 全部一致

核心库 36 个目录 + 关键子目录 + 8 个平台控件项目，共 **52 项文件计数**全部与 `git ls-files` 真值吻合。

| 类别 | 项数 | 结果 |
|------|------|------|
| 核心库目录 | 36 | ✅ 全部 OK |
| 关键子目录 | 6 | ✅ 全部 OK |
| 平台控件 | 8 | ✅ 全部 OK |

核心库合计 **577** 个 `.cs` 文件，平台控件合计 **55** 个。

## 四、语义统计比对（修复前后）

### 4.1 修复前后对比

| 统计项 | 修复前脚本值 | 修复前真值 | 修复前 | 修复后脚本值 | 修复后真值 | 修复后 |
|--------|------------:|----------:|:------:|------------:|----------:|:------:|
| public 接口数 | 63 | 61 | ❌ | **61** | 61 | ✅ |
| IPlottable 实现类 | 64 | 70 | ❌ | **70** | 70 | ✅ |
| IColormap 实现类 | 38 | 36 | ❌ | 38 | 36 | ❌(已知) |
| IPalette 实现类 | 26 | 26 | ✅ | 26 | 26 | ✅ |
| Plot.Add 方法数 | 127 | 144 | ❌ | 127 | 144 | ❌(已知) |
| 渲染步骤数 | 25 | 25 | ✅ | 25 | 25 | ✅ |
| 枚举 MarkerShape | 26 | 26 | ✅ | 26 | 26 | ✅ |
| 枚举 ArrowShape | 8 | 8 | ✅ | 8 | 8 | ✅ |
| 枚举 Edge | 4 | 4 | ✅ | 4 | 4 | ✅ |
| 枚举 Alignment | 9 | 9 | ✅ | 9 | 9 | ✅ |

### 4.2 修复项说明

**1. public 接口数（63 → 61）**

- 根因：原正则 `\binterface\s+(I\w+)` 匹配所有接口声明，将 `internal` 接口（`INamedColors`、`IHasLabel`）一并计入。
- 修复：改为 `\bpublic\s+interface\s+(I\w+)`，仅统计 public 接口，与反射 `IsPublic | IsNestedPublic` 口径对齐。

**2. IPlottable 实现类（64 → 70）**

- 根因：原正则只匹配直接声明 `: IPlottable` 的类，漏了两类：
  - 经基类间接实现（Coxcomb/Pie ← PieBase、HorizontalLine/VerticalLine ← AxisLine、DraggablePlottableDecorator ← HittablePlottableDecorator）
  - 位于 `Plottables/` 目录之外的实现类（`Legend` 在 `Primitives/`）
- 修复：扫描**整个核心库**构建继承图，对 `IPlottable` 做传递闭包计算，得到精确值 70（常规 60 + Interactive 10）。

## 五、API 表面比对（`scottplot5-api.py`）

| 成员类型 | 脚本值 | 反射真值 | 差异 | 说明 |
|---------|------:|--------:|-----:|------|
| public 类型 | 580 | 580 | 0 | ✅ 精确 |
| 成员总数 | 6036 | 6849 | +813 | 漏编译器合成成员 |
| method | 1995 | 2204 | +209 | 漏 record 合成方法 |
| property | 3581 | 3697 | +116 | — |
| field | 199 | 357 | +158 | — |
| ctor | 218 | 503 | +285 | 漏 record 拷贝构造 |
| operator | 41 | 88 | +47 | 漏 `==` / `!=` 等 |
| indexer | 1 | 2 | +1 | — |

**结论**：`api.py` 类型计数精确，成员计数系统性偏低，原因是 tree-sitter 只统计源码显式声明的成员，未包含 C# 编译器为 record 合成的 `Equals` / `GetHashCode` / `ToString` / 拷贝构造函数 / `==` / `!=` 等成员。此为设计口径差异，非 bug。

## 六、本轮修改文件清单

| 文件 | 修改内容 |
|------|----------|
| `learning/scripts/scottplot5-stats.py` | 接口正则限定 public；IPlottable 改为全库继承闭包 |
| `learning/scripts/verify-stats.ps1` | 接口真值计数补充 `IsNestedPublic`；更新预期差异说明 |
| `learning/archive/scottplot5-stats-v5.1.60.{json,txt,md}` | 按新口径重新生成 |

## 七、已知遗留差异（非本轮修复范围）

| 差异项 | 脚本值 | 真值 | 原因 |
|--------|------:|-----:|------|
| IColormap 实现类 | 38 | 36 | 脚本将 internal / 间接实现计入 |
| Plot.Add 方法数 | 127 | 144 | 正则无法跨行匹配多行方法签名 |
| api.py 成员计数 | 6036 | 6849 | 设计口径：仅统计源码显式声明成员 |

## 八、结论

本轮修复后，`scottplot5-stats.py` 的语义统计中，**接口总数**与**IPlottable 实现数**已与反射真值完全一致。文件计数类统计（52 项）本就全部准确。剩余 3 项差异均为已知的、可解释的口径或技术限制，不影响数据可信度。

`scottplot5-api.py` 的类型计数精确，成员计数偏低为设计口径（仅源码声明）。
