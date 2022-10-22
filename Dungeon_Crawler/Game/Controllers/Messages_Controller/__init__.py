from Controllers.Messages_Controller.standard_messages import StandardMessages
from Controllers.base_controller import BaseController
from time import sleep
from Controllers.Player_Registry_Actions import UniversalPlayerActions

from constants import GameConstants




class MessagesController(BaseController):
    default_typewriter_delay = None
    standard_messages_list = StandardMessages.messages

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def show_available_actions (cls, **kwargs):
        event = kwargs.get("event_object")

        display_text: str = """
Please select an action by entering a number:
=============================================
"""
        cls.display_message(message=display_text)
        # print("\n")
        sleep(1.25)
        
        for key, action in event.possible_actions.items():
            cls.display_message(message=f"{key} - {action}")
            sleep(0.8)
            print() # Skips to new line after printing the action
        
        print("\n")
        for key, action in UniversalPlayerActions.actions.items():
            cls.display_message(message=f"{key} - {action}")
            sleep(0.8)
            print() # Skips to new line after printing the action

    @classmethod
    def display_intro_message(cls):
        cls.display_message(message=cls.standard_messages_list["intro_message"])

    @classmethod
    def display_message(cls, **kwargs) -> None:
        event = kwargs.get("event_object")
        message: str = event.message if event and event.message else kwargs.get("message")
        typewriter_delay: int = event.typewriter_delay if event and hasattr(event, "typewriter_delay") else kwargs.get("typewriter_delay", cls.default_typewriter_delay)
        message_end_character: str = event.message_end_character if event and hasattr(event, "message_end_character") else kwargs.get("message_end_character", '')

        for char in message:
            sleep(typewriter_delay)
            print(char, end=message_end_character, flush=True)

    @classmethod
    def display_staggered_messages(cls, **kwargs):
        event = kwargs.get("event_object")
        messages = event.messages
        for msg in messages:
            cls.display_message(message=msg)
            if (msg == "."):
                sleep(1)
            else:
                sleep(2)

            if msg == messages[-1]:
                print("\n")