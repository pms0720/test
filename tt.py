# import turtle
# colors = ["red", "purple", "green", "yellow", "orange" ]
# t = turtle.Turtle()

# turtle.bgcolor("black")
# t.speed(0)
# t.width(3)
# length = 10

# while length < 500:
#     t.forward(length)
#     t.pencolor(colors[length%6])
#     t.right (89)
#     length += 5
   
 
# turtle.done()
import streamlit as st

# 거북이 기본
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(0)




# turtle.done()



# st.title('7과 4의 연산')
# '덧셈',7+4
# '뺄셈',7-4
# '곱셈',7*4
# '나눗셈',7/4
# '몫',7//4
# '나머지',7%4
# '거듭제곱', 7**4

# s= 0
# for i in range(1,1001,3):
    # 's= ', s, 'i = ', i
    # s = s + i 
    # s += i
    # 's + i = ', s

# a=3 
# a==3
# a!= 3
# a>3
# a<3
# a>=3
# a<=3

# a = 1
# b= '1'
# c = "1"

# b+c

# print('a=',a)
# 'a=',a
# b
# c

# s = 55
# if s >= 90:
#     '귀하의 점수는' + str(s) +'점으로 :red [A등급]입니다'
# elif s >= 80:
#     '귀하의 점수는 '+ str(s) +'점으로 :blue[B등급]입니다'
# elif s >= 70:
#     '귀하의 점수는 '+ str(s) +'점으로 :yellow[C등급]입니다'
# elif s >= 60:
#     '귀하의 점수는 '+ str(s) +'점으로 :gray[D등급]입니다'
# else:
#     '귀하의 점수는 '+ str(s) +'점으로 :brown[F등급]입니다'


# 반복문과 조건문----------------------------

# for i in range(1,10):
#     if i%3 == 1:
#         i

# 무지개색의 이상한거 만들기----------------------------

# import turtle

# t =turtle.Turtle()
# t.shape('turtle')
# t.speed(2000)
# colors = ["red","purple","blue","green","yellow","orange","magenta"]
# turtle.bgcolor("white")
# t.width(2)

# length = 5
# for i in range(50000):
#     t.forward(length)
#     t.pencolor(colors[length%7])
#     t.right(120)
#     length +=2

# turtle.done()


# 랜덤 원 마들기-----------------------------------

# import turtle
# import random
# def getRGB():
#     r, g, b = 0, 0, 0
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     return (r, g, b)
# t = turtle.Turtle()
# t.speed(3)
# def draw_circle(radius, x, y, color):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.begin_fill()
#     r,g,b = getRGB()
#     t.color(r,g,b)
#     t.circle(radius)
#     t.end_fill()
# for _ in range(30):
#     radius = random.randint(10, 100)
#     x = random.randint(-200, 200)
#     y = random.randint(-200, 200)
#     color = random.choice(["red", "blue", "green", "orange", "purple", "yellow"])
#     draw_circle(radius, x, y, color)

# 무지개 만들기---------------------------

# import turtle
# rainbow_color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# t = turtle.Turtle()
# t.pensize(20)
# radius = 100  # 
# for colors in rainbow_color:
#     t.penup()
#     t.goto(+radius,0)
#     t.pendown()
#     t.color(colors)
#     t.setheading(90)
#     t.circle(radius, 180)
#     radius += 25  
# turtle.done()



# 함수-----------------------

# def print_address():                     # def print_address():
#     print("")                            #     print('seoul special city')
#     print("")                            #     print('building 7th')
#     print("")                            #     print('honggildong')
# print_address()                          #print_address()


# def user_summer(n):
#     s= 00
#     for i in range(n,n+1):
#         s = s + 1
#     s

# user_summer(100)
# user_summer(200)

     
# s = 0
# for i in range(10,21):
#     s =s+ i
# s


# 함수로 사각형 만들기---------------------------------------
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)

# def rec(x, y, lx, ly):           
#     t.up()
#     t.goto(x, y)
#     t.down()
#     for i in range(2):
#         t.forward(lx)
#         t.left(90)
#         t.forward(ly)
#         t.left(90)

# rec(-200,0,100,50)
# rec(0,0,100,150)
# rec(200,0,100,100)

# turtle.done()

#   랜덤 코드--------------------------------------

# import random

# for i in range(6):                      # i안쓰면 '_'써도됨
#     a1 = random.randint(1,45)
#     a1

# 외부에서 가져오는거----------------------------------------

# import time
# import random as r

# 랜덤 숫자 --------------------------------

# for i in range(6):                     
#     a1 = r.randint(1,45)
#     a2 = r.random()
#     a1,a2

# a=0
# n=100000000000
# for i in range(100):
#     c= r.choice('abcdef')
#     if c == 'a':
#         a = a+1
# a/n, "%'"

# 거북이 경주 게임 ----------------------------------
# import turtle
# import random as r
# t1 = turtle.Turtle()
# t2 = turtle.Turtle()

# t1.shape('turtle')
# t2.shape('turtle')

# t1.penup()
# t1.shapesize(3)
# t1.pensize(5)
# t1.goto(-300, 100)

# t2.penup()
# t2.shapesize(3)
# t2.pensize(5)
# t2.goto(-300, -100)

# t1.pendown()
# t2.pendown()
# t1.speed(1)
# t2.speed(2)

# for i in range(50):
#     d1 = r.randint(1,30)
#     t1.forward(d1)
#     d2 = r.randint(1,30)
#     t2.forward(d2)




# turtle.done()
#--------------------------------------------------------------
# import turtle
# import random as r

