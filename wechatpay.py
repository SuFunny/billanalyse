import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

myfont = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

#filepath = input("Enter your inputfile: ");
wechat_data =pd.read_csv('微信支付账单(20200201-20200229).csv',header=16,skipinitialspace=True)  # 读取训练数据

print(wechat_data)
print(wechat_data.columns)