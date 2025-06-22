import os
import shutil

# 设置根目录路径（包含各日期文件夹）
root_dir = r"C:\Users\lenovo\Desktop\phd\language characteristic\数据"

# 设置目标文件夹路径
output_dir = os.path.join(root_dir, "音频统一")

# 创建目标文件夹（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# 遍历所有子文件夹
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.lower().endswith(('.wav', '.mp3', '.m4a')):
            src_file = os.path.join(subdir, file)
            dst_file = os.path.join(output_dir, file)

            # 如果同名文件已存在，则重命名
            if os.path.exists(dst_file):
                base, ext = os.path.splitext(file)
                i = 1
                while os.path.exists(os.path.join(output_dir, f"{base}_{i}{ext}")):
                    i += 1
                dst_file = os.path.join(output_dir, f"{base}_{i}{ext}")

            shutil.copy2(src_file, dst_file)

print("✅ 所有音频文件已成功集中到：", output_dir)
