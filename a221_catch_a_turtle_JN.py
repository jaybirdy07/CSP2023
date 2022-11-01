# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
turtle_size = 1
turtle_shape = "turtle"
turtle_color = "blue"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
turtle = trtl.Turtle()
score_writer = trtl.Turtle()
counter = trtl.Turtle()
turtle.color(turtle_color)
turtle.shape(turtle_shape)
turtle.shapesize(turtle_size)
score_writer.penup()
score_writer.goto(300,300)
score_writer.pendown()
counter.penup()
counter.goto(-300,300)
counter.pendown

#-----game functions--------

def turtle_clicked(x,y):
    global timer, timer_up
    if(timer_up == True):
      turtle.hideturtle()
    else:
     turtle.penup()
     turtle.hideturtle()
     update_score()
     change_position()
     turtle.pendown()
     turtle.showturtle()
     
def change_position():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-200, 200)
    turtle.goto(new_xpos, new_ypos)
     
def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------
turtle.onclick(turtle_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.bgcolor("lime")
wn.mainloop()
