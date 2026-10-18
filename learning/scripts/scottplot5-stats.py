# -*- coding: utf-8 -*-
"""ScottPlot 5 全库源码统计 —— 学习文档事实核查辅助工具

用途：一次性扫描 src/ScottPlot5 全部源码，输出解决方案全貌、核心库分层
      文件数、Primitives 类型分类、接口清单、数据源继承关系、Plottable
      清单、渲染管线步骤、交互响应器、Add 方法数、枚举成员数等关键事实，
      供 learning/ 下各编号文档核对数字口径使用。

运行：python learning/scripts/scottplot5-stats.py           # 人类可读输出
      python learning/scripts/scottplot5-stats.py --json    # 纯 JSON 输出（可重定向落盘做前后 diff）
      python learning/scripts/scottplot5-stats.py --out     # 一键落盘：txt+json 双格式保存到桌面
      python learning/scripts/scottplot5-stats.py --out X   # 同上，但保存到指定目录
      python learning/scripts/scottplot5-stats.py --sln X   # 指定源码根目录（默认按脚本位置自动推导）
"""
import argparse
import json
import os
import re
from collections import OrderedDict

# ============================================================
# 路径常量：默认基于脚本自身位置推导仓库根目录
# （scripts → learning → 仓库根，共上溯 3 级），
# 避免硬编码绝对路径导致换机器或移动仓库后失效；可用 --sln 覆盖
# ============================================================
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLN = os.path.join(REPO, 'src', 'ScottPlot5')          # ScottPlot5 源码根目录
CORE = os.path.join(SLN, 'ScottPlot5')                 # 核心库 ScottPlot5
CTRL = os.path.join(SLN, 'ScottPlot5 Controls')        # 平台控件解决方案

# 文件内容缓存：全库文件内容只读一次、多节复用
# （原先第四节与第十节等会各自全量重读核心库，同一文件最多被重复读 7 遍）
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
        # 跳过编译输出目录，避免把生成代码计入统计
        dirs[:] = [d for d in dirs if d not in ('bin', 'obj')]
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
    """统计一组文件的总行数（复用 read 缓存，不再二次打开文件）"""
    return sum(len(read(p).splitlines()) for p in paths)


def out(line=''):
    """统一输出入口：始终收集进行缓冲（供 --out 落盘），非 QUIET 时同步打印终端"""
    _LINES.append(line)
    if not QUIET:
        print(line)


def section(title):
    """打印统一风格的分节标题（--json 模式下仅入缓冲、不打印）"""
    out('')
    out('=' * 78)
    out(title)
    out('=' * 78)


def default_out_dir():
    """探测当前用户桌面目录，作为 --out 不带值时的默认落盘位置。

    依次尝试常见桌面路径（兼容 OneDrive 重定向与中文系统「桌面」文件夹），
    全部不存在时兜底返回用户主目录。
    """
    home = os.path.expanduser('~')
    for cand in (os.path.join(home, 'Desktop'),
                 os.path.join(home, 'OneDrive', 'Desktop'),
                 os.path.join(home, '桌面')):
        if os.path.isdir(cand):
            return cand
    return home


def parse_args():
    """解析命令行参数：源码根目录覆盖项、JSON 输出开关与落盘目录"""
    ap = argparse.ArgumentParser(description='ScottPlot5 全库源码统计（学习文档事实核查辅助）')
    ap.add_argument('--sln', help='ScottPlot5 源码根目录（默认按脚本位置自动推导）')
    ap.add_argument('--json', action='store_true', help='仅输出纯 JSON 统计结果')
    ap.add_argument('--out', nargs='?', const='', default=None, metavar='目录',
                    help='一键落盘：不带值时保存到桌面；也可指定输出目录。'
                         '会同时生成 scottplot5-stats.txt（人类可读）与 '
                         'scottplot5-stats.json（机器可读），同名旧文件被覆盖')
    return ap.parse_args()


