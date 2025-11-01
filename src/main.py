import os
import shutil
from copystatic import recursive_copy
from generatepage import generate_page

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    recursive_copy(dir_path_static, dir_path_public)
    generate_page("content/index.md", "template.html", "public/index.html")
    

main()