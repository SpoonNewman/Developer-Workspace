from Controllers.Game_Manager import GameManager

def main():
    game_manager = GameManager()
    game_manager.start_game()
    
    while(True):
        game_manager.process_loop()
        

if "__main__" == __name__:
    main()

    