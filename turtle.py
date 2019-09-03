import turtle


def square(t, l):
    for i in range(4):
        t.fd(l)
        t.lt(90)


def polygon(t, l, n):
    for i in range(n):
        t.fd(l)
        t.lt(360/n)


def circle(t, r):
    c = 2 * 3.1415 * r  # Circumference
    n = 100  # Number of segments
    l = c / n  # Length of each segment
    polygon(t, l, n)


def arc(t, r, a):
    f = a / 360  # Fraction of the whole circle
    c = f * 2 * 3.1415 * r  # Length of the arc
    n = 100  # Number of segments
    l = c / n  # Length of each segment
    a = f*360/n  # Degrees to turn after each segment
    for i in range(n):
        t.fd(l)
        t.lt(a)


bob = turtle.Turtle()
bob.speed(0)
arc(bob, 100, 270)
bob.left(90)
bob.fd(100)
turtle.mainloop()
