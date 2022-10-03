#   a116_buggy_image.py
import turtle as trtl
spider = trtl.Turtle()

# Create a spider body
spider.pensize(40)
spider.circle(20)

# Configure spider legs 
num_legs = 6
length_legs = 70
spider_angle = 380 / num_legs
spider.pensize(5)
repeat = 0

# Draw spider legs 
while (repeat < num_legs):
  spider.goto(0,0)
  spider.setheading(spider_angle*repeat)
  spider.forward(length_legs)
  repeat = repeat + 1

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
