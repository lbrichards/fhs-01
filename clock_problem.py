from wall_clock import draw_clock

import sympy
t = sympy.symbols('t')

def hour_hand(t):
    return 20 + 5 * t / 60

def minute_hand(t):
    return t

def check(t):
    d = minute_hand(t) - hour_hand(t)
    return 35 == hour_hand(t) + 2 * d

def difference(t):
    return minute_hand(t) - hour_hand(t)


solution = sympy.solve(
    hour_hand(t) + (difference(t) * 2) - 35,t)[0]

# draw_clock(4, solution)





print('solution as proper fraction: {}'.format(solution))
print('solution as decimal: {}'.format(sympy.N(solution, 50)))
solution =  sympy.N(solution)
print(hour_hand(solution))
print(solution - hour_hand(solution))
print('answer is correct: {}'.format(check(solution)))


draw_clock(4, solution)

