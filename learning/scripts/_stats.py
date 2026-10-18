# -*- coding: utf-8 -*-
"""ScottPlot 5 全库源码统计 —— 学习文档事实核查辅助工具

用途：一次性扫描 src/ScottPlot5 全部源码，输出解决方案全貌、核心库分层
      文件数、Primitives 类型分类、接口清单、数据源继承关系、Plottable
      清单、渲染管线步骤、交互响应器、Add 方法数、枚举成员数等关键事实，
      供 learning/ 下各编号文档核对数字口径使用。

运行：python learning/scripts/_stats.py
"""
import os
import re
from collections import OrderedDict

# ============================================================
# 路径常量
# ============================================================
SLN = r'd:\dev\store\ScottPlot\src\ScottPlot5'        # ScottPlot5 源码根目录
CORE = os.path.join(SLN, 'ScottPlot5')                 # 核心库 ScottPlot5
CTRL = os.path.join(SLN, 'ScottPlot5 Controls')        # 平台控件解决方案


def read(path):
    """读取文本文件内容（忽略编码错误，容错处理）"""
    with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
        return fp.read()


def cs_files(folder):
    """递归收集目录下所有手写 .cs 文件（排除生成文件 bin/obj/.g.cs/Designer）"""
    out = []
    for root, dirs, files in os.walk(folder):
        # 跳过编译输出目录，避免把生成代码计入统计
        dirs[:] = [d for d in dirs if d not in ('bin', 'obj')]
        for f in files:
            if f.endswith('.cs') and not f.endswith(('.g.cs', '.Designer.cs')):
                out.append(os.path.join(root, f))
    return out


def strip_comments(code):
    """去掉 C# 的 // 行注释与 /* */ 块注释，保证后续正则只匹配真实代码"""
    code = re.sub(r'//[^\n]*', '', code)          # 删除行注释
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.S)  # 删除块注释（含跨行）
    return code


def line_count(paths):
    """统计一组文件的总行数（用于体量概览）"""
    total = 0
    for p in paths:
        try:
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                total += sum(1 for _ in fp)
        except OSError:
            pass
    return total


def section(title):
    """打印统一风格的分节标题"""
    print('\n' + '=' * 78)
    print(title)
    print('=' * 78)


# ============================================================
# 一、解决方案全貌：每个项目的 .cs 文件数与代码行数
# ============================================================
section('一、解决方案全貌（src/ScottPlot5 下各项目）')
for proj in sorted(os.listdir(SLN)):
    pdir = os.path.join(SLN, proj)
    if not os.path.isdir(pdir):
        continue
    files = cs_files(pdir)
    print(f'  {proj:28s} {len(files):5d} 个 .cs   {line_count(files):8d} 行')

# ============================================================
# 二、核心库分层地图：ScottPlot5 主项目各目录文件数
# ============================================================
section('二、核心库分层地图（ScottPlot5 各目录 .cs 文件数）')
core_root_files = [f for f in os.listdir(CORE) if f.endswith('.cs')]
print(f'  {"(根目录散文件)":28s} {len(core_root_files):5d}')
for sub in sorted(os.listdir(CORE)):
    subdir = os.path.join(CORE, sub)
    if os.path.isdir(subdir) and sub not in ('bin', 'obj'):
        n = len(cs_files(subdir))
        if n:
            print(f'  {sub:28s} {n:5d}')

# ============================================================
# 三、Primitives 类型分类（按文件内首个类型声明的种类统计）
# ============================================================
section('三、Primitives 基础类型分类')
prim_dir = os.path.join(CORE, 'Primitives')
kind_re = re.compile(
    r'\b(public|internal)?\s*(?:sealed\s+|abstract\s+|static\s+|partial\s+)*'
    r'(record\s+struct|record\s+class|record|struct|class|interface|enum)\s+(\w+)')
kinds = OrderedDict([('struct', []), ('record struct', []), ('record', []),
                     ('class', []), ('interface', []), ('enum', [])])
for path in cs_files(prim_dir):
    m = kind_re.search(strip_comments(read(path)))
    if m:
        kind = m.group(2)
        if kind == 'record class':   # record class 归并到 record 一类
            kind = 'record'
        kinds.setdefault(kind, []).append(os.path.basename(path)[:-3])
for kind, names in kinds.items():
    if names:
        preview = ', '.join(sorted(names)[:8])
        more = f' ... 等 {len(names)} 个' if len(names) > 8 else ''
        print(f'  {kind:14s} {len(names):3d} 个  {preview}{more}')

