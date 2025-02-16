from turtle import Screen
from dbt import Dbt
from fire import Fire
from alien import Aliens, AliensFire
from scoreboard import Scoreboard
from PIL import Image
import time

# Create the screen
screen = Screen()

# Define the desired screen size (e.g., 991x595)
screen_width = 991
screen_height = 595

# Set the background color (optional, you can adjust the color)
screen.bgcolor("black")

# Open the background image using Pillow
image = Image.open("space.jpg")

# Resize the image to fit the screen size
image = image.resize((screen_width, screen_height))

# Save the resized image as a temporary file (optional)
image.save("resized_space.png")

# Set the background image using the resized image
screen.bgpic("resized_space.png")

# Set up the screen
screen.setup(width=screen_width, height=screen_height)
screen.title('? Space Invaders ?')
screen.tracer(0)

# Set up the turtle class with an initial position within the visible screen area
dbt = Dbt((0, -271))

# Create a fire turtle
fire = Fire(dbt)  # Create the Fire object without passing dbt initially

user = Scoreboard()

# Create an empty list to store fire instances
fires = []

# Create an empty list to store alien instances
aliens = []

# Create an empty list to store active aliens
active_aliens = []


# Function to shoot fire from the dbt turtle
def shoot_fire():
    new_fire = Fire(dbt, is_player_fire=True)  # Create a new Fire instance
    new_fire.shoot()
    fires.append(new_fire)  # Add the fire instance to the list


# Function to remove an alien from the active aliens list
def remove_alien(alien_):
    if alien_ in active_aliens:
        active_aliens.remove(alien_)
        alien_.hideturtle()


# Create aliens and add them to the list
green_alien_start_x = -389  # Starting x-coordinate for the first green alien
for _ in range(19):
    alien = Aliens(position_=(green_alien_start_x, 145), color_='green')
    aliens.append(alien)
    active_aliens.append(alien)
    green_alien_start_x += 40

yellow_alien_start_x = -369  # Starting x-coordinate for the first yellow alien
for _ in range(18):
    alien = Aliens(position_=(yellow_alien_start_x, 125), color_='yellow')
    aliens.append(alien)
    active_aliens.append(alien)
    yellow_alien_start_x += 40

red_alien_start_x = -349  # Starting x-coordinate for the first red alien
for _ in range(17):
    alien = Aliens(position_=(red_alien_start_x, 100), color_='red')
    aliens.append(alien)
    active_aliens.append(alien)
    red_alien_start_x += 40

# Listen for key presses
screen.listen()
screen.onkey(dbt.go_right, 'Right')
screen.onkey(dbt.go_left, 'Left')
# Bind the spacer key to shoot_fire function
screen.onkey(shoot_fire, 'space')

game_is_on = True

# Add a variable to keep track of the last collision time
last_collision_time = 0

# Initialize alien_direction outside the game loop
alien_direction = "right"
alien_speed = 1

# Game loop
while game_is_on:
    time.sleep(fire.move_speed)
    screen.update()

    # Check if any aliens should shoot and create fires accordingly
    for alien in active_aliens:
        alien_fire = alien.update_shooting(dbt.xcor(), dbt.ycor())
        if alien_fire is not None:
            new_alien_fire = AliensFire(alien_fire, dbt)
            new_alien_fire.shoot()
            fires.append(new_alien_fire)

    for fire in fires:
        fire.move()

    # Remove fires that go out of the screen
    fires = [fire for fire in fires if not fire.is_out_of_screen()]

    # Move all the aliens simultaneously
    for alien in active_aliens:
        if alien.active:
            if alien_direction == "right":
                alien.goto(alien.xcor() + alien_speed, alien.ycor())
            else:
                alien.goto(alien.xcor() - alien_speed, alien.ycor())

        # Check if any alien reaches the left or right edge of the screen
    if any(alien.xcor() >= screen_width / 2 - 20 or alien.xcor() <= -screen_width / 2 + 20 for alien in active_aliens):
        # Move all the aliens down when they reach the edge
        for alien in active_aliens:
            alien.goto(alien.xcor(), alien.ycor() - 1.9)

        # Change the direction here, outside the loop
        if alien_direction == "right":
            alien_direction = "left"
        else:
            alien_direction = "right"

    # Handle collisions and destroy fires and aliens
    collisions = []  # A list to store the collisions

    # Check for collisions between player-fired bullets and aliens
    for fire in fires:
        if isinstance(fire, Fire):
            for alien in active_aliens:
                if alien.active and fire.distance(alien) < 9:
                    collisions.append((fire, alien))  # Store the collision
                    user.point()  # Add this line to update the score
                    print(f'Score: {user.score}')
                    if user.score == 54:
                        user.winner()
                        game_is_on = False

    # Check for collisions between alien-fired bullets and DBT
    for fire in fires:
        if not isinstance(fire, Fire) and dbt.distance(fire) < 9:
            collisions.append((fire, dbt))  # Store the collision

    # Check for collisions between player-fired bullets and alien-fired bullets
    for fire1 in fires:
        if isinstance(fire1, Fire) and fire1.is_player_fire:  # Exclude alien-fired bullets
            for fire2 in fires:
                if not isinstance(fire2, Fire) and fire1.distance(fire2) < 9:
                    collisions.append((fire1, fire2))  # Store the collision

    # Handle the collisions
    for fire1, fire2 in collisions:
        if isinstance(fire1, Fire):
            fire1.reset_fire()  # Reset the first fire
            fire2.reset_fire()  # Reset the second fire
        else:
            if isinstance(fire2, Fire) and fire2.is_player_fire:  # Check if fire2 is the player's fire
                fire2.reset_fire()  # Reset the player's fire
            user.life_left()
            user.get_hit(dbt)  # Process the player getting hit
            print(f'DBT Lives: {user.life}')
            if user.life <= 0:
                user.game_over()
                game_is_on = False

# Keep the window open
screen.exitonclick()