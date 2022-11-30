#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
apples = []
appleletters = []
wn.addshape(apple_image) # Make the screen aware of the new file
letters = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']

for i in range (5): 
  Apple = trtl.Turtle()
  apples.append(Apple)
  appleletters.append(rand.choice(letters))
  
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(index):
  global appleletters
  apples[index].penup()
  apples[index].shape(apple_image)
  wn.tracer(False)
  apples[index].sety(rand.randint(-25, 150)) #reset apple position
  apples[index].setx(rand.randint(-125,125))
  apples[index].sety(apples[index].ycor()-30)
  apples[index].color("white")
  apples[index].write(appleletters[index], align="center",font=("Arial", 40, "bold"))
  apples[index].sety(apples[index].ycor()+30)
  apples[index].showturtle()
  wn.tracer(True)
  wn.update()

def apple_fall(index):
  apples[index].penup()
  apples[index].clear()
  apples[index].sety(-150)
  apples[index].hideturtle()
  appleletters[index] = rand.choice(letters)
  draw_apple(index)

def typedA():
  for i in range (5):
    if appleletters[i] == 'a':
      apple_fall(i)

def typedS():
  for i in range (5):
    if appleletters[i] == 's':
      apple_fall(i)

def typedD():
  for i in range (5):
    if appleletters[i] == 'd':
      apple_fall(i)

def typedF():
  for i in range (5):
    if appleletters[i] == 'f':
      apple_fall(i)

def typedG():
  for i in range (5):
    if appleletters[i] == 'g':
      apple_fall(i)

def typedH():
  for i in range (5):
    if appleletters[i] == 'h':
      apple_fall(i)

def typedJ():
  for i in range (5):
    if appleletters[i] == 'j':
      apple_fall(i)

def typedK():
  for i in range (5):
    if appleletters[i] == 'k':
      apple_fall(i)

def typedL():
  for i in range (5):
    if appleletters[i] == 'l':
      apple_fall(i)


  
#-----function calls-----
for i in range(5):  
  draw_apple(i)

wn.onkeypress(typedA, 'a')
wn.onkeypress(typedS, 's')
wn.onkeypress(typedD, 'd')
wn.onkeypress(typedF, 'f')
wn.onkeypress(typedG, 'g')
wn.onkeypress(typedH, 'h')
wn.onkeypress(typedJ, 'j')
wn.onkeypress(typedK, 'k')
wn.onkeypress(typedL, 'l')


wn.listen()
wn.bgpic("background.gif")
wn.mainloop()
