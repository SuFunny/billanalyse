import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

myfont = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

# filepath = input("Enter your inputfile: ");
alipay_data = pd.read_csv('alipay_record_20200328_1745_1.csv', encoding="gbk",
                          header=4, skipfooter=7, engine='python', skipinitialspace=True)  # 读取训练数据
# del alipay_data[16]
csvlength = alipay_data.shape[0]
# csv_data[(csv_data['收/支']=='支出')]
# print(alipay_data.columns)
alipay_data.rename(columns=lambda x: x.strip(), inplace=True)
del alipay_data['Unnamed: 16']
newinout = alipay_data['收/支'].str.strip()
alipay_data['收/支'] = newinout

# the  pay this month
a = alipay_data[(alipay_data['收/支'] == '支出')]
print("本月共支出",a['金额（元）'].sum())
print("本月共支出",a['交易号'].value_counts().count(),"笔")
a = a.groupby('交易对方')
a = a.sum()
a = a.sort_values(['金额（元）'], ascending=False)
print(a.head(1))


# the income this month
b = alipay_data[alipay_data['收/支'] == '收入']
print("本月共收入",b['金额（元）'].sum())
print("本月共收入",b['交易号'].value_counts().count(),"笔")
b = b.groupby('交易对方')
b = b.sum()
b = b.sort_values(['金额（元）'], ascending=False)
print(b.head(1))
