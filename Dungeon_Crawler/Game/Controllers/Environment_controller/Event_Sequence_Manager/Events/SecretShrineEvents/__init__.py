from Controllers.Environment_controller.Event_Sequence_Manager.base_play_event import BasePlayEvent
from Controllers.Player_Registry_Actions import PlayerStandardActions


class EventsSecretShrineIntro(BasePlayEvent):
    def __init__(self) -> None:
        super().__init__()

        self.name = "Intro scene of investigating the hidden shrine"
        self.description = "You approach a book case in front of you and begin investigating the books resting in the book case. You run your finger over every book wiggling them around as you go until you land on a book that doesnt move left to right. You grab the top of the book and begin pulling it towards you. There is a slight grinding noise as metal scrapes agaisnt metal. You hear a loud click and the book case begins to shift. The book case grinds against rails attatched to the wall behind it. Revealing a hole barely large enough for you to fit through. In front of you is the opening to a small crawl space barely wide enough for you to lay on your stomach and crawl through. You hear faint echos of noises from the other end of the tunnel."
        # self.is_completed = None # OnStudyWallSwitchActivated
        self.possible_actions = self.get_possible_actions()
        self.next_scene = EventsSecretShrinePart2()

    def handle_event(self):
        # on_display_possible_actions(self.get_possible_actions())
        # on_player_input
        pass

    def trigger_next_scene(self):
        self.next_scene.handle_event()

    def get_possible_actions(self):
        return [
            PlayerStandardActions.KILL_SELF,
            PlayerStandardActions.INVESTIGATE,
            PlayerStandardActions.MOVE_BACKWARD,
            PlayerStandardActions.ACTIVATE_SWITCH
        ]


class EventsSecretShrinePart2(BasePlayEvent):
    def __init__(self) -> None:
        super().__init__()

        self.name = "Intro scene of investigating the hidden shrine"
        self.description = "You study the wall and notice a hidden switch on the wall"
        # self.is_completed = None # OnStudyWallSwitchActivated
        self.possible_actions = self.get_possible_actions()
        self.next_scene = None

    def get_possible_actions(self):
        return [
            PlayerStandardActions.KILL_SELF,
            PlayerStandardActions.MOVE_FORWARD,
            PlayerStandardActions.MOVE_BACKWARD,
        ]