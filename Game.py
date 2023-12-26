import pygame
from pygame.locals import *

class Game:
    """The generic game class."""
    def __init__(self):
        """Game initialization."""
        pygame.init()
        self.window = pygame.display.set_mode((600, 800))
        pygame.display.set_caption('OpPyTetris')

Game()