from enum import Enum
import pygame_menu
import pygame
from time import sleep
from Controllers.base_controller import BaseController
from Controllers.Surfaces_Registry import SurfacesRegistry
from Controllers.EventController import EventController
from Controllers.game_events import OnDieEvent, OnVolumeChangeEvent
from Controllers.Player_Controller import PlayerStatusCharacteristic, PlayerController
from Controllers.Music_Controller import MusicController


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
        cls.font = pygame.font.SysFont("monospace", 18)
        cls.rect = cls.window.get_rect()
        
        cls.player_input_surf = PlayerInputSurface()
        cls.message_description_surf = MessagesDescriptionSurface()
        cls.message_side_panel_surf = MessagesSidePanelSurface()
        cls.text_cursor = TextCursor()
        cls.description_cursor = DescriptionCursor()
        cls.opening_menu = OpeningMenu()
        cls.settings_menu = SettingsMenu()
        
        


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

    # region
    @classmethod
    def display_settings(cls):
        cls.settings_menu.menu.draw(cls.background)
        cls.settings_menu.menu.update(pygame.event.get())
        cls.post_update()

    @classmethod
    def display_opening_menu(cls):
        cls.opening_menu.menu.draw(cls.background)
        cls.opening_menu.menu.update(pygame.event.get())
        cls.post_update()
    
    @classmethod
    def toggle_settings_menu(cls):
        cls.settings_menu.menu.toggle()

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

    # endregion

class BaseMenu():
    @classmethod
    def close_menu(cls):
        cls.menu.reset(100)
        if cls.menu.is_enabled():
            cls.menu.close()
        UIManager.all_sprites.draw(UIManager.background)
        UIManager.post_update()

class OpeningMenu():
    @classmethod
    def __init__(cls):
        cls.theme = pygame_menu.themes.THEME_DARK
        cls.menu_height = 400
        cls.menu_width = 600
        cls.title = "Dungeon Crawl"

        cls.menu = pygame_menu.Menu(
            enabled=False,
            height=cls.menu_height,
            onclose=pygame_menu.events.RESET,
            theme=cls.theme,
            title=cls.title,
            width=cls.menu_width
        )

        cls.settings_menu = SettingsMenu(
            use_back_button=True,
            use_return_to_game_button=False
        ).menu

        cls.menu.add.button("Start", cls.start_game)
        cls.menu.add.button(cls.settings_menu.get_title(), cls.settings_menu)
        cls.menu.add.button("Exit", exit)

    @classmethod
    def start_game(cls):
        cls.menu.close()
        cls.menu.disable()
        UIManager.post_update()

class SettingsMenu(BaseMenu):
    @classmethod
    def __init__(cls, use_back_button=False, use_return_to_game_button=True):
        cls.theme = pygame_menu.themes.THEME_DARK
        cls.menu_height = 400
        cls.menu_width = 600
        cls.title = "Settings"
        cls.exit_game_button = None
        cls.back_button = None
        cls.return_to_game_button = None

        cls.menu = pygame_menu.Menu(
            enabled=False,
            height=cls.menu_height,
            onclose=cls.close_menu,
            theme=cls.theme,
            title=cls.title,
            width=cls.menu_width
        )

        cls.audio_menu = AudioMenu().menu
        cls.gameplay_menu = GameplayMenu().menu
        cls.video_menu = VideoMenu().menu

        if use_return_to_game_button:
            cls.return_to_game_button = cls.menu.add.button("Return to Game", cls.close_menu)

        cls.menu.add.button(cls.audio_menu.get_title(), cls.audio_menu)
        cls.menu.add.button(cls.video_menu.get_title(), cls.video_menu)
        cls.menu.add.button(cls.gameplay_menu.get_title(), cls.gameplay_menu)
        if use_back_button:
            cls.back_button = cls.menu.add.button("Back", pygame_menu.events.BACK)
        else:
            cls.exit_game_button = cls.menu.add.button("Quit Game", exit)
    

class AudioMenu():
    @classmethod
    def __init__(cls):
        cls.theme = pygame_menu.themes.THEME_DARK
        cls.menu_height = SettingsMenu.menu_height
        cls.menu_width = SettingsMenu.menu_width
        cls.title = "Audio"
        cls.default_volume: float = MusicController.get_music_volume()

        cls.menu = pygame_menu.Menu(
            height=cls.menu_height, 
            theme=cls.theme,
            title=cls.title,
            width=cls.menu_width
        )

        cls.volume_slider = cls.menu.add.range_slider(
            "Volume", cls.default_volume * 100, (0, 100), 1, cls.change_volume
        )

        cls.menu.add.button("Back", pygame_menu.events.BACK)

    @classmethod
    def change_volume(cls, volume):
        evt = OnVolumeChangeEvent()
        evt.volume_value = volume
        EventController.broadcast_event(event_object=evt)

class GameplayMenu():
    @classmethod
    def __init__(cls):
        cls.theme = pygame_menu.themes.THEME_DARK
        cls.menu_height = SettingsMenu.menu_height
        cls.menu_width = SettingsMenu.menu_width
        cls.title = "Gameplay"

        cls.menu = pygame_menu.Menu(
            height=cls.menu_height, 
            theme=cls.theme,
            title=cls.title,
            width=cls.menu_width
        )

        cls.menu.add.button("Back", pygame_menu.events.BACK)

