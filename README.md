# PhD-SpeechWPM-Analysis
Doctoral research code: Speech Rate (WPM) analysis with Whisper
# PhD-SpeechWPM-Analysis

This repository contains the code used in my doctoral research to analyze **speech rate (WPM)** using OpenAI's Whisper.

## 📂 Project Structure

- `2_whisper_wpm_analysis_batch1.py`: Script to batch transcribe and compute WPM for the first 179 audio clips
- `speech_wpm_analysis.csv`: Output file containing filename, duration, transcription, and WPM

## 🛠 Requirements

- Python 3.8+
- openai-whisper
- pandas
- tqdm

## 🚀 How to Use

```bash
!pip install -q openai-whisper
python 2_whisper_wpm_analysis_batch1.py
