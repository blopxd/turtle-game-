from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color_score = '#A6F7CB'  # Color for the score and life
        self.color_title = '#784AC3'  # Color for the title
        self.color_win = '#784AC3'  # Color for win
        self.color_lose = 'red'  # Color for losing
        self.penup()
        self.hideturtle()
        self.title = '? Space Invaders ?'
        self.score = 0
        self.life = 5
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-413, 239)
        self.color(self.color_score)  # Set the color for score and life
        self.write(f"pts: {self.score}", align='center', font=('Courier', 37, 'normal'))
        self.goto(399, 239)
        self.write(f"life: {self.life}", align='center', font=('Courier', 37, 'normal'))
        self.goto(0, 219)
        self.color(self.color_title)  # Set the color for the title
        self.write(f"{self.title}", align='center', font=('Cardo', 37, 'bold'))
        self.color(self.color_score)  # Reset color for score and life

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def get_hit(self, dbt):
        self.goto(0, -19)
        self.write(f'Life Left: {self.life}', align='center', font=('Cardo', 79, 'normal'))
        dbt.goto((0, -271))

    def life_left(self):
        self.life -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -109)
        self.color(self.color_lose)  # Set the color for losing
        self.write("GAM€ - ?V€R ¡!¡", align='center', font=('Cardo', 79, 'bold'))

    def winner(self):
        self.goto(0, -109)
        self.color(self.color_win)  # Set the color for win
        self.write("Y?U WIN ¡!¡", align='center', font=('Cardo', 79, 'bold'))