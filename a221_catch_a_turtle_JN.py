# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
turtle_color = "blue"
turtle_size = 1
turtle_shape = "turtle"
score = 0
score_writer = (300,300)

#-----initialize turtle-----
turtle = trtl.Turtle
turtle.shape(turtle_shape)
turtle.shapesize(turtle_size)
turtle.color(turtle_color)

sw = trtl.Turtle
sw.penup()
sw.goto(300,300)
sw.pendown()

#-----game functions--------
def turtle_clicked(x,y):
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
    print(score)

#-----events----------------
turtle.onclick(turtle_clicked)

wn = trtl.Screen()
wn.mainloop()
