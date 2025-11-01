import os
import sys
import shutil
from copystatic import recursive_copy
from generatepage import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"
dir_path_docs = "./docs"

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    recursive_copy(dir_path_static, dir_path_docs)
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)

main()