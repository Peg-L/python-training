# 1. 集合的運算 # in /not in
# s1 = {3, 4, 5}
# print(3 in s1)
# print(10 not in s1)

# s1 = {3, 4, 5}
# s2 = {4, 5, 6, 7}
# s3 = s1 & s2  # 交集:取兩個集合中，相同的資料
# s3 = s1 | s2  # 聯集: 取兩個集合中的所有資料，但不重複
# print(s3)
# s3 = s1 - s2  # 差集: 從s1中，減去和s2重疊的部分
# s3 = s1 ^ s2  # 反交集:取兩個集合中，不重疊的部分
# print(s3)

# s = set("Hello")  # set (字串)
# print("A" in s)

# 字典的運算: key-value 配對
dic = {"apple": "蘋果", "bug": "蟲蟲", "banana": "香蕉"}
# print(dic["apple"])
# print(dic["bug"])
# print(dic["banana"])
# dic["apple"] = "小蘋果"
# print(dic["apple"])

# print()  # 判斷 Key 是否存在
# print("apple" in dic)
# print("cat" in dic)
# print("duck" not in dic)

# del dic["apple"]  # 刪除字典中的鍵值對 (key-value pair)
# print(dic)

dic = {x: x*2 for x in [3, 4, 5, 6]}  # 從列表的資料產生字典
print(dic)
