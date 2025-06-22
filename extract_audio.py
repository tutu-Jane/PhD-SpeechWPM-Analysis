import os
import subprocess

# 视频所在文件夹路径（注意：Windows路径需用双反斜杠 \\ 或 r'原路径'）
video_dir = r'C:\Users\lenovo\Desktop\phd\language characteristic\数据\2025623'

# 输出文件夹（默认保存到同一目录下的“音频”文件夹）
output_dir = os.path.join(video_dir, 'audio')
os.makedirs(output_dir, exist_ok=True)

# 遍历文件夹下所有视频
for file in os.listdir(video_dir):
    if file.lower().endswith(('.mp4', '.flv', '.mov', '.mkv')):
        input_path = os.path.join(video_dir, file)
        output_filename = os.path.splitext(file)[0] + '.wav'
        output_path = os.path.join(output_dir, output_filename)

        # 调用 ffmpeg 提取音频为 wav 格式（单声道，16kHz，保留全长）
        command = [
            'ffmpeg', '-i', input_path,
            '-ac', '1', '-ar', '16000',
            '-vn',  # 不要视频流
            output_path
        ]

        print(f"🎧 正在提取音频：{file}")
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("✅ 所有视频音频提取完成！输出路径：", output_dir)
