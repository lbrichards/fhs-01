from numpy import pi
from scipy.special import factorial
import numpy
from scipy.special import gammaln
import sys
sys.setrecursionlimit(15000)
from decimal import *
import math
from sympy import pi as PI
from sympy import N, Float
from functools import lru_cache
RECIPROCAL_OF_PI = Float(1 / N(PI, n = 50))




getcontext().prec = 50

@lru_cache(maxsize=None)
def factorial(n):
    if n in (0, 1):
        return Float(1)
    temp = factorial(n - 1)
    
    return Float(n) * temp


def is_odd(x):
    return x % 2 == 1

def is_even(x):
    return not is_odd(x)

def alternating_signs(x):
    for i in range(x):
        yield 1 if is_even(i) else - 1

def odd_values(n):
    for i in range(1, n):
        yield i * 2 - 1
        

def calc_pi(n):
    total = 0
    for x, sign in zip(odd_values(n), alternating_signs(n)):
        total += 1 / (x * sign)
    return total * 4

def log_factorial(x):
    if x in [0, 1]:
        return 0
    if x < 50:
        return numpy.log(x) + log_factorial(x - 1)
    else:
        return gammaln_factorial(x)

def gammaln_factorial(x):
    if x in [0, 1]:
        return 0
    return numpy.log(x) + gammaln_factorial(x - 1)
    




def estimate_pi():
    """Computes an estimate of pi.

    Algorithm due to Srinivasa Ramanujan, from 
    http://en.wikipedia.org/wiki/Pi
    """
    total = Float(0, 50)
    k = Float(0)
    factor = Float(2 * math.sqrt(2) / 9801)
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        # term = factor * num / den
        term = num / den
        total += Float(term)
        print(1 / (factor * total))
        print(N(PI, 50))
        print('*' * 20)
        if abs(1 / (factor * total) - PI)< Float(1e-16): break
        # print(k)
        k += 1
        
    return 1 / total

def estimate_via_BBP():
    def BBP(k):
        a = 1 / 16 ** k
        b = 4 / (8 * k + 1)
        c = -2 / (8 * k + 4)
        d = -1 / (8 * k + 5)
        e = -1 / (8 * k + 6)
        return a * sum([b, c, d, e])

    total = Float(0, 100)
    k = 0
    previous = None
    while True:
        total += BBP(k)
        k += 1
        if previous == total:
            break
        previous = total
        
    return total


print(calc_pi(300))

