import turtle
turtle.color('white', 'pink')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.position()) < 1:
        break
turtle.end_fill()
turtle.done()