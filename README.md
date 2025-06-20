
# 📊 PhD Speech WPM Analysis

This repository contains the Whisper-based speech rate analysis pipeline for PhD research on linguistic features in AI-scripted livestream micro-courses.

---

## ✅ Batch 1: Whisper WPM Analysis (179 Files)

- 📅 Run Date: June 20, 2025  
- 📂 Input Directory: `/content/drive/MyDrive/speech_wpm_clean344/speech-WPM`  
- 🟢 Files Processed: 179  
- 🧠 Model: `whisper base`  
- 🔄 Output: `speech_wpm_analysis.csv`  
- 📈 Output Fields:  
  - `filename`  
  - `duration` (seconds)  
  - `text` (transcript)  
  - `words` (word count)  
  - `wpm` (words per minute)  
- 💬 Notes:  
  - Stable run with no errors.  
  - Incremental processing handled in a second script.

---

## ✅ Batch 2: Whisper WPM Analysis (165 Files)

- 📅 Run Date: June 20, 2025  
- 📂 Input Directory: `/content/drive/MyDrive/speech_wpm_clean344/speech-WPM`  
- 🟠 Files Processed: 165 (manually filtered)  
- 🧠 Model: `whisper base`  
- 🔄 Output: `speech_wpm_analysis_batch2.csv`  
- 📈 Output Fields: same as Batch 1  
- 💬 Notes:  
  - Excluded already processed files  
  - Processed on Google Colab Pro with A100  
  - Ready to merge with Batch 1 for full dataset

---

## 📌 Next Step

- Merge batch outputs → `speech_wpm_full.csv`  
- Proceed to WPM-based analysis → explore relations with engagement & sales
