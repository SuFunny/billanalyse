import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

myfont = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

#filepath = input("Enter your inputfile: ");
i = 1
df = pd.DataFrame()
while i < 13:
    if i < 10:
        filename='statement_20190'+ str(i)+'10.csv'
        if os.path.exists(filename):
            print("the file"+filename+"is exist")
            csv_data = pd.read_csv(filename, header=None, index_col=False, keep_default_na=False)  # 读取训练数据
            newdf = pd.DataFrame({'Accountcycle': str.strip(str(csv_data[6:7][5].values[0]))[13:15],
                              'Newbalance_cny': float(str.strip(str(csv_data[12:13][1].values[0]))),
                              'Newbalance_usd': float(str.strip(str(csv_data[13:14][1].values[0])))
                              },
                             index=[1])
            df = df.append(newdf, ignore_index=True)
        else:
            print("the file"+filename+"is not exist")
    if i >= 10:
        filename = 'statement_2019' + str(i) + '10.csv'
        if os.path.exists(filename):
            print("the file" + filename + "is exist")
            csv_data = pd.read_csv(filename, header=None, index_col=False, keep_default_na=False)  # 读取训练数据
            newdf = pd.DataFrame({'Accountcycle': str.strip(str(csv_data[6:7][5].values[0]))[13:15],
                              'Newbalance_cny': float(str.strip(str(csv_data[12:13][1].values[0]))),
                              'Newbalance_usd': float(str.strip(str(csv_data[13:14][1].values[0])))
                              },
                             index=[1])
            df = df.append(newdf, ignore_index=True)
        else:
            print("the file" + filename + "is not exist")
    i=i+1
print(df)
temp_cursort=df.sort_values(by="Newbalance_cny",ascending=[False])
print(temp_cursort)
print("本年共消费:"+str(df.Newbalance_cny.sum(axis=0))+"元")
print("平均每月消费"+str(df.Newbalance_cny.sum()/12)+"元")
print("本年消费最多的月份为"+temp_cursort[0:1]['Accountcycle'].values[0])
print("消费金额为:"+str(df.Newbalance_cny.max())+"元")
print("本年消费最少的月份为"+temp_cursort[11:12]['Accountcycle'].values[0])
print("消费金额为:"+str(df.Newbalance_cny.min())+"元")

# #plot根据列表绘制出有意义的图形，linewidth是图形线宽，可省略
plt.plot(df['Accountcycle'],df['Newbalance_cny'],linewidth=3,color='red')
# #设置图标标题
plt.title("年度消费表",fontsize = 24, fontproperties=myfont)
# #设置坐标轴标签
plt.xlabel("月份",fontsize = 14,fontproperties=myfont)
plt.ylabel("金额",fontsize = 14,fontproperties=myfont)
# #设置刻度标记的大小
plt.tick_params(axis='both',labelsize = 10,rotation = 45)
# #打开matplotlib查看器，并显示绘制图形
for a, b in zip(df['Accountcycle'],df['Newbalance_cny']):
    plt.text(a,b, float('%.2f' %b), ha='center', va='top', fontsize=8)

plt.show()