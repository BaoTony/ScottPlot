"""
将 ScottPlot Cookbook 生成的 .md 文件转换为本地可浏览的 .html 文件。
零依赖（仅使用标准库）。

用法:
    python cookbook-to-html.py [cookbook目录]
"""

import os
import re
import sys
import html as html_module


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """解析 YAML frontmatter（仅提取顶级键值对，足够用了）"""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text

    fm_text = parts[1]
    body = parts[2]

    result = {}
    for line in fm_text.strip().split("\n"):
        line = line.strip()
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        # 去掉引号
        if (value.startswith('"') and value.endswith('"')) or \
           (value.startswith("'") and value.endswith("'")):
            value = value[1:-1]
        result[key] = value

    return result, body


def parse_frontmatter_with_arrays(text: str) -> tuple[dict, str]:
    """解析 YAML frontmatter（处理列表类型的值）"""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text

    fm_text = parts[1]
    body = parts[2]

    result = {}
    current_key = None
    current_list = []

    for line in fm_text.strip().split("\n"):
        stripped = line.strip()
        if not stripped:
            continue

        # 列表项
        if stripped.startswith("- "):
            val = stripped[2:].strip()
            val = val.strip('"').strip("'")
            if current_key:
                current_list.append(val)
            continue

        # 保存上一条列表
        if current_key and current_list:
            result[current_key] = current_list
            current_key = None
            current_list = []

        if ":" not in stripped:
            continue

        key, _, value = stripped.partition(":")
        key = key.strip()
        value = value.strip()

        # 数组开始标记 [ 或空值
        if value.startswith("["):
            # 内联数组: ["a", "b"]
            arr_str = value.strip("[]")
            items = []
            for item in arr_str.split(","):
                item = item.strip().strip('"').strip("'")
                if item:
                    items.append(item)
            result[key] = items
        elif value == "":
            current_key = key
            current_list = []
        else:
            val = value.strip('"').strip("'")
            result[key] = val

    if current_key and current_list:
        result[current_key] = current_list

    return result, body


def convert_recipe_sp5(md_text: str) -> str:
    """将 Hugo 短代码 {{< recipe-sp5 >}} 转换为 HTML"""
    pattern = re.compile(
        r'\{\{<\s*recipe-sp5\s+sourceUrl="([^"]*)"\s+imageUrl="([^"]*)"\s*>\}\}'
        r'(.*?)'
        r'\{\{<\s*/recipe-sp5\s*>\}\}',
        re.DOTALL
    )

    def replacer(m):
        source_url = m.group(1)
        image_url = m.group(2)
        code = m.group(3).strip()
        escaped_code = html_module.escape(code)
        return f"""<div class="recipe-code">
<div class="recipe-image">
    <a href="{image_url}" target="_blank">
        <img src="{image_url}" style="max-width: 100%; border: 1px solid #ddd; border-radius: 4px;" loading="lazy" />
    </a>
</div>
<pre class="recipe-source"><code class="language-csharp">{escaped_code}</code></pre>
<small><a href="{source_url}" target="_blank">View source on GitHub</a></small>
</div>"""
    return pattern.sub(replacer, md_text)


def fix_links(md_text: str) -> str:
    """修复内部链接"""
    # 分类链接: href='/cookbook/5/CategoryName' → href='CategoryName.html'
    md_text = re.sub(
        r"""href=['"]/cookbook/5/([\w]+)/?['"]""",
        r"href='\1.html'",
        md_text
    )
    # 食谱链接: href='/cookbook/5/Cat/Recipe' → href='Cat.Recipe.html'
    md_text = re.sub(
        r"""href=['"]/cookbook/5/([\w]+)/([\w]+)/?['"]""",
        r"href='\1.\2.html'",
        md_text
    )
    # 特殊页面
    for page in ["colors", "colormaps", "palettes", "search"]:
        md_text = re.sub(
            rf"""href=['"]\b{page}\b['"]""",
            rf"href='{page.capitalize()}.html'",
            md_text
        )
    return md_text


def fix_image_paths(md_text: str) -> str:
    """将绝对图片路径转为相对路径，并移除时间戳"""
    # Markdown 图片: [alt](/cookbook/5/images/xxx.png) → [alt](images/xxx.png)
    md_text = re.sub(
        r'\]\(/cookbook/5/images/',
        r'](images/',
        md_text
    )
    # HTML img src: 保留原引号类型，只替换路径
    md_text = re.sub(
        r"""src=(['"])/cookbook/5/images/""",
        r"""src=\1images/""",
        md_text
    )
    # HTML href: 保留原引号类型，只替换路径
    md_text = re.sub(
        r"""href=(['"])/cookbook/5/images/""",
        r"""href=\1images/""",
        md_text
    )
    # 移除时间戳: .png?123456 → .png
    md_text = re.sub(r'\.png\?\d+', '.png', md_text)
    return md_text


