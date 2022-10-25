from Controllers.Game_Manager import GameManager

# WIDTH = 500
# HEIGHT = 500
# standard_delay = 0.05

# class Cursor(pygame.sprite.Sprite):
#     @classmethod
#     def __init__(cls) -> None:
#         cls.initialize()

#     @classmethod
#     def initialize(cls):
#         pygame.sprite.Sprite.__init__(cls)
#         cls.image = pygame.Surface((10, 20))
#         cls.image.fill((0,255,0))
#         cls.text_height = 17
#         cls.text_width = 10
#         cls.rect = cls.image.get_rect(topleft=(cls.text_width, cls.text_height))

#     @classmethod
#     def update(cls, text):
#         if text:
#             for index, letter in enumerate(text):
#                 if letter == '\n' or index == 50:
#                     cls.rect.move_ip((0, cls.text_height))
#                     cls.rect.x = cls.text_width
#                 else:
#                     Board.add(letter, cls.rect.topleft)
#                     cls.rect.move_ip((cls.text_width, 0))
#                 sleep(standard_delay)
#                 EntryPoint.screen.fill((0, 0, 0)) # set screen to block
#                 EntryPoint.all_sprites.draw(EntryPoint.screen) # draw images
#                 pygame.display.flip() # redraw everything
#             # self.cooldown = self.cooldowns.get(letter, 8)

# class Board(pygame.sprite.Sprite):
#     @classmethod
#     def __init__(cls) -> None:
#         cls.initialize()

#     @classmethod
#     def initialize(cls):
#         pygame.sprite.Sprite.__init__(cls)
#         cls.image = pygame.Surface((WIDTH, HEIGHT))
#         cls.image.fill((13,13,13))
#         cls.image.set_colorkey((13,13,13))
#         cls.rect = cls.image.get_rect()
#         cls.font = pygame.font.SysFont("monospace", 18)

#     @classmethod
#     def add(cls, letter, pos):
#         s = cls.font.render(letter, 1, (255, 255, 0))
#         cls.image.blit(s, pos)

class EntryPoint:
    @classmethod
    def main(cls):
        #Initializes the screen - Careful: all pygame commands must come after the init
    #     cls.intro_message = """
    # Welcome to the world of...DungeonCrawl.

    # You stand on the precipice of glory and greatness which await beyond the gates of this dungeon.

    # Move forward into darkness...if you dare
    # """
        # pygame.init()
        # pygame.mouse.set_visible(False)
        # cls.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # board = Board()
        # cursor = Cursor()
        # cls.all_sprites = pygame.sprite.Group()
        # cls.all_sprites.add(cursor, board)

        # cls.all_sprites.update(cls.intro_message) # update all sprite images

        # cls.screen.fill((0, 0, 0)) # set screen to block
        # cls.all_sprites.draw(cls.screen) # draw images
        # pygame.display.flip() # redraw everything
        # clock.tick(60) # increase the clock tick
            
        game_manager = GameManager()
        # game_manager.ui_sprites = cls.all_sprites
        game_manager.start_game()

if "__main__" == __name__:
    EntryPoint.main()

    