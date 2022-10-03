#   a116_buggy_image.py
import turtle as trtl
spider = trtl.Turtle()

# Create a spider body
spider.pensize(40)
spider.circle(20)

# Configure spider legs 
num_legs = 4
length_legs = 70
spider_angle = 120 / num_legs
spider.pensize(5)
repeat = 0

# Draw spider legs
while (repeat < num_legs):
  spider.goto(0,20)
  spider.setheading(spider_angle*repeat)
  spider.forward(length_legs)
  repeat = repeat + 1

spider.penup()
num_legs = 4
repeat = 0
while (repeat < num_legs):
  spider.goto(0,20)
  spider.pendown()
  spider.setheading(-spider_angle*repeat)
  spider.right(90)
  spider.forward(length_legs)
  repeat = repeat + 1

spider.penup()
spider.pencolor("white")
spider.goto(-20,30)
spider.pendown()
spider.circle(5)
spider.penup()
spider.goto(3,45)
spider.pendown()
spider.circle(5)


spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
