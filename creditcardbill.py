import pandas as pd

csv_data = pd.read_csv('birth_weight.csv')  # 读取训练数据
print(csv_data.shape)  # (189, 9)
N = 5
csv_batch_data = csv_data.tail(N)  # 取后5条数据
print(csv_batch_data.shape)  # (5, 9)
train_batch_data = csv_batch_data[list(range(3, 6))]  # 取这20条数据的3到5列值(索引从0开始)
print(train_batch_data)