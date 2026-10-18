# ScottPlot 5 编译指南

> 环境：Windows · .NET SDK 10.0.402 · 2026-10-18

---

## 一、环境信息

| 项目 | 版本 |
|------|------|
| .NET SDK | `10.0.402` |
| 运行时 | .NET 10.0 |
| 操作系统 | Windows x64 |

### 已安装工作负载（8 个）

| 工作负载 ID | 版本 | 用途 |
|------------|------|------|
| `android` | 36.1.118 | Android 构建工具链 |
| `ios` | 27.0.10722 | iOS 构建工具链 |
| `maccatalyst` | 27.0.10722 | macOS Catalyst 构建工具链 |
| `maui-android` | 10.0.110 | MAUI Android 控件运行时 |
| `maui-ios` | 10.0.110 | MAUI iOS 控件运行时 |
| `maui-maccatalyst` | 10.0.110 | MAUI macOS 控件运行时 |
| `maui-tizen` | 10.0.110 | MAUI Tizen 控件运行时 |
| `wasm-tools` | 10.0.113 | WebAssembly 编译工具链（Blazor 需要） |

> **安装命令**：`dotnet workload restore`（从解决方案的 workload manifest 自动安装）

---

## 二、项目结构与目标框架

### 核心库

| 项目 | 目标框架 | 备注 |
|------|---------|------|
| **ScottPlot** | `net462` `netstandard2.0` `net8.0` `net9.0` `net10.0` | 核心渲染引擎 |
| **ScottPlot Unit Tests** | `net10.0` | 单元测试 |
| **ScottPlot Cookbook** | `net10.0` | 示例代码生成器 |
| **ScottPlot.GLControl** | `net8.0-windows` `net10.0-windows` | OpenGL 控件（WinForms） |

### 跨平台控件

| 项目 | 目标框架 |
|------|---------|
| **ScottPlot.WinForms** | `net8.0-windows` |
| **ScottPlot.WPF** | `net8.0-windows` |
| **ScottPlot.Avalonia** | `net8.0` |
| **ScottPlot.Eto** | `net8.0` |
| **ScottPlot.OpenGL** | `net8.0-windows` |
| **ScottPlot.Blazor** | `net8.0` `net9.0` `net10.0` |
| **ScottPlot.Maui** | `net10.0` `net10.0-android` `net10.0-ios` `net10.0-maccatalyst` |
| **ScottPlot.WinUI** | `net10.0` `net8.0` `net10.0-windows10.0.19041.0` `net10.0-ios` `net10.0-maccatalyst` `net10.0-android` |

### Demo 项目

| 项目 | 目标框架 |
|------|---------|
| **WinForms Demo** | `net10.0-windows` |
| **WPF Demo** | `net10.0-windows` |
| **Avalonia Demo** | `net10.0` |

### 工具项目

| 项目 | 目标框架 |
|------|---------|
| **Benchmark** | `net8.0` |
| **Graphical Test Runner** | `net10.0-windows` |

---

## 三、编译命令

### 3.1 核心库编译（最快）

从仓库根目录执行：

```powershell
dotnet build "src/ScottPlot5/ScottPlot5/ScottPlot.csproj"
dotnet build "src/ScottPlot5/ScottPlot5 Tests/Unit Tests/ScottPlot Unit Tests.csproj"
```

**耗时**：~15 秒  
**结果**：核心库 + 单元测试，5 个 TFM 全部通过

### 3.2 完整解决方案编译

从 `src/ScottPlot5` 执行：

```powershell
dotnet workload restore
dotnet restore
dotnet build --configuration Release
```

**耗时**：~57 秒（不含 workload 首次安装的 ~5 分钟）  
**结果**：除 Android TFM 外全部通过

### 3.3 跳过 Android TFM 编译

完整构建时，`ScottPlot.WinUI` 和 `ScottPlot.Maui` 的 `net10.0-android` TFM 需要 Google Android SDK，
无此 SDK 会报 `XA5300` 错误。以下方式跳过：

```powershell
# 方法一：仅构建 Windows TFM（推荐）
dotnet build --configuration Release -f net10.0-windows

# 方法二：仅构建核心库（最快）
dotnet build "src/ScottPlot5/ScottPlot5/ScottPlot.csproj" --configuration Release
```

> Windows 桌面开发不需要 Android SDK，方法一即可获得全部桌面端二进制。

---

## 四、本次编译结果

### 核心库编译 — ✅ 全部通过

| 项目 | 结果 |
|------|------|
| ScottPlot（5 个 TFM） | ✅ 成功 |
| ScottPlot Unit Tests | ✅ 成功 |

### 完整解决方案编译 — ⚠️ 2 个错误（Android SDK 未安装）

| 项目 | 桌面 TFM | Android TFM |
|------|----------|-------------|
| ScottPlot 核心库 | ✅ | — |
| ScottPlot Unit Tests | ✅ | — |
| ScottPlot Cookbook | ✅ | — |
| ScottPlot.GLControl | ✅ | — |
| ScottPlot.WinForms | ✅ | — |
| ScottPlot.WPF | ✅ | — |
| ScottPlot.Avalonia | ✅ | — |
| ScottPlot.Eto | ✅ | — |
| ScottPlot.OpenGL | ✅ | — |
| ScottPlot.Blazor | ✅ | — |
| ScottPlot.Maui | ✅ (net10.0) | ❌ XA5300 (net10.0-android) |
| ScottPlot.WinUI | ✅ (3 个桌面 TFM) | ❌ XA5300 (net10.0-android) |
| WinForms Demo | ✅ | — |
| WPF Demo | ✅ | — |
| Avalonia Demo | ✅ | — |
| Graphical Test Runner | ✅ | — |
| Benchmark | ✅ | — |

**总计**：17 个项目 / 40+ 个 TFM 编译成功，2 个 android TFM 因缺少 Google Android SDK 失败

---

## 五、常见问题

### Q: `XA5300: 找不到 Android SDK 目录`
**原因**：`.NET Android SDK`（Microsoft 提供的 workload）已安装，但缺少 **Google Android SDK**。  
**解决**：安装 Android Studio 并设置 `ANDROID_HOME` 环境变量，或用 `-f net10.0-windows` 跳过。

### Q: `NETSDK1138: 目标框架不兼容`
**原因**：WinForms/WPF 项目需要 Windows SDK，在 macOS/Linux 上无法编译这些 TFM。  
**解决**：使用 `-f net10.0` 过滤（通用 TFM），或在 Windows 上编译。