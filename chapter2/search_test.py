# -*- coding: utf-8 -*-

s = "crazyit.org is a good site"
print(s.startswith("crazy"))
print(s.endswith("ite"))
print(s.find("org"))
print(s.index("org"))
print(s.find("org", 9))
#print(s.index("org", 9))
print(s.replace("it", "It"))
print(s.replace("it", "It", 1))

table = {97: 945, 98: 946, 116: 964}
print(s.translate(table))

table = str.maketrans("abt", "αβτ")
print(table)
print(s.translate(table))

table = str.maketrans("abt", "123")
print(table)
print(s.translate(table))
