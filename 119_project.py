import turtle as trtl
import random
painter = trtl.Turtle()

wn = trtl.Screen()


#make it nighttime
wn.bgcolor("black")

#create flower

#make stem
painter.color("#52A146")
painter.pensize(5)
painter.penup()
painter.goto(-200, -150)
painter.pendown()
painter.setheading(90)
painter.forward(40)
#make leaf
painter.setheading(270)
painter.circle(10, 60, 10)
painter.setheading(90)
painter.goto(-200, -110)
#rest of stem
painter.forward(30)
painter.setheading(0)

#turn into circle shape
painter.penup()
painter.shape("circle")

#draw first row of petals
painter.color("#9C7DCB")
painter.goto(-190,-30)

for petal in range(10):
  painter.right(36)
  painter.forward(15)
  painter.stamp()

painter.penup()
painter.goto(-190,-40)

#draw smaller second row of petals
painter.color("#E38EBE")
for petal in range(6):
  painter.right(60)
  painter.forward(15)
  painter.stamp()

#draw middle of flower
painter.goto(-197,-52)
painter.color("#F9DE5A")
painter.stamp()


painter.shape("classic")

painter.pensize(1)


#make stars
painter.pencolor("white")
painter.fillcolor("white")
painter.begin_fill()
xcord = -500
ycord = -150
for _ in range(24):
    painter.penup()

    #make each star a random location
    painter.goto(xcord,ycord)
    painter.pendown()
    painter.begin_fill()

    #make each star a random size
    painter.circle(random.randint(1,2))
    painter.end_fill()
    xcord = xcord + 45
    ycord = random.randint(-220,400)



#create the fireworks
painter.penup()
painter.goto(-200,200)
painter.pendown()
painter.speed(0)
height = 310
height2 = 425
angle = 170


color1 = "pink"
color2 = "purple"
space = 1

#create first firework
while painter.ycor() < height: 
   if painter.pencolor() == color2: 
       painter.fillcolor(color1) 
       painter.color(color1) 
   else: 
       painter.fillcolor(color2) 
       painter.color(color2) 

   painter.right(angle) 
   painter.forward(2 * space + 10)
   painter.begin_fill() 
   painter.circle(1) 
   painter.end_fill() 
   space = space + 1

painter.penup()
painter.goto(200,300)
painter.pendown()
space = 1
color3 = "blue"
color4 = "lime"

#make second firework
while painter.ycor() < height2: 
   if painter.pencolor() == color4: 
       painter.fillcolor(color3) 
       painter.color(color3) 
   else: 
       painter.fillcolor(color4) 
       painter.color(color4) 

   painter.right(angle) 
   painter.forward(2 * space + 10)
   painter.begin_fill() 
   painter.circle(1) 
   painter.end_fill() 
   space = space + 1


#make the grass at the bottom
painter.penup()
painter.goto(-600,-150)
painter.pendown()
painter.pencolor("green")
painter.begin_fill()
painter.fillcolor("green")
painter.setheading(0)

for _ in range(4):
    painter.forward(1300)
    painter.right(90)



#make shooting star
painter.end_fill()
painter.penup()
painter.pencolor("white")
painter.color("white")
painter.shape("circle")
painter.pensize(4)
painter.speed(1)
painter.goto(-500,-50)
painter.pendown()
painter.goto(500,100)




wn.mainloop()