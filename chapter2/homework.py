# -*- coding: utf-8 -*-

'''
import re
str = "ABCDCDCDC"
num = len(re.findall(r"(?=CDC)", str))
print(num)
'''

input_str = input("输入的字符串:")
modiy_str = input("输入修改的内容")
modiy_list = modiy_str.split(" ")
num = int(modiy_list[0])
stri = modiy_list[1]
new_string = input_str.replace(input_str[num], stri)
print(new_string)
