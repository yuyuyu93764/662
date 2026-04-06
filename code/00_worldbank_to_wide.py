import matplotlib
matplotlib.use('Agg')
import pandas as pd
import os

# ===================== 1. 配置文件路径 =====================
# 输入：你的GDP宽表文件（左图格式，表头：Country Code, Country Name, Y_2005...）
gdp_input_path = "data/raw/ceic_gdp_wide.csv"
# 输入：你的人口宽表文件（表头和GDP一致）
pop_input_path = "data/raw/ceic_pop_wide.csv"
# 输出：合并后的长表文件（你给的目标格式：city,year,gdp,pop）
output_path = "data/raw/ceic_gdp_pop_multi.csv"

# ===================== 2. 检查输入文件 =====================
for path in [gdp_input_path, pop_input_path]:
    if not os.path.exists(path):
        print(f"❌ 输入文件不存在：{path}")
        exit()
print("✅ 两个输入文件都正常！")

# ===================== 3. 读取并转换GDP宽表 =====================
df_gdp_wide = pd.read_csv(gdp_input_path, encoding='utf-8-sig', on_bad_lines='skip')
# 提取Y_开头的年份列
year_cols = [col for col in df_gdp_wide.columns if col.startswith('Y_')]
# 宽转长
df_gdp_long = df_gdp_wide.melt(
    id_vars=['Country Name'],
    value_vars=year_cols,
    var_name='year',
    value_name='gdp'
)
# 清洗年份：去掉Y_，转整数
df_gdp_long['year'] = df_gdp_long['year'].str.replace('Y_', '').astype(int)
# 重命名国家列，匹配目标格式的"country"
df_gdp_long = df_gdp_long.rename(columns={'Country Name': 'country'})

# ===================== 4. 读取并转换人口宽表 =====================
df_pop_wide = pd.read_csv(pop_input_path, encoding='utf-8-sig', on_bad_lines='skip')
df_pop_long = df_pop_wide.melt(
    id_vars=['Country Name'],
    value_vars=year_cols,
    var_name='year',
    value_name='pop'
)
df_pop_long['year'] = df_pop_long['year'].str.replace('Y_', '').astype(int)
df_pop_long = df_pop_long.rename(columns={'Country Name': 'country'})

# ===================== 5. 合并GDP和人口数据 =====================
df_merged = pd.merge(df_gdp_long, df_pop_long, on=['country', 'year'], how='inner')


# ===================== 7. 按目标格式排序列 =====================
df_merged = df_merged[['country', 'year', 'gdp', 'pop']]

# ===================== 8. 保存为目标格式CSV =====================
df_merged.to_csv(output_path, index=False, encoding='utf-8-sig')

# ===================== 9. 结果预览（和你给的格式完全一致） =====================
print("\n✅ 转换完成！长表预览（和目标格式完全一致）：")
print(df_merged.head(10))
print(f"\n✅ 长表已保存到：{output_path}")
print(f"✅ 总数据量：{len(df_merged)} 行")
print(f"✅ 覆盖国家：{df_merged['country'].unique()}")
print(f"✅ 年份范围：{df_merged['year'].min()} - {df_merged['year'].max()}")

