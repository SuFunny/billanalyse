import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

myfont = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

#filepath = input("Enter your inputfile: ");
csv_data = pd.read_csv('statement_20200210.csv', header=None, index_col=False, keep_default_na=False)  # 读取训练数据

csvlength = csv_data.shape[0]
df = pd.DataFrame()
i = 31
while i < csvlength - 2:
    if float(str.strip(str(csv_data[i:i + 1][4].values[0]))[4:]) > 0:
        newdf = pd.DataFrame({'AcctDate': str.strip(str(csv_data[i:i + 1][0].values[0])),
                              'CardNumber': str.strip(str(csv_data[i:i + 1][2].values[0])),
                              'Currency': float((str.strip(str(csv_data[i:i + 1][4].values[0])))[4:]),
                              'AcctDesc': str.strip(str(csv_data[i:i + 1][5].values[0]))
                              },
                             index=[1])
        df = df.append(newdf, ignore_index=True)
    i = i + 1
temp_cursort=df.sort_values(by="Currency",ascending=[False])
print("本月共消费:"+str(df.AcctDate.count())+"笔,本月共消费:"+str(df.Currency.sum(axis=0))+"元")
print("本月最大单笔消费发生在:"+temp_cursort[0:1]['AcctDate'].values[0])
print("商家:"+temp_cursort[0:1]['AcctDesc'].values[0])
print("消费金额为:"+str(df.Currency.max())+"元")