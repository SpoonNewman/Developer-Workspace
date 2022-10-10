from Controllers.Game_Manager import GameManager

def main():
    game_manager = GameManager()
    game_manager.start_game()
    
    while(True):
        current_actions = game_manager.messages_controller.show_available_actions(game_manager.player_controller, None)
        current_action_input = input("Make your selection:  ") # Show Prompt of things they can do
        game_manager.player_take_action(current_actions[current_action_input])

if "__main__" == __name__:
    main()

    