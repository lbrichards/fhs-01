import turtle



def hour_hand_in_degrees(h, m):
    hours = (h / 12) * 360
    minutes = (m / 60 / 12) * 360
    return hours + minutes

def minute_hand_in_degrees(m):
    return (m / 60 ) * 360


def draw_clock( h, m):
    wn = turtle.Screen()
    wn.bgcolor('black')
    wn.setup(width = 600, height = 600)
    wn.title('Analog Clock')    
    
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)    
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color('green')
    pen.pendown()
    pen.circle(210)
    
    # hour lines
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    
    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)
    
    #  hour hand
    pen.penup()
    pen.goto(0, 0)
    pen.color('white')
    pen.setheading(90)
    angle = hour_hand_in_degrees(h, m)
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    
    #  minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color('blue')
    pen.setheading(90)
    angle = minute_hand_in_degrees(m)
    pen.rt(angle)
    pen.pendown()
    pen.fd(200)
    wn.mainloop()
    

if __name__ == '__main__':
    draw_clock(4, 28)

    