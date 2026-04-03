# 🌍 三国甲烷排放时空分析与未来30年预测
**Methane Emission Analysis & Prediction for China, Australia, Aruba**

---

## 📋 项目简介
本项目基于 EDGAR 全球大气排放数据库与世界银行（World Bank）公开数据，完成中国、澳大利亚、阿鲁巴三国 2005–2024 年甲烷排放的全流程分析与复现，结合 ARIMA 时间序列模型实现未来 30 年（2025–2054）高精度预测，同时挖掘甲烷排放与 GDP、人口的内在关联，生成多类学术级可视化图表。

项目核心价值：从数据预处理到成果可视化，形成完整的环境数据分析闭环，代码可复用、结果可复现，兼顾专业性与实用性。

---
## 数据来源
1. EDGAR v8.0 甲烷数据:https://edgar.jrc.ec.europa.eu/dataset_ghg80
2. 世界银行官网：https://data.worldbank.org/


## 🎯 核心研究内容
1.  数据标准化处理：将原始宽表数据转换为长表格式，完成甲烷排放、GDP、人口多源数据的融合与清洗，剔除异常值与缺失值。
2.  历史排放趋势分析：可视化三国 2005–2024 年甲烷排放总量变化，对比不同国家的排放规模与趋势差异。
3.  高精度未来预测：基于 ARIMA 时间序列模型，完成未来 30 年甲烷排放预测（含 95% 置信区间），验证模型拟合精度。
4.  驱动因素分析：量化甲烷排放与 GDP、人口的相关关系，揭示经济发展与人口规模对排放的影响机制。
5.  拓展指标分析：计算人均甲烷排放量，从“人均公平”视角补充排放差异分析，完善研究维度。

---


---

## 📊 核心可视化成果
| 图表名称 | 用途 | 保存路径 |
|----------|------|----------|
| 三国甲烷排放历史对比图 | 对比2005–2024年三国排放总量趋势 | output/results/甲烷排放历史对比.png |
| 甲烷排放ARIMA预测图 | 展示2025–2054年排放预测结果（含置信区间） | output/results/甲烷排放ARIMA预测.png |
| 甲烷排放与人口GDP相关性.png | 直观展示排放与GDP、人口的散点关联 | output/results/甲烷排放与人口GDP相关性.png |
| 三国人均甲烷排放对比图 | 从人均视角对比排放差异，体现公平性 | output/results/三国人均甲烷排放对比图.png |
| 相关性热力图 | 量化展示ch4、gdp、pop三者两两相关系数 | output/results/相关性热力图.png |

---

## 🚀 环境配置与运行说明
### 1. 核心依赖包
项目基于 Python 3.10+ 开发，需安装以下依赖（pip 安装即可）：
```bash
pip install pandas numpy matplotlib seaborn statsmodels scipy

## 运行方式
1. 环境准备
本项目基于 Python 3.10+ 开发，推荐使用虚拟环境管理依赖。
（1）创建并激活虚拟环境
# 创建虚拟环境
python -m venv .venv
# Windows 激活
.venv\Scripts\Activate.ps1
# macOS/Linux 激活
source .venv/bin/activate
（2）安装依赖包
pip install -r requirements.txt
# 若没有requirements.txt，可手动安装核心依赖：
pip install pandas numpy matplotlib seaborn statsmodels scipy

2. 数据准备
python src/00_convert_wide_to_long.py
python src/00_worldbank_to_wide.py

# 数据合并与清洗
原始数据存放于 data/raw/ 目录
运行数据预处理脚本，自动完成宽表转长表、数据清洗与合并，生成标准化分析数据：
python src/01_data.py
# 数据格式转换
python src/00_convert_wide_to_long.py
python src/00_worldbank_to_wide.py
# 数据合并与清洗
python src/01_data.py

3. 分步复现
# 1. 历史排放趋势可视化
python src/02_ch4_trend.py
# 2. ARIMA 未来30年排放预测
python src/03_ch4_forecast_arima.py
# 3. 排放与GDP、人口相关性散点图
python src/04_ch4_correlation.py
# 4. 人均甲烷排放对比图
python src/05_per_capita_ch4.py
# 5. 相关性热力图
python src/06_correlation_heatmap.py
