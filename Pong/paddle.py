from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,x,y):
        # x and y are parameters and they represents coordinates
        # we give these values when we create the object
        
        super().__init__()
        # this one uses the parameters inside init
        self.setpos(x=x,y=y)
        self.penup()
        # self.setheading(90) --> now we can use forward() and backward() instead of setpos() 
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 35
        self.setpos(x=self.xcor(),y=new_y)
    
    def go_down(self):
        new_y = self.ycor() - 35
        self.setpos(x=self.xcor(),y=new_y)