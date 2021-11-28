from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        # these are default values but we can always change them
        self.x_move = 15
        self.y_move = 15
        # ball's speed
        self.ball_speed = 0.1
        
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        # these attributes track the movement

    
    # to make the ball move we're going to increase the x and y coordinates by a certain amount. 
    # Both x and y will increase based on their actual coordinates
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(x=new_x,y=new_y)
        
    # Reset the ball's position
    def reset_position(self):
        self.setpos(x=0,y=0)
        # reset the speed when one of the player score a point
        self.ball_speed = 0.1
        
    # if we change the ycor() our ball will bounce
    # it is still on the x-axis but we only change the y-axis to chage the ball's direciton
    # THIS FUNCTION CHANGES THE VALUE OF "self.y_move"
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        # by multiplying this for "move_speed" the value decrease
        self.ball_speed *= .9