# ============================================================
# 四、接口统计：核心库中声明的全部 interface
# ============================================================
section('四、核心库接口（interface）统计')
iface_re = re.compile(r'\binterface\s+(I\w+)')
ifaces_by_dir = {}
for path in cs_files(CORE):
    rel = os.path.relpath(path, CORE)
    top = rel.split(os.sep)[0]
    names = iface_re.findall(strip_comments(read(path)))
    if names:
        ifaces_by_dir.setdefault(top, []).extend(names)
total_ifaces = sum(len(v) for v in ifaces_by_dir.values())
print(f'  合计 {total_ifaces} 个接口，分布：')
for top, names in sorted(ifaces_by_dir.items(), key=lambda kv: -len(kv[1])):
    preview = ', '.join(sorted(names)[:6])
    more = f' ...' if len(names) > 6 else ''
    print(f'    {top:22s} {len(names):3d} 个  {preview}{more}')

# ============================================================
# 五、DataSources：具体类型及其实现的数据源接口
# ============================================================
section('五、DataSources 类型与实现的接口')
ds_dir = os.path.join(CORE, 'DataSources')
type_re = re.compile(r'\b(class|record(?:\s+struct)?|struct)\s+(\w+)\s*[:<{]?([^\n{{]*)')
iface_def_re = re.compile(r'\binterface\s+(I\w+)')
defined_ifaces = []
impl_types = []
for path in cs_files(ds_dir):
    code = strip_comments(read(path))
    defined_ifaces += iface_def_re.findall(code)
    for m in type_re.finditer(code):
        kind, name, bases = m.group(1), m.group(2), m.group(3)
        if name in defined_ifaces or kind.startswith('interface'):
            continue
        src_bases = re.findall(r'I\w*(?:Source|DataSource)\w*', bases)
        impl_types.append((name, kind.replace(' ', ''), ', '.join(src_bases) or '(基类间接实现)'))
for name, kind, bases in sorted(impl_types):
    print(f'  {name:38s} {kind:14s} {bases}')

# ============================================================
# 六、Plottables：文件数口径（根目录 / Interactive / 其他）
# ============================================================
section('六、Plottable 图表类（实现 IPlottable）')
plottables_dir = os.path.join(CORE, 'Plottables')
# 主口径 = .cs 文件数：根目录 + Interactive 子目录（其余子目录单独列出）
root_files = [f for f in os.listdir(plottables_dir) if f.endswith('.cs')]
for sub in sorted(os.listdir(plottables_dir)):
    subdir = os.path.join(plottables_dir, sub)
    if os.path.isdir(subdir):
        n = len([f for f in os.listdir(subdir) if f.endswith('.cs')])
        print(f'  Plottables/{sub:20s} {n:3d} 个')
print(f'  Plottables 根目录          {len(root_files):3d} 个')
print(f'  Plottables 合计            {len(cs_files(plottables_dir)):3d} 个（= 根目录 + 各子目录）')

# 辅助口径 = 从类声明中提取 IPlottable 实现类名（供交叉核对）
iplottable_re = re.compile(r'class\s+(\w+)\b[^:;\n]*:\s*([^\n{]*IPlottable[^\n{]*)')
normal, interactive = [], []
for path in cs_files(plottables_dir):
    code = strip_comments(read(path))
    for m in iplottable_re.finditer(code):
        name = m.group(1)
        (interactive if 'Interactive' in name or os.sep + 'Interactive' + os.sep in path
         else normal).append(name)
print(f'  （按类声明识别：常规 {len(normal)} 个，Interactive {len(interactive)} 个；'
      f'部分类经由 PlottableBase 间接实现 IPlottable，故文件数为准）')

# ============================================================
# 七、渲染管线：RenderManager 中的 RenderActions 步骤序列
# ============================================================
section('七、RenderManager 渲染管线步骤')
rm_path = os.path.join(CORE, 'Rendering', 'RenderManager.cs')
actions = re.findall(r'new RenderActions\.(\w+)\(\)', read(rm_path))
ra_dir = os.path.join(CORE, 'Rendering', 'RenderActions')
ra_files = len([f for f in os.listdir(ra_dir) if f.endswith('.cs')])
for i, a in enumerate(actions):
    print(f'  {i+1:2d}. {a}')
print(f'  （管道中调用 {len(actions)} 步；RenderActions 目录文件数 {ra_files}）')

