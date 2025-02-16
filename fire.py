from turtle import Turtle


class Fire(Turtle):

    def __init__(self, dbt, is_player_fire=True):
        super().__init__()

        self.hideturtle()
        self.shape('circle')
        self.color('#784AC3')
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.penup()
        self.x_move = 0
        self.y_move = 5
        self.move_speed = 0.001
        self.is_moving = False
        self.active = True
        self.dbt = dbt
        self.is_player_fire = is_player_fire  # Add an attribute to track if it's a player's fire

        # Set the initial position of the fire to the turtle's position
        self.goto(dbt.xcor(), dbt.ycor())

    def shoot(self):
        if not self.is_moving:
            x, y = self.dbt.pos()
            self.goto(x, y)
            self.is_moving = True
            self.showturtle()

    def move(self):
        if self.is_moving:
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)

            # Check if the fire is out of the screen
            if new_y > self.dbt.screen.window_height() / 2:
                self.reset_fire()

    def reset_fire(self):
        self.is_moving = False
        self.hideturtle()
        self.goto(self.dbt.xcor(), self.dbt.ycor())

    def is_out_of_screen(self):
        return self.ycor() > self.dbt.screen.window_height() / 2
