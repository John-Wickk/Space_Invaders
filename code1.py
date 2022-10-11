import turtle
import os
import math
import random

#  set up The Screen

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("bgg.gif")

#  register the shapes
wn.register_shape("gdp.gif")
wn.register_shape("player.gif.gif")
#  draw border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(7):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#  set the score to 0
score=0

#  draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("green")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "score: %s" %score
score_pen.write(scorestring, False, align="left", font=('Arial', 14, "normal"))
score_pen.hideturtle()

#  create the turtle player
player=turtle.Turtle()
player.color("yellow")
player.shape("player.gif.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player.speed=0

#  choose the number of enemies
number_of_enemies=5
#  create an empty list of enemies
enemies=[]

#  Add enemies to the list
for i in range(number_of_enemies):
    #   create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color('red')
    enemy.shape("gdp.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

    enemyspeed = 2


#  create players bullet

bullet=turtle.Turtle()
bullet.color('cyan')
bullet.shape('triangle')
bullet.shapesize(0.5,0.5)
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=20

#  define bullet state
#  ready-ready to fire bullet
#  fire- bullet is firing

bulletstate="ready"

#  move the player left and right

def move_left():
    player.speed = -15

def move_right():
    player.speed = 15

def move_player():
    x=player.xcor()
    x+=player.speed
    if x < -280:
        x=-280
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #  declare bulletstate as a global if its needed
    global bulletstate
    if bulletstate=='ready':
       os.system("afplay laser.mp3&")
       bulletstate='fire'
        #  move the bullet  to just above the player
       x=player.xcor()
       y=player.ycor()+10
       bullet.setposition(x,y)
       bullet.showturtle()

def iscollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<15:
        return True
    else:
        return False

#  create keyboard bindings
turtle.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet,"space")

#  main game loop

while True:
    move_player()
    if enemy in enemies:
       #  enemy move
       x = enemy.xcor()
       x += enemyspeed
       enemy.setx(x)

       #  move the enemy back and down
       if enemy.xcor() > 280:
          for e in enemies:
              #  move all enemy down
              y=e.ycor()
              y-=40
              e.sety(y)
              #  changes the direction
          enemyspeed *= -1

       if enemy.xcor() < -280:
           for e in enemies:
               #  move all enemy down
               y=e.ycor()
               y-=40
               e.sety(y)
               #  changes the direction
           enemyspeed *= -1

       #  move the bullet
       if bulletstate =="fire":
         y=bullet.ycor()
         y+= bulletspeed
         bullet.sety(y)
         #   check for the collision between bullet and the enemy
       if iscollision(bullet, enemy):

           #   reset the bullet
           bullet.hideturtle()
           bulletstate = "ready"
           bullet.setposition(0, -400)
           #   reset the enemy
           x = random.randint(-200, 200)
           y = random.randint(100, 250)
           enemy.setposition(x, y)
           #  update the score
           score += 10
           scorestring = "score:%s" %score
           score_pen.clear()
           score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
           #   check for the collision between enemy and player
       if iscollision(enemy, player):
           player.hideturtle()
           enemy.hideturtle()
           print('GAME OVER')
           break

    #  check to see if the bullet has gone to the top
    if bullet.ycor()>275:
       bullet.hideturtle()
       bulletstate='ready'





















delay = raw_input("press enter to finsh.")
