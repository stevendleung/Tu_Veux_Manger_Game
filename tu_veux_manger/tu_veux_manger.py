"""
Charlie Collect treats Moving Down
"""

import random
import arcade
import os
import operator

#Local Import to pull in high scores
import manger_hi_scores as mhs

# ---Global Constants---
CHARLIE_SCALING = .15
CALINE_SCALING = .15
SCALING_TREAT = 0.2
SCALING_CATCHER = 0.5
TREAT_COUNT_L1 = 30
TREAT_COUNT_L2 = 40
TREAT_COUNT_L3 = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tu Veux Manger?"

#Movement speed of character
MOVEMENT_SPEED = 8

# These numbers represent "states" that the game can be in.
INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
BEFORE_LEVEL_2 = 2
BEFORE_LEVEL_3 = 3
GAME_RUNNING = 4
GAME_OVER = 5
GAME_WON = 6

class Player(arcade.Sprite):
    """
    This class represents the dog on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """
    def update(self):
        #Update characters position based on user input from mouse or keyboard
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class FallingL1(arcade.Sprite):
    """
    This class represents the treats and catchers on our screen in Level 1. It is a child class of
    the arcade library's "Sprite" class.
    """
    def reset_pos(self):
        # Reset the falling object to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the falling object down the screen
        self.center_y -= 2
        # See if the falling object has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

class FallingL2(arcade.Sprite):
    """
    This class represents the treats and catchers on our screen in Level 2. It is a child class of
    the arcade library's "Sprite" class.
    """
    def reset_pos(self):
        # Reset the falling object to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the falling object down the screen
        self.center_y -= 3
        # See if the falling object has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

class FallingL3(arcade.Sprite):
    """
    This class represents the treats and catchers on our screen in Level 3. It is a child class of
    the arcade library's "Sprite" class.
    """
    def reset_pos(self):
        # Reset the falling object to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the falling object down the screen
        self.center_y -= 4
        # See if the falling object has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

