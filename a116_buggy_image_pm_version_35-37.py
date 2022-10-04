#   a116_buggy_image.py
import turtle as trtl
spider = trtl.Turtle()

# Create a spider body
spider.pensize(40)
spider.circle(20)

spider.penup()
spider.goto(-30, 15)
spider.pendown()
spider.pensize(40)
spider.circle(5)

# Configure spider legs 
num_legs = 4
spider_angle = 120 / num_legs
spider.pensize(5)
repeat = 0

# Draw spider legs
while (repeat < num_legs):
  spider.penup()
  spider.goto(0,20)
  spider.pendown()
  spider.setheading(spider_angle*repeat)
  spider.circle(50,100)
  repeat = repeat + 1

spider.penup()
num_legs = 4
repeat = 0
while (repeat < num_legs):
  spider.penup()
  spider.goto(0,20)
  spider.pendown()
  spider.pendown()
  spider.setheading(-spider_angle*repeat)
  spider.right(180)
  spider.circle(50, -100)
  repeat = repeat + 1

spider.penup()
spider.pencolor("white")
spider.goto(-35,25)
spider.pendown()
spider.circle(5)
spider.penup()
spider.goto(-35,10)
spider.pendown()
spider.circle(5)


spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
