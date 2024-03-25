import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#解决乱码
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

#导入数据
all_data = pd.read_csv('shunde_new.csv',encoding = 'utf-8',header = 0)

#删除编码语句
data = all_data.drop([5992])

#各区域房源单价均值
sp_mean = data.groupby(by = '所在地址')['单价'].mean().sort_values(ascending = False).to_frame().reset_index()
f,[ax1,ax2] = plt.subplots(2,1,figsize = (20,15))
sns.barplot(x = "所在地址",y = "单价",palette='Spectral_r',data = sp_mean,ax = ax1)
ax1.set_title("顺德区各区域房源单价对比")
ax1.set_xlabel('区域')
ax1.set_ylabel('单价均值')

#各区域房源单价分布
sns.boxplot(x = "所在地址",y = "单价",palette='Spectral_r',data = data,ax = ax2)
ax2.set_title("顺德区各区域房源单价分布")
ax2.set_xlabel('区域')
ax2.set_ylabel('单价')
plt.xticks(fontsize = 10)

#图片保存
plt.savefig('sp.png')