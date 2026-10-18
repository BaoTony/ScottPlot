# -*- coding: utf-8 -*-
"""ScottPlot 5 公共 API 签名提取 —— 学习文档事实核查辅助工具

用途：基于 tree-sitter 语法解析（语法级准确，支持多行签名/泛型/元组参数/
      默认值/扩展方法/索引器）提取核心库 ScottPlot5 全部对外公开 API：
      类型（class/struct/interface/record/enum/delegate）及其 public
      方法、属性、字段、事件、运算符、构造函数的完整签名，按命名空间
      分组输出，供 learning/ 下各编号文档做成员级口径核查与版本 diff。

口径：声明口径，仅 public（含嵌套 public 类型/成员）；
      protected/protected internal/internal 不计入对外 API。

运行（需 Python 3.13 + tree-sitter 依赖，本机 3.15 无 wheel）：
      py -3.13 learning/scripts/scottplot5-api.py           # Markdown 输出到终端
      py -3.13 learning/scripts/scottplot5-api.py --json    # 纯 JSON 输出
      py -3.13 learning/scripts/scottplot5-api.py --out     # 一键落盘：md+json 保存到桌面
      py -3.13 learning/scripts/scottplot5-api.py --out X   # 同上，但保存到指定目录
      py -3.13 learning/scripts/scottplot5-api.py --sln X   # 指定源码根目录（默认按脚本位置自动推导）
"""
import argparse
import json
import os
import re
from collections import OrderedDict

import tree_sitter_c_sharp
from tree_sitter import Language, Parser

# ============================================================
# 路径常量：默认基于脚本自身位置推导仓库根目录（与 scottplot5-stats.py 同规则）
# ============================================================
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLN = os.path.join(REPO, 'src', 'ScottPlot5')          # ScottPlot5 源码根目录
CORE = os.path.join(SLN, 'ScottPlot5')                 # 核心库 ScottPlot5

# tree-sitter C# 解析器（语法级解析，一次构建全程复用）
CS_LANGUAGE = Language(tree_sitter_c_sharp.language())
CS_PARSER = Parser(CS_LANGUAGE)

# 类型声明节点 → 显示用的类型关键字
TYPE_KINDS = {
    'class_declaration': 'class',
    'struct_declaration': 'struct',
    'interface_declaration': 'interface',
    'record_declaration': 'record',
    'record_struct_declaration': 'record struct',
    'enum_declaration': 'enum',
    'delegate_declaration': 'delegate',
}
# 成员声明节点 → 显示用的成员种类
MEMBER_KINDS = {
    'method_declaration': 'method',
    'property_declaration': 'property',
    'field_declaration': 'field',
    'event_declaration': 'event',
    'event_field_declaration': 'event',
    'operator_declaration': 'operator',
    'checked_operator_declaration': 'operator',
    'conversion_operator_declaration': 'conversion',
    'indexer_declaration': 'indexer',
    'constructor_declaration': 'ctor',
    'delegate_declaration': 'delegate',
}
# 成员节点中"签名结束"的边界：遇到下列子节点即截断签名文本
# （block=方法/构造函数体，declaration_list=类体，accessor_list=属性访问器等）
BODY_NODES = {'block', 'declaration_list', 'accessor_list', 'arrow_expression_clause',
              'equals_value_clause', 'variable_declarator', 'initializer'}


def read_bytes(path):
    """读取源文件字节流（tree-sitter 以字节偏移定位，必须用字节切片）"""
    with open(path, 'rb') as fp:
        return fp.read()


def node_text(src, node):
    """按字节偏移从源码切片并解码为文本（容错替换非法字节）"""
    return src[node.start_byte:node.end_byte].decode('utf-8', errors='replace')


def modifiers_of(node):
    """提取节点上全部修饰符文本（modifier 子节点，如 public/static/sealed）"""
    return [c.text.decode('utf-8', errors='replace')
            for c in node.children if c.type == 'modifier']


def is_public(node):
    """判断声明节点是否带 public 修饰符"""
    return 'public' in modifiers_of(node)


def signature_of(src, node):
    """提取声明节点的完整签名文本：从首个非特性子节点起，到方法体/访问器/
    表达式体/初始化器等边界之前的全部内容（含返回类型、名称、泛型参数、
    参数表、约束子句与基类列表，天然支持跨行签名）"""
    start = node.start_byte
    # 跳过节点开头的 [Attribute] 列表，避免签名里混入特性噪音
    for c in node.children:
        if c.type == 'attribute_list':
            start = max(start, c.end_byte)
        else:
            break
    end = node.end_byte
    for c in node.children:
        if c.type in BODY_NODES or c.text == b';':
            end = c.start_byte
            break
    sig = src[start:end].decode('utf-8', errors='replace')
    # 压缩换行与多余空白：多行签名折叠为单行，便于清单阅读与 diff
    return re.sub(r'\s+', ' ', sig).strip()


