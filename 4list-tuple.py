# # 有序可變動列表 List
grades = [12, 60, 15, 70, 90]
print(grades)
print(grades[0])
print(grades[3])
grades[0] = 55
print(grades)
print(grades[1:4])
grades[1:4] = []
print(grades)
grades = grades+[12, 33, 100]
print(grades)

length = len(grades)
print(length)

data = [[3, 4, 5], [6, 7, 8]]
print(data)
data[0][0:2] = [5, 5, 5]
print(data)


# # 有序不可變動列表 Tuple
data = (3, 4, 5)
print(data[0:2])
# data[0] = 5  # 錯誤: Tuple 的資料不可以變動
print(data)
