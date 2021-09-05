from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as f:
            current_high_score = int(f.read())
        self.high_score = current_high_score
        self.color('white')
        self.penup()
        self.setpos(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as f:
                f.write(str(self.score))

        self.score = 0
        self.update_score()

    def game_over(self):
        self.setpos(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

