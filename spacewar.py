import os
import random

#Import turtle module
import turtle
turtle.fd(0) #fd is short for forward for the window to open on mac 
turtle.speed(0) #Sets the speed of the turtle module to 0 which is the speed of the animation.
turtle.bgcolor("black") #Sets the background color to black 
turtle.ht() #Hides the turtle
turtle.setundobuffer(1) #Sets the undo buffer to 1
turtle.tracer(1) #Traces the animation

class Sprite(turtle.Turtle):
    def __init__(self, sprite_shape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=sprite_shape)
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(startx, starty)
        self.speed = 1
        self.fd(0)
        
    def move(self):
        self.fd(self.speed)
        
        #Detect boundaries
        if self.xcor() > 290:  #If the x coordinate of the sprite is greater than 290
            self.setx(290)  #Set the x coordinate of the sprite to 290
            self.rt(60)  #Turn the sprite to the right by 60 degrees
        
        if self.xcor() < -290:  #If the x coordinate of the sprite is less than -290
            self.setx(-290)  #Set the x coordinate of the sprite to -290
            self.rt(60)   #Turn the sprite to the right by 60 degrees
            
        if self.ycor() > 290:  #If the y coordinate of the sprite is greater than 290
            self.sety(290)
            self.rt(60)
            
        if self.ycor() < -290:  #If the y coordinate of the sprite is less than -290
            self.sety(-290)
            self.rt(60)
            
    def is_collision(self, other):  #Method to check for collision between two sprites
        if (self.xcor() >= (other.xcor() - 20)) and \
            (self.xcor() <= (other.xcor() + 20)) and \
            (self.ycor() >= (other.ycor() - 20)) and \
            (self.ycor() <= (other.ycor() + 20)):
                return True
        else:
            return False
        
            

class Player(Sprite):  #Inherits from Sprite class  #Player class is a subclass of the Sprite class
    def __init__(self, sprite_shape, color, startx, starty): #Constructor  __init__ is a special method in Python classes, it is the constructor method for a class. It is called when an object of the class is created.
        Sprite.__init__(self, sprite_shape, color, startx, starty)  #Calls the constructor of the Sprite class and passes the parameters to it.  #The super() function is used to give access to methods and properties of a parent or sibling class.
        self.speed = 2
        self.lives = 3
        
    def turn_left(self):  #Method to turn the player to the left and it needs to be connected to the arrow key on the keyboard.
        self.lt(45)
        
    def turn_right(self):
        self.rt(45)
        
    def accelerate(self):
        self.speed += 1
        
    def decelerate(self):
        self.speed -= 1
        
class Enemy(Sprite):  #Inherits from Sprite class  #Enemy class is a subclass of the Sprite class
    def __init__(self, sprite_shape, color, startx, starty):  #Constructor
        Sprite.__init__(self, sprite_shape, color, startx, starty)  #Calls the constructor of the Sprite class and passes the parameters to it.
        self.speed = 6
        self.setheading(random.randint(0,360))
        
class Ally(Sprite):  #Inherits from Sprite class  #Enemy class is a subclass of the Sprite class
    def __init__(self, sprite_shape, color, startx, starty):  #Constructor
        Sprite.__init__(self, sprite_shape, color, startx, starty)  #Calls the constructor of the Sprite class and passes the parameters to it.
        self.speed = 8
        self.setheading(random.randint(0,360))
        
    def move(self):
        self.fd(self.speed)
        
        #Detect boundaries
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
            
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)
            
        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)
            
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)
            
    def is_collision(self, other):  #Method to check for collision between two sprites
        if (self.xcor() >= (other.xcor() - 20)) and \
            (self.xcor() <= (other.xcor() + 20)) and \
            (self.ycor() >= (other.ycor() - 20)) and \
            (self.ycor() <= (other.ycor() + 20)):
                return True
        else:
            return False
        

class Missile(Sprite):  #Inherits from Sprite class  #Missile class is a subclass of the Sprite class
    def __init__(self, sprite_shape, color, startx, starty):  #Constructor
        Sprite.__init__(self, sprite_shape, color, startx, starty)  #Calls the constructor of the Sprite class and passes the parameters to it.
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        # self.goto(-1000, 1000) 
        
    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
            
    def move(self):
        if self.status == "ready":
            self.goto(-1000, 1000)
            
        if self.status == "firing":
            self.fd(self.speed)
            
        # Border check
        if self.xcor() < -290 or self.xcor() > 290 or \
            self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"
            
#Create game class
class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3
        
    def draw_border(self):
        #Draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()

#Create game object
game = Game()

#Draw the game border
game.draw_border()

#Create my Sprite 
player = Player("triangle", "white", 0, 0)
enemy = Enemy("circle", "red", -100, 0)
missile = Missile("triangle", "yellow", 0, 0)
ally = Ally("square", "blue", 100, 0)



#Keyboard bindings  #These are the key bindings that are used to control the player.  #The onkey() method is used to bind a function to a key.  #The listen() method is used to listen for events.
turtle.onkey(player.turn_left, "Left")    # this binds the arrow to the keyboard and also you need to tell it to listen.
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()

#Main game loop
while True:
    player.move()
    enemy.move()
    missile.move()
    ally.move()
    
    if player.is_collision(enemy):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        enemy.goto(x, y)
        game.score -= 100
        game.lives -= 1
        print("Score: {}".format(game.score))
        print("Lives: {}".format(game.lives))
        
    if player.is_collision(ally):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        ally.goto(x, y)
        game.score -= 100
        print("Score: {}".format(game.score))
        
    # Check for a collision between the missile and the enemy
    if missile.is_collision(enemy):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        enemy.goto(x, y)
        missile.status = "ready"
        game.score += 100
        print("Score: {}".format(game.score))





delay = input("Press enter to finish. > ")