import sys
import os


# 生成资源文件目录访问路径
def config_path(relative_path):
    if getattr(sys, "frozen", False):  # 是否Bundle Resource
        base_path = getattr(sys, "_MEIPASS")
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)