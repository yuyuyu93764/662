# src/02_ch4_trend.py
import matplotlib.pyplot as plt
import pandas as pd

# 读取干净数据
df = pd.read_csv("data/processed/methane_clean.csv")

# 解决中文乱码（如果用中文国家名，保留；用英文可删除）
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 绘图
plt.figure(figsize=(12, 6))
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
countries = df["country"].unique()

for idx, country in enumerate(countries):
    data = df[df["country"] == country]
    plt.plot(data["year"], data["ch4"], marker="o", linewidth=2.5, 
             color=colors[idx], label=country)

# 图表美化
plt.title("2005-2024年中国、阿鲁巴、澳大利亚甲烷排放对比", fontsize=16, pad=20)
plt.xlabel("年份", fontsize=14)
plt.ylabel("甲烷排放量 (kt)", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=12)
plt.xticks(range(2005, 2025, 2), rotation=45)
plt.tight_layout()

# 保存高清图
plt.savefig("甲烷排放历史对比.png", dpi=300, bbox_inches="tight")
plt.show()
print("✅ 图1：历史排放对比图生成完成！")