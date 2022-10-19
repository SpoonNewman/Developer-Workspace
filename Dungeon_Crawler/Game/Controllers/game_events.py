class EventTypes():
    def __init__(self) -> None:
        pass

    @classmethod
    def get_registered_events(cls) -> None:
        cls.ON_KILL_SELF = OnKillSelfEvent().__class__.__name__
        cls.ON_DIE = OnDieEvent().__class__.__name__
        cls.ON_MESSAGE_DISPLAY = OnMessageDisplayEvent().__class__.__name__
        cls.ON_STAGGERED_MESSAGE_DISPLAY = OnStaggeredMessageDisplayEvent().__class__.__name__
        cls.ON_SHOW_AVAILABLE_ACTIONS = OnShowAvailableActionsEvent().__class__.__name__
        cls.ON_INTRO_DISPLAY = OnIntroDisplayEvent().__class__.__name__
        cls.ON_GAME_START = OnGameStartEvent().__class__.__name__
        cls.ON_PLAYER_ACTION = OnPlayerActionEvent().__class__.__name__
        cls.ON_ITEM_PICKUP = OnItemPickupEvent().__class__.__name__
        cls.ON_PLAYER_INVESTIGATE = OnPlayerInvestgateEvent().__class__.__name__
        cls.ON_LOCATION_CHANGE = OnLocationChangeEvent().__class__.__name__

        return [
            cls.ON_KILL_SELF,
            cls.ON_DIE,
            cls.ON_MESSAGE_DISPLAY,
            cls.ON_STAGGERED_MESSAGE_DISPLAY,
            cls.ON_SHOW_AVAILABLE_ACTIONS,
            cls.ON_INTRO_DISPLAY,
            cls.ON_GAME_START,
            cls.ON_PLAYER_ACTION,
            cls.ON_ITEM_PICKUP,
            cls.ON_PLAYER_INVESTIGATE,
            cls.ON_LOCATION_CHANGE
        ]

class GameEvent():
    pass

class OnGameStartEvent(GameEvent):
    def __init__(self) -> None:
        pass

class OnLocationChangeEvent(GameEvent):
    def __init__(self, location = None) -> None:
        self.location = location

class OnShowAvailableActionsEvent(GameEvent):
    def __init__(self, possible_actions = {}) -> None:
        self.possible_actions = possible_actions

class OnMessageDisplayEvent(GameEvent):
    def __init__(self, message: str = None) -> None:
        self.message = message

class OnKillSelfEvent(GameEvent):
    def __init__(self) -> None:
        self.kill_self_message = "\n\nA creeping hollowness begins to edge it's way into your thoughts drilling deeper to hollow out your hopes and dreams. In the span of heartbeats you lose all compulsion to resist the temptation to give up. You draw your blade and gaze longingly into the silver reflection of light in the metal. You watch as the blade thrusts itself into your throat, piercing cartalage and bone. You fall to the ground while the life blood leaks from your wound to form a puddle of hot blood."

class OnDieEvent(GameEvent):
    def __init__(self) -> None:
        self.dead_message = ["\n\nYou wonder if the stories are true, that a soul's death is welcomed by angel song. ", "As your lifeforce seeps away the only sound that greets you is the laughter of Dark Gods", ".", ".", ".", "\n\nGame Over"]

class OnStaggeredMessageDisplayEvent(GameEvent):
    def __init__(self) -> None:
        pass

class OnIntroDisplayEvent(GameEvent):
    def __init__(self) -> None:
        pass

class OnPlayerActionEvent(GameEvent):
    def __init__(self) -> None:
        pass

class OnItemPickupEvent(GameEvent):
    def __init__(self) -> None:
        pass

class OnPlayerInvestgateEvent(GameEvent):
    def __init__(self) -> None:
        pass