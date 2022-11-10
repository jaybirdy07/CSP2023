#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
drawer = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def draw_an_A():
  drawer.color("blue")
  drawer.write("A", font=("Arial", 74, "bold"))

def apple_fall():
  apple.penup()
  apple.sety(-150)
  
def draw_letter():
  drawer.pencolor("white")
  drawer.penup()
  drawer.goto(-250,100)
  drawer.pendown()
  drawer.write("A", font=("Arial", 74, "bold") )
  
#-----function calls-----
draw_apple(apple)
draw_letter()

wn.onkeypress(apple_fall, "a")
wn.listen()
wn.bgpic("background.gif")
wn.mainloop()