def accessors_of(src, prop_node):
    """从属性节点的 accessor_list 中提取访问器名（get/set/init）。

    语法中访问器节点是通用的 accessor_declaration，
    具体的 get/set/init 关键字位于其子节点。
    """
    accs = []
    for c in prop_node.children:
        if c.type != 'accessor_list':
            continue
        for a in c.children:
            if 'accessor' not in a.type:
                continue
            kw = next((k.type for k in a.children if k.type in ('get', 'set', 'init')), None)
            if kw:
                accs.append(kw)
    return accs


def enum_member_names(src, enum_node):
    """提取枚举的全部成员名（供清单中列出枚举字面量）"""
    names = []
    for c in enum_node.children:
        if c.type == 'enum_member_declaration_list':
            for m in c.children:
                if m.type == 'enum_member_declaration':
                    names.append(node_text(src, m.child_by_field_name('name')))
    return names


def param_is_extension(src, method_node):
    """判断方法是否为扩展方法（首参数带 this 修饰符）"""
    params = method_node.child_by_field_name('parameters')
    if params is None:
        return False
    for c in params.children:
        if c.type == 'parameter':
            return 'this' in [m.text.decode() for m in c.children if m.type == 'modifier']
    return False


def walk_type(src, node, ns, file_rel, parent_public, stats):
    """递归遍历一个类型声明节点，产出该类型及其嵌套类型的 API 记录。

    parent_public 控制可见性传导：外层类型非 public 时，嵌套类型即使
    声明为 public 也不属于对外 API（C# 可访问性规则）。
    """
    kind = TYPE_KINDS.get(node.type)
    if kind is None:
        return None
    pub = is_public(node) and parent_public
    name = node_text(src, node.child_by_field_name('name'))
    # 类型签名：从声明起截到类型体/分号之前（record 主构造参数、基类列表、约束全含）
    type_sig = signature_of(src, node)
    if not pub:
        # 非 public 类型：仅嵌套的 public 类型不可能存在（外层已不可见），直接返回
        return None
    stats['types'] += 1
    record = {'name': name, 'kind': kind, 'signature': type_sig,
              'file': file_rel, 'members': [], 'enum_members': [], 'nested': []}

    # 遍历类型体内的成员与嵌套类型
    body = node.child_by_field_name('body')
    if body is not None:
        for c in body.children:
            m = collect_member(src, c, ns, name, stats)
            if m is not None:
                record['members'].append(m)
            elif c.type in TYPE_KINDS:
                sub = walk_type(src, c, ns, file_rel, True, stats)
                if sub is not None:
                    record['nested'].append(sub)
            elif c.type == 'enum_member_declaration_list' and kind == 'enum':
                record['enum_members'] = enum_member_names(src, node)
    if kind == 'enum':
        record['enum_members'] = enum_member_names(src, node)
    return record


def collect_member(src, node, ns, owner, stats):
    """提取单个成员声明节点的 API 记录（非 public 成员返回 None）"""
    kind = MEMBER_KINDS.get(node.type)
    if kind is None:
        return None
    if not is_public(node):
        return None
    name_field = node.child_by_field_name('name')
    name = node_text(src, name_field) if name_field is not None else ''
    sig = signature_of(src, node)
    # 属性/索引器：签名截断在访问器列表之前，补充 { get; set; } 摘要
    if kind == 'property' and 'get' not in sig:
        accs = accessors_of(src, node)
        if accs:
            sig += ' { ' + ', '.join(accs) + '; }'
    stats['members'] += 1
    stats['by_kind'][kind] = stats['by_kind'].get(kind, 0) + 1
    extra = ' [扩展方法]' if kind == 'method' and param_is_extension(src, node) else ''
    return {'kind': kind, 'name': name, 'signature': sig + extra}


def parse_file(path, rel):
    """解析单个 .cs 文件，返回 {命名空间: [类型记录]} 与计数增量"""
    src = read_bytes(path)
    tree = CS_PARSER.parse(src)
    root = tree.root_node
    # 定位命名空间：优先文件级（file_scoped），兼容块级与无命名空间
    ns = '(global)'
    file_scoped = False
    block_body = None
    for c in root.children:
        if c.type == 'file_scoped_namespace_declaration':
            ns = node_text(src, c.child_by_field_name('name'))
            file_scoped = True
            break
        if c.type == 'namespace_declaration':
            ns = node_text(src, c.child_by_field_name('name'))
            block_body = c.child_by_field_name('body')
            break

    stats = {'types': 0, 'members': 0, 'by_kind': {}}
    types = []
    # 声明位置随命名空间形式而异（tree-sitter 语法的关键差异）：
    # - 块级 namespace：类型在 namespace 的 body 内
    # - 文件级 namespace / 无命名空间：类型是编译单元 root 的直接子节点
    #   （file_scoped 节点本身无花括号主体，后续声明被解析为 root 子节点）
    if file_scoped or ns == '(global)':
        candidates = list(root.children)
    else:
        candidates = list(block_body.children) if block_body is not None else []
    for c in candidates:
        if c.type in TYPE_KINDS:
            t = walk_type(src, c, ns, rel, True, stats)
            if t is not None:
                types.append(t)
    return ns, types, stats


