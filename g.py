# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""

import turtle
import random #We'll need this later in the lab

colorlist=['red','green','purple','blue','orange','yellow','pink']

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 4

score=turtle.clone()
score.hideturtle()
score.penup()
score.goto(0,-350)

screen = turtle.Screen()
screen.setup()
screen.bgpic('constellationanimation.gif')

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
score.write(int(len(stamp_list)),align='center',font=("times",33,"bold"))

#Set up positions (x,y) of boxes that make up the snakeSQARE_SIZEsnake = turtle.clone()
snake = turtle.clone()
snake.shape("square")

turtle.register_shape("trash.gif") #Add trash picture
food = turtle.clone()
food.shape("trash.gif")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for CAT in range(START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(my_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    bshara = snake.stamp()
    stamp_list.append(bshara)
b=turtle.clone()
b.hideturtle()
b.pensize(10)
b.pencolor("black")
b.penup()
b.goto(300,300)
b.pendown()
b.goto(300,-300)
b.goto(-300,-300)
b.goto(-300,300)
b.goto(300,300)
###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
DOWN=1
LEFT=2
RIGHT=3
direction = UP




def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    
    #Update the snake drawing <- remember me later
    print("You pressed the up key!")
turtle.onkeypress(up, UP_ARROW) 
turtle.listen()
def down():
    global direction
    direction=DOWN
    
    print("you pressed the down key!")
turtle.onkeypress(down, DOWN_ARROW) 
turtle.listen()
def left():
    global direction
    direction=LEFT
    
    print("you pressed the left key!")
turtle.onkeypress(left, LEFT_ARROW) 
turtle.listen()
def right():
    global direction
    direction=RIGHT
    
    print("you pressed the right key!")
turtle.onkeypress(right, RIGHT_ARROW) 
turtle.listen()
  
def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=(LEFT_EDGE/SQUARE_SIZE)+1
    max_x=(RIGHT_EDGE/SQUARE_SIZE)-1
    min_y=(DOWN_EDGE/SQUARE_SIZE)+1
    max_y=(UP_EDGE/SQUARE_SIZE)-1

    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food_stamps.append(food.stamp())
        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position 
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
count=0        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    
def move_snake():
    global count
    count+=1
    snake.color(colorlist[count%7])
    

    
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")

        
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")

    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE
    elif direction==UP:
        snake.goto(x_pos,y_pos +SQUARE_SIZE)
        print("you moved left!")

        
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print("You moved DOWN!")

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()
    for j in pos_list:
        if snake.pos()==j:
            quit()
    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print('You have eaten the food!')
        stamp_list.append(snake.stamp())
        pos_list.append(snake.pos())
        score.clear()
        score.write(int(len(stamp_list)-5),align='center',font=("times",33,"bold"))

    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
        print('You hit the right edge! Game over!')
        quit()

    elif new_x_pos <= LEFT_EDGE:
        print('You hit the left edge! Game over!')
        quit()
    elif new_y_pos >= UP_EDGE:
        print('You hit the up edge! Game over!')
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print('You hit the down edge! Game over!')
        quit()
    if len(food_stamps) <= 6 :
        make_food()



    turtle.ontimer(move_snake,TIME_STEP) #<--- new line here

    
move_snake()
 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
for this_food_pos in food_pos :
    food.goto(this_food_pos)
    food_stamps.append(food.stamp())
    ####WRITE YOUR CODE HERE!!


# You should do the same for the up(), down(), left(), and right()  functions


##### YOUR CODE HERE

