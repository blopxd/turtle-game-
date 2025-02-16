from turtle import Turtle


class Dbt(Turtle):
    def __init__(self, position):
        super().__init__()

        self.hideturtle()
        self.shape('turtle')
        self.color('#784AC3')
        self.penup()
        self.left(90)
        self.life = 5
        self.goto(position)
        self.showturtle()

    # Define the functions for moving the turtle
    def go_right(self):
        new_x = self.xcor() + 9
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 9
        self.goto(new_x, self.ycor())
