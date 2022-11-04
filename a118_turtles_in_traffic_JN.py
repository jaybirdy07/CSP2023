#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
speed = 50

for s in turtle_shapes:
  #move the new turtle horazontaly
  ht = trtl.Turtle(shape=s)
  ht.speed(speed)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
  #move the new turtle verticly 
  vt = trtl.Turtle(shape=s)
  vt.speed(speed)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  #reset end point
  tloc += 50
  speed ++ 50

# TODO: move turtles across and down screen, stopping for collisions

speed = 50

for step in range(50):
	for ht in horiz_turtles:
         for vt in vert_turtles:
             ht.forward(5)
             vt.forward(3)
             speed ++ 50
             if (abs(ht.xcor() - vt.xcor()) < 20):
                 if (abs(ht.ycor() - vt.ycor()) < 20):
                  ht.fillcolor(new_color)
                  ht.shape("square")
                  vt.fillcolor(new_color)
                  vt.shape("square")
                  ht.forward(-15)
                  vt.forward(-12)
                  if (abs(ht.xcor() - vt.xcor()) < 18):
                    if (abs(ht.ycor() - vt.ycor()) < 18):
                      vt.fillcolor("red")
                      ht.fillcolor("red")
                      horiz_turtles.remove(ht)
                      vert_turtles.remove(vt)
