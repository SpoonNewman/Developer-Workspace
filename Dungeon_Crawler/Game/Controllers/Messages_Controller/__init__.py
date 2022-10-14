from Controllers.Messages_Controller.messages_list import MessagesList
from Controllers.Player_Controller import PlayerController
from Controllers.base_controller import BaseController
from time import sleep




class MessagesController(BaseController):
    action_message_display_delay = 0.03
    standard_messages_list = MessagesList.standard_messages

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def show_available_actions (cls, possible_actions):
        display_text: str = """
Please select an action by entering a number:
=============================================
"""
        cls.display_message(display_text, typewriter_delay=0.008)
        # print("\n")
        sleep(1.25)
        
        for key, action in possible_actions.items():
            cls.display_message(f"{key} - {action}", typewriter_delay=cls.action_message_display_delay)
            sleep(0.8)
            print() # Skips to new line after printing the action
        
    @classmethod
    def get_available_actions(cls, player_object: PlayerController, room_object) -> list:
        return player_object.get_available_actions(room=room_object)

    @classmethod
    def display_intro_message(cls):
        cls.display_message(message=cls.standard_messages_list["intro_message"])

    @classmethod
    def display_message(cls, message: str, typewriter_delay: int = 0.1, message_end_character: str = '') -> None:
        for char in message:
            sleep(typewriter_delay)
            print(char, end=message_end_character, flush=True)

    @classmethod
    def display_room_messages(cls, current_room_messages: list[str]):
        for msg in current_room_messages:
            cls.display_message(msg)
            if (msg == "."):
                sleep(1)
            else:
                sleep(2)

            if msg == current_room_messages[-1]:
                print("\n")