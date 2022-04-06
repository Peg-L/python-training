import statistics as stat  # 可取別名
import statistics
import random
# data1 = random.choice([0, 1, 5, 8]) # 從列表中隨機選取 1 個資料
# data2 = random.sample([0, 1, 5, 8], 2) # 從列表中隨機選取 2 個資料
# print(data1)
# print(data2)

# data = [0, 1, 5, 8]
# random.shuffle(data)  # 將列表的資料「就地」隨機調換順序
# print(data)

# 取得 0.0~1.0之間的隨機亂數
random.random()  # 0 到 1 之間的數出現的機率是相等的
random.uniform(0.0, 1.0)  # 出現的機率相同

# 取的平均數 100, 標準差 10 的 常態分配亂數
a = random.normalvariate(100, 10)

# 計算列表中數字的 平均數
statistics.mean([1, 4, 6, 9])
# 計算列表中數字的 中位數
statistics.median([1, 4, 6, 9])
# 計算列表中數字的 標準差
statistics.stdev([1, 4, 6, 9])

# 隨機模組
# 隨機選取
data = random.choice([1, 5, 6, 10, 20])
print(data)
data2 = random.sample([1, 5, 6, 10, 20], 3)
print(data2)

# 隨機調換順序 (洗牌)
data = [1, 5, 8, 20]
random.shuffle(data)
print(data)

# 隨機取得亂數
data = random.random()  # = random.uniform(0.0, 1.0)  # 0-1隨機算數
print(data)
data = random.uniform(60, 100)  # 60 - 100 之間的隨機亂數
print(data)

# 取得常態分配亂數
# 平均數100, 標準差 10, 得到的資料大部分會落在 90-100之間
data = random.normalvariate(0, 5)  # 得到的資料【多數】在 -5 到 5 之間
print(data)

# 統計模組
data = stat.mean([1, 2, 3, 4, 5, 8, 100])  # 平均數
print(data)

data = stat.median([1, 2, 3, 4, 5, 8, 100])  # 中位數
print(data)

data = stat.stdev([1, 2, 3, 4, 5, 8, 10])  # 標準差
print(data)
