import turtle
import tkinter
from random import (
    choice,
    randint,
    random,
    paretovariate,
    gammavariate,
    shuffle
    )

fred = turtle.Turtle()
fred.speed(5)
fred.shape("circle")
fred.shapesize(2)
fred.color('blue')
fred.pensize(3)
for i in range(60):
    # fred.pensize(randint(1, 10))
    # fred.color(
    #    choice([
    #        'blue',
    #        'green',
    #        'red',
    #        'orange',
    #        'black',
    #        'purple',
    #        'magenta'
    #    ])
    # )
    fred.forward(100)
    fred.right(59)


tkinter.mainloop()
