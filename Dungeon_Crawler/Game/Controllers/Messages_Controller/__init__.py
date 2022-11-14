from Controllers.Messages_Controller.standard_messages import StandardMessages
from Controllers.base_controller import BaseController
from time import sleep
from Controllers.Player_Registry_Actions import UniversalPlayerActions
from Controllers.UI_Controller import UIManager
from Controllers.Surfaces_Registry import SurfacesRegistry

class MessagesController(BaseController):
    default_typewriter_delay = None
    standard_messages_list = StandardMessages.messages
    show_action_delay = 0.3

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def show_available_actions (cls, event):
        display_text: str = """
Please select an action by entering a number:
============================================="""
        cls.display_message(message=display_text)
        sleep(1.25)
        
        for key, action in event.possible_actions.items():
            cls.display_message(message=f"{key} - {action}")
            sleep(cls.show_action_delay)
            print() # Skips to new line after printing the action
        
        for key, action in UniversalPlayerActions.actions.items():
            cls.display_message(message=f"{key} - {action}")
            sleep(cls.show_action_delay)
            print() # Skips to new line after printing the action

    @classmethod
    def show_item_actions(cls, event = None):
        display_text = """
\nSelect an action to perform with this item:
==========================================="""
        print(display_text)

        sleep(1.25)
        
        for key, action in event.possible_actions.items():
            cls.display_message(message=f"{key} - {action}")
            sleep(cls.show_action_delay)
            print() # Skips to new line after printing the action

    @classmethod
    def display_intro_message(cls):
        cls.display_message(message=cls.standard_messages_list["intro_message"])

    @classmethod
    def display_message(cls, event = None, message = None, surface_key = SurfacesRegistry.DESCRIPTION_SURFACE) -> None:
        msg: str = event.message if event and event.message else message
        typewriter_delay: int = event.typewriter_delay if event and hasattr(event, "typewriter_delay") else cls.default_typewriter_delay
        surface = event.surface_key if event and hasattr(event, "surface_key") else surface_key

        UIManager.display_message(message=msg, typewriter_delay=typewriter_delay, surface_key=surface)
        # cls.print_to_terminal(msg=message, delay=typewriter_delay)

    @classmethod
    def print_to_terminal(cls, msg, delay, end_character = ''):
        # msg += "\n"
        if msg:
            for char in msg:
                sleep(delay)
                print(char, end=end_character, flush=True)

    @classmethod
    def display_staggered_messages(cls, event):
        messages = event.messages
        for msg in messages:
            cls.display_message(message=msg)
            if (msg == "."):
                sleep(1)
            else:
                sleep(2)

            if msg == messages[-1]:
                print("\n")