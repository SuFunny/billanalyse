import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

myfont = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

#filepath = input("Enter your inputfile: ");
csv_data = pd.read_csv('statement_20190110.csv', header=None, index_col=False, keep_default_na=False)  # 读取训练数据

bankname = str.strip(str(csv_data[0:1][2].values[0]))
print("银行名称:" + bankname)

billname = str.strip(str(csv_data[1:2][2].values[0]))
print("账单类型:" + billname)

custname = str.strip(str(csv_data[2:3][1].values[0]))
print("姓名:" + custname)

custaddress = str.strip(str(csv_data[3:4][1].values[0]))
print("地址:" + custaddress)

accountcycle = str.strip(str(csv_data[6:7][5].values[0]))
print("账单周期:" + accountcycle)

newbalance_cny = str.strip(str(csv_data[12:13][1].values[0]))
print("账单金额(人民币):" + newbalance_cny)

newbalance_usd = str.strip(str(csv_data[13:14][1].values[0]))
print("账单金额(美元):" + newbalance_usd)

# file_handle = open("result.csv", mode='w')
csvlength = csv_data.shape[0]
#csvwidth = csv_data.shape[1]

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

df['new']=1
df2 = df.groupby('AcctDesc')['new','Currency'].sum().reset_index().sort_values(by ='new',ascending=False)
shopname=str(df2[0:1]['AcctDesc'].values[0])
shopnum=str(df2[0:1]['new'].values[0])
shopmoney=str(df2[0:1]['Currency'].values[0])
print("本月最常去的商家:"+shopname+",共消费了"+shopnum+"次"+shopmoney+"元")

#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
patches, texts, autotexts=ax1.pie(df2['new'],  labels=df2['AcctDesc'], autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
myfont.set_size('xx-small')
# font size include: ‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xx-large’ or number, e.g. '12'
plt.setp(autotexts, fontproperties=myfont)
plt.setp(texts, fontproperties=myfont)
# 添加图标题
plt.title('商家消费次数分布',fontproperties=myfont)
plt.savefig('商家消费次数分布.png')
# 显示图形
plt.show()

fig2, ax2 = plt.subplots()
patches, texts, autotexts=ax2.pie(df2['Currency'],  labels=df2['AcctDesc'], autopct='%1.1f%%',
        shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# font size include: ‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xx-large’ or number, e.g. '12'
plt.setp(autotexts, fontproperties=myfont)
plt.setp(texts, fontproperties=myfont)
# 添加图标题
plt.title('商家消费金额分布',fontproperties=myfont)
plt.savefig('商家消费金额分布.png')
# 显示图形
plt.show()


df3 = df.groupby('AcctDate')['Currency'].sum().reset_index()
print(df3)
# #plot根据列表绘制出有意义的图形，linewidth是图形线宽，可省略
plt.plot(df3['AcctDate'],df3['Currency'],linewidth=3,color='red')
# #设置图标标题
plt.title("消费时间表",fontsize = 24, fontproperties=myfont)
# #设置坐标轴标签
plt.xlabel("日期",fontsize = 14,fontproperties=myfont)
plt.ylabel("金额",fontsize = 14,fontproperties=myfont)
# #设置刻度标记的大小
plt.tick_params(axis='both',labelsize = 10,rotation = 45)
# #打开matplotlib查看器，并显示绘制图形
# plt.show()

# 设置数字标签
for a, b in zip(df3['AcctDate'],df3['Currency']):
    plt.text(a,b, float('%.2f' %b), ha='center', va='top', fontsize=8)

plt.show()