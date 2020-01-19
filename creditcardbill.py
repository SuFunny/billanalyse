import math

import pandas as pd
import numpy as np

csv_data = pd.read_csv('statement_20190110.csv', header=None, index_col=False, keep_default_na=False)  # 读取训练数据
# print(csv_data[1:2])
# print(csv_data[1:2]['c'].values[0])# (51, 6)
file_handle = open("result.csv", mode='w')
csvlength = csv_data.shape[0]
csvwidth = csv_data.shape[1]
i = 0
print("start the collect")
while i < csvlength:
    j = 0
    while j < csvwidth:
        if len(str(csv_data[i:i + 1][j].values[0])) != 0:
            if not str(csv_data[i:i + 1][j].values[0]).isspace():
                print(str.strip(str(csv_data[i:i + 1][j].values[0])))
        j = j + 1
    i = i + 1
print("end the collect")
# result2txt = str(csv_data[i:i+1][j].values[0])
# file_handle.write(result2txt)
