import os
from md_to_html import markdown_to_html_node
from extracttitle import extract_title
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r') as f:
        markdown = f.read()
    
    with open(template_path, 'r') as f:
        template = f.read()
    
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    html_page = template.replace(r"{{ Title }}", title).replace(r"{{ Content }}", html_string)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    
    with open(dest_path, 'w') as f:
        f.write(html_page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, filename)
        dst_path = os.path.join(dest_dir_path, filename)
        if os.path.isdir(src_path):
            generate_pages_recursive(src_path, template_path, dst_path)
        elif os.path.isfile(src_path) and filename.endswith(".md"):
            generate_page(src_path, template_path, Path(dst_path).with_suffix(".html"))