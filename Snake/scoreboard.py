from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",14,"normal")

class Score(Turtle):
    
    def __init__(self):
        
        # superclass reference
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setpos(x=0,y=270)
        self.color("white")
        self.increase_score()
    
    # BEHAVIOR
    def increase_score(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
         
    def update(self):        
        self.score += 1
        self.clear()
        self.increase_score()
        self.setpos(x=0,y=270)
        
    def game_over(self):
        self.setpos(x=0,y=0)
        self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)
        