# -*- coding: utf-8 -*-

from math import pow

class NarcNum(object):
    def __init__(self):
        self.narc_list = []

    def get_hundred(self, num):
        hundred = int(num % 1000 / 100)
        return hundred

    def get_ten(self, num):
        ten = int(num % 100 / 10)
        return ten

    def get_unit(self, num):
        unit = int(num % 10)
        return unit

    def run(self):
        for num in range(100, 1000):
            hundred = self.get_hundred(num)
            ten = self.get_ten(num)
            unit = self.get_unit(num)
            if pow(hundred, len(str(num))) + pow(ten, len(str(num))) + pow(unit, len(str(num))) == num:
                self.narc_list.append(num)
            else:
                pass
        print(self.narc_list)

def main():
    Action = NarcNum()
    Action.run()

if __name__ == "__main__":
    main()
