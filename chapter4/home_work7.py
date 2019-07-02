# -*- coding: utf-8 -*-

from math import sqrt

class Check_num(object):
    def __init__(self):
        self.prime_list = []

    def is_prime(self, num):
        if num == 1:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def run(self):
        for num in range(101, 201):
            check_prime = self.is_prime(num)
            if check_prime:
                self.prime_list.append(num)
            else:
                pass
        print("101~200之间有{0}个素数.\n".format(len(self.prime_list)))
        print("这些质数分别是: {0}".format(self.prime_list))

def main():
    Action = Check_num()
    Action.run()

if __name__=="__main__":
    main()
