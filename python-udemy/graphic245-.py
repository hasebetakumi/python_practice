# 245. 子供向けグラフィックスturtle
import turtle
window = turtle.Screen()

turtle.speed(0)

turtle.pencolor('green')

for i in range(300):
    turtle.forward(i)
    turtle.right(360 / 4 + 10)

window.exitonclick()

# 246. turtleで描画してみる

