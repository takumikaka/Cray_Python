# -*- coding: utf-8 -*-

for i in range(1, 10):
    for j in range(1, i + 1):
        print("{0}*{1}={2} \t".format(j, i, i*j), end = "")
    print()
