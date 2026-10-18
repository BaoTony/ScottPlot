# -*- coding: utf-8 -*-
"""ScottPlot 5 数据链路分析 - 从数据源到屏幕像素的完整追踪"""
import os, re
from collections import defaultdict

base = r'd:\dev\store\ScottPlot\src\ScottPlot5\ScottPlot5'

# ============================================================
# 1. 追踪 IPlottable 的实现类（图表数据的消费者）
# ============================================================
plottables_dir = os.path.join(base, 'Plottables')
plottable_classes = []
for root, dirs, files in os.walk(plottables_dir):
    for f in files:
        if f.endswith('.cs') and not f.endswith('.g.cs'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            # 找实现了 IPlottable 的 class
            matches = re.findall(r'class\s+(\w+).*?:\s*(.*?IPlottable.*?)(?:\n|{)', content)
            if matches:
                cls_name = matches[0][0]
                # 找构造函数中注入的数据源类型
                ctor_match = re.search(r'public\s+' + cls_name + r'\s*\((.*?)\)', content)
                ctor_params = ctor_match.group(1) if ctor_match else ''
                # 找 Data 属性类型
                data_matches = re.findall(r'(?:public|private|protected|internal)\s+(\w+(?:Source|DataSource|List|Array))\s+\w+\s*[{=]', content)
                data_types = list(set(data_matches))
                plottable_classes.append((cls_name, ctor_params.strip(), data_types))

print("=" * 75)
print("链路一：数据源 → Plottable（图表）")
print("=" * 75)
print(f"{'Plottable':25s} {'构造函数参数':45s}")
print("-" * 75)
for name, ctor, dts in sorted(plottable_classes):
    print(f"{name:25s} {ctor[:45]:45s}")

# ============================================================
# 2. 追踪 PlottableAdder（Plot.Add.XXX 的入口）
# ============================================================
adder_file = os.path.join(base, 'PlottableAdder.cs')
if os.path.exists(adder_file):
    with open(adder_file, 'r', encoding='utf-8', errors='ignore') as fp:
        adder_content = fp.read()
    add_methods = re.findall(r'public\s+(\w+)\s+(\w+)\((.*?)\)', adder_content)
    print(f"\nPlot.Add 提供 {len(add_methods)} 个添加方法")

# ============================================================
# 3. 追踪 RenderManager 渲染管道
# ============================================================
rm_file = os.path.join(base, 'Rendering', 'RenderManager.cs')
if os.path.exists(rm_file):
    with open(rm_file, 'r', encoding='utf-8', errors='ignore') as fp:
        rm_content = fp.read()
    actions = re.findall(r'new RenderActions\.(\w+)\(\)', rm_content)
    print(f"\n{'='*75}")
    print("链路二：RenderManager 渲染管道（20+ 步）")
    print("=" * "75")
    for i, a in enumerate(actions):
        print(f"  {i+1:2d}. {a}")

# ============================================================
# 4. 追踪 Primitives（基础数据类型）
# ============================================================
primitives_dir = os.path.join(base, 'Primitives')
primitives = []
for root, dirs, files in os.walk(primitives_dir):
    for f in files:
        if f.endswith('.cs') and not f.endswith('.g.cs'):
            primitives.append(f.replace('.cs', ''))

print(f"\n{'='*75}")
print("链路零：Primitives 基础类型（{0} 个）".format(len(primitives)))
print("=" * "75")
# Group by category
structs = []
classes = []
records = []
for f in sorted(primitives):
    fpath = os.path.join(primitives_dir, f + '.cs') if os.path.exists(os.path.join(primitives_dir, f + '.cs')) else None
    if fpath:
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
            first = fp.readline()[:100]
        if 'struct' in first or 'partial struct' in first:
            structs.append(f)
        elif 'record' in first:
            records.append(f)
        else:
            classes.append(f)

print(f"  Structs ({len(structs)}): {', '.join(structs[:15])}...")
print(f"  Records ({len(records)}): {', '.join(records)}")

# ============================================================
# 5. 追踪 Controls 中的 Plot 绑定
# ============================================================
controls_base = r'd:\dev\store\ScottPlot\src\ScottPlot5\ScottPlot5 Controls'
controls = defaultdict(str)
for root, dirs, files in os.walk(controls_base):
    for f in files:
        if f.endswith('.cs') and 'Plot' in f and 'Control' in f:
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                for line in fp:
                    if 'Plot' in line and '=' in line and 'new' in line:
                        controls[os.path.basename(root)] += line.strip()[:100] + '\n'
                        break

print(f"\n{'='*75}")
print("链路三：Plot ↔ Controls 双向绑定")
print("=" * "75")
for ctrl, info in sorted(controls.items()):
    print(f"  {ctrl}: {info.strip()[:80]}")

# ============================================================
# 6. 追踪 Interactivity 交互数据流
# ============================================================
inter_dir = os.path.join(base, 'Interactivity')
actions_dir = os.path.join(inter_dir, 'UserActions')
responses_dir = os.path.join(inter_dir, 'UserActionResponses')

actions_list = []
responses_list = []

for root, dirs, files in os.walk(actions_dir):
    for f in files:
        if f.endswith('.cs'):
            actions_list.append(f.replace('.cs', ''))

for root, dirs, files in os.walk(responses_dir):
    for f in files:
        if f.endswith('.cs'):
            responses_list.append(f.replace('.cs', ''))

print(f"\n{'='*75}")
print("链路四：用户输入 → 交互响应")
print("=" * "75")
print(f"  UserActions ({len(actions_list)})   →  UserInputProcessor")
print(f"     {', '.join(actions_list)}")
print(f"  UserActionResponses ({len(responses_list)})   →  修改 Plot 状态")
print(f"     {', '.join(responses_list)}")

# ============================================================
# 7. 追踪 DataSources 接口层次
# ============================================================
ds_dir = os.path.join(base, 'DataSources')
ds_classes = []
for root, dirs, files in os.walk(ds_dir):
    for f in files:
        if f.endswith('.cs') and not f.endswith('.g.cs'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            cls = re.findall(r'class\s+(\w+)\s*:', content)
            ifaces = re.findall(r':\s*(I\w+Source[^,\n{]*)', content)
            if cls:
                ds_classes.append((cls[0], ifaces))

print(f"\n{'='*75}")
print("链路一详细：DataSource 继承/接口层次")
print("=" * "75")
for cls, ifaces in sorted(ds_classes):
    print(f"  {cls:35s} : {', '.join(ifaces[:3])}")

print("\n" + "=" * 75)
print("数据链路总图")
print("=" * 75)