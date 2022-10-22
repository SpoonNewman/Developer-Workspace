from Controllers.Player_Registry_Actions import PlayerStandardActions
from Controllers.game_events import OnKillSelfEvent, OnShowAvailableActionsEvent, OnMessageDisplayEvent
from Controllers.EventController import EventController
from Controllers.Environment_controller.Event_Sequence_Manager.Events.base_story_event import BaseStoryEvent
from Controllers.Item_Manager.Adventuring_Items import BookItem
from Controllers.game_events import OnItemPickupEvent
from Controllers.game_events import OnSfxPlayEvent
from Controllers.Player_Registry_Actions import UniversalPlayerActions


class EventsSecretShrineIntro(BaseStoryEvent):
    description = "You approach a book case in front of you and begin investigating the books resting in the book case. You run your finger over every book wiggling them around as you go until you land on a book that doesnt move left to right.\n\n"
    possible_actions = {
        "1": PlayerStandardActions.PICKUP_BOOK.value,
    }
    # cls.is_completed = None # OnStudyWallSwitchActivated

    @classmethod
    def __init__(cls) -> None:
        cls.next_scene = EventsSecretShrinePart2
        cls.book_item = BookItem()

    @classmethod
    def handle_event(cls):
        show_actions_evt = OnShowAvailableActionsEvent()
        show_actions_evt.possible_actions = cls.possible_actions
        EventController.broadcast_event(event_object=show_actions_evt)
        player_input = str(input("What do you choose?"))
        
        if cls.possible_actions[player_input] == PlayerStandardActions.PICKUP_BOOK.value:
            switch_description = "You grab the top of the book and begin pulling it towards you. There is a slight grinding noise as metal scrapes agaisnt metal. You hear a loud click and the book case begins to shift. The book case grinds against rails attatched to the wall behind it. Revealing a hole barely large enough for you to fit through."
            switch_evt = OnMessageDisplayEvent()
            switch_evt.message = switch_description
            EventController.broadcast_event(event_object=switch_evt)

            book_pickup_sound_evt = OnSfxPlayEvent()
            book_pickup_sound_evt.sfx_name = "book_page"
            EventController.broadcast_event(event_object=book_pickup_sound_evt)

            pickup_book_evt = OnItemPickupEvent()
            cls.book_item.name = "mouldering book"
            pickup_book_evt.item = cls.book_item
            EventController.broadcast_event(event_object=pickup_book_evt)
        elif player_input in UniversalPlayerActions.actions.keys():
            UniversalPlayerActions.take_action(action=player_input)
            cls.handle_event()
        else:
            raise ValueError("That player action is not yet supported")

    @classmethod
    def trigger_next_scene(cls):
        cls.next_scene.handle_event()


class EventsSecretShrinePart2():
    description = ["You lay on your stomach and begin shifting into the hole.", ".", ".", "You crawl for several minutes and finally see a faint light and movement at the end of the tunnel."]
    possible_actions = [
        PlayerStandardActions.MOVE_FORWARD,
        PlayerStandardActions.MOVE_BACKWARD,
    ]

    @classmethod
    def __init__(cls) -> None:
        cls.next_scene = None

    @classmethod
    def handle_event(cls):
        show_actions_evt = OnShowAvailableActionsEvent()
        show_actions_evt.possible_actions = cls.possible_actions
        EventController.broadcast_event(event_object=show_actions_evt)
        player_input = str(input("What do you choose?"))
        
        if cls.possible_actions[player_input] == PlayerStandardActions.KILL_SELF.value:
            kill_self_evt = OnKillSelfEvent()
            EventController.broadcast_event(event_object=kill_self_evt)
        elif cls.possible_actions[player_input] == PlayerStandardActions.MOVE_BACKWARD.value:
            pass
        elif cls.possible_actions[player_input] == PlayerStandardActions.MOVE_FORWARD.value:
            pass
        elif player_input in UniversalPlayerActions.actions.keys():
            UniversalPlayerActions.take_action(action=player_input)
            cls.handle_event()
        else:
            raise ValueError("That player action is not yet supported")