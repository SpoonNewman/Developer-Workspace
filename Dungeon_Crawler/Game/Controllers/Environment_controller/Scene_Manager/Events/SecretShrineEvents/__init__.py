from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.game_events import OnKillSelfEvent, OnShowAvailableActionsEvent
from Controllers.EventController import EventController
from Controllers.Environment_controller.Scene_Manager.Events.Base_Scene_Event import BaseSceneEvent
from Controllers.Player_Registry_Actions import UniversalPlayerActions


class EventsSecretShrinePart1(BaseSceneEvent):
    description = ["You approach a book case in front of you and begin investigating the books resting in the book case.", " You run your finger over every book wiggling them around as you go until you land on a book that doesnt move left to right.\n\n"]

    @classmethod
    def __init__(cls) -> None:
        cls.next_scene = EventsSecretShrinePart2

class EventsSecretShrinePart2(BaseSceneEvent):
    description = ["You grab the top of the book and begin pulling it towards you.", " There is a slight grinding noise as metal scrapes agaisnt metal.", "You hear a loud click and the book case begins to shift.", "The book case grinds against rails attatched to the wall behind it.", "Revealing a hole barely large enough for you to fit through.\n\n"]

    @classmethod
    def __init__(cls) -> None:
        cls.next_scene = EventsSecretShrinePart3


class EventsSecretShrinePart3(BaseSceneEvent):
    description = ["You lay on your stomach and begin shifting into the hole.", ".", ".", "You crawl for several minutes and finally see a faint light and movement at the end of the tunnel."]

    @classmethod
    def __init__(cls) -> None:
        cls.next_scene = None