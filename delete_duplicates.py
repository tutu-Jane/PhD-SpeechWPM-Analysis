import os

# 设置你的音频统一文件夹路径
folder_path = r"C:\Users\lenovo\Desktop\phd\language characteristic\数据\音频统一"

# 遍历该文件夹中的所有文件
deleted_count = 0
for file in os.listdir(folder_path):
    if file.lower().endswith('_1.wav'):
        file_path = os.path.join(folder_path, file)
        try:
            os.remove(file_path)
            print(f"🗑️ 已删除: {file}")
            deleted_count += 1
        except Exception as e:
            print(f"⚠️ 删除失败: {file}, 原因: {e}")

print(f"\n✅ 共删除 {deleted_count} 个重复文件。")
