from Controllers.Game_Manager import GameManager

class EntryPoint:
    @classmethod
    def main(cls):
        game_manager = GameManager()
        game_manager.start_game()

if "__main__" == __name__:
    EntryPoint.main()

    