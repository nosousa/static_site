import os
import shutil

def recursive_copy(src_path, dst_path) :    
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)

    for name in os.listdir(src_path):
        new_src_path = os.path.join(src_path, name)
        new_dst_path = os.path.join(dst_path, name)
        if os.path.isdir(new_src_path):
            recursive_copy(new_src_path, new_dst_path)
        else:
            shutil.copy(new_src_path, dst_path)
