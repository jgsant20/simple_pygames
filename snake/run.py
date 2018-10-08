from snake.game import *

# Side-note
# -Due to how game.check_collisions() is implemented, snake can run into
#    self if that part isn't moving
# -Game could of implemented sprite groups
# -SO MANY CALLS TO GET INSTANCE ATTRIBUTES... make more local vars
# -snake.bodies_dir grows without limit
# -So many dirty fixes...
# -bug with head_body_loc not being where it is, dirty fix by making check sides smaller
# -The code, however, is surprisingly modular
# -I am able to edit parts of it without ruining the rest quite easily


class Settings:
    """Contains the settings for snake game"""

    def __init__(self):
        # Block sizes
        self.x_blocks = 20
        self.y_blocks = 20

        # Snake settings
        self.init_size = 4
        self.block_length = 40
        self.rgb_snake = 255, 255, 255
        self.snake_start_x = self.block_length * int(self.x_blocks/4)
        self.snake_start_y = self.block_length * int(self.y_blocks/2)

        # Apple settings
        self.apple_limit = 2
        self.rgb_apple = 150, 150, 150

        # Window settings
        self.res_x = self.x_blocks * self.block_length
        self.res_y = self.y_blocks * self.block_length
        self.rgb_bg = 30, 30, 30

        # Menu settings
        self.font = 'comicsansms'
        self.font_size = 100
        self.font_color = 200, 200, 200

        # Speed of game (period of frame)
        self.time_wait = 1/16

        # Amount of blocks needed to win
        self.win_condition = self.x_blocks * self.y_blocks

        # How big the snake grows per apple
        self.apple_growth = 1


class App:
    """Class to initialize the game"""

    def __init__(self, settings, screen, mode=0):
        self.running = True

        self.settings = settings
        self.screen = screen
        self.pause = Pause(self.settings, self.screen, self)
        self.snake = Snake(self.settings, self.screen)
        self.apple = Apple(self.settings, self.screen)
        self.game = Game(self, self.settings, self.snake, self.apple, self.pause, mode)

        self.sounda = pygame.mixer.Sound('menu_bgm.wav')

    def run(self):
        """Runs the app"""

        self.sounda.play()

        while self.running:

            # Logic
            self.event_listener()
            self.snake.movement()
            self.game.game_logic()

            # Render
            self.screen.fill(self.settings.rgb_bg)
            self.apple.draw_apple()
            self.snake.update()
            self.game.display_points()
            pygame.display.flip()

        self.on_exit()

    def event_listener(self):
        """Listens for key presses by user"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: self.pause.pause()
                if event.key == pygame.K_UP: self.snake.change_dir(1)
                if event.key == pygame.K_DOWN: self.snake.change_dir(2)
                if event.key == pygame.K_LEFT: self.snake.change_dir(3)
                if event.key == pygame.K_RIGHT: self.snake.change_dir(4)

    @staticmethod
    def on_exit():
        """Un-initialize all extraneous modules"""
        pygame.quit()


class Run:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.res_x, self.settings.res_y))

    def menu(self):
        """todo"""

    def run(self):
        app = App(self.settings, self.screen)
        app.run()


class Pause:
    """Class to include a menu and pausing"""

    def __init__(self, settings, screen, app):
        self.running = False
        self.settings = settings
        self.screen = screen
        self.app = app

        self.font = pygame.font.SysFont(self.settings.font, self.settings.font_size)
        self.text = self.font.render("Game is paused.", True, self.settings.font_color)

    def pause(self):
        self.running = True

        while self.running:
            self.event_listener()
            self.screen.blit(self.text, ((self.settings.res_x - self.text.get_width())//2,
                                         (self.settings.res_y - self.text.get_height())//4))
            pygame.display.flip()

    def event_listener(self):
        """Listens for key presses by user"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.app.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: self.running = False


if __name__ == "__main__":
    run = Run()
    run.run()
