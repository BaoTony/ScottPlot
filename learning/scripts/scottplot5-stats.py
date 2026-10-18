# -*- coding: utf-8 -*-
"""ScottPlot 5 全库源码统计 —— 学习文档事实核查辅助工具

用途：一次性扫描 src/ScottPlot5 全部源码，输出解决方案全貌、核心库分层
      文件数、Primitives 类型分类、接口清单、数据源继承关系、Plottable
      清单、渲染管线步骤、交互响应器、Add 方法数、枚举成员数等关键事实，
      供 learning/ 下各编号文档核对数字口径使用。

运行：python learning/scripts/scottplot5-stats.py           # 人类可读输出
      python learning/scripts/scottplot5-stats.py --json    # 纯 JSON 输出（可重定向落盘做前后 diff）
      python learning/scripts/scottplot5-stats.py --out     # 一键落盘：txt+md+json 三格式保存到桌面（文件名含版本号）
      python learning/scripts/scottplot5-stats.py --out X   # 同上，但保存到指定目录
      python learning/scripts/scottplot5-stats.py --sln X   # 指定源码根目录（默认按脚本位置自动推导）
"""
import argparse
import json
import os
import re
from collections import OrderedDict

# 路径常量：按脚本位置上溯 3 级推导仓库根（scripts → learning → 仓库根），可用 --sln 覆盖
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLN = os.path.join(REPO, 'src', 'ScottPlot5')          # ScottPlot5 源码根目录
CORE = os.path.join(SLN, 'ScottPlot5')                 # 核心库 ScottPlot5
CTRL = os.path.join(SLN, 'ScottPlot5 Controls')        # 平台控件解决方案

# 文件内容缓存：全库文件只读一次，多节复用
_CACHE = {}

# --json 模式下抑制人类可读输出，保证 stdout 只有纯 JSON 便于重定向/解析
QUIET = False

# 人类可读输出的行缓冲：无论是否打印到终端都持续收集，
# 供 --out 落盘时写入 txt 文件（--json 模式下也能照常生成 txt）
_LINES = []


def read(path):
    """读取文本文件内容（忽略编码错误；带缓存避免同一文件被多节重复读盘）"""
    if path not in _CACHE:
        with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
            _CACHE[path] = fp.read()
    return _CACHE[path]


def cs_files(folder):
    """递归收集目录下所有手写 .cs 文件（排除生成文件 bin/obj/.g.cs/Designer）"""
    out = []
    for root, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in ('bin', 'obj')]  # 跳过编译输出目录
        for f in files:
            if f.endswith('.cs') and not f.endswith(('.g.cs', '.Designer.cs')):
                out.append(os.path.join(root, f))
    return out


def strip_comments(code):
    """去掉 C# 的 // 行注释与 /* */ 块注释，保证后续正则只匹配真实代码"""
    code = re.sub(r'//[^\n]*', '', code)               # 删除行注释
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.S)  # 删除块注释（含跨行）
    return code


def line_count(paths):
    """统计一组文件的总行数（复用 read 缓存）"""
    return sum(len(read(p).splitlines()) for p in paths)


def out(line=''):
    """统一输出入口：始终收集进行缓冲（供 --out 落盘），非 QUIET 时同步打印终端"""
    _LINES.append(line)
    if not QUIET:
        print(line)


def section(title):
    """打印统一风格的分节标题（--json 模式下不打印）"""
    out('')
    out('=' * 78)
    out(title)
    out('=' * 78)


def default_out_dir():
    """探测桌面目录作为 --out 默认落盘位置（兼容 OneDrive 重定向与中文「桌面」）"""
    home = os.path.expanduser('~')
    for cand in (os.path.join(home, 'Desktop'),
                 os.path.join(home, 'OneDrive', 'Desktop'),
                 os.path.join(home, '桌面')):
        if os.path.isdir(cand):
            return cand
    return home


def get_version(sln_dir):
    """读取 ScottPlot.csproj 的 <Version>（即编译产物 AssemblyInformationalVersion 的来源）"""
    csproj = os.path.join(sln_dir, 'ScottPlot5', 'ScottPlot.csproj')
    if os.path.exists(csproj):
        with open(csproj, 'r', encoding='utf-8', errors='ignore') as fp:
            m = re.search(r'<Version>([^<]+)</Version>', fp.read())
        if m:
            return m.group(1).strip()
    return '(未知)'


