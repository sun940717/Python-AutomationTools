import os

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            new_name = "new_" + filename
            os.rename(
                os.path.join(folder_path, filename),
                os.path.join(folder_path, new_name)
            )

if __name__ == "__main__":
    path = input("請輸入資料夾路徑：")
    rename_files(path)
