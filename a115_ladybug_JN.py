#   a116_ladybug.py
import turtle as trtl
ladybug = trtl.Turtle()

# Configure ladybug legs 
num_legs = 3
length_legs = 50
ladybug_angle = 120 / num_legs
ladybug.pensize(5)
repeat = 0

# Draw ladybug legs
while (repeat < num_legs):
  ladybug.goto(0,-30)
  ladybug.setheading(ladybug_angle*repeat)
  ladybug.right(60)
  ladybug.forward(length_legs)
  repeat = repeat + 1

ladybug.penup()
num_legs = 3
repeat = 0
while (repeat < num_legs):
  ladybug.goto(0,-30)
  ladybug.pendown()
  ladybug.setheading(-ladybug_angle*repeat)
  ladybug.right(120)
  ladybug.forward(length_legs)
  repeat = repeat + 1

# create ladybug head
ladybug.penup()
ladybug.goto(3, 15)
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(8, -10) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 8)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()
