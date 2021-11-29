from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.penup()
        self.hideturtle()
        # default value
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.setpos(-100,200)
        self.write(self.l_score, align="center",font=("Courier",60,"normal"))
        self.setpos(100,200)
        self.write(self.r_score, align="center",font=("Courier",60,"normal"))
        # since it's been initialized here it will be a default feature of our object as soon as it gets initialized 
        self.scoreboard()
    
    # default
    def scoreboard(self):
        self.clear()
        
        self.setpos(-100,200)
        self.write(self.l_score, align="center",font=("Courier",60,"normal"))
        self.setpos(100,200)
        self.write(self.r_score, align="center",font=("Courier",60,"normal"))
    
    def l_point(self):
        self.l_score += 1
        #self.clear()
        self.scoreboard()
    
    def r_point(self):
        self.r_score += 1
        #self.clear()
        self.scoreboard()
        
    def game_over(self):
        self.setpos(0,0)
        self.write("GAME OVER",align="center",font=("Arial", 40,"normal"))
    
    def winner(self):
        self.setpos(0,-70)
        if self.l_score > self.r_score:
            self.write("Player on the left won",align="center",font=("Arial", 20,"normal"))
        else:
            self.write("Player on the right won",align="center",font=("Arial", 20,"normal"))

            