import os
import shutil

def copy_static():    
    if os.path.exists("public"):
        shutil.rmtree("public")
    
    os.mkdir("public")

    src = "static"
    dst = "public"

    def recursive_copy(src_path, dst_path):
        for name in os.listdir(src_path):
            new_src_path = os.path.join(src_path, name)
            if os.path.isdir(new_src_path):
                new_dst_path = os.path.join(dst_path, name)
                os.mkdir(new_dst_path)
                recursive_copy(new_src_path, new_dst_path)
            else:
                shutil.copy(new_src_path, dst_path)
    
    recursive_copy(src, dst)