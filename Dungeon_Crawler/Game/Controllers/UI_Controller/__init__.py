from time import sleep
from Controllers.base_controller import BaseController
import pygame

WIDTH = 1280
HEIGHT = 720
GRAY = (197,194,197)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
MAX_LETTER_COUNT = 40

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
                cls.display_text(text=letter)
                sleep(typewriter_delay)

    @classmethod
    def display_text(cls, text: str):
        # if cls.rect.y + (cls.text_height*4) >= HEIGHT:
        #     Board.scroll_screen(change_y=(cls.text_height*4))
        
        if text == '\n' or cls.placement_on_line + cls.text_width >= Board.rect.right:
            cls.rect.move_ip((0, cls.text_height))
            cls.placement_on_line = cls.text_width
            cls.rect.x = cls.text_width
        else:
            Board.add(text, cls.rect.topleft)
            cls.rect.move_ip((cls.text_width, 0))
            cls.placement_on_line += cls.text_width
        UIManager.screen.fill((0, 0, 0)) # set screen to block
        UIManager.all_sprites.draw(UIManager.screen) # draw images
        pygame.display.flip() # redraw everything

    @classmethod
    def remove_text(cls, pos):
        Board.image.fill((13, 13, 13), pos)
        UIManager.screen.fill((0, 0, 0)) # set screen to block
        UIManager.all_sprites.draw(UIManager.screen) # draw images
        pygame.display.flip()

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

    @classmethod
    def scroll_screen(cls, change_y: int):
        text_screen = cls.image

        Board.image.fill((13, 13, 13))
        UIManager.screen.fill((0, 0, 0)) # set screen to block
        UIManager.all_sprites.draw(UIManager.screen) # draw images
        pygame.display.flip()

        cls.image.blit(text_screen, (0, -change_y))
        UIManager.screen.fill((0, 0, 0)) # set screen to block
        UIManager.all_sprites.draw(UIManager.screen) # draw images
        pygame.display.flip() # redraw everything



class TextInput():
    def __init__(self) -> None:
        pass

    @classmethod
    def get_input(cls):
        user_text = ''

        cls.input_rect = pygame.Rect(200, 200, 140, 32)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.unicode == "\r":
                    return user_text
        
                if event.type == pygame.KEYDOWN:
        
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
                        # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
                        if Cursor.rect.left >= 20:
                            Cursor.remove_text(pos=(Cursor.rect.left - Cursor.text_width, Cursor.rect.top, Cursor.rect.width, Cursor.rect.height))
                            Cursor.rect.move_ip((-Cursor.text_width, 0)) # Move cursor to the left
                        elif Cursor.rect.left == 10: #then move up by the text height and all the way to the right
                            Cursor.remove_text(pos=(Board.rect.right - (Cursor.text_width*2), Cursor.rect.top, Cursor.rect.width, Cursor.rect.height - Cursor.text_height))
                            Cursor.rect.move_ip((Board.rect.right - (Cursor.text_width*2), -Cursor.text_height)) # Move the line

                        UIManager.screen.fill((0, 0, 0)) # set screen to block
                        UIManager.all_sprites.draw(UIManager.screen) # draw images
                        pygame.display.flip() # redraw everything

                    elif len(user_text) < MAX_LETTER_COUNT:
                        user_text += event.unicode
                        Cursor.display_text(event.unicode)