def build_markdown(results):
    """把统计结果渲染为 Markdown 文档（与 json 同源，永不失同步）"""
    L = ['# ScottPlot5 全库源码统计', '',
         f'> ScottPlot5 版本：**{results["version"]}**（提取自 ScottPlot.csproj，便于跨版本比对）',
         '> 由 `learning/scripts/scottplot5-stats.py` 自动生成，'
         '供 `learning/` 编号文档核对数字口径。', '']

    L += ['## 一、解决方案全貌（src/ScottPlot5 下各项目）', '',
          '| 项目 | .cs 文件数 | 代码行数 |', '|---|---:|---:|']
    for proj, v in results['solution'].items():
        L.append(f'| {proj} | {v["files"]} | {v["lines"]} |')

    L += ['', '## 二、核心库分层地图（ScottPlot5 各目录 .cs 文件数）', '',
          '| 目录 | .cs 文件数 |', '|---|---:|']
    for name, n in results['core_layout'].items():
        L.append(f'| {name} | {n} |')

    L += ['', '## 三、Primitives 基础类型分类', '',
          '| 种类 | 个数 | 类型（最多列 8 个） |', '|---|---:|---|']
    for kind, names in results['primitives'].items():
        preview = ', '.join(names[:8]) + (' 等' if len(names) > 8 else '')
        L.append(f'| {kind} | {len(names)} | {preview} |')

    itf = results['interfaces']
    L += ['', f'## 四、核心库接口统计（合计 {itf["total"]} 个）', '',
          '| 目录 | 个数 | 接口（最多列 6 个） |', '|---|---:|---|']
    for top, names in sorted(itf['by_dir'].items(), key=lambda kv: -len(kv[1])):
        preview = ', '.join(names[:6]) + (' …' if len(names) > 6 else '')
        L.append(f'| {top} | {len(names)} | {preview} |')

    L += ['', '## 五、DataSources 类型与实现的接口', '',
          '| 类型 | 种类 | 实现的数据源接口 |', '|---|---|---|']
    for ds in results['data_sources']:
        L.append(f'| {ds["name"]} | {ds["kind"]} | {ds["bases"]} |')

    pl = results['plottables']
    L += ['', '## 六、Plottable 图表类（实现 IPlottable）', '',
          '| 位置 | .cs 文件数 |', '|---|---:|']
    for sub, n in pl['by_dir'].items():
        L.append(f'| Plottables/{sub} | {n} |')
    L.append(f'| Plottables 根目录 | {pl["root"]} |')
    L.append(f'| **合计** | **{pl["total"]}** |')
    bd = pl['by_class_declaration']
    L += ['', f'（按类声明识别：常规 {bd["normal"]} 个，Interactive {bd["interactive"]} 个；'
          '部分类经由 PlottableBase 间接实现 IPlottable，故以文件数为准）']

    rp = results['render_pipeline']
    L += ['', '## 七、RenderManager 渲染管线步骤', '']
    for i, step in enumerate(rp['steps'], 1):
        L.append(f'{i}. {step}')
    L.append(f'（管道中调用 {len(rp["steps"])} 步；RenderActions 目录文件数 {rp["render_action_files"]}）')

    pa = results['plot_add']
    L += ['', f'## 八、Plot.Add 添加方法（{pa["method_count"]} 个，含重载；'
          f'分部文件 {pa["partial_files"]} 个）', '',
          ', '.join(pa['methods'])]

    ia = results['interactivity']
    L += ['', '## 九、Interactivity 交互层', '',
          f'- UserActions（用户输入动作）：{len(ia["user_actions"])} 个 → '
          + ', '.join(ia['user_actions']),
          f'- UserActionResponses（响应器文件）：{len(ia["responses"])} 个 → '
          + ', '.join(ia['responses']),
          f'- UserInputProcessor 默认注册：{len(ia["default_registered"])} 个'
          f'（{ia["default_call_sites"]} 处调用）→ ' + ', '.join(ia['default_registered'])]

    L += ['', '## 十、常用枚举与集合口径', '',
          '| 枚举/集合 | 个数 |', '|---|---:|']
    for name, n in results['enums'].items():
        L.append(f'| {name}（枚举成员） | {n} |')
    L.append(f'| IColormap 实现 | {len(results["colormaps"])} |')
    L.append(f'| IPalette 实现 | {len(results["palettes"])} |')
    L += ['', f'Colormap：{", ".join(results["colormaps"])}', '',
          f'Palette：{", ".join(results["palettes"])}']

    L += ['', '## 十一、平台控件（ScottPlot5 Controls）', '',
          '| 平台项目 | .cs 文件数 | IPlotControl 实现 |', '|---|---:|---|']
    for plat, v in results['platform_controls'].items():
        L.append(f'| {plat} | {v["files"]} | {", ".join(v["impl"]) or "-"} |')
    return '\n'.join(L)


