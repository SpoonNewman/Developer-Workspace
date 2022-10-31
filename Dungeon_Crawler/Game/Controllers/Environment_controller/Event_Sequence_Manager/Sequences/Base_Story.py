from Controllers.UI_Controller import TextInput
from Controllers.game_events import OnMessageDisplayEvent
from Controllers.EventController import EventController

class BaseStory():
    @classmethod
    def get_player_input(cls):
        evt = OnMessageDisplayEvent()
        evt.message = "\nWhat do you choose?  "
        evt.typewriter_display = 0
        EventController.broadcast_event(evt)

        # Do an event loop and grab the input, then return it
        while True:
            input_obj = TextInput()
            user_input = input_obj.get_input()
            del input_obj
            return user_input