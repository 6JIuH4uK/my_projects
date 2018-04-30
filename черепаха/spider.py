import turtle
#Рисуем спираль
i = 0
n = 8
turtle.shape("turtle")
turtle.pendown()
while i <= n:
    turtle.right(10)
    turtle.forward(60)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(60)
    turtle.right(210)
    i += 1
