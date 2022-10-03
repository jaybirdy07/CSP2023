#   a116_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

num_legs = 8
length_legs = 70
spider_angle = 360 / num_legs
spider.pensize(5)
repeat = 0
while (repeat < num_legs):
  spider.goto(0,20)
  spider.setheading(spider_angle*repeat)
  spider.forward(length_legs)
  repeat = repeat + 1

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
