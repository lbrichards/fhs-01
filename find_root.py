import numpy
from numpy import sign


def f(x):
    return x ** 2 - 4


def bisect(f, x_left, x_right):
    
    y_left = f(x_left)
    y_right = f(x_right)
    
    assert (
        sign(y_left) != sign(y_right))
    
    
    for i in range(100):
    
        x_mid = (x_left + x_right) / 2
        y_mid = f(x_mid)
        
        # print('left: {}, mid: {}, right: {}'.format(
        #    x_left, x_mid, x_right)
        #    )
        
        if sign(y_mid) == sign(y_right):
            x_right = x_mid
            y_right = f(x_right)
        
        else:
            x_left = x_mid
            y_left = f(x_left)
            
        if abs(f(x_mid)) < 0.00001:
            
            break
        
    return x_mid
        
    
if __name__ == '__main__':
    from matplotlib import pyplot as plt
    import numpy
    
    f = lambda x: x ** 3 - .05
    
    root = bisect(
        f,
        -5,
        5)
    
    x = numpy.linspace(-5, 5, 2000)
    y = f(x)
    
    plt.plot(x, y)
    
    plt.grid()
    
    plt.ylim(-15, 15)
    plt.xlim(-15, 15)
    plt.scatter([root], [0], color = 'r')
    plt.show()
    
    
    
    
    
    
    
    
