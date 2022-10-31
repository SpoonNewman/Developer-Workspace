import pygame
from time import sleep
from Controllers.base_controller import BaseController

WIDTH = 1280
HEIGHT = 720
GRAY = (197,194,197)
GRAY_OTHER = (160, 160, 160)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
MAX_LETTER_COUNT = 40

class UIManager(BaseController):
    @classmethod
    def initialize(cls):
        pygame.init()
        pygame.mouse.set_visible(True)
        cls.window = pygame.display.set_mode((WIDTH, HEIGHT))
        cls.window.fill(BLACK)
        cls.background = pygame.Surface(cls.window.get_size())
        cls.window.blit(cls.background, (0, 0))
        cls.font = pygame.font.SysFont(None, 50)
        cls.rect = cls.window.get_rect()
        

        cls.player_input_surf = PlayerInputSurface()
        cls.message_description_surf = MessagesDescriptionSurface()
        cls.message_side_panel_surf = MessagesSidePanelSurface()
        cls.text_cursor = Cursor()

        cls.all_sprites = pygame.sprite.Group()
        cls.all_sprites.add(cls.player_input_surf, cls.message_description_surf, cls.message_side_panel_surf, cls.text_cursor)

        
        # pygame.draw.rect(cls.window, BLUE, cls.window.get_rect(), 5) # Border

        cls.post_update()

    @classmethod
    def load_cursor(cls):
        PlayerInputSurface.image.blit(Cursor.image, (50, 50))


    @classmethod
    def display_message(cls, message: str, typewriter_delay: int):
        for letter in message:
            cls.render_letter(letter=letter)
            sleep(typewriter_delay)
            cls.post_update()

    @classmethod
    def render_letter(cls, letter):
        char = UIManager.font.render(letter, True, BLACK)
        # cls.window.blit(cls.background, (0, 0)) # blit background
        cls.window.blit(char, (0, 0))
        cls.all_sprites.draw(cls.window)
        

    @classmethod
    def post_update(cls):
        cls.all_sprites.update()
        cls.window.blit(cls.background, (0, 0))
        pygame.display.flip()

class PlayerInputSurface(pygame.sprite.Sprite):
    @classmethod
    def __init__(cls):
        pygame.sprite.Sprite.__init__(cls)
        cls.size = (WIDTH, HEIGHT/4)
        cls.image = pygame.Surface(cls.size)
        cls.image.fill(WHITE)
        cls.rect = cls.image.get_rect()
        UIManager.background.blit(cls.image, (0, HEIGHT - (HEIGHT/4))) # Draw onto the window

class MessagesDescriptionSurface(pygame.sprite.Sprite):
    @classmethod
    def __init__(cls):
        pygame.sprite.Sprite.__init__(cls)
        cls.size = (WIDTH - (WIDTH/4), HEIGHT - HEIGHT/4)
        cls.image = pygame.Surface(cls.size)
        cls.image.fill(GRAY)
        cls.rect = cls.image.get_rect()
        UIManager.background.blit(cls.image, (0 + (WIDTH/4), 0)) # Draw onto the window

class MessagesSidePanelSurface(pygame.sprite.Sprite):
    @classmethod
    def __init__(cls):
        pygame.sprite.Sprite.__init__(cls)
        cls.size = (WIDTH/4, HEIGHT - HEIGHT/4)
        cls.image = pygame.Surface(cls.size)
        cls.image.fill(GRAY_OTHER)
        cls.rect = cls.image.get_rect()
        UIManager.background.blit(cls.image, (0, 0)) # Draw onto the window


class Cursor(pygame.sprite.Sprite):
    @classmethod
    def __init__(cls) -> None:
        pygame.sprite.Sprite.__init__(cls)
        cls.cursor_size = (10, 20)
        cls.image = pygame.Surface(cls.cursor_size)
        cls.image.fill(BLACK)
        cls.text_height = 17
        cls.text_width = 10
        cls.placement_on_line = cls.text_width
        cls.rect = cls.image.get_rect()





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
                            Cursor.remove_text(pos=(PlayerInputSurface.rect.right - (Cursor.text_width*2), Cursor.rect.top, Cursor.rect.width, Cursor.rect.height - Cursor.text_height))
                            Cursor.rect.move_ip((PlayerInputSurface.rect.right - (Cursor.text_width*2), -Cursor.text_height)) # Move the line

                        UIManager.window.fill((0, 0, 0)) # set screen to block
                        UIManager.all_sprites.draw(UIManager.window) # draw images
                        UIManager.update_surfaces()
                        pygame.display.flip() # redraw everything

                    elif len(user_text) < MAX_LETTER_COUNT:
                        user_text += event.unicode
                        Cursor.display_text(event.unicode)
