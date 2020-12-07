################################
#                              #
# SNAKE.PY                     #
#                              #
# Author:  Hoger Teimouri      #
# Date:    18 November 2020    #
#                              #
################################
  
input("Geben Sie Ihren Namen ein")
# the player has to write a name
###########
# IMPORTS #
###########


from gturtle import *


#####################
# GLOBAL PROPERTIES #
#####################

# Turtle properties
frame = TurtleFrame()
frameTurtle = makeTurtle()
frameTurtle.hideTurtle()
frameTurtle.setPenColor("gold")
snakeTurtle = Turtle (frameTurtle,"snake.png")
snakeTurtle.penUp()
appleTurtle = Turtle (frameTurtle, "apple.png")
stoneTurtles = Turtle (frameTurtle,"stone.png")
stoneTurtles.hideTurtle()
#instant settings
frameSize = 500

# General properties
points = 0
highScore = 0
lastKey = None
name = ""
Zone = 15
#############
# FUNCTIONS #
#############

# FUNCTIONS TO DRAW SHAPES WITH TURTLES
def square():
    frameTurtle.setPos(-250, -250)
    repeat 4:
        frameTurtle.fd (frameSize)
        frameTurtle.rt(90)
    # the playground

# Checks whether the snake (turtle) is alive or not.
# We have to find out the position of the turtle.
# Then we check if the turtle touches a stone or the main frame (blue square).
# Returns True or False.
def snakeTurtleIsAlive():
    # if the snake is outside the square it will be dead or if it touch a stone 
    x = snakeTurtle.getX ()
    y = snakeTurtle.getY()
    stoneSize = 25
    if (x >= 250 or y <= -250 or x <= -250 or y >= 250):
        print "Game over"
        return False  
    if x < caillou.getX() + stoneSize/2 and x > caillou.getX() - stoneSize/2 and y < caillou.getY() + stoneSize/2 and y > caillou.getY() - stoneSize/2:
        print "Game over"
        return False
    if x < caillou1.getX() + stoneSize/2 and x > caillou1.getX() - stoneSize/2 and y < caillou1.getY() + stoneSize/2 and y > caillou1.getY() - stoneSize/2:
        print "Game over"
        return False
    if x < caillou2.getX() + stoneSize/2 and x > caillou2.getX() - stoneSize/2 and y < caillou2.getY() + stoneSize/2 and y > caillou2.getY() - stoneSize/2:
        print "Game over"
        return False
    if x < caillou3.getX() + stoneSize/2 and x > caillou3.getX() - stoneSize/2 and y < caillou3.getY() + stoneSize/2 and y > caillou3.getY() - stoneSize/2:
        print "Game over"
        return False
    if x < caillou4.getX() + stoneSize/2 and x > caillou4.getX() - stoneSize/2 and y < caillou4.getY() + stoneSize/2 and y > caillou4.getY() - stoneSize/2:
        print "Game over"
        return False
    if x < caillou5.getX() + stoneSize/2 and x > caillou5.getX() - stoneSize/2 and y < caillou5.getY() + stoneSize/2 and y > caillou5.getY() - stoneSize/2:
        print "Game over"
        return False
    if x < caillou6.getX() + stoneSize/2 and x > caillou6.getX() - stoneSize/2 and y < caillou6.getY() + stoneSize/2 and y > caillou6.getY() - stoneSize/2:
        print "Game over"
        return False
    if x < caillou7.getX() + stoneSize/2 and x > caillou7.getX() - stoneSize/2 and y < caillou7.getY() + stoneSize/2 and y > caillou7.getY() - stoneSize/2:
        print "Game over"
        return False
    if x < caillou8.getX() + stoneSize/2 and x > caillou8.getX() - stoneSize/2 and y < caillou8.getY() + stoneSize/2 and y > caillou8.getY() - stoneSize/2:
        print "Game over"
        return False
    if x < caillou9.getX() + stoneSize/2 and x > caillou9.getX() - stoneSize/2 and y < caillou9.getY() + stoneSize/2 and y > caillou9.getY() - stoneSize/2:
        print "Game over"
        return False
    if x < caillou10.getX() + stoneSize/2 and x > caillou10.getX() - stoneSize/2 and y < caillou10.getY() + stoneSize/2 and y > caillou10.getY() - stoneSize/2:
        print "Game over"
        return False
    # if the snake touches the square or one of the stones it will be dead
    else: 
        return True
    # if snake doesn't touch the square or a stone it will be alive
#posSX = stoneTurtles.getX
#posSY = stoneTurtles.getY    
#posX = snakeTurtle.getX       
#posY = snakeTurtle.getY 

# Waits until a name is entered by a dialog.
# It saves the name to the global variable name.
def waitForInputName():
    global name # we want to change the value
    name = "Anonymous"
    print "Name entered: " + name 
# to write your name at the beginning

def apple():
    global appleTurtle
    appleTurtle.setRandomPos(0.9*frameSize,0.9*frameSize)
# apple is create and comes everytime back when the snake ate it   
def eatApple(): 
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY()
    posAX = appleTurtle.getX()
    posAY = appleTurtle.getY()
    abst = snakeTurtle.distance(posAX, posAY)
    if abst < Zone:
        global points
        appleTurtle.setRandomPos(0.9*frameSize, 0.9*frameSize)
        points = points + 100
        playTone("a", 40,instrument = "piano")
