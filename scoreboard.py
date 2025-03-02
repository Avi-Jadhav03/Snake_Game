from turtle import Turtle

class ScoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score : {self.score}",align="center",font=("Arial ",21,"normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial ", 21, "normal"))

    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER", align="center", font=("Arial ", 21, "normal"))


            