def main():
    global SLN, CORE, CTRL, QUIET
    args = parse_args()
    QUIET = args.json
    if args.sln:
        # 命令行显式指定源码根目录时，覆盖默认推导出的路径
        SLN = args.sln
        CORE = os.path.join(SLN, 'ScottPlot5')
        CTRL = os.path.join(SLN, 'ScottPlot5 Controls')

    # 全部统计结果汇总，--json 模式下整体输出
    results = OrderedDict()

    # ============================================================
    # 一、解决方案全貌：每个项目的 .cs 文件数与代码行数
    # ============================================================
    section('一、解决方案全貌（src/ScottPlot5 下各项目）')
    solution = OrderedDict()
    for proj in sorted(os.listdir(SLN)):
        pdir = os.path.join(SLN, proj)
        if not os.path.isdir(pdir):
            continue
        files = cs_files(pdir)
        n_lines = line_count(files)
        out(f'  {proj:28s} {len(files):5d} 个 .cs   {n_lines:8d} 行')
        solution[proj] = {'files': len(files), 'lines': n_lines}
    results['solution'] = solution

    # ============================================================
    # 二、核心库分层地图：ScottPlot5 主项目各目录文件数
    # ============================================================
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

    # ============================================================
    # 三、Primitives 类型分类（按文件内首个类型声明的种类统计）
    # ============================================================
    section('三、Primitives 基础类型分类')
    prim_dir = os.path.join(CORE, 'Primitives')
    kind_re = re.compile(
        r'\b(public|internal)?\s*(?:sealed\s+|abstract\s+|static\s+|partial\s+)*'
        r'(record\s+struct|record\s+class|record|struct|class|interface|enum)\s+(\w+)')
    # 注：record class 在下方被归并进 record 一类，故键中不再单列
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
    out(f'  合计 {total_ifaces} 个接口，分布：')
    for top, names in sorted(ifaces_by_dir.items(), key=lambda kv: -len(kv[1])):
        preview = ', '.join(sorted(names)[:6])
        more = f' ...' if len(names) > 6 else ''
        out(f'    {top:22s} {len(names):3d} 个  {preview}{more}')
    results['interfaces'] = {'total': total_ifaces,
                             'by_dir': {k: sorted(v) for k, v in ifaces_by_dir.items()}}

    # ============================================================
    # 五、DataSources：具体类型及其实现的数据源接口
    # ============================================================
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
            # 仅跳过本目录内定义的接口自身
            # （type_re 的备选分支不含 interface 关键字，不会误匹配接口声明）
            if name in defined_ifaces:
                continue
            src_bases = re.findall(r'I\w*(?:Source|DataSource)\w*', bases)
            impl_types.append((name, kind.replace(' ', ''), ', '.join(src_bases) or '(基类间接实现)'))
    for name, kind, bases in sorted(impl_types):
        out(f'  {name:38s} {kind:14s} {bases}')
    results['data_sources'] = [
        {'name': n, 'kind': k, 'bases': b} for n, k, b in sorted(impl_types)]

    # ============================================================
    # 六、Plottables：文件数口径（根目录 / Interactive / 其他）
    # ============================================================
    section('六、Plottable 图表类（实现 IPlottable）')
    plottables_dir = os.path.join(CORE, 'Plottables')
    all_plottable_files = cs_files(plottables_dir)
    # 主口径 = .cs 文件数：根目录 + Interactive 子目录（其余子目录单独列出）
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

    # 辅助口径 = 从类声明中提取 IPlottable 实现类名（供交叉核对）
    iplottable_re = re.compile(r'class\s+(\w+)\b[^:;\n]*:\s*([^\n{]*IPlottable[^\n{]*)')
    normal, interactive = [], []
    for path in all_plottable_files:
        code = strip_comments(read(path))
        for m in iplottable_re.finditer(code):
            name = m.group(1)
            (interactive if 'Interactive' in name or os.sep + 'Interactive' + os.sep in path
             else normal).append(name)
    out(f'  （按类声明识别：常规 {len(normal)} 个，Interactive {len(interactive)} 个；'
        f'部分类经由 PlottableBase 间接实现 IPlottable，故文件数为准）')
    results['plottables'] = {
        'by_dir': by_dir, 'root': len(root_files), 'total': len(all_plottable_files),
        'by_class_declaration': {'normal': len(normal), 'interactive': len(interactive)},
    }

    # ============================================================
    # 七、渲染管线：RenderManager 中的 RenderActions 步骤序列
    # ============================================================
    section('七、RenderManager 渲染管线步骤')
    rm_path = os.path.join(CORE, 'Rendering', 'RenderManager.cs')
    actions = re.findall(r'new RenderActions\.(\w+)\(\)', read(rm_path))
    ra_dir = os.path.join(CORE, 'Rendering', 'RenderActions')
    ra_files = len([f for f in os.listdir(ra_dir) if f.endswith('.cs')])
    for i, a in enumerate(actions):
        out(f'  {i+1:2d}. {a}')
    out(f'  （管道中调用 {len(actions)} 步；RenderActions 目录文件数 {ra_files}）')
    results['render_pipeline'] = {'steps': actions, 'render_action_files': ra_files}

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
    out(f'  分部文件数：{len(adder_files)}；添加方法合计 {len(adder_methods)} 个（含重载）')
    results['plot_add'] = {'partial_files': len(adder_files),
                           'method_count': len(adder_methods),
                           'methods': adder_methods}

    # ============================================================
    # 九、Interactivity：用户动作、响应器、默认注册清单
    # ============================================================
    section('九、Interactivity 交互层')
    actions_dir = os.path.join(CORE, 'Interactivity', 'UserActions')
    responses_dir = os.path.join(CORE, 'Interactivity', 'UserActionResponses')
    ua = [f[:-3] for f in os.listdir(actions_dir) if f.endswith('.cs')]
    uar = [f[:-3] for f in os.listdir(responses_dir) if f.endswith('.cs')]
    out(f'  UserActions（用户输入动作）：{len(ua)} 个 → {", ".join(sorted(ua))}')
    out(f'  UserActionResponses（响应器文件）：{len(uar)} 个 → {", ".join(sorted(uar))}')
    # 默认注册的响应器：从 UserInputProcessor 中提取 new UserActionResponses.X()
    # （用 dict.fromkeys 按出现顺序去重，避免重复注册点造成虚高计数）
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
                # 顶层成员以逗号分隔（成员内可能有 = 赋值，但不影响计数）。
                # 口径注：若未来成员特性字符串中出现逗号（如 [Description("a, b")]）
                # 会导致虚计；当前统计目标均为纯标识符成员，无此情况
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

    # ============================================================
    # 十一、平台控件：8 个平台项目与 IPlotControl 实现
    # ============================================================
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

    # ============================================================
    # 输出：默认人类可读；--json 时仅输出机器可读的汇总结果
    # ============================================================
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        out('\n（统计完成）')

    # ============================================================
    # 一键落盘：--out 同时写出 txt 与 json 两份文件
    # （不带值默认桌面，也可指定目录；同名旧文件覆盖）
    # ============================================================
    if args.out is not None:
        out_dir = args.out or default_out_dir()
        os.makedirs(out_dir, exist_ok=True)
        txt_path = os.path.join(out_dir, 'scottplot5-stats.txt')
        json_path = os.path.join(out_dir, 'scottplot5-stats.json')
        # 人类可读版：写入行缓冲中收集的全部输出行（UTF-8 无 BOM，便于 diff）
        with open(txt_path, 'w', encoding='utf-8', newline='\n') as fp:
            fp.write('\n'.join(_LINES))
        # 机器可读版：与 --json 终端输出完全一致的汇总结果
        with open(json_path, 'w', encoding='utf-8', newline='\n') as fp:
            fp.write(json.dumps(results, ensure_ascii=False, indent=2))
        if not args.json:
            # JSON 模式下终端必须保持纯 JSON，故保存提示仅在文本模式打印
            print(f'\n已保存：{txt_path}')
            print(f'已保存：{json_path}')


if __name__ == '__main__':
    main()