def collect_all(core_dir):
    """扫描核心库全部 .cs 文件，汇总为按命名空间分组的 API 清单"""
    namespaces = OrderedDict()
    totals = {'types': 0, 'members': 0, 'by_kind': {}}
    files = sorted(
        os.path.join(root, f)
        for root, dirs, fs in os.walk(core_dir)
        for f in fs
        if f.endswith('.cs') and not f.endswith(('.g.cs', '.Designer.cs'))
        and 'obj' not in root.split(os.sep) and 'bin' not in root.split(os.sep))
    for path in files:
        rel = os.path.relpath(path, core_dir)
        ns, types, stats = parse_file(path, rel)
        if not types:
            continue
        buckets = namespaces.setdefault(ns, [])
        buckets.extend(types)
        totals['types'] += stats['types']
        totals['members'] += stats['members']
        for k, v in stats['by_kind'].items():
            totals['by_kind'][k] = totals['by_kind'].get(k, 0) + v
    # 各命名空间内按类型名排序，保证多次生成的清单可稳定 diff
    for ns in namespaces:
        namespaces[ns].sort(key=lambda t: t['name'])
    return namespaces, totals


def build_markdown(namespaces, totals):
    """把 API 清单渲染为人类可读的 Markdown 文档"""
    lines = ['# ScottPlot5 公共 API 签名清单', '',
             '> 由 `learning/scripts/scottplot5-api.py` 自动生成（声明口径，'
             '仅 public；protected/internal 不计入）。', '']
    # 摘要表：命名空间 × 类型与成员数
    lines += ['## 摘要', '',
              '| 命名空间 | 类型数 | 成员数 |', '|---|---:|---:|']
    for ns, types in namespaces.items():
        n_members = sum(len(t['members']) for t in types)
        lines.append(f'| `{ns}` | {len(types)} | {n_members} |')
    lines += ['', f'**合计：{totals["types"]} 个类型，'
              f'{totals["members"]} 个成员（' +
              '，'.join(f'{k} {v}' for k, v in sorted(totals["by_kind"].items())) + '）', '']
    # 逐命名空间展开：类型签名 + 成员签名代码块
    for ns, types in namespaces.items():
        lines += [f'## {ns}', '']
        for t in types:
            lines += [f'### `{t["signature"]}`', f'<!-- {t["file"]} -->', '```csharp']
            lines += [t['signature']]
            if t['enum_members']:
                lines.append('成员: ' + ', '.join(t['enum_members']))
            for m in t['members']:
                lines.append(m['signature'])
            lines += ['```', '']
            for sub in t['nested']:
                lines += [f'### `{sub["signature"]}`（嵌套于 {t["name"]}）',
                          '```csharp']
                lines += [sub['signature']] + [m['signature'] for m in sub['members']]
                lines += ['```', '']
    return '\n'.join(lines)


def default_out_dir():
    """探测当前用户桌面目录（与 scottplot5-stats.py 同规则）"""
    home = os.path.expanduser('~')
    for cand in (os.path.join(home, 'Desktop'),
                 os.path.join(home, 'OneDrive', 'Desktop'),
                 os.path.join(home, '桌面')):
        if os.path.isdir(cand):
            return cand
    return home


def parse_args():
    """解析命令行参数：源码根目录覆盖项、JSON 输出开关与落盘目录"""
    ap = argparse.ArgumentParser(description='ScottPlot5 公共 API 签名提取（学习文档事实核查辅助）')
    ap.add_argument('--sln', help='ScottPlot5 源码根目录（默认按脚本位置自动推导）')
    ap.add_argument('--json', action='store_true', help='仅输出纯 JSON 统计结果')
    ap.add_argument('--out', nargs='?', const='', default=None, metavar='目录',
                    help='一键落盘：不带值时保存到桌面；也可指定输出目录。'
                         '同时生成 scottplot5-api.md 与 scottplot5-api.json')
    return ap.parse_args()


def main():
    global SLN, CORE
    args = parse_args()
    if args.sln:
        SLN = args.sln
        CORE = os.path.join(SLN, 'ScottPlot5')

    namespaces, totals = collect_all(CORE)
    result = OrderedDict()
    result['core'] = CORE
    result['totals'] = totals
    result['namespaces'] = namespaces

    # 落盘：md+json 双格式（默认桌面，可指定目录）
    if args.out is not None:
        out_dir = args.out or default_out_dir()
        os.makedirs(out_dir, exist_ok=True)
        md_path = os.path.join(out_dir, 'scottplot5-api.md')
        json_path = os.path.join(out_dir, 'scottplot5-api.json')
        with open(md_path, 'w', encoding='utf-8', newline='\n') as fp:
            fp.write(build_markdown(namespaces, totals))
        with open(json_path, 'w', encoding='utf-8', newline='\n') as fp:
            fp.write(json.dumps(result, ensure_ascii=False, indent=2))
        if not args.json:
            print(f'已保存：{md_path}')
            print(f'已保存：{json_path}')

    # 终端输出：默认 Markdown；--json 时仅纯 JSON（保证可重定向解析）
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif args.out is None:
        print(build_markdown(namespaces, totals))


if __name__ == '__main__':
    main()
