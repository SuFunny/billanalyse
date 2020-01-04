import pandas as pd

csv_data = pd.read_csv('statement_20190110.csv', header=None, index_col=False, names=['a', 'b', 'c', 'd', 'e', 'f'])  # 读取训练数据
print(csv_data)  # (51, 6)