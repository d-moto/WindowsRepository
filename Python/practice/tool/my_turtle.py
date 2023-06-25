import turtle
from turtle import *

# ウィンドウの初期化
window = turtle.Screen()
window.title("Simple Animation")
window.bgcolor("white")

# タートルの初期化
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.shape("turtle")
t2.shape("turtle")
t1.color("blue")
t2.color("red")
t1.speed(1)
t2.speed(1)

t1.home()
t2.home()

t1.setposition(-100, 100)
t2.setposition(-50, 150)

# アニメーションのループ
# for _ in range(4):
#     t1.forward(100)  # 前進
#     t1.right(90)  # 右に回転
#     t2.setposition(10, 0)

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()



# ウィンドウを閉じる
window.mainloop()
