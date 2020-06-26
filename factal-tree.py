import turtle

t = turtle.Turtle()
t.speed(5000)
t.shape('turtle')


def set_pos(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()


set_pos(0, -100)

t.left(90)


def fractal(x):
    if x < 1:
        return
    else:
        t.forward(x)
        t.left(30)
        fractal(x * 0.7)
        t.right(60)
        fractal(x * 0.7)
        t.left(30)
        t.back(x)


fractal(150)
