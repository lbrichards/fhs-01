from scipy.optimize import bisect, newton, fsolve, brent
from matplotlib import pyplot as plt
import numpy


f = lambda x: x ** 3 - 5
x = numpy.linspace(-10, 10, 2000)




def g(y):
    F = lambda x_hat: f(x_hat) - y
    return bisect(F, f(-100), f(100))


yy = numpy.linspace(-10, 10, 2000)
xx = [g(y) for y in yy]


plt.ylim(-10, 10)
plt.xlim(-10, 10)
plt.plot(yy, xx)
plt.grid()
plt.show()

root1 = bisect(f, -100, 100, full_output= False)
# root2 = newton(f, 10)
# minimum = brent(f, brack = (-2, 10))
plt.plot(x, f(x))
plt.scatter([root1], [0], color = 'r')
# plt.scatter([root2], [0], color = 'g')
# plt.scatter([minimum], [f(minimum)], color = 'orange')
plt.ylim(-10, 10)
plt.xlim(-10, 10)
plt.grid()
plt.show()