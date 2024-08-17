import turtle

turtle.speed(0)

r = 90
a = 360

for i in range(100):
    turtle.circle(r, a)
    turtle.forward(10)

turtle.done()