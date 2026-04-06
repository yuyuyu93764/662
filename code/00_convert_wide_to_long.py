import matplotlib
matplotlib.use('Agg')
import pandas as pd
import os

# ===================== 1. 检查文件是否存在 =====================
file_path = "data/raw/edgar_ch4_wide.csv"
if not os.path.exists(file_path):
    print(f"❌ 错误：文件不存在！请检查路径：{file_path}")
    print("✅ 请确认：data/raw/ 文件夹里有 edgar_ch4_wide.csv")
    exit()

# ===================== 2. 读取数据（加详细报错） =====================
try:
    df_wide = pd.read_csv(file_path, encoding='utf-8-sig')
    print(f"✅ 成功读取文件，数据行数：{len(df_wide)}")
    print(f"✅ 文件列名：{list(df_wide.columns)}")
except Exception as e:
    print(f"❌ 读取文件失败：{e}")
    print("✅ 尝试用GBK编码读取...")
    try:
        df_wide = pd.read_csv(file_path, encoding='gbk')
        print(f"✅ 成功用GBK读取，数据行数：{len(df_wide)}")
    except Exception as e2:
        print(f"❌ 读取失败：{e2}")
        print("✅ 请检查文件格式、编码是否正确")
        exit()

# ===================== 3. 检查年份列 =====================
year_cols = [col for col in df_wide.columns if col.startswith('Y_')]
if len(year_cols) == 0:
    print("❌ 错误：没有找到以Y_开头的年份列！")
    print(f"✅ 当前列名：{list(df_wide.columns)}")
    print("✅ 请确认年份列名是 Y_2005、Y_2006... 格式")
    exit()
print(f"✅ 找到年份列：{year_cols[:5]}...（共{len(year_cols)}列）")

# ===================== 4. 宽表转长表 =====================
df_long = df_wide.melt(
    id_vars=['Name'],
    value_vars=year_cols,
    var_name='year',
    value_name='ch4'
)

# ===================== 5. 清洗年份 =====================
df_long['year'] = df_long['year'].str.replace('Y_', '').astype(int)
df_long = df_long.rename(columns={'Name': 'country'})

# ===================== 6. 校验数据 =====================
print(f"\n✅ 转换完成！")
print(f"✅ 年份范围：{df_long['year'].min()} - {df_long['year'].max()}")
print(f"✅ 覆盖国家：{df_long['country'].unique()}")
print(f"✅ 总数据量：{len(df_long)} 行")
print("\n✅ 数据预览：")
print(df_long[['country', 'year', 'ch4']].head(10))

# ===================== 7. 保存文件 =====================
output_path = "data/raw/edgar_ch4_multi.csv"
df_long.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"\n✅ 已保存到：{output_path}")
print("✅ 可以直接用后续的分析代码了！")