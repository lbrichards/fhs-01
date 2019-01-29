from sympy import (
    Symbol,
    Sum,
    oo,
    N,
    pi
    )

k = Symbol('k', integer=True)

L = 4 * Sum(
    (-1) ** k / (2 * k + 1),
    (k, 0, oo)
)

print(N(L, 1000))
# print(N(pi, 100))