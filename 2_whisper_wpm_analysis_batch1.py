Python

# -------------------------------------------------------------
# File       : 2_whisper_wpm_analysis_batch1.py
# Author     : Jane Gao
# Date       : 2025-06-20
# Project    : PhD Dissertation - Language Characteristics in Livestream OKP
# Description: 使用 Whisper 模型提取语速（WPM），处理首批 179 个音频样本
#
# Input      : /content/drive/MyDrive/speech_wpm_clean344/speech-WPM/
# Output     : /content/drive/MyDrive/speech_wpm_clean344/speech_wpm_analysis.csv
# Output Fields: file_name, transcript, duration_seconds, word_count, WPM
#
# Notes:
# - 模型版本：openai-whisper base
# - 平台环境：Google Colab Pro（A100 GPU）
# - 运行时间：约 30 分钟
# - 此文件将作为博士论文附录材料保存
# -------------------------------------------------------------




import os
import pandas as pd
import whisper
from tqdm import tqdm

# 设定路径
audio_dir = "/content/drive/MyDrive/speech_wpm_clean344/speech-WPM"
output_csv_path = "/content/drive/MyDrive/speech_wpm_clean344/speech_wpm_analysis.csv"

# 加载模型
model = whisper.load_model("base")

# 获取音频文件列表
wav_files = [f for f in os.listdir(audio_dir) if f.lower().endswith(".wav")]
results = []

# 循环处理
for filename in tqdm(wav_files, desc="Processing Audio"):
    file_path = os.path.join(audio_dir, filename)
    try:
        audio = whisper.load_audio(file_path)
        duration = round(len(audio) / whisper.audio.SAMPLE_RATE, 2)
        result = model.transcribe(file_path, verbose=False)
        transcript = result["text"].strip()
        word_count = len(transcript.split())
        wpm = round(word_count / (duration / 60), 2) if duration > 0 else 0

        results.append({
            "file_name": filename,
            "transcript": transcript,
            "duration_seconds": duration,
            "word_count": word_count,
            "WPM": wpm
        })

    except Exception as e:
        print(f"❌ Failed to process {filename}: {e}")

# 输出到 CSV
df = pd.DataFrame(results)
df.to_csv(output_csv_path, index=False)
