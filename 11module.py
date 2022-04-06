# # # 載入 sys 模組

# import sys as system
# 使用 sys 模組
# print(system.platform)  # 印出作業系統
# print(system.maxsize)  # 印出整數型態的最大值


# # # 建立 geometry 模組，載入使用
#
# result = geometry.distance(1, 1, 5, 5)
# print(result)
# result = geometry.slope(1, 2, 5, 6)
# print(result)

# # 調整搜尋模組的路徑
# import modules.geometry as geometry
# import sys
# sys.path.append("modules")
# print(sys.path)  # 印出模組的搜尋路徑
# print(geometry.distance(1, 1, 5, 5))
