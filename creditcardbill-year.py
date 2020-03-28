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
df_detail=pd.DataFrame()
while i < 13:
    if i < 10:
        filename='statement_20190'+ str(i)+'10.csv'
        if os.path.exists(filename):
            #print("the file"+filename+"is exist")
            csv_data = pd.read_csv(filename, header=None, index_col=False, keep_default_na=False)  # 读取训练数据
            newdf = pd.DataFrame({'Accountcycle': str.strip(str(csv_data[6:7][5].values[0]))[13:15],
                              'Newbalance_cny': float(str.strip(str(csv_data[12:13][1].values[0]))),
                              'Newbalance_usd': float(str.strip(str(csv_data[13:14][1].values[0])))
                              },
                             index=[1])
            df = df.append(newdf, ignore_index=True)
            j = 31
            csvlength = csv_data.shape[0]
            while j < csvlength - 2:
                if float(str.strip(str(csv_data[j:j + 1][4].values[0]))[4:]) > 0:
                    newdf_detail = pd.DataFrame({'AcctDate': str.strip(str(csv_data[j:j + 1][0].values[0])),
                                                 'AcctMonth': str.strip(str(csv_data[j:j + 1][0].values[0]))[0:6],
                                          'CardNumber': str.strip(str(csv_data[j:j + 1][2].values[0])),
                                          'Currency': float((str.strip(str(csv_data[j:j + 1][4].values[0])))[4:]),
                                          'AcctDesc': str.strip(str(csv_data[j:j + 1][5].values[0]))
                                          },
                                         index=[1])
                    df_detail = df_detail.append(newdf_detail, ignore_index=True)
                j=j + 1
        # else:
        #     print("the file"+filename+"is not exist")
    if i >= 10:
        filename = 'statement_2019' + str(i) + '10.csv'
        if os.path.exists(filename):
            #print("the file" + filename + "is exist")
            csv_data = pd.read_csv(filename, header=None, index_col=False, keep_default_na=False)  # 读取训练数据
            newdf = pd.DataFrame({'Accountcycle': str.strip(str(csv_data[6:7][5].values[0]))[13:15],
                              'Newbalance_cny': float(str.strip(str(csv_data[12:13][1].values[0]))),
                              'Newbalance_usd': float(str.strip(str(csv_data[13:14][1].values[0])))
                              },
                             index=[1])
            df = df.append(newdf, ignore_index=True)

            j = 31
            csvlength = csv_data.shape[0]
            while j < csvlength - 2:
                if float(str.strip(str(csv_data[j:j + 1][4].values[0]))[4:]) > 0:
                    newdf_detail = pd.DataFrame({'AcctDate': str.strip(str(csv_data[j:j + 1][0].values[0])),
                                                 'AcctMonth': str.strip(str(csv_data[j:j + 1][0].values[0]))[0:6],
                                                 'CardNumber': str.strip(str(csv_data[j:j + 1][2].values[0])),
                                                 'Currency': float(
                                                     (str.strip(str(csv_data[j:j + 1][4].values[0])))[4:]),
                                                 'AcctDesc': str.strip(str(csv_data[j:j + 1][5].values[0]))
                                                 },
                                                index=[1])
                    df_detail = df_detail.append(newdf_detail, ignore_index=True)
                j = j + 1
        # else:
        #     print("the file" + filename + "is not exist")
    i=i+1
# print(df)
# print(df_detail)
temp_cursort=df.sort_values(by="Newbalance_cny",ascending=[False])
#print(temp_cursort)
print("本年共消费:"+str(df.Newbalance_cny.sum(axis=0))+"元")
print("平均每月消费"+str(df.Newbalance_cny.sum()/12)+"元")
print("本年消费最多的月份为"+temp_cursort[0:1]['Accountcycle'].values[0])
print("消费金额为:"+str(df.Newbalance_cny.max())+"元")
print("本年消费最少的月份为"+temp_cursort[11:12]['Accountcycle'].values[0])
print("消费金额为:"+str(df.Newbalance_cny.min())+"元")

temp_detailcursort=df_detail.sort_values(by="Currency",ascending=[False])
print("本年度共消费:"+str(df_detail.AcctDate.count())+"笔,共消费:"+str(df_detail.Currency.sum(axis=0))+"元")
print("本年度最大单笔消费发生在:"+temp_detailcursort[0:1]['AcctDate'].values[0])
print("商家:"+temp_detailcursort[0:1]['AcctDesc'].values[0])
print("消费金额为:"+str(df_detail.Currency.max())+"元")

df_detail['new']=1
dfshop_detail = df_detail.groupby('AcctDesc')['new','Currency'].sum().reset_index().sort_values(by ='new',ascending=False)
shopname=str(dfshop_detail[0:1]['AcctDesc'].values[0])
shopnum=str(dfshop_detail[0:1]['new'].values[0])
shopmoney=str(dfshop_detail[0:1]['Currency'].values[0])
print("本年度最常去的商家:"+shopname+",共消费了"+shopnum+"次"+shopmoney+"元")

dfmonth_detail = df_detail.groupby('AcctMonth')['new','Currency'].sum().reset_index().sort_values(by ='new',ascending=False)
monthname=str(dfmonth_detail[0:1]['AcctMonth'].values[0])
monthnum=str(dfmonth_detail[0:1]['new'].values[0])
monthmoney=str(dfmonth_detail[0:1]['Currency'].values[0])
print("本年度消费次数最多的月份:"+monthname+",共消费了"+monthnum+"次"+monthmoney+"元")
print("平均每月消费"+str(float(dfmonth_detail.new.sum())/12)+"次,"+str(dfmonth_detail.Currency.sum()/12)+"元")
#
# # #plot根据列表绘制出有意义的图形，linewidth是图形线宽，可省略
# plt.plot(df['Accountcycle'],df['Newbalance_cny'],linewidth=3,color='red')
# # #设置图标标题
# plt.title("年度消费表",fontsize = 24, fontproperties=myfont)
# # #设置坐标轴标签
# plt.xlabel("月份",fontsize = 14,fontproperties=myfont)
# plt.ylabel("金额",fontsize = 14,fontproperties=myfont)
# # #设置刻度标记的大小
# plt.tick_params(axis='both',labelsize = 10,rotation = 45)
# # #打开matplotlib查看器，并显示绘制图形
# for a, b in zip(df['Accountcycle'],df['Newbalance_cny']):
#     plt.text(a,b, float('%.2f' %b), ha='center', va='top', fontsize=8)
#
# plt.show()