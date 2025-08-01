import os

# 自動改檔名工具 - Day 2 起點

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            new_name = "new_" + filename
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
建立 rename_tool/rename.py 初版