def parse_args():
    """解析命令行参数：源码根目录覆盖项、JSON 输出开关与落盘目录"""
    ap = argparse.ArgumentParser(description='ScottPlot5 全库源码统计（学习文档事实核查辅助）')
    ap.add_argument('--sln', help='ScottPlot5 源码根目录（默认按脚本位置自动推导）')
    ap.add_argument('--json', action='store_true', help='仅输出纯 JSON 统计结果')
    ap.add_argument('--out', nargs='?', const='', default=None, metavar='目录',
                    help='一键落盘：不带值时保存到桌面；也可指定输出目录。'
                         '会同时生成 scottplot5-stats-v<版本>.txt（终端文本原样）、'
                         'scottplot5-stats-v<版本>.md（Markdown 表格）与 '
                         'scottplot5-stats-v<版本>.json（机器可读），同名旧文件被覆盖；'
                         '文件名含版本号便于跨版本比对')
    return ap.parse_args()


def main():
    global SLN, CORE, CTRL, QUIET
    args = parse_args()
    QUIET = args.json
    if args.sln:  # 显式指定源码根目录，覆盖默认推导
        SLN = args.sln
        CORE = os.path.join(SLN, 'ScottPlot5')
        CTRL = os.path.join(SLN, 'ScottPlot5 Controls')

    results = OrderedDict()  # 全部统计结果，--json 模式整体输出

    # 版本号置于最前部，便于跨版本比对统计口径
    version = get_version(SLN)
    results['version'] = version
    out(f'ScottPlot5 版本：{version}')

    section('一、解决方案全貌（src/ScottPlot5 下各项目）')
    solution = OrderedDict()
    for proj in sorted(os.listdir(SLN)):
        pdir = os.path.join(SLN, proj)
        if not os.path.isdir(pdir):
            continue
        files = cs_files(pdir)
        if not files:
            # 跳过无源码的目录（如 .vs 缓存），避免计入解决方案全貌
            continue
        n_lines = line_count(files)
        out(f'  {proj:28s} {len(files):5d} 个 .cs   {n_lines:8d} 行')
        solution[proj] = {'files': len(files), 'lines': n_lines}
    results['solution'] = solution

    section('二、核心库分层地图（ScottPlot5 各目录 .cs 文件数）')
    layout = OrderedDict()
    core_root_files = [f for f in os.listdir(CORE) if f.endswith('.cs')]
    out(f'  {"(根目录散文件)":28s} {len(core_root_files):5d}')
    layout['(根目录散文件)'] = len(core_root_files)
    for sub in sorted(os.listdir(CORE)):
        subdir = os.path.join(CORE, sub)
        if os.path.isdir(subdir) and sub not in ('bin', 'obj'):
            n = len(cs_files(subdir))
            if n:
                out(f'  {sub:28s} {n:5d}')
                layout[sub] = n
    results['core_layout'] = layout

    # 按文件内首个类型声明的种类统计
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
    primitives = {k: sorted(v) for k, v in kinds.items() if v}
    for kind, names in primitives.items():
        preview = ', '.join(names[:8])
        more = f' ... 等 {len(names)} 个' if len(names) > 8 else ''
        out(f'  {kind:14s} {len(names):3d} 个  {preview}{more}')
    results['primitives'] = primitives

    section('四、核心库接口（interface）统计')
    # 口径：只统计 public 接口（与反射 IsPublic/IsNestedPublic 一致），
    # 排除 internal 接口（如 INamedColors、IHasLabel）
    iface_re = re.compile(r'\bpublic\s+interface\s+(I\w+)')
    ifaces_by_dir = {}
    for path in cs_files(CORE):
        rel = os.path.relpath(path, CORE)
        top = rel.split(os.sep)[0]
        names = iface_re.findall(strip_comments(read(path)))
        if names:
            ifaces_by_dir.setdefault(top, []).extend(names)
    total_ifaces = sum(len(v) for v in ifaces_by_dir.values())
    out(f'  合计 {total_ifaces} 个 public 接口，分布：')
    for top, names in sorted(ifaces_by_dir.items(), key=lambda kv: -len(kv[1])):
        preview = ', '.join(sorted(names)[:6])
        more = f' ...' if len(names) > 6 else ''
        out(f'    {top:22s} {len(names):3d} 个  {preview}{more}')
    results['interfaces'] = {'total': total_ifaces,
                             'by_dir': {k: sorted(v) for k, v in ifaces_by_dir.items()}}

    section('五、DataSources 类型与实现的接口')
    ds_dir = os.path.join(CORE, 'DataSources')
    type_re = re.compile(r'\b(class|record(?:\s+struct)?|struct)\s+(\w+)\s*[:<{]?([^\n{]*)')
    iface_def_re = re.compile(r'\binterface\s+(I\w+)')
    defined_ifaces = []
    impl_types = []
    for path in cs_files(ds_dir):
        code = strip_comments(read(path))
        defined_ifaces += iface_def_re.findall(code)
        for m in type_re.finditer(code):
            kind, name, bases = m.group(1), m.group(2), m.group(3)
            # 跳过本目录内定义的接口自身（type_re 无 interface 分支，不会误匹配）
            if name in defined_ifaces:
                continue
            src_bases = re.findall(r'I\w*(?:Source|DataSource)\w*', bases)
            impl_types.append((name, kind.replace(' ', ''), ', '.join(src_bases) or '(基类间接实现)'))
    for name, kind, bases in sorted(impl_types):
        out(f'  {name:38s} {kind:14s} {bases}')
    results['data_sources'] = [
        {'name': n, 'kind': k, 'bases': b} for n, k, b in sorted(impl_types)]

    # 主口径 = .cs 文件数；IPlottable 实现类数通过全核心库继承闭包精确计算
    section('六、Plottable 图表类（实现 IPlottable）')
    plottables_dir = os.path.join(CORE, 'Plottables')
    all_plottable_files = cs_files(plottables_dir)
    by_dir = OrderedDict()
    for sub in sorted(os.listdir(plottables_dir)):
        subdir = os.path.join(plottables_dir, sub)
        if os.path.isdir(subdir):
            n = len([f for f in os.listdir(subdir) if f.endswith('.cs')])
            out(f'  Plottables/{sub:20s} {n:3d} 个')
            by_dir[sub] = n
    root_files = [f for f in os.listdir(plottables_dir) if f.endswith('.cs')]
    out(f'  Plottables 根目录          {len(root_files):3d} 个')
    out(f'  Plottables 合计            {len(all_plottable_files):3d} 个（= 根目录 + 各子目录）')

    # IPlottable 实现类：扫描整个核心库构建继承图，计算传递闭包
    # （部分类经 PieBase / AxisLine / HittablePlottableDecorator 等基类间接实现，
    #  且 Legend 等个别实现类位于 Plottables/ 之外，故必须全库扫描）
    decl_re = re.compile(r'\b(?:class|record(?:\s+struct)?|struct)\s+(\w+)\b[^:;\n{]*:\s*([^{]+)', re.S)
    name_bases = {}            # 类型名 -> 基类/接口名集合
    name_file = {}             # 类型名 -> 所在文件（用于判断 Interactive）
    for path in cs_files(CORE):
        code = strip_comments(read(path))
        for m in decl_re.finditer(code):
            name_bases[m.group(1)] = set(re.findall(r'\b[A-Z]\w*\b', m.group(2)))
            name_file[m.group(1)] = path
    direct_impl = {n for n, bs in name_bases.items() if 'IPlottable' in bs}
    iplottable_impl = set(direct_impl)
    changed = True
    while changed:
        changed = False
        for n, bs in name_bases.items():
            if n not in iplottable_impl and bs & iplottable_impl:
                iplottable_impl.add(n)
                changed = True
    normal = [n for n in iplottable_impl
              if not ('Interactive' in n or os.sep + 'Interactive' + os.sep in name_file.get(n, ''))]
    interactive = [n for n in iplottable_impl if n not in normal]
    out(f'  IPlottable 实现类（继承闭包）：{len(iplottable_impl)} 个'
        f'（常规 {len(normal)}，Interactive {len(interactive)}）')
    results['plottables'] = {
        'by_dir': by_dir, 'root': len(root_files), 'total': len(all_plottable_files),
        'by_class_declaration': {'normal': len(normal), 'interactive': len(interactive)},
    }

    section('七、RenderManager 渲染管线步骤')
    rm_path = os.path.join(CORE, 'Rendering', 'RenderManager.cs')
    actions = re.findall(r'new RenderActions\.(\w+)\(\)', read(rm_path))
    ra_dir = os.path.join(CORE, 'Rendering', 'RenderActions')
    ra_files = len([f for f in os.listdir(ra_dir) if f.endswith('.cs')])
    for i, a in enumerate(actions):
        out(f'  {i+1:2d}. {a}')
    out(f'  （管道中调用 {len(actions)} 步；RenderActions 目录文件数 {ra_files}）')
    results['render_pipeline'] = {'steps': actions, 'render_action_files': ra_files}

    section('八、Plot.Add 添加方法（PlottableAdder.cs）')
    # 方法声明行匹配（不会误匹配字段初始化器）
    method_re = re.compile(r'^\s*public\s+[\w<>\[\],\.\?]+\s+(\w+)\s*\(', re.M)
    adder_methods = []
    adder_files = [p for p in cs_files(CORE) if os.path.basename(p).startswith('PlottableAdder')]
    for path in adder_files:
        for m in method_re.finditer(strip_comments(read(path))):
            name = m.group(1)
            # 排除类声明（主构造函数）与 Get 开头的辅助方法（如 GetNextColor）
            if name != 'PlottableAdder' and not name.startswith('Get'):
                adder_methods.append(name)
    out(f'  分部文件数：{len(adder_files)}；添加方法合计 {len(adder_methods)} 个（含重载）')
    results['plot_add'] = {'partial_files': len(adder_files),
                           'method_count': len(adder_methods),
                           'methods': adder_methods}

    section('九、Interactivity 交互层')
    actions_dir = os.path.join(CORE, 'Interactivity', 'UserActions')
    responses_dir = os.path.join(CORE, 'Interactivity', 'UserActionResponses')
    ua = [f[:-3] for f in os.listdir(actions_dir) if f.endswith('.cs')]
    uar = [f[:-3] for f in os.listdir(responses_dir) if f.endswith('.cs')]
    out(f'  UserActions（用户输入动作）：{len(ua)} 个 → {", ".join(sorted(ua))}')
    out(f'  UserActionResponses（响应器文件）：{len(uar)} 个 → {", ".join(sorted(uar))}')
    # 默认注册的响应器：提取 UserInputProcessor 中的 new 调用（dict.fromkeys 保序去重）
    uip_path = os.path.join(CORE, 'Interactivity', 'UserInputProcessor.cs')
    defaults = re.findall(r'new UserActionResponses\.(\w+)\(', read(uip_path)) \
        if os.path.exists(uip_path) else []
    unique_defaults = list(dict.fromkeys(defaults))
    if os.path.exists(uip_path):
        out(f'  UserInputProcessor 默认注册：{len(unique_defaults)} 个（{len(defaults)} 处调用）')
        out(f'    → {", ".join(unique_defaults)}')
    results['interactivity'] = {'user_actions': sorted(ua), 'responses': sorted(uar),
                                'default_registered': unique_defaults,
                                'default_call_sites': len(defaults)}

    section('十、常用枚举与集合口径')

    def enum_members(enum_name):
        """在全核心库中查找 enum 定义并统计成员个数"""
        for path in cs_files(CORE):
            code = strip_comments(read(path))
            m = re.search(r'enum\s+' + enum_name + r'\b[^{]*\{(.+?)\}', code, re.S)
            if m:
                body = m.group(1)
                # 成员按顶层逗号切分；若特性字符串含逗号会虚计（当前目标均为纯标识符）
                members = [x for x in body.replace('\n', ' ').split(',') if x.strip()]
                return len(members), path
        return None, None

    enums = {}
    for enum_name in ('MarkerShape', 'ArrowShape', 'ColorType', 'Edge', 'Alignment'):
        n, p = enum_members(enum_name)
        if n:
            out(f'  {enum_name:16s} {n:3d} 个成员  （{os.path.basename(p)}）')
            enums[enum_name] = n

    # Colormap / Palette 实现（每种样式一个类）
    colormaps = set()
    palettes = set()
    for path in cs_files(CORE):
        code = strip_comments(read(path))
        colormaps |= set(re.findall(r'class\s+(\w+)\b[^:;\n]*:\s*[^\n{]*IColormap', code))
        palettes |= set(re.findall(r'class\s+(\w+)\b[^:;\n]*:\s*[^\n{]*IPalette', code))
    out(f'  IColormap 实现：{len(colormaps)} 个；IPalette 实现：{len(palettes)} 个')
    results['enums'] = enums
    results['colormaps'] = sorted(colormaps)
    results['palettes'] = sorted(palettes)

    section('十一、平台控件（ScottPlot5 Controls）')
    iplotcontrol_re = re.compile(r'class\s+(\w+)\b[^:;\n]*:\s*([^\n{]*IPlotControl)')
    controls = OrderedDict()
    for plat in sorted(os.listdir(CTRL)):
        pdir = os.path.join(CTRL, plat)
        if not os.path.isdir(pdir):
            continue
        files = cs_files(pdir)
        impls = []
        for path in files:
            impls += iplotcontrol_re.findall(strip_comments(read(path)))[0:1]
        impl_names = [n for n, _ in impls]
        out(f'  {plat:24s} {len(files):4d} 个 .cs   IPlotControl 实现: '
            f'{", ".join(impl_names) or "-"}')
        controls[plat] = {'files': len(files), 'impl': impl_names}
    results['platform_controls'] = controls

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        out('\n（统计完成）')

    # --out 落盘：txt+md+json 三格式（文件名含版本号，便于跨版本比对；不带值默认桌面）
    if args.out is not None:
        out_dir = args.out or default_out_dir()
        os.makedirs(out_dir, exist_ok=True)
        # 版本号用于文件名，若含特殊字符则替换为下划线（版本号通常为数字+点，此处防御性处理）
        ver_tag = re.sub(r'[^\w.]', '_', version)
        txt_path = os.path.join(out_dir, f'scottplot5-stats-v{ver_tag}.txt')
        md_path = os.path.join(out_dir, f'scottplot5-stats-v{ver_tag}.md')
        json_path = os.path.join(out_dir, f'scottplot5-stats-v{ver_tag}.json')
        # 人类可读版（终端文本原样）：写入行缓冲中收集的全部输出行（UTF-8 无 BOM，便于 diff）
        with open(txt_path, 'w', encoding='utf-8', newline='\n') as fp:
            fp.write('\n'.join(_LINES))
        with open(md_path, 'w', encoding='utf-8', newline='\n') as fp:
            fp.write(build_markdown(results))
        with open(json_path, 'w', encoding='utf-8', newline='\n') as fp:
            fp.write(json.dumps(results, ensure_ascii=False, indent=2))
        if not args.json:  # --json 时终端保持纯 JSON，保存提示仅文本模式打印
            print(f'\n已保存：{txt_path}')
            print(f'已保存：{md_path}')
            print(f'已保存：{json_path}')


if __name__ == '__main__':
    main()
