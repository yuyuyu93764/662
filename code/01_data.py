#src/01_data_merge.py
import pandas as pd
import os

# 读取两份长表
df_ch4 = pd.read_csv("data/raw/edgar_ch4_multi.csv")
df_gdp_pop = pd.read_csv("data/raw/ceic_gdp_pop_multi.csv")

# 按 country + year 合并（完全匹配你的列名）
df_merged = pd.merge(df_ch4, df_gdp_pop, on=["country", "year"], how="inner")

# 数据清洗：去除空值、异常值
df_merged = df_merged.dropna(subset=["ch4", "gdp", "pop"])
df_merged = df_merged[(df_merged["gdp"] > 0) & (df_merged["pop"] > 0) & (df_merged["ch4"] > 0)]

# 计算衍生指标（用于相关性分析）
df_merged["ch4_intensity"] = df_merged["ch4"] / df_merged["gdp"]  # 排放强度
df_merged["gdp_per_capita"] = df_merged["gdp"] / df_merged["pop"]  # 人均GDP

# 保存干净数据
os.makedirs("data/processed", exist_ok=True)
df_merged.to_csv("data/processed/methane_clean.csv", index=False, encoding="utf-8-sig")

print("✅ 数据合并完成！")
print(f"📊 合并后数据量：{len(df_merged)} 行")
print(f"🌍 覆盖国家：{df_merged['country'].unique()}")
print(f"📅 年份范围：{df_merged['year'].min()} - {df_merged['year'].max()}")
print(df_merged.head())