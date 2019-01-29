from sympy import (
    Symbol,
    Sum,
    oo,
    N,
    pi,
    sqrt
    )
from sympy import factorial as f

n = Symbol('n', integer=True)

ramanujan_pi_estimate = 9801/sqrt(8)/Sum(
    f(4*n)*(1103+26390*n)/f(n)**4/396**(4*n),
    (n, 0, oo)
)

print(N(ramanujan_pi_estimate, 10000))
# print(N(pi, 1000))
# print(N(ramanujan_pi_estimate, 1000) == N(pi, 1000))