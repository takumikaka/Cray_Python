# -*- coding: utf-8 -*-

i = 1
while i <= 5:
    j = 1
    while j <= 5-i:
        print(" ", end="")
        j += 1
    k = 1
    while k <= 2*i - 1:
        print("*", end="")
        k += 1
    print()
    i += 1
