from turtle import Turtle, Screen
import random

MOVEMENTS = [0,90,180,270]
FORWARD = 15
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("green")
        self.speed("slowest")
        self.refresh()
        self.move()
    
    # BEHAVIOR
    def refresh(self):
        rand_x = random.randint(-270,270)
        rand_y = random.randint(-270,270)
        self.setpos(x=rand_x,y=rand_y)
        
    def move(self):
        if self.xcor() > 280 or self.xcor() < -280 or self.ycor() > 280 or self.ycor() < -280:
            pass
        else:
            self.speed("slowest")
            self.forward(FORWARD)
            self.setheading(random.choice(MOVEMENTS))
            self.forward(0)