from Controllers.Game_Manager import GameManager

class Cursor(pygame.sprite.Sprite):
    def __init__(self, board):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill((0,255,0))
        self.text_height = 17
        self.text_width = 10
        self.rect = self.image.get_rect(topleft=(self.text_width, self.text_height))
        self.board = board
        self.text = ''
        self.cooldown = 0
        self.cooldowns = {'.': 12,
                        '[': 18,
                        ']': 18,
                        ' ': 5,
                        '\n': 30}

    def write(self, text):
        self.text = list(text)

    def update(self):
        if not self.cooldown and self.text:
            letter = self.text.pop(0)
            if letter == '\n':
                self.rect.move_ip((0, self.text_height))
                self.rect.x = self.text_width
            else:
                self.board.add(letter, self.rect.topleft)
                self.rect.move_ip((self.text_width, 0))
            self.cooldown = self.cooldowns.get(letter, 8)

        if self.cooldown:
            self.cooldown -= 1

class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill((13,13,13))
        self.image.set_colorkey((13,13,13))
        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont("monospace", 18)

    def add(self, letter, pos):
        s = self.font.render(letter, 1, (255, 255, 0))
        self.image.blit(s, pos)

def main():
    #Initializes the screen - Careful: all pygame commands must come after the init
    pygame.init()
    clock = pygame.time.Clock()

    #Sets mouse cursor visibility
    pygame.mouse.set_visible(False)
    #Sets the screen note: must be after pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    all_sprites = pygame.sprite.Group()
    board = Board()
    cursor = Cursor(board)
    all_sprites.add(cursor, board)

    text = """[i] Initializing ...
    [i] Entering ghost mode ...

    done ...

    """

    cursor.write(text)

    game_manager = GameManager()
    game_manager.start_game()
    # region Loop, this is where the update happens
    running = True
    while running:
        all_sprites.update() # update all sprite images
        screen.fill((0, 0, 0)) # set screen to block
        all_sprites.draw(screen) # draw images
        pygame.display.flip() # redraw everything
        clock.tick(60) # increase the clock tick
        

if "__main__" == __name__:
    main()

    