# -*- coding: utf-8 -*-

import random

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
listB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

randomA = random.sample(listA, 6)
randomB = random.sample(listB, 1)
print("红区: {0};\t 蓝区: {1}\t".format(randomA, randomB))
