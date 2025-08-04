import os

def rename_files(folder_path, prefix, suffix, extension_filter):
    count = 0
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if not os.path.isfile(full_path):
            continue  # 跳過資料夾或非檔案

        name, ext = os.path.splitext(filename)

        if extension_filter and ext.lower() != extension_filter.lower():
            continue

        new_name = prefix + name + suffix + ext
        new_full_path = os.path.join(folder_path, new_name)

        os.rename(full_path, new_full_path)
        print(f"✅ {filename} → {new_name}")
        count += 1

    print(f"\n總共改了 {count} 個檔案")

if __name__ == "__main__":
    path = input("請輸入資料夾路徑：")
    prefix = input("想加在前面的字（可留空）：")
    suffix = input("想加在後面的字（可留空）：")
    extension_filter = input("只修改哪種副檔名（例如 .txt，留空代表全部）：")

    rename_files(path, prefix, suffix, extension_filter)
v2
