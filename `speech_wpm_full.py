Python

import pandas as pd

# 加载两个文件
df1 = pd.read_csv("/content/drive/MyDrive/speech_wpm_clean344/speech_wpm_analysis.csv")
df2 = pd.read_csv("/content/drive/MyDrive/speech_wpm_clean344/speech_wpm_analysis_batch2.csv")

# 合并
merged_df = pd.concat([df1, df2], ignore_index=True)

# 去重（防止文件重复）
merged_df = merged_df.drop_duplicates(subset="file_name")

# 保存新文件
merged_df.to_csv("/content/drive/MyDrive/speech_wpm_clean344/speech_wpm_analysis_full.csv", index=False)
print("✅ 所有语速数据已合并并保存完毕。")