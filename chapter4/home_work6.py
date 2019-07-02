# -*- coding: utf-8 -*-

score = int(input("请输入分数: "))
if score >= 90:
    print("A")
elif score >= 80 and score <90:
    print("B")
elif score >=70 and score < 79:
    print("C")
else:
    print("D")
