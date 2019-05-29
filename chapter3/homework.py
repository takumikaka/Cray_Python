# -*- coding: utf-8 -*-
import random

#1
strings = "hello,this is python"
tuple_a = tuple(strings)
result = tuple_a * 3
print(result)
new_result = result + ("fkjava", "crazyit")
print(new_result)

#2
list_one = ["fkjava", "crazyit", "hello", "cool"]
print(list_one)
list_two = list_one[::]
print(list_two)

#3
n = 10
list_one = []
for i in range(n):
    list_one.append(random.randint(1, 100))
print(list_one)

#4
n = 10
list_one = []
for i in range(n):
    j = random.randint(1, 100)
    if j%2 == 1:
        list_one.append(j)
    else:
        list_one.append(j+1)
print(list_one)

#5
n = 10
list_one = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
list_two = []
for i in range(n):
    j = list_one[random.randint(0, len(list_one) - 1)]
    list_two.append(j)
print(list_two)

#6
list_one = []
list_two = []
str1 = "hello"
list_one.append(str1)
str2 = "crazyit"
list_one.append(str2)
str3 = "hello"
list_one.append(str3)
for i in range(len(list_one)):
    if list_one.count(list_one[i]) != 1:
        pass
    else:
        list_two.append(list_one[i])
print(list_two)

#8
list_one = ["A", "B", "C", "D", "C", "D", "G", "A", "C"]
list_two = []
dict = {}
for i in range(len(list_one)):
    k = list_one[i]
    if k in list_two:
        pass
    else:
        list_two.append(k)
        v = list_one.count(k)
        dict[k]= v
print(dict)
