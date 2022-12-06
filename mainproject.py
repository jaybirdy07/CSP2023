import turtle as trtl
import leaderboard as lb

#Game configuration
wn = trtl.Screen()
backround = "78cm.gif"
dresser_image = "dresser.png"
wn.addshape(dresser_image)
leaderboard_file_name="leaderboard"
player_name = input("Please enter your name:")

font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#initalize turtle 
dresser = trtl.Turtle()
counter = trtl.Turtle()
counter.penup()
counter.goto(-250,150)
counter.pendown

# Functions
def dresser(dresser_1):
    dresser_1.shape(dresser_image)
    dresser_1.sety(200)
    dresser_1.setx(100)
    wn.update()


'''def open_drawer():'''


    

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def manage_leaderboard():

  global score
  global turtle

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, turtle, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, turtle, score)

#Events
dresser(dresser)


wn.ontimer(countdown, counter_interval)
wn.bgpic("78cm.gif")
wn.mainloop()