class MyGame(arcade.Window):
    """
    This class is our game engine. It is a child class of the arcade library's
    "Window" class.
    """

    def __init__(self):
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. This is useful if we plan to run game
        # from outside local directories
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Store character value given by user from input call
        self.record_character('manger_hi_scores.py')

        # Start 'state' will be showing the title page.
        self.current_state = INSTRUCTIONS_PAGE_0

        # Variables that will hold player, treats and catcher lists
        self.player_sprite_list = None
        self.treat_sprite_list = None
        self.catcher_sprite_list = None

        # Set up the character as either Charlie or Caline based on user input
        if self.character == 'Charlie' or self.character == 'charlie':
            self.player_sprite = arcade.Sprite("game_images/Charlie.png", CHARLIE_SCALING)
        if self.character == 'Caline' or self.character == 'caline':
            self.player_sprite = arcade.Sprite("game_images/Caline5.png", CALINE_SCALING)
        self.score = 0

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

        # Store the images for intro pages and final page in lists that we will
        # call on later
        self.instructions = []
        texture = arcade.load_texture("game_images/tu veux manger intro screen 1.png")
        self.instructions.append(texture)

        texture = arcade.load_texture("game_images/tu veux manger intro screen 2.png")
        self.instructions.append(texture)

        self.final = []
        texture = arcade.load_texture("game_images/charlie_caline_win.png")
        self.final.append(texture)

    def level_1(self):
        # Method to initiate level 1
        for i in range(TREAT_COUNT_L1):
            # Create the number of treats specified in global variable
            treat = FallingL1("game_images/dog-treat3.png", SCALING_TREAT)

            # Position the treat
            treat.center_x = random.randrange(SCREEN_WIDTH)
            treat.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT * 6)

            # Add the treat to the treat list
            self.treat_sprite_list.append(treat)

        for i in range(10):
            # Create the dog catchers
            catcher = FallingL1("game_images/dog_catcher2.png", SCALING_CATCHER)

            # Position the catcher
            catcher.center_x = random.randrange(SCREEN_WIDTH)
            catcher.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT * 5)

            # Add the catcher to the lists
            self.catcher_sprite_list.append(catcher)

    def level_2(self):
        # Method to initiate level 2
        for i in range(TREAT_COUNT_L2):
            # Create the number of treats specified in global variable
            treat = FallingL2("game_images/dog-treat3.png", SCALING_TREAT)

            # Position the treat
            treat.center_x = random.randrange(SCREEN_WIDTH)
            treat.center_y = random.randrange(SCREEN_HEIGHT + 100, SCREEN_HEIGHT * 8)

            # Add the treat to the lists
            self.treat_sprite_list.append(treat)

        for i in range(9):
            # Create the dog catchers
            catcher = FallingL2("game_images/dog_catcher2.png", SCALING_CATCHER)

            # Position the catcher
            catcher.center_x = random.randrange(SCREEN_WIDTH)
            catcher.center_y = random.randrange(SCREEN_HEIGHT + 100, SCREEN_HEIGHT * 6)

            # Add the catcher to the lists
            self.catcher_sprite_list.append(catcher)

    def level_3(self):
        # Method to initiate level 23
        for i in range(TREAT_COUNT_L3):
            # Create the number of treats specified in global variable
            treat = FallingL3("game_images/dog-treat3.png", SCALING_TREAT)

            # Position the treat
            treat.center_x = random.randrange(SCREEN_WIDTH)
            treat.center_y = random.randrange(SCREEN_HEIGHT + 200, SCREEN_HEIGHT * 10)

            # Add the treat to the lists
            self.treat_sprite_list.append(treat)

        for i in range(8):
            # Create the dogcatchers
            catcher = FallingL3("game_images/dog_catcher2.png", SCALING_CATCHER)

            # Position the catcher
            catcher.center_x = random.randrange(SCREEN_WIDTH)
            catcher.center_y = random.randrange(SCREEN_HEIGHT + 200, SCREEN_HEIGHT * 8)

            # Add the catcher to the lists
            self.catcher_sprite_list.append(catcher)

    def record_character(self, scores):
        #Pull the character specified by user
        with open(scores, 'rt') as s:
            self.character = mhs.character

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.treat_sprite_list = arcade.SpriteList()
        self.catcher_sprite_list = arcade.SpriteList()

        # If game is starting for first time
        if not self.score:
            self.score = 0
            self.level = 1

        # Set up the player
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)

        # Initiate level based on current state of game
        if self.current_state == INSTRUCTIONS_PAGE_1:
            self.level_1()
        elif self.current_state == BEFORE_LEVEL_2:
            self.level_2()
        elif self.current_state == BEFORE_LEVEL_3:
            self.level_3()
        else:
            self.level_1()

    def draw_instructions_page(self, page_number):
        """
        Draw an intro page. Load the page as an image.
        """
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)

    def draw_between_levels(self, level_number):
        """
        Draw pre-level message across the screen.
        """

        output = "Level {} Complete!".format(level_number - 1)
        arcade.draw_text(output, 158, 400, arcade.color.WHITE, 54)

        output = "Click to Start Level {}".format(level_number)
        arcade.draw_text(output, 270, 300, arcade.color.WHITE, 24)

    def draw_game_over(self):
        """
        Draw "Game Over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        self.print_scores(mhs.hi_scores_list)

        output = "Click Anywhere to Restart"
        arcade.draw_text(output, 240, 70, arcade.color.WHITE, 24)

        self.level = 1
        self.score = 0

    def draw_win_game(self):
        """
        Draw "Congratulations!" across the screen.
        """

        page_texture = self.final[0]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)

        self.print_scores(mhs.hi_scores_list)

        output = "Click Anywhere to Play Again"
        arcade.draw_text(output, 200, 70, arcade.color.BLUE, 24)

        self.level = 1
        self.score = 0

    def print_scores(self, scores):
        # Print the high scores. Implemented on game over and game won screens
        output = "High Scores"
        arcade.draw_text(output, 300, 310, arcade.color.BLUE, 34)

        rank = 1
        y_pos = 270

        # Only print out top 5 scores
        for score in sorted(scores, key = lambda x: x[1], reverse = True):
            if rank == 6:
                break
            output = "{}. {}: {}".format(rank, score[0], score[1])
            arcade.draw_text(output, 320, y_pos, arcade.color.BLUE, 24)
            rank += 1
            y_pos -= 30

    def add_score(self, scores):
        # Add score of user from gameplay. Method called on game over and game won
        # screens
        with open(scores, 'wt') as s:
            mhs.hi_scores_list[len(mhs.hi_scores_list)-1].append(self.score)
            s.write("hi_scores_list = {}".format(mhs.hi_scores_list))
        with open('manger_hi_scores.py', 'at') as s:
            s.write("\ncharacter = '{}'".format(self.character))

    def duplicate_user(self, scores):
        # Add additional element on high scores list in case user plays again
        with open(scores, 'wt') as s:
            mhs.hi_scores_list.append([mhs.hi_scores_list[len(mhs.hi_scores_list)-1][0]])
            s.write("hi_scores_list = {}".format(mhs.hi_scores_list))
        with open('manger_hi_scores.py', 'at') as s:
            s.write("\ncharacter = '{}'".format(self.character))

    def draw_game(self):
        """
        Draw all the sprites, along with the score. Run when game is running.
        """
        arcade.start_render()
        self.treat_sprite_list.draw()
        self.player_sprite_list.draw()
        self.catcher_sprite_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        output = f"Level: {self.level}"
        arcade.draw_text(output, 10, 35, arcade.color.WHITE, 15)

    def on_draw(self):
        """ Draw everything based on state of the game"""
        # This command has to happen before we start drawing game
        arcade.start_render()

        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instructions_page(0)

        elif self.current_state == INSTRUCTIONS_PAGE_1:
            self.draw_instructions_page(1)

        elif self.current_state == BEFORE_LEVEL_2:
            self.draw_between_levels(2)

        elif self.current_state == BEFORE_LEVEL_3:
            self.draw_between_levels(3)

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        elif self.current_state == GAME_WON:
            self.draw_win_game()

        else:
            self.draw_game()
            self.draw_game_over()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change states as needed.
        if self.current_state == INSTRUCTIONS_PAGE_0:
            # Next page of instructions.
            self.current_state = INSTRUCTIONS_PAGE_1
        elif self.current_state == INSTRUCTIONS_PAGE_1:
            # Start the game at level 1
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == BEFORE_LEVEL_2:
            # Start the game at level 2
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == BEFORE_LEVEL_3:
            # Start the game at level 3
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            # Restart the game.
            self.setup()
            self.duplicate_user('manger_hi_scores.py')
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_WON:
            # Restart the game.
            self.setup()
            self.duplicate_user('manger_hi_scores.py')
            self.current_state = GAME_RUNNING

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def update(self, delta_time):
        """ Movement and game logic """

        # Only move and do things if the game is running.
        if self.current_state == GAME_RUNNING:

            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0

            if self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif self.down_pressed and not self.up_pressed:
                self.player_sprite.change_y = -MOVEMENT_SPEED
            if self.left_pressed and not self.right_pressed:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif self.right_pressed and not self.left_pressed:
                self.player_sprite.change_x = MOVEMENT_SPEED

            # Call update to move the player
            self.player_sprite_list.update()
            # Call update on the treats and catchers
            self.treat_sprite_list.update()
            self.catcher_sprite_list.update()

            # Generate a list of all treats that collided with the player.
            hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.treat_sprite_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for treat in hit_list:
                treat.kill()

                self.score += 1

            # Check for collision between player and dogcatcher
            catcher_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                     self.catcher_sprite_list)

            # If player hits a catcher, add score to high scores and change states
            # to game over
            if catcher_hit_list:
                self.add_score('manger_hi_scores.py')
                self.current_state = GAME_OVER

            # See if we should go to level 2
            if len(self.treat_sprite_list) == 0 and self.level == 1 and \
            self.score == TREAT_COUNT_L1:
                self.catcher_sprite_list = arcade.SpriteList()
                self.level += 1
                self.current_state = BEFORE_LEVEL_2

            # See if we should go to level 3
            elif len(self.treat_sprite_list) == 0 and self.level == 2 and \
            self.score == TREAT_COUNT_L1 + TREAT_COUNT_L2:
                self.catcher_sprite_list = arcade.SpriteList()
                self.level += 1
                self.current_state = BEFORE_LEVEL_3

            # See if player has won the game. If so, add score to high scores list
            # and enter won game state
            elif len(self.treat_sprite_list) == 0 and self.level == 3 and \
            self.score == TREAT_COUNT_L1 + TREAT_COUNT_L2 + TREAT_COUNT_L3:
                self.catcher_sprite_list = arcade.SpriteList()
                self.add_score('manger_hi_scores.py')
                self.current_state = GAME_WON

def main():
    #Function to take user input and run game
    while True:
        #Take a username 8 characters or less
        username = input("Who is playing?: ")
        if len(username) >= 8:
            print("Please enter a name 8 characters or less.")
        else:
            break
    while True:
        #Ask user which character they would like to play with
        active_character = input("Would you like to play as Charlie or Caline?: ")
        if active_character not in ["Charlie", "charlie", "Caline", "caline"]:
            print("Please enter Charlie or Caline.")
        else:
            break
    #Ensure that hi scores list only has elements in form [username, score]
    mhs.hi_scores_list = [item for item in mhs.hi_scores_list if not len(item) == 1]
    mhs.hi_scores_list.append([username])
    #Log character choice in external module to pull in later
    mhs.character = active_character

    #Run game
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
