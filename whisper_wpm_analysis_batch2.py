Python

# ---------------------------------------------------------
# File: 3_whisper_wpm_analysis_batch2.py
# Author: Jane Gao
# Date: 2025-06-20
# Description: Extract speech rate (WPM) using Whisper for the second batch of 165 audio clips.
# Input: Audio directory at /content/drive/MyDrive/speech_wpm_clean344/speech-WPM
# Output: WPM partial file speech_wpm_analysis_batch2.csv containing filename, duration, transcript, and WPM
# Notes:
# - Using Whisper 'base' model
# - Approx. runtime: 22 minutes on Colab A100 GPU
# - Saved as part of code appendix for doctoral dissertation
# - Complements the first batch (179 samples) for full dataset coverage
# ---------------------------------------------------------

import os
import pandas as pd
import whisper
from tqdm import tqdm

# Define paths
audio_dir = "/content/drive/MyDrive/speech_wpm_clean344/speech-WPM"
output_csv_path = "/content/drive/MyDrive/speech_wpm_clean344/speech_wpm_analysis_batch2.csv"

# Load already processed filenames from batch 1
processed_files_path = "/content/drive/MyDrive/speech_wpm_clean344/speech_wpm_analysis.csv"
processed_df = pd.read_csv(processed_files_path)
processed_filenames = set(processed_df["file_name"].tolist())

# Identify unprocessed audio files
all_filenames = sorted([f for f in os.listdir(audio_dir) if f.endswith(".wav")])
remaining_files = [f for f in all_filenames if f not in processed_filenames]

# Load Whisper model
model = whisper.load_model("base")
results = []

# Transcribe remaining files
for filename in tqdm(remaining_files):
    audio_path = os.path.join(audio_dir, filename)
    try:
        result = model.transcribe(audio_path)
        text = result["text"]
        duration = result["segments"][-1]["end"]
        words = len(text.strip().split())
        wpm = round(words / (duration / 60), 2)


