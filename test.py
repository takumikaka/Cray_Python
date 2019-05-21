# -*- coding: utf-8 -*-

s = "商品名\t\t单价\t\t数量\t\t总价\t\t"
s2 = "<疯狂python>\t\t22\t\t1\t\t22\t\t"

print(s)
print(s2)


#去除重复的元素

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7, 7]
b = []

b.append(a[0])

for i in range(1, len(a)):
    if a[i] in b:
        pass
    else:
        b.append(a[i])
print(b)
