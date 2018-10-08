import time
import random
import pygame

from collections import deque


class Game:
    """Class containing all game elements of snake"""

    check_apple_collision_flag = False

    def __init__(self, app, settings, snake, apple, pause, mode=0):
        """Using mode enables different game modes"""
        self.app = app
        self.settings = settings
        self.snake = snake
        self.apple = apple
        self.mode = mode
        self.snake_head_loc = (0, 0)

        self.font = pygame.font.SysFont(self.settings.font, self.settings.font_size // 2)
        self.text = self.font.render("Game is paused.", True, self.settings.font_color)

        # Change settings according to easy modo
        if self.mode == 1:
            print("Easy mode settings\n"
                  "settings.win_condition /= 8")
            self.settings.win_condition /= 8

    def game_logic(self):
        """Runs all methods in game class"""
        # Location of head snake
        self.snake_head_loc = self.snake.bodies_loc[0]

        self.check_sides()
        self.check_collisions()
        self.check_apple_collision()
        self.check_win()

        if self.mode == 1:
            self.easy_modo()

        if self.mode == 2:
            self.hard_mode()

        if self.mode == 3:
            self.experimentation()

        self.check_apple_collision_flag = False

    def display_points(self):
        self.text = self.font.render(str(len(self.snake.bodies_loc)), True, self.settings.font_color)
        self.app.screen.blit(self.text, (10, 10))

    def check_sides(self):
        """Exits out of app if snake collides with sides"""
        if self.snake_head_loc[1] < 0 or self.snake_head_loc[1] > self.settings.res_y - self.settings.block_length or\
                self.snake_head_loc[0] < 0 or self.snake_head_loc[0] > self.settings.res_x - self.settings.block_length:
            self.app.running = False
            print("Rip.")

    def check_collisions(self):
        """Checks if snake collides with itself"""
        # Compares the snake's head position with the (x, y) of the other bodies
        # Only those that are moving to account for growth from apple
        for body_num in range(1, len(self.snake.bodies)):
            if self.snake_head_loc == (self.snake.bodies[body_num].x, self.snake.bodies[body_num].y) and\
                    self.snake.bodies_dir[body_num] != 0:
                self.app.running = False
                print("Rip.")
                break

    def check_apple_collision(self):
        """Checks if collided with apple, if so then add another apple and make snake bigger"""

        # Iterates through each apple location and compares it with the snake head's location
        for i in range(len(self.apple.loc)):
            if self.snake_head_loc == self.apple.loc[i]:
                self.apple.new_apple(i, 1, self.snake.bodies_loc)
                self.snake.add_body(self.settings.apple_growth)
                self.check_apple_collision_flag = True
                break

    def check_win(self):
        """Checks if user has won"""
        # Checks if the amount of snake bodies is bigger than the win condition
        if len(self.snake.bodies_loc) >= self.settings.win_condition:
            self.app.running = False
            print("You win.")

    def easy_modo(self):
        """Three lives cuz why not"""
        if self.check_apple_collision_flag:
            self.settings.apple_growth += 1

    def hard_mode(self):
        """Enables acceleration"""
        # todo

    def experimentation(self):
        """?????"""
        # todo


class Snake:
    """Class to emulate the snake and it's movements"""

    #   1 - Up      2 - Down
    #   3 - Left    4 - Right

    # Initial size of snake's body
    append_flag = False

    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        # bodies and bodies_dir contains list of bodies and list of their directions, respectively
        # bodies_dir starts at 0 so snake doesn't move initially
        self.bodies = []
        self.bodies_dir = []
        self.bodies_loc = deque()

        # Snake's body
        for i in range(self.settings.init_size):
            new_body = pygame.Rect(self.settings.snake_start_x,
                                   self.settings.snake_start_y -
                                   self.settings.block_length, self.settings.block_length,
                                   self.settings.block_length)
            self.bodies.append(new_body)
            self.bodies_loc.append((self.settings.snake_start_x, self.settings.snake_start_y))
            self.bodies_dir.append(0)

    def update(self):
        """Draws the body onto the screen"""
        for body_num in range(len(self.bodies)):
            pygame.draw.rect(self.screen, self.settings.rgb_snake, self.bodies[body_num])
        self.append_flag = False

    def movement(self):
        """Moves snake according to direction given"""
        time.sleep(self.settings.time_wait)
        self.append_dir(self.bodies_dir[0])
        for body_num in range(len(self.bodies)):
            if self.bodies_dir[body_num] == 1:
                self.bodies[body_num].y -= self.settings.block_length
            if self.bodies_dir[body_num] == 2:
                self.bodies[body_num].y += self.settings.block_length
            if self.bodies_dir[body_num] == 3:
                self.bodies[body_num].x -= self.settings.block_length
            if self.bodies_dir[body_num] == 4:
                self.bodies[body_num].x += self.settings.block_length
            self.store_loc(body_num)

    def store_loc(self, n):
        """Store location of n'th body into its respective position in bodies_loc"""
        self.bodies_loc[n] = (self.bodies[n].x, self.bodies[n].y)

    def append_dir(self, dir):
        """Will append bodies_dir if not yet appended"""
        # The snake copies the direction's of previous bodies through a second list
        # This function ensures the appending of that list
        if not self.append_flag:
            self.bodies_dir.insert(0, dir)
        self.append_flag = True

    def change_dir(self, dir):
        """Changes the direction of the snake"""
        if dir == 1 and self.bodies_dir[0] != 2:
            self.append_dir(1)
        if dir == 2 and self.bodies_dir[0] != 1:
            self.append_dir(2)
        if dir == 3 and self.bodies_dir[0] != 4:
            self.append_dir(3)
        if dir == 4 and self.bodies_dir[0] != 3:
            self.append_dir(4)

    def add_body(self, x=1):
        """Adds x amount of bodies"""
        for i in range(x):
            bodies_length = len(self.bodies)
            new_body = pygame.Rect(self.bodies[bodies_length-1].x, self.bodies[bodies_length-1].y,
                                   self.settings.block_length, self.settings.block_length)
            self.bodies_dir.append(0)
            self.bodies.append(new_body)
            self.bodies_loc.append((new_body.x, new_body.y))

            self.bodies_dir[bodies_length - 1] = 0


class Apple:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        # List to store all the apples
        self.apples = []
        self.loc = []

        self.generate_apples(self.settings.apple_limit)

    def draw_apple(self):
        """Draws apple onto screen"""
        for apple in self.apples:
            pygame.draw.rect(self.screen, self.settings.rgb_apple, apple)

    def generate_apples(self, apple_num, snake_bodies_loc = (0, 0)):
        """Generates apples"""

        # Checks if apple num at limit
        if len(self.apples) == self.settings.apple_limit:
            return

        for i in range(apple_num):
            # subtract by 1 because rand in inclusive
            loc_x = random.randint(0, self.settings.x_blocks - 1) * self.settings.block_length
            loc_y = random.randint(0, self.settings.y_blocks - 1) * self.settings.block_length

            # Iterates through until block lands on an empty tile
            while (loc_x, loc_y) in self.loc or (loc_x, loc_y) in snake_bodies_loc:
                loc_x = random.randint(0, self.settings.x_blocks - 1) * self.settings.block_length
                loc_y = random.randint(0, self.settings.y_blocks - 1) * self.settings.block_length

            self.loc.append((loc_x, loc_y))
            new_apple = pygame.Rect(loc_x, loc_y, self.settings.block_length, self.settings.block_length)
            self.apples.append(new_apple)

    def new_apple(self, i, x, snake_bodies_loc = (0, 0)):
        """Replaces i'th apple, spawns by x amount"""
        del self.apples[i]
        del self.loc[i]
        self.generate_apples(x, snake_bodies_loc)
