#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
apple = trtl.Turtle()
apple_letter = 'a'
letters = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.penup()
  active_apple.shape(apple_image)
  wn.tracer(False)
  active_apple.sety(rand.randint(-25, 150)) #reset apple position
  active_apple.setx(rand.randint(-125,125))
  apple_letter = letters[rand.randint(0,8)]
  active_apple.sety(active_apple.ycor()-30)
  active_apple.color("white")
  active_apple.write(apple_letter, align="center",font=("Arial", 40, "bold"))
  active_apple.sety(active_apple.ycor()+30)
  active_apple.showturtle()
  wn.tracer(True)
  wn.update()
  wn.onkeypress(apple_fall, apple_letter)

def apple_fall():
  apple.penup()
  apple.clear()
  apple.sety(-150)
  apple.hideturtle()
  draw_apple(apple)


  
#-----function calls-----
draw_apple(apple)

wn.listen()
wn.bgpic("background.gif")
wn.mainloop()
