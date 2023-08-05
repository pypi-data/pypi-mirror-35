# coding:utf-8

import turtle
import time

# 画爱心的顶部
def xzh_heart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)


# 输入表白的语句
# beibei = "就算雨水倒流，世界颠倒，我也会牵着你的手，为你撑伞，给你怀抱.因为是你，所以我愿意和你像孩子一样的肆无忌惮，陪你一起发疯. 因为喜欢你，所以你只能吃我一个人做的饭. 因为喜欢你，所以我懂得你的饭. 因为喜欢你，我愿意变成一个孩子,因为喜欢你，我愿意把你宠成一个孩子。 我把前半辈子写在纸上，余生请多指教"
love = input("Please enter a sentence of love, otherwise the default is: ")
# 输入署名
me = input("Please enter pen name, otherwise the default do not execute: ")
if love == "bei520":
    love = "\n子曰:三思而后行\n  1...2...3...\n    我爱你"
# 窗口大小
turtle.setup(width=1100, height=700)
# 颜色
turtle.color("red", "red")
# 笔粗细
turtle.pensize(6)
# 速度
turtle.speed(2)
# 提笔
turtle.up()
# 隐藏笔
turtle.hideturtle()
# 去到的坐标,窗口中心为0,0
turtle.goto(0, -180)
turtle.showturtle()
# 画上线
turtle.down()
turtle.speed(2)
turtle.begin_fill()
turtle.left(140)
turtle.forward(224)
# 调用画爱心左边的顶部
xzh_heart()
# 调用画爱右边的顶部
turtle.left(120)
xzh_heart()
# 画下线
turtle.forward(224)
turtle.end_fill()
turtle.pensize(5)
turtle.up()
turtle.hideturtle()
# 在心中写字 一次
turtle.goto(0, 0)
turtle.showturtle()
turtle.color("#CD5C5C", "purple")
# 在心中写字 font可以设置字体自己电脑有的都可以设 align开始写字的位置
turtle.write(love, font=("gungsuh", 20,), align="center")
turtle.up()
turtle.hideturtle()
time.sleep(2)
# 在心中写字 二次
turtle.goto(0, 0)
turtle.showturtle()
turtle.color("purple", "purple")
turtle.write(love, font=("gungsuh", 20,), align="center")
turtle.up()
turtle.hideturtle()
# 写署名
if me != "":
    turtle.color("blue", "pink")
    time.sleep(1)
    turtle.goto(180, -180)
    turtle.showturtle()
    turtle.write(me, font=(30), align="center", move=True)

# 点击窗口关闭
window = turtle.Screen()
window.exitonclick()