# ============================================================
# 八、Plot.Add 入口：PlottableAdder 各分部文件中的添加方法
# ============================================================
section('八、Plot.Add 添加方法（PlottableAdder.cs）')
# 精确匹配方法声明行：public 返回类型 方法名(
# 该模式不会误匹配字段初始化器（其括号不在标识符后紧邻位置）
method_re = re.compile(r'^\s*public\s+[\w<>\[\],\.\?]+\s+(\w+)\s*\(', re.M)
adder_methods = []
adder_files = [p for p in cs_files(CORE) if os.path.basename(p).startswith('PlottableAdder')]
for path in adder_files:
    for m in method_re.finditer(strip_comments(read(path))):
        name = m.group(1)
        # 排除类声明（主构造函数）与 Get 开头的辅助方法（如 GetNextColor）
        if name != 'PlottableAdder' and not name.startswith('Get'):
            adder_methods.append(name)
print(f'  分部文件数：{len(adder_files)}；添加方法合计 {len(adder_methods)} 个（含重载）')

# ============================================================
# 九、Interactivity：用户动作、响应器、默认注册清单
# ============================================================
section('九、Interactivity 交互层')
actions_dir = os.path.join(CORE, 'Interactivity', 'UserActions')
responses_dir = os.path.join(CORE, 'Interactivity', 'UserActionResponses')
ua = [f[:-3] for f in os.listdir(actions_dir) if f.endswith('.cs')]
uar = [f[:-3] for f in os.listdir(responses_dir) if f.endswith('.cs')]
print(f'  UserActions（用户输入动作）：{len(ua)} 个 → {", ".join(sorted(ua))}')
print(f'  UserActionResponses（响应器文件）：{len(uar)} 个 → {", ".join(sorted(uar))}')
# 默认注册的响应器：从 UserInputProcessor 中提取 new UserActionResponses.X()
# （用 dict.fromkeys 按出现顺序去重，避免重复注册点造成虚高计数）
uip_path = os.path.join(CORE, 'Interactivity', 'UserInputProcessor.cs')
if os.path.exists(uip_path):
    defaults = re.findall(r'new UserActionResponses\.(\w+)\(', read(uip_path))
    unique = list(dict.fromkeys(defaults))
    print(f'  UserInputProcessor 默认注册：{len(unique)} 个（{len(defaults)} 处调用）')
    print(f'    → {", ".join(unique)}')

# ============================================================
# 十、枚举成员数：MarkerShape / Colormap / Palette 等常用口径
# ============================================================
section('十、常用枚举与集合口径')


def enum_members(enum_name):
    """在全核心库中查找 enum 定义并统计成员个数"""
    for path in cs_files(CORE):
        code = strip_comments(read(path))
        m = re.search(r'enum\s+' + enum_name + r'\b[^{]*\{(.+?)\}', code, re.S)
        if m:
            body = m.group(1)
            # 顶层成员以逗号分隔（成员内可能有 = 赋值，但不影响计数）
            members = [x for x in body.replace('\n', ' ').split(',') if x.strip()]
            return len(members), path
    return None, None


for enum_name in ('MarkerShape', 'ArrowShape', 'ColorType', 'Edge', 'Alignment'):
    n, p = enum_members(enum_name)
    if n:
        print(f'  {enum_name:16s} {n:3d} 个成员  （{os.path.basename(p)}）')

# Colormap / Palette 实现（每种样式一个类）
colormaps = set()
palettes = set()
for path in cs_files(CORE):
    code = strip_comments(read(path))
    colormaps |= set(re.findall(r'class\s+(\w+)\b[^:;\n]*:\s*[^\n{]*IColormap', code))
    palettes |= set(re.findall(r'class\s+(\w+)\b[^:;\n]*:\s*[^\n{]*IPalette', code))
print(f'  IColormap 实现：{len(colormaps)} 个；IPalette 实现：{len(palettes)} 个')

# ============================================================
# 十一、平台控件：8 个平台项目与 IPlotControl 实现
# ============================================================
section('十一、平台控件（ScottPlot5 Controls）')
iplotcontrol_re = re.compile(r'class\s+(\w+)\b[^:;\n]*:\s*([^\n{]*IPlotControl)')
for plat in sorted(os.listdir(CTRL)):
    pdir = os.path.join(CTRL, plat)
    if not os.path.isdir(pdir):
        continue
    files = cs_files(pdir)
    impls = []
    for path in files:
        impls += iplotcontrol_re.findall(strip_comments(read(path)))[0:1]
    impl_names = ', '.join(n for n, _ in impls) or '-'
    print(f'  {plat:24s} {len(files):4d} 个 .cs   IPlotControl 实现: {impl_names}')

print('\n（统计完成）')
