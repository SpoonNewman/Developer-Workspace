from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.game_events import OnKillSelfEvent, OnLocationChangeEvent, OnShowAvailableActionsEvent, OnMessageDisplayEvent
from Controllers.EventController import EventController


class EventsSecretShrineIntro():
    typewritter_delay = 0.05
    name = "Intro scene of investigating the hidden shrine"
    description = "You approach a book case in front of you and begin investigating the books resting in the book case. You run your finger over every book wiggling them around as you go until you land on a book that doesnt move left to right.\n\n"
    possible_actions = {
        "1": PlayerStandardActions.KILL_SELF.value,
        "2": PlayerStandardActions.INVESTIGATE.value,
        "3": PlayerStandardActions.MOVE_BACKWARD.value,
        "4": PlayerStandardActions.ACTIVATE_SWITCH.value
    }
    # cls.is_completed = None # OnStudyWallSwitchActivated

    @classmethod
    def __init__(cls) -> None:
        cls.next_scene = EventsSecretShrinePart2

    @classmethod
    def handle_event(cls):
        show_actions_evt = OnShowAvailableActionsEvent()
        show_actions_evt.possible_actions = cls.possible_actions
        EventController.broadcast_event(event_object=show_actions_evt)
        player_input = str(input("What do you choose?"))
        if cls.possible_actions[player_input] == PlayerStandardActions.KILL_SELF.value:
            kill_self_evt = OnKillSelfEvent()
            EventController.broadcast_event(event_object=kill_self_evt)
        elif cls.possible_actions[player_input] == PlayerStandardActions.INVESTIGATE.value:
            pass
        elif cls.possible_actions[player_input] == PlayerStandardActions.MOVE_BACKWARD.value:
            pass
        elif cls.possible_actions[player_input] == PlayerStandardActions.ACTIVATE_SWITCH.value:
            switch_description = "You grab the top of the book and begin pulling it towards you. There is a slight grinding noise as metal scrapes agaisnt metal. You hear a loud click and the book case begins to shift. The book case grinds against rails attatched to the wall behind it. Revealing a hole barely large enough for you to fit through. In front of you is the opening to a small crawl space barely wide enough for you to lay on your stomach and crawl through. You hear faint echos of noises from the other end of the tunnel."
            switch_evt = OnMessageDisplayEvent()
            switch_evt.message = switch_description
            setattr(switch_evt, "typewriter_delay", cls.typewritter_delay)
            EventController.broadcast_event(event_object=switch_evt)
        else:
            raise ValueError("That player action is not yet supported")

    @classmethod
    def trigger_next_scene(cls):
        cls.next_scene.handle_event()


class EventsSecretShrinePart2():
    name = "Intro scene of investigating the hidden shrine"
    description = "You study the wall and notice a hidden switch on the wall"
    possible_actions = [
        PlayerStandardActions.KILL_SELF,
        PlayerStandardActions.MOVE_FORWARD,
        PlayerStandardActions.MOVE_BACKWARD,
    ]
    # is_completed = None # OnStudyWallSwitchActivated

    @classmethod
    def __init__(cls) -> None:
        cls.next_scene = None

    @classmethod
    def handle_event():
        pass