# -*- coding: utf-8 -*-

SIZE = 7
array = [[0] * SIZE]
# 创建一个长度为SIZE * SIZE的二维表
for i in range(SIZE - 1):
    array += [[0]  * SIZE]
# 该orient代表绕圈的方向
# 其中0代表向下，1代表向右，2代表向左，3代表向上
orient = 0
# 控制将1~SIZE * SIZE的数值填入二维表中
# 其中j控制行索引，k控制列索引
j = 0
k = 0
for i in range(1, SIZE * SIZE + 1):
    array[j][k] = i
    # 如果位于1号转弯线上
    if j + k == SIZE - 1:
        if j > k:
            orient = 1
        else:
            orient = 2
    elif (k == j) and (k >= SIZE / 2):
        orient = 3
    elif (j == k - 1) and (k <= SIZE / 2):
        orient = 0
    if orient == 0:
        j += 1
    elif orient == 1:
        k += 1
    elif orient == 2:
        k -= 1
    elif orient == 3:
        j -= 1
for i in range(SIZE):
    for j in range(SIZE):
        print("%02d " % array[i][j], end = "")
    print("")

