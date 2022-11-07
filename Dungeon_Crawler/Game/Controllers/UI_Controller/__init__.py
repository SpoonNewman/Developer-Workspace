from enum import Enum
import random
import pygame
from time import sleep
from Controllers.base_controller import BaseController
from Controllers.Surfaces_Registry import SurfacesRegistry
from Controllers.EventController import EventController
from Controllers.game_events import OnDieEvent
from Controllers.Player_Controller import PlayerStatusCharacteristic

WIDTH = 1280
HEIGHT = 720
BLUE = (0,0,255)
GRAY = (197,194,197)
DARK_GRAY_1 = (160, 160, 160)
DARK_GRAY_2 = (69, 69, 69)
BLACK = (0,0,0)
LIGHT_BLACK_1 = (32, 33, 33)
LIGHT_BLACK_2 = (45, 45, 45)
GREEN = (0,255,0)
PINK = (255, 192, 203)
FUCHSIA = (255, 0, 255)
ORANGE = (255,69,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
MAX_LETTER_COUNT = 40

class subsurface_keys(Enum):
        HEALTH = "health"

class UIManager(BaseController):
    @classmethod
    def initialize(cls):
        pygame.init()
        pygame.mouse.set_visible(True)
        cls.window = pygame.display.set_mode((WIDTH, HEIGHT))
        # cls.window.fill(BLACK)
        
        cls.background = pygame.Surface(cls.window.get_size())
        cls.background_rect = cls.background.get_rect()
        
        cls.window.blit(cls.background, (0, 0))
        cls.border_width = 8
        
        cls.player_input_surf = PlayerInputSurface()
        cls.message_description_surf = MessagesDescriptionSurface()
        cls.message_side_panel_surf = MessagesSidePanelSurface()
        cls.text_cursor = TextCursor()
        cls.description_cursor = DescriptionCursor()
        
        cls.font = pygame.font.SysFont("monospace", 18)
        cls.rect = cls.window.get_rect()
        


        cls.all_sprites = pygame.sprite.Group()
        cls.all_sprites.add(
            cls.message_side_panel_surf,
            cls.player_input_surf,
            cls.message_description_surf,
            cls.description_cursor,
            cls.text_cursor
        )

        # pygame.draw.rect(cls.message_description_surf.image, LIGHT_BLACK_2, cls.message_description_surf.image.get_rect(), cls.border_width) # Border
        pygame.draw.rect(cls.player_input_surf.image, LIGHT_BLACK_2, cls.player_input_surf.image.get_rect(), cls.border_width)
        pygame.draw.rect(cls.message_side_panel_surf.image, LIGHT_BLACK_2, cls.message_side_panel_surf.image.get_rect(), 5)
        # pygame.draw.rect(cls.background, FUCHSIA, cls.background_rect, 5)

        cls.post_update()

    @classmethod
    def clear_input_field(cls):
        cls.player_input_surf.image.fill(cls.player_input_surf.surface_color)
        pygame.draw.rect(cls.player_input_surf.image, LIGHT_BLACK_2, cls.player_input_surf.image.get_rect(), cls.border_width)
        cls.text_cursor.rect.topleft=(cls.text_cursor.starting_left, cls.text_cursor.starting_top)

    @classmethod
    def display_message(cls, message: str, typewriter_delay: int, surface_key):
        for letter in message:
            cls.render_letter(letter=letter, surface_key=surface_key)
            cls.post_update()
            sleep(typewriter_delay)

    @classmethod
    def render_letter(cls, letter, surface_key):
        if surface_key is SurfacesRegistry.DESCRIPTION_SURFACE:
            cls.render_letter_to_description(letter)
        elif surface_key is SurfacesRegistry.PLAYER_INPUT_SURFACE:
            cls.render_letter_to_input(letter)

    @classmethod
    def render_letter_to_description(cls, letter):
        cls.description_cursor.move_cursor(letter)
        char = UIManager.font.render(letter, True, YELLOW, cls.message_description_surf.surface_color)
        char_position = (cls.description_cursor.rect.left - cls.message_description_surf.rect.left, cls.description_cursor.rect.top)

        cls.message_description_surf.image.blit(char, char_position)
        cls.all_sprites.draw(cls.background)
        
    @classmethod
    def render_letter_to_input(cls, letter):
        cls.text_cursor.move_cursor()
        char = UIManager.font.render(letter, True, WHITE, cls.player_input_surf.surface_color)
        char_position = (cls.text_cursor.rect.left - cls.text_cursor.text_width, cls.text_cursor.rect.top - cls.player_input_surf.rect.top)

        cls.player_input_surf.image.blit(char, char_position)
        cls.all_sprites.draw(cls.background)

    @classmethod
    def remove_text(cls, pos):
        cls.background.fill(BLACK, pos)
        cls.post_update()

    @classmethod
    def update_player_status(cls, event):
        if event:
            stat_type = event.stat_type
            stat_value = event.stat_value
            
            rendered_stat_value = UIManager.font.render(str(f"{stat_type}: {stat_value}"), True, WHITE, cls.message_side_panel_surf.surface_color)
            stat_surface = cls.message_side_panel_surf.subsurfaces[stat_type]
            stat_surface_position = (stat_surface.get_rect().left, stat_surface.get_rect().centery)
            stat_surface.blit(rendered_stat_value, stat_surface_position)

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
        cls.surface_color = BLACK
        cls.image.fill(cls.surface_color)
        cls.rect = UIManager.background.blit(cls.image, (0, HEIGHT - (HEIGHT/4))) # Draw onto the window

class MessagesDescriptionSurface(pygame.sprite.Sprite):
    @classmethod
    def __init__(cls):
        pygame.sprite.Sprite.__init__(cls)
        cls.size = (WIDTH - (WIDTH/4), HEIGHT - HEIGHT/4)
        cls.image = pygame.Surface(cls.size)
        cls.surface_color = BLACK
        cls.image.fill(cls.surface_color)
        cls.rect = UIManager.background.blit(cls.image, (WIDTH/4, 0)) # Draw onto the window
        cls.copy_image = None

    @classmethod
    def scroll_up(cls, scroll_height):
        cls.image.scroll(dy=scroll_height)
        cls.copy_image = cls.image.copy()
        cls.image.fill(cls.surface_color, cls.copy_image.get_rect())
        cls.image = cls.copy_image.copy()
        UIManager.background.blit(cls.image, (WIDTH/4, 0))

class MessagesSidePanelSurface(pygame.sprite.Sprite):
    @classmethod
    def __init__(cls):
        pygame.sprite.Sprite.__init__(cls)
        cls.size = (WIDTH/4, HEIGHT - HEIGHT/4)
        cls.image = pygame.Surface(cls.size)
        cls.surface_color = LIGHT_BLACK_1
        cls.image.fill(cls.surface_color)
        cls.rect = UIManager.background.blit(cls.image, (0, 0)) # Draw onto the window
        cls.text_width = 17
        cls.stats_buffer = 100
        cls.stats_margin_left = 100
        cls.stats_margin_top = 20
        cls.stats_margin_width = 145
        cls.stats_height = 30


        # Build subsurfaces
        cls.health_subsurf = cls.image.subsurface(cls.stats_margin_left, cls.stats_margin_top + cls.stats_buffer, cls.stats_margin_width, cls.stats_height)
        cls.mana_subsurf = cls.image.subsurface(cls.stats_margin_left, cls.stats_margin_top*3 + cls.stats_buffer, cls.stats_margin_width, cls.stats_height)
        cls.faith_subsurf = cls.image.subsurface(cls.stats_margin_left, cls.stats_margin_top*5 + cls.stats_buffer, cls.stats_margin_width, cls.stats_height)

        cls.subsurfaces = {
            PlayerStatusCharacteristic.HEALTH.name: cls.health_subsurf,
            PlayerStatusCharacteristic.MANA.name: cls.mana_subsurf,
            PlayerStatusCharacteristic.FAITH.name: cls.faith_subsurf
        }


class BaseCursor(pygame.sprite.Sprite):
    pass

class DescriptionCursor(pygame.sprite.Sprite):
    @classmethod
    def __init__(cls) -> None:
        pygame.sprite.Sprite.__init__(cls)
        cls.cursor_size = (10, 20)
        cls.image = pygame.Surface(cls.cursor_size)
        cls.surface_color = BLACK
        cls.image.fill(cls.surface_color)
        cls.text_height = 17
        cls.text_width = 10
        cls.placement_on_line = cls.text_width
        cls.margin_width = (cls.text_width*2)
        cls.starting_left = UIManager.message_description_surf.rect.left + cls.margin_width
        cls.starting_top = cls.text_height
        cls.rect = cls.image.get_rect(topleft=(cls.starting_left, cls.starting_top))
        cls.margin_bottom = (UIManager.message_description_surf.rect.bottom - (cls.text_height*2))
        cls.scroll_speed = cls.text_height*2

    @classmethod
    def move_cursor(cls, character):
        # Check if we hit the bottom margin, then scroll
        if cls.rect.top + (cls.text_height*2) >= cls.margin_bottom:
            UIManager.message_description_surf.scroll_up(scroll_height=-cls.scroll_speed)
            # UIManager.message_description_surf.image.scroll(0, cls.text_height*15)
            cls.rect.move_ip(0, -cls.scroll_speed)

        else:
            # Check if we need to move to next line
            if character == "\n" or cls.rect.left + (cls.text_width*2) >= WIDTH:
                # Move to next line
                cls.rect.left = cls.starting_left # Move to starting x, and incremented y
                cls.rect.top += cls.text_height
                cls.placement_on_line = cls.text_width
            
            # Check if we can print letter at spot
            elif cls.rect.left + cls.margin_width < WIDTH:
                    cls.rect.move_ip(cls.text_width, 0)
                    cls.placement_on_line += cls.text_width

class TextCursor(pygame.sprite.Sprite):
    @classmethod
    def __init__(cls) -> None:
        pygame.sprite.Sprite.__init__(cls)
        cls.cursor_size = (10, 20)
        cls.image = pygame.Surface(cls.cursor_size)
        cls.surface_color = WHITE
        cls.image.fill(cls.surface_color)
        cls.text_height = 17
        cls.text_width = 10
        cls.placement_on_line = cls.text_width
        cls.margin_width = (cls.text_width*2)
        cls.margin_top = (cls.text_height*1.2)
        cls.margin_bottom = (UIManager.player_input_surf.rect.bottom - (cls.text_height*2))
        cls.starting_left = UIManager.player_input_surf.rect.left + cls.margin_width
        cls.starting_top = UIManager.player_input_surf.rect.top + cls.margin_top
        cls.rect = cls.image.get_rect(topleft=(cls.starting_left, cls.starting_top))
        cls.scroll_speed = cls.text_height*2

    @classmethod
    def move_cursor(cls):
        if cls.rect.left + (cls.text_width*2) >= WIDTH:
            # Move to next line
            cls.rect.left = cls.starting_left # Move to starting x, and incremented y
            cls.rect.top += cls.text_height
            cls.placement_on_line = cls.text_width
        
        # Check if we can print letter at spot
        elif cls.rect.left + cls.margin_width < WIDTH:
            # Check if we're at the starting place or not
            if cls.rect.left == cls.text_width:
                cls.rect.topleft = (cls.starting_left, cls.text_height)
            else:
                cls.rect.move_ip(cls.text_width, 0)
                cls.placement_on_line += cls.text_width

class TextInput():
    @classmethod
    def __init__(cls) -> None:
        pass
        

    @classmethod
    def get_input(cls):
        cls.text_length_boundary = 140
        cls.text_height_boundary = 32
        user_text = ''

        cls.input_rect = pygame.Rect(TextCursor.rect.left - TextCursor.text_width, TextCursor.rect.top, cls.text_length_boundary, cls.text_height_boundary)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_evt = OnDieEvent()
                    EventController.broadcast(quit_evt)
                    
                if event.type == pygame.KEYDOWN and event.unicode == "\r":
                    return user_text
        
                if event.type == pygame.KEYDOWN:
        
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                        UIManager.remove_text(pos=(TextCursor.rect.left - TextCursor.text_width, TextCursor.rect.top, TextCursor.rect.width, TextCursor.rect.height))
                        TextCursor.rect.move_ip(-TextCursor.text_width, 0) # Move cursor to the left
                        TextCursor.placement_on_line -= TextCursor.text_width
                        UIManager.post_update()


                    elif len(user_text) < MAX_LETTER_COUNT:
                        user_text += event.unicode
                        UIManager.render_letter_to_input(letter=event.unicode)
                        UIManager.post_update()

