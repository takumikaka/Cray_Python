# -*- coding: utf-8 -*-

n = int(input("请输入菱形对角线长度" ))
for i in range(-n//2, n//2+1):
    if i <= 0:
        print(""*(-i) + "*"*(n+2*i))
    else:
        print(""*i + "*"*(n-2*i))
