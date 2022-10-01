from Controllers.Game_Manager import GameManager

def main():
    game_manager = GameManager()
    game_manager.start_game()
    
    while(True):
        game_manager.messages_controller.show_available_actions(game_manager.player_controller, None)
        current_action = input("Make your selection:  ") # Show Prompt of things they can do
        game_manager.player_take_action(current_action)

if "__main__" == __name__:
    main()