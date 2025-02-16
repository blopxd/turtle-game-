from turtle import *
import random


class Aliens(Turtle):

    def __init__(self, position_, color_):
        super().__init__()

        self.hideturtle()
        self.shape('turtle')
        self.color(color_)
        self.penup()
        self.rt(90)
        self.goto(position_)
        self.active = True
        self.is_shooting = False
        self.is_moving = False
        self.fired_bullets = []  # Store fired bullets
        self.showturtle()
        self.ycor_orig = self.ycor()  # Store the original y-coordinate

    # Method to determine if the alien should shoot
    def should_shoot(self, dbt_x, dbt_y):
        # Alien can shoot if it's not already shooting and the target is not itself
        return not self.is_shooting and self.distance(dbt_x, dbt_y) > 0  # Adjust the distance as needed

    def update_shooting(self, dbt_x, dbt_y):
        # Randomly decide whether to shoot
        if self.should_shoot(dbt_x, dbt_y) and random.random() < 0.0005:  # Adjust the probability as needed
            self.is_shooting = True
            alien_fire = AliensFire(self, dbt_x)  # Pass both alien and dbt
            self.fired_bullets.append(alien_fire)  # Store the fired bullet
            return alien_fire
        return None

    # Add the reset_fire method for the alien's fire
    def reset_fire(self):
        self.is_moving = False
        self.hideturtle()
        self.goto(self.xcor(), -991)
        self.active = False


class AliensFire(Turtle):
    def __init__(self, alien, dbt):
        super().__init__()

        self.hideturtle()
        self.shape('square')
        self.color('#DC00E9', '#fff')
        self.shapesize(stretch_wid=0.7, stretch_len=0.15)
        self.penup()
        self.x_move = 0
        self.y_move = -5
        self.move_speed = 0.01
        self.is_moving = False
        self.alien = alien
        self.dbt = dbt  # Store the dbt object

        # Set the initial position of the fire to the alien's position
        self.goto(alien.xcor(), alien.ycor())

    def shoot(self):
        if not self.is_moving:
            self.is_moving = True
            self.showturtle()

    def move(self):
        if self.is_moving:
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)

            # Check if the fire is out of the screen
            if new_y < -300:  # Adjust this value to match your screen size
                self.aliens_reset_fire()

    def is_out_of_screen(self):
        return self.ycor() < -300  # Adjust this value to match your screen size

    def aliens_reset_fire(self):
        if self.ycor() < -300:
            self.is_moving = False
            self.hideturtle()
            self.goto(self.alien.xcor(), self.alien.ycor())

    def reset_fire(self):
        self.is_moving = False
        self.hideturtle()
        self.goto(991, -991)