# the snake can eat the apple 
def stone():
    global caillou
    global caillou1
    global caillou2
    global caillou3
    global caillou4 
    global caillou5
    global caillou6
    global caillou7
    global caillou8
    global caillou9
    global caillou10
    caillou = Turtle (frameTurtle, "stone.png")
    posSX = caillou.getX()
    posSY = caillou.getY()
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY()
    caillou.setRandomPos (0.9*frameSize, 0.9*frameSize)
    
    caillou1 = Turtle (frameTurtle, "stone.png")
    posSX1 = caillou.getX()
    posSY1 = caillou.getY()
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY()
    caillou1.setRandomPos (0.9*frameSize, 0.9*frameSize)
    
    caillou2 = Turtle (frameTurtle, "stone.png")
    posSX2 = caillou.getX()
    posSY2 = caillou.getY()
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY()
    caillou2.setRandomPos (0.9*frameSize, 0.9*frameSize)
    
    caillou3 = Turtle (frameTurtle, "stone.png")
    posSX3 = caillou.getX()
    posSY3 = caillou.getY()
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY()
    caillou3.setRandomPos (0.9*frameSize, 0.9*frameSize)
    
    caillou4 = Turtle (frameTurtle, "stone.png")
    posSX4 = caillou.getX()
    posSY4 = caillou.getY()
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY()
    caillou4.setRandomPos (0.9*frameSize, 0.9*frameSize)
    
    caillou5 = Turtle (frameTurtle, "stone.png")
    posSX5 = caillou.getX()
    posSY5 = caillou.getY()
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY()
    caillou5.setRandomPos (0.9*frameSize, 0.9*frameSize)
    
    caillou6 = Turtle (frameTurtle, "stone.png")
    posSX6 = caillou.getX()
    posSY6 = caillou.getY()
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY()
    caillou6.setRandomPos (0.9*frameSize, 0.9*frameSize)
    
    caillou7 = Turtle (frameTurtle, "stone.png")
    posSX7 = caillou.getX()
    posSY7 = caillou.getY()
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY()
    caillou7.setRandomPos (0.9*frameSize, 0.9*frameSize)
    
    caillou8 = Turtle (frameTurtle, "stone.png")
    posSX8 = caillou.getX()
    posSY8 = caillou.getY()
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY()
    caillou8.setRandomPos (0.9*frameSize, 0.9*frameSize)
    
    caillou9 = Turtle (frameTurtle, "stone.png")
    posSX9 = caillou.getX()
    posSY9 = caillou.getY()
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY()
    caillou9.setRandomPos (0.9*frameSize, 0.9*frameSize)
    
    caillou10 = Turtle (frameTurtle, "stone.png")
    posSX10 = caillou.getX()
    posSY10= caillou.getY()
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY()
    caillou10.setRandomPos (0.9*frameSize, 0.9*frameSize)
# the stones are created   

def deleteStone ():
    global caillou
    global caillou1
    global caillou2
    global caillou3
    global caillou4
    global caillou5
    global caillou6
    global caillou7
    global caillou8
    global caillou9
    global caillou10
    caillou.hideTurtle()
    caillou1.hideTurtle()  
    caillou2.hideTurtle()
    caillou3.hideTurtle()
    caillou4.hideTurtle()
    caillou5.hideTurtle()
    caillou6.hideTurtle()
    caillou7.hideTurtle()
    caillou8.hideTurtle()
    caillou9.hideTurtle()
    caillou10.hideTurtle()
    del caillou
    del caillou1 
    del caillou2
    del caillou3
    del caillou4
    del caillou5 
    del caillou6
    del caillou7
    del caillou8
    del caillou9
    del caillou10
# to delete the stones when you restart    
    
# The function to play the game.
# Reset some stuff first, like the snake turtle, points, etc.
def play():
    global points 
    print "Play function started" 
    square()
    snakeTurtle.setPos(0, 0)
    stone()
 
    i = 0
    isAlive = True
    while (isAlive): # Run the game while the snake is alive
        facing = snakeTurtle.heading()
        keyPressed = getKeyCode()
        if keyPressed == 37:
            if facing == 0 or  facing == 180: # LEFT
                snakeTurtle.setHeading(270)
        if keyPressed == 39:
            if facing == 0 or  facing == 180: # RIGHT
                snakeTurtle.setHeading(90)
        if keyPressed == 38:
            if facing == 90 or facing == 270: # UP
                snakeTurtle.setHeading(0)
        if keyPressed == 40:
            if facing == 270 or facing == 90: # DOWN
                snakeTurtle.setHeading(180)
        #with this function can the snake move 
        
        snakeTurtle.fd(2.25)
        snakeTurtle.speed(-1)
        eatApple()
        
        # Check if the snake is still alive
        isAlive = snakeTurtleIsAlive()
        
        i = i + 1
    # The game is over now
    
    playTone("e", 40,instrument = "piano") 
    print points
    if getKeyCodeWait()== 10:
        deleteStone ()
        play()
    # with enter you can restart the game
       
def main(): #the hole functions in one, the hole gameplay 

    print "Main function started" 

    # Wait until a name is input
    waitForInputName();

    # Start the actual game
    play()

#############
# MAIN CODE #
#############

main()

