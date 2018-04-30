import turtle
# Рисуем квадраты
turtle.shape("turtle")
i = 0
step = 0
while i <= 10:
    turtle.pendown()
    turtle.forward(20+step)
    turtle.left(90)
    turtle.forward(20+step)
    turtle.left(90)
    turtle.forward(20+step)
    turtle.left(90)
    turtle.forward(20+step)
    turtle.penup()
    turtle.right(45)
    step +=10
    turtle.forward(7)
    turtle.left(135)
    i += 1