def remove_external_icons(md_text: str) -> str:
    """移除外部图标"""
    return re.sub(
        r"<img src=['\"]/images/icons/[^'\"]+['\"][^>]*>",
        "",
        md_text
    )


def remove_target_blank(md_text: str) -> str:
    """移除 target='_blank'"""
    return md_text.replace(" target='_blank'", "")


def simple_markdown_to_html(text: str) -> str:
    """简版 Markdown → HTML（不依赖外部库）"""
    lines = text.split("\n")
    result = []
    in_code_block = False
    code_lang = ""
    code_lines = []
    in_list = False

    for line in lines:
        # 代码块
        if line.strip().startswith("```"):
            if in_code_block:
                # 结束代码块
                escaped = "\n".join(html_module.escape(l) for l in code_lines)
                result.append(f'<pre><code class="language-{code_lang}">{escaped}</code></pre>')
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
                code_lang = line.strip()[3:].strip() or ""
            continue

        if in_code_block:
            code_lines.append(line)
            continue

        # HTML 标签原样保留（div, h1-h6 等）
        if re.match(r'^\s*<', line):
            # 关闭列表（如果有）
            if in_list and not line.strip().startswith("<li"):
                result.append("</ul>")
                in_list = False
            result.append(line)
            continue

        stripped = line.strip()
        if not stripped:
            if in_list:
                result.append("</ul>")
                in_list = False
            continue

        # 标题
        m = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if m:
            if in_list:
                result.append("</ul>")
                in_list = False
            level = len(m.group(1))
            content = m.group(2)
            result.append(f'<h{level}>{content}</h{level}>')
            continue

        # 无序列表
        m = re.match(r'^[\-\*\+]\s+(.+)$', stripped)
        if m:
            if not in_list:
                result.append("<ul>")
                in_list = True
            content = m.group(1)
            content = _inline_markdown(content)
            result.append(f'<li>{content}</li>')
            continue

        # 水平线
        if stripped in ("---", "***", "___", "<hr>", "<hr/>"):
            if in_list:
                result.append("</ul>")
                in_list = False
            result.append("<hr>")
            continue

        # 普通段落
        if in_list:
            result.append("</ul>")
            in_list = False
        result.append(f'<p>{_inline_markdown(line)}</p>')

    if in_code_block and code_lines:
        escaped = "\n".join(html_module.escape(l) for l in code_lines)
        result.append(f'<pre><code class="language-{code_lang}">{escaped}</code></pre>')

    if in_list:
        result.append("</ul>")

    return "\n".join(result)


def _inline_markdown(text: str) -> str:
    """内联 Markdown 处理（粗体、斜体、链接、代码、图片）"""
    # 行内代码
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # 图片
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" />', text)
    # 链接
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    # 粗斜体
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # 粗体
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # 斜体
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # 删除线
    text = re.sub(r'~~(.+?)~~', r'<del>\1</del>', text)
    return text


def convert_md_to_html(input_path: str, output_path: str):
    """将单个 .md 文件转换为 .html"""
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    fm, body = parse_frontmatter_with_arrays(content)

    # 处理内容
    body = convert_recipe_sp5(body)
    body = fix_links(body)
    body = fix_image_paths(body)
    body = remove_external_icons(body)
    body = remove_target_blank(body)

    # Markdown → HTML
    html_body = simple_markdown_to_html(body)

    title = fm.get("Title") or fm.get("title") or "ScottPlot Cookbook"
    description = fm.get("Description") or fm.get("description") or ""
    breadcrumbs = fm.get("BreadcrumbNames", [])
    breadcrumb_urls = fm.get("BreadcrumbUrls", [])
    version = fm.get("Version", "ScottPlot 5")

    if isinstance(breadcrumbs, str):
        breadcrumbs = [x.strip().strip('"') for x in breadcrumbs.strip("[]").split(",")]
    if isinstance(breadcrumb_urls, str):
        breadcrumb_urls = [x.strip().strip('"') for x in breadcrumb_urls.strip("[]").split(",")]

    # 构建面包屑
    breadcrumb_html = ""
    if breadcrumbs and breadcrumb_urls and len(breadcrumbs) == len(breadcrumb_urls):
        parts = []
        for i, (name, url) in enumerate(zip(breadcrumbs, breadcrumb_urls)):
            if i < len(breadcrumbs) - 1:
                fixed_url = url
                fixed_url = re.sub(r"/cookbook/5/(\w+)/?$", r"\1.html", fixed_url)
                fixed_url = re.sub(r"/cookbook/5/(\w+)/(\w+)/?$", r"\1.\2.html", fixed_url)
                fixed_url = re.sub(r"/cookbook/5/?$", "index.html", fixed_url)
                parts.append(f'<a href="{fixed_url}">{name}</a>')
            else:
                parts.append(f'<span>{name}</span>')
        breadcrumb_html = " &raquo; ".join(parts)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            max-width: 960px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
            line-height: 1.6;
        }}
        .breadcrumb {{
            font-size: 0.9em;
            color: #666;
            margin-bottom: 20px;
            padding: 8px 12px;
            background: #f5f5f5;
            border-radius: 4px;
        }}
        .breadcrumb a {{ color: #0366d6; text-decoration: none; }}
        .breadcrumb a:hover {{ text-decoration: underline; }}
        .version {{
            font-size: 0.8em;
            color: #999;
            text-align: right;
            margin-bottom: 10px;
        }}
        h1 {{ border-bottom: 2px solid #0366d6; padding-bottom: 8px; margin-top: 24px; }}
        h2 {{ margin-top: 30px; }}
        .recipe-code {{
            background: #f6f8fa;
            border: 1px solid #d1d5da;
            border-radius: 6px;
            padding: 16px;
            margin: 16px 0;
        }}
        .recipe-image {{ text-align: center; margin-bottom: 16px; }}
        .recipe-image img {{ max-width: 100%; }}
        .recipe-source {{
            background: #fff;
            border: 1px solid #e1e4e8;
            border-radius: 4px;
            padding: 12px;
            overflow-x: auto;
            font-size: 0.85em;
            line-height: 1.5;
        }}
        pre code {{
            font-family: "Cascadia Code", "Fira Code", Consolas, "Courier New", monospace;
        }}
        code {{
            background: #f0f0f0;
            padding: 2px 5px;
            border-radius: 3px;
            font-size: 0.9em;
        }}
        pre code {{
            background: none;
            padding: 0;
        }}
        small a {{ color: #0366d6; }}
        ul {{ padding-left: 24px; }}
        li {{ margin: 4px 0; }}
        hr {{ border: 0; border-top: 1px solid #e1e4e8; margin: 24px 0; }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 16px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px 12px;
            text-align: left;
        }}
        th {{ background: #f5f5f5; }}
        .back-link {{
            display: inline-block;
            margin-top: 30px;
            padding: 8px 16px;
            background: #0366d6;
            color: #fff !important;
            text-decoration: none;
            border-radius: 4px;
        }}
        .back-link:hover {{ background: #0256b9; }}
        .mt-5 {{ margin-top: 32px; }}
        .my-5 {{ margin-top: 32px; margin-bottom: 32px; }}
        .d-flex {{ display: flex; }}
        .align-items-center {{ align-items: center; }}
        .me-2 {{ margin-right: 8px; }}
        .text-dark {{ color: #333; }}
        .text-center {{ text-align: center; }}
        .fs-4 {{ font-size: 1.25rem; }}
    </style>
</head>
<body>
    <div class="version">{version}</div>
    <div class="breadcrumb">
        <a href="index.html">ScottPlot 5 Cookbook</a>
        {f" &raquo; {breadcrumb_html}" if breadcrumb_html else ""}
    </div>
    {html_body}
    <a href="index.html" class="back-link">&larr; Back to Cookbook</a>
</body>
</html>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    cookbook_dir = sys.argv[1] if len(sys.argv) > 1 else None
    if cookbook_dir:
        cookbook_dir = os.path.abspath(cookbook_dir)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        cookbook_dir = os.path.join(script_dir, "..", "..", "dev", "www", "cookbook", "5")
        cookbook_dir = os.path.abspath(cookbook_dir)

    if not os.path.isdir(cookbook_dir):
        print(f"Error: directory not found: {cookbook_dir}")
        sys.exit(1)

    md_files = [f for f in os.listdir(cookbook_dir) if f.endswith(".md")]
    print(f"Found {len(md_files)} .md files in {cookbook_dir}\n")

    failed = 0
    for i, filename in enumerate(sorted(md_files)):
        input_path = os.path.join(cookbook_dir, filename)
        if filename == "index_.md":
            output_filename = "index.html"
        else:
            output_filename = filename.replace(".md", ".html")
        output_path = os.path.join(cookbook_dir, output_filename)

        try:
            convert_md_to_html(input_path, output_path)
            print(f"  [{i+1:3d}/{len(md_files)}] OK  {filename} -> {output_filename}")
        except Exception as e:
            print(f"  [{i+1:3d}/{len(md_files)}] FAIL  {filename}: {e}")
            failed += 1

    print(f"\nDone! {len(md_files) - failed} succeeded, {failed} failed.")
    print(f"Open: {os.path.join(cookbook_dir, 'index.html')}")


if __name__ == "__main__":
    main()