class VideoMenu():
    @classmethod
    def __init__(cls):
        cls.theme = pygame_menu.themes.THEME_DARK
        cls.menu_height = SettingsMenu.menu_height
        cls.menu_width = SettingsMenu.menu_width
        cls.title = "Video"

        cls.menu = pygame_menu.Menu(
            height=cls.menu_height, 
            theme=cls.theme,
            title=cls.title,
            width=cls.menu_width
        )

        cls.menu.add.button("Back", pygame_menu.events.BACK)

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

class InventoryTable():
    @classmethod
    def __init__(cls, menu):
        cls.table_name = "inventory-window-table"
        cls.table = menu.add.table(table_id=cls.table_name, margin=(20, 20))
        cls.table.default_cell_padding = 10
        cls.default_row_background_color = BLACK
        cls.table.default_cell_align = pygame_menu.locals.ALIGN_CENTER
        cls.table.add_row(["NAME", "DESCRIPTION", "WEIGHT"], cell_font=UIManager.font)
        cls.current_rows = []

    @classmethod
    def clear_rows(cls):
        for index, row in enumerate(cls.current_rows):
            cls.table.remove_row(row)
            cls.current_rows.pop(index)

class InventoryWindow(BaseMenu):
    @classmethod
    def __init__(cls):
        cls.theme = pygame_menu.themes.THEME_DARK
        cls.menu_height = 600
        cls.menu_width = 1200
        cls.title = "Inventory"
        cls.exit_game_button = None
        cls.back_button = None
        cls.return_to_game_button = None

        cls.menu = pygame_menu.Menu(
            enabled=False,
            height=cls.menu_height,
            onclose=cls.close_menu,
            theme=cls.theme,
            title=cls.title,
            width=cls.menu_width
        )

        cls.inventory_table = InventoryTable(menu=cls.menu)

    @classmethod
    def close_menu(cls):
        if len(cls.inventory_table.current_rows) > 0:
            cls.inventory_table.clear_rows()
        super().close_menu()

    @classmethod
    def set_inventory_items(cls, items):
        for item in items:
            row_frame = cls.inventory_table.table.add_row(cells=[item.name, item.description, str(item.inv_socket_weight)], cell_font=UIManager.font)
            cls.inventory_table.current_rows.append(row_frame)

class SidePanelButton(pygame.sprite.Sprite):
    def __init__(self, button_text: str, position, debug_color = DARK_GRAY_1) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.size = (75, 25)
        self.image = pygame.Surface(self.size)
        self.surface_color = DARK_GRAY_2
        self.border_color = GRAY
        self.border_width = 4
        self.image.fill(self.surface_color)
        self.text = UIManager.font.render(button_text, True, WHITE, self.surface_color)
        self.text_position = (5, 5)
        self.image.blit(self.text, self.text_position)
        self.rect = MessagesSidePanelSurface.image.blit(self.image, position) # Draw onto the window
        self.text_width = 17

        # pygame.draw.rect(self.image, self.border_color, self.rect, self.border_width) # Border
        

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

        cls.inventory_window = InventoryWindow()
        cls.inventory_window_menu = cls.inventory_window.menu

        cls.show_inventory_btn = SidePanelButton(button_text="INV", position=(10, 15))
        cls.show_character_btn = SidePanelButton(button_text="CHAR", position=(100, 15))
        cls.show_help_btn = SidePanelButton(button_text="HELP", position=(190, 15))

    def display_inventory_window(cls):
        cls.inventory_window_menu.draw(UIManager.background)
        cls.inventory_window_menu.update(pygame.event.get())
        UIManager.post_update()
    
    def toggle_inventory_menu(cls):
        cls.inventory_window_menu.toggle()


# region Cursors
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
                    EventController.broadcast_event(quit_evt)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_click_position = pygame.mouse.get_pos()
                    # is click position in the side panel
                    # activate the side panel click
                    if mouse_click_position[0] >= UIManager.message_side_panel_surf.show_inventory_btn.rect.left and mouse_click_position[0] <= UIManager.message_side_panel_surf.show_inventory_btn.rect.right and mouse_click_position[1] >= UIManager.message_side_panel_surf.show_inventory_btn.rect.top and mouse_click_position[1] <= UIManager.message_side_panel_surf.show_inventory_btn.rect.bottom:
                        UIManager.message_side_panel_surf.toggle_inventory_menu()
                        UIManager.message_side_panel_surf.inventory_window.set_inventory_items(PlayerController.get_inventory())
                        while True:
                            if UIManager.message_side_panel_surf.inventory_window_menu.is_enabled():
                                UIManager.message_side_panel_surf.display_inventory_window()
                            else:
                                break
                        
                    
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

                    elif event.key == pygame.K_ESCAPE:
                        UIManager.toggle_settings_menu()
                        while True:
                            if UIManager.settings_menu.menu.is_enabled():
                                UIManager.display_settings()
                            else:
                                break

                    elif len(user_text) < MAX_LETTER_COUNT:
                        user_text += event.unicode
                        UIManager.render_letter_to_input(letter=event.unicode)
                        UIManager.post_update()

            # if UIManager.settings_menu.menu.is_enabled():
            #     UIManager.display_settings()
        # endregion
                
