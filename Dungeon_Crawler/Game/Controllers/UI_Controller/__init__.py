from time import sleep
from Controllers.base_controller import BaseController
import pygame

WIDTH = 1280
HEIGHT = 720
# standard_delay = 0.05

class UIManager(BaseController):
    @classmethod
    def initialize(cls):
        pygame.init()
        pygame.mouse.set_visible(False)
        cls.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        cls.board = Board()
        cls.cursor = Cursor()
        cls.all_sprites = pygame.sprite.Group()
        cls.all_sprites.add(cls.cursor, cls.board)

    @classmethod
    def update_sprites(cls, message: str, typewriter_delay: int):
        cls.all_sprites.update(message, typewriter_delay=typewriter_delay)

class Cursor(pygame.sprite.Sprite):
    @classmethod
    def __init__(cls) -> None:
        cls.initialize()

    @classmethod
    def initialize(cls):
        pygame.sprite.Sprite.__init__(cls)
        cls.image = pygame.Surface((10, 20))
        cls.image.fill((0,255,0))
        cls.text_height = 17
        cls.text_width = 10
        cls.rect = cls.image.get_rect(topleft=(cls.text_width, cls.text_height))
        cls.placement_on_line = cls.text_width

    @classmethod
    def update(cls, text: str, typewriter_delay: int):
        if text:
            for letter in text:
                if letter == '\n' or cls.placement_on_line + cls.text_width >= Board.rect.right:
                    cls.rect.move_ip((0, cls.text_height))
                    cls.placement_on_line = cls.text_width
                    cls.rect.x = cls.text_width
                else:
                    Board.add(letter, cls.rect.topleft)
                    cls.rect.move_ip((cls.text_width, 0))
                    cls.placement_on_line += cls.text_width
                sleep(typewriter_delay)
                UIManager.screen.fill((0, 0, 0)) # set screen to block
                UIManager.all_sprites.draw(UIManager.screen) # draw images
                pygame.display.flip() # redraw everything

class Board(pygame.sprite.Sprite):
    @classmethod
    def __init__(cls) -> None:
        cls.initialize()

    @classmethod
    def initialize(cls):
        pygame.sprite.Sprite.__init__(cls)
        cls.image = pygame.Surface((WIDTH, HEIGHT))
        cls.image.fill((13,13,13))
        cls.image.set_colorkey((13,13,13))
        cls.rect = cls.image.get_rect()
        cls.font = pygame.font.SysFont("monospace", 18)

    @classmethod
    def add(cls, letter, pos):
        s = cls.font.render(letter, 1, (255, 255, 0))
        cls.image.blit(s, pos)
