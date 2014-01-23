#! python3
__author__ = 'kitti'

import math
from fractions import Fraction
from decimal import Decimal, getcontext


def main():
    global n
    if n.isdigit():
        toiter = int(int(n) * 10 / 3) + 5
        pi = Fraction(0)
        for i in range(toiter):
            a = math.factorial(i)
            asquare = pow(a, 2)
            b = pow(2, (i + 1))
            num = asquare * b
            c = (2 * i) + 1
            deno = math.factorial(c)
            pi = pi + Fraction(num, deno)
            #print(Fraction(num, deno))
        getcontext().prec = int(n) + 1
        print(Decimal(pi.numerator) / Decimal(pi.denominator))
    else:
        n = input("Please enter a digit")
        main()


n = input("Enter number of decimals to print π(pi) value")
main()