# screen = turtle.Screen()
# im1 = 'rabbit.gif'
# im2 = 'turtle.gif'
# im3 = 'turtle.gif'
# screen.addshape(im1)
# screen.addshape(im2)
# screen.addshape(im3)
# image1 = 'rabbit.gif'
# image2 = 'turtle.gif'
# image3 = 'bear.gif'
# screen.addshape(image1)
# screen.addshape(image2)
# screen.addshape(image3)

# t1 = turtle.Turtle()
# t1.shape(image1)
# t1.pensize(5)
# t1.penup()
# t1.goto(-300,0)

# t2 = turtle.Turtle()
# t2.shape(image2)
# t2.pensize(5)
# t2.penup()
# t2.goto(-300,-100)

# t3 = turtle.Turtle()
# t3.shape(image3)
# t3.pensize(5)
# t3.penup()
# t3.goto(-300,-200)



# t1.pendown()
# t2.pendown()
# t3.pendown()
# t1.speed(1)
# t2.speed(1)
# t3.speed(1)

# for i in range(100):
#     d1 = r.randint(1,10)
#     t1.forward(d1)
#     d2 = r.randint(1,10)
#     t2.forward(d2)
#     d3 = r.randint(1,10)
#     t3.forward(d3)


# turtle.done()

            # 애니메이션 만들기------------------------------
                 #(1) 책 내용
# import turtle
# import random 
# t = turtle.Turtle()
# t.speed(0)
# t.pensize(5)
# t.goto(0,0)
# while True:
#     for i in range(20):
#         t.circle(1 + 5*i)
#         t.color((random.random(),random.random(),random.random()))
#         t.goto(i*20,0)
#     t.clear()
# turtle.done()

# 기말고사 사각형으로 만들기 ************************************

# import turtle
# import random 
# t = turtle.Turtle()
# t.speed(0)
# t.pensize(5)
# t.goto(0,0)
# sh=5

# while True:
#     for i in range(20):
#         for j in range(sh):
#             t.forward(1 + 5*i)
#             t.left(360/sh)

#         t.color((random.random(),random.random(),random.random()))
#         t.goto(i*20,0)
    
# turtle.done()


            #앵그리 터틀 게임---------------------------------------------
# import turtle
# import math
# import random

# player = turtle.Turtle()
# player.shape('turtle')
# screen =player.getscreen()
# screen.bgcolor('black')
# player.color('yellow')
# player.goto(-300,0)
# velocity = 70
# player.left(45)
# def turnleft():
#     player.left(5)
# def turnright():
#     player.right(5)
# def turnup():
#     global velocity
#     velocity += 10
# def turndown():
#     global velocity
#     velocity -= 10
# def fire():
#     x= -300
#     y= 0
#     player.color(random.random(),random.random(),random.random())
#     player.goto(x, y)
#     angle = player.heading()
#     vx = velocity * math.cos(angle * 3.14 / 180.0)
#     vy = velocity * math.sin(angle * 3.14 / 180.0)
#     while player.ycor() >=0 :
#         vx =vx
#         vy= vy -10
#         x = x+vx
#         y = y+vy
#         player.goto(x,y)
#         player.stamp()
        
# screen.onkeypress(turnleft,'Left')
# screen.onkeypress(turnright, 'Right')
# screen.onkeypress(turnup, 'Up')
# screen.onkeypress(turndown,'Down')
# screen.onkeypress(fire, 'space')
# screen.listen()
# turtle.mainloop()


# turtle.done


           #리스트로 그래프 그리기----------------------------------------
# import streamlit as st

# import random 

# import matplotlib.pyplot as plt


# fig, ax = plt.subplots()

# numbers = []
# for i in range(10):
#     numbers.append(random.randint(1,10))

# plt.plot(numbers)
# plt.ylabel('some random numbers')
# plt.xlabel('x=axis')

# st.pyplot(fig)

# t = 0
# for i in s:
#     # t = t+i
#     t += i
# t
    


#2차 함수 그래프 만들기================================================



#밑에 다 주석처리해주는 기능============
# import sys  
# sys.exit()

# import streamlit as st 
# import matplotlib.pyplot as plt


# fig, ax = plt.subplots()

# x = []
# for i in range (-100,101):
#     x.append(i/10.0)


# col = st.columns(3)
# with col[0]:
#     a = st.number_input('Insert a', step =10)
# with col[1]:
#     b = st.number_input('Insert b', step =10)
# with col[2]:
#     c = st.number_input('Insert c', step =10)

# y = []
# for i in x:
#     y.append(a*i**2 + b *i + c)

# plt.plot(x,y)
# plt.show()
# st.pyplot(fig)

#------------------------------------------------- 2차 함수 색 선택 그래프

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np



co11,co12,co13 = st.columns(3) 

with co11:
    c1=st.radio('선의 색을 선택',('red','green','blue','orange'))
with co12: 
    s1=st.radio('선의 형태를 선택',('-',':','-','--'))
with co13:
    m1=st.radio('마커의 형태를 선택',('o','^','s','p'))

fig,ax = plt.subplots()
c1 = st.sidebar.radio('선의색을 선택하시오',( 'red','yellow','green','blue'))

x = []
y = []
for i in range(-20, 21, 2):
    x.append(i)
    y.append(-2 *i*i + i+5) 

plt.plot(x,y, color = c1, linestyle=s1, marker=m1)

st.pyplot(fig)


import sys  
sys.exit()



x = []
y = []
ysin = []
for i in range(-20,21,1):   
    x.append(i)
    y.append(3*i*i - 5*i + 2)
    ysin.append(1200*np.sin(i))
plt.plot(x, y, color = c1, label ='2nd equation')
plt.plot(x, ysin, color = c1, label ='sin function')
plt.legend()
plt.xlabel('x-label')
plt.xlabel('y-axis')
plt.xlim(-15,15)
plt.ylim(-2000,2000)
st.pyplot(fig)









