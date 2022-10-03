from Controllers.Event_Types import EventTypes
from Controllers.Messages_Controller.messages_list import MessagesList
from Controllers.Player_Controller import PlayerController
from time import sleep



class MessagesController ():
    action_message_display_delay = 0.03
    def __init__(self) -> None:
        self.standard_messages_list = MessagesList.standard_messages

    def show_available_actions (self, player_object, room_object):
        display_text: str = """
Please select an action by entering a number:
=================
        """

        actions_texts = {}
        for index, action in enumerate(self.get_available_actions(player_object, room_object)):
            actions_texts[str(index + 1)] = action
            # actions_texts["1"] = "Kill Self"
            # actions_texts["2"] = "Move Forward"

        for key, item in actions_texts.items():
            self.display_message(f"{key} - {item}", typewriter_delay=self.action_message_display_delay, message_end_character='')
            sleep(0.4)
            print() # Skips to new line after printing the action
            
        return actions_texts
        
        
    def get_available_actions(self, player_object: PlayerController, room_object) -> list:
        return player_object.get_available_actions()

    def display_intro_message(self):
        self.display_message(message=self.standard_messages_list["intro_message"])

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