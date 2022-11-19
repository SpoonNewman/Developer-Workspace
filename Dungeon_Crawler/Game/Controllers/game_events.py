class EventTypes():
    def __init__(self) -> None:
        pass

    @classmethod
    def get_registered_events(cls) -> None:
        cls.ON_KILL_SELF = OnKillSelfEvent().__class__.__name__
        cls.ON_INVENTORY_DISPLAY = OnInventoryDisplay().__class__.__name__
        cls.ON_PRAY = OnPrayEvent().__class__.__name__
        cls.ON_DIE = OnDieEvent().__class__.__name__
        cls.ON_MESSAGE_DISPLAY = OnMessageDisplayEvent().__class__.__name__
        cls.ON_STAGGERED_MESSAGE_DISPLAY = OnStaggeredMessageDisplayEvent().__class__.__name__
        cls.ON_SHOW_AVAILABLE_ACTIONS = OnShowAvailableActionsEvent().__class__.__name__
        cls.ON_SHOW_ITEM_ACTIONS = OnShowItemActionsEvent().__class__.__name__
        cls.ON_INTRO_DISPLAY = OnIntroDisplayEvent().__class__.__name__
        cls.ON_GAME_START = OnGameStartEvent().__class__.__name__
        cls.ON_GAME_INITIALIZE = OnGameInitializeEvent().__class__.__name__
        cls.ON_PLAYER_ACTION = OnPlayerActionEvent().__class__.__name__
        cls.ON_ITEM_PICKUP = OnItemPickupEvent().__class__.__name__
        cls.ON_PLAYER_INVESTIGATE = OnPlayerInvestgateEvent().__class__.__name__
        cls.ON_LOCATION_CHANGE = OnLocationChangeEvent().__class__.__name__
        cls.ON_MUSIC_TRACK_PLAY = OnMusicTrackPlayEvent().__class__.__name__
        cls.ON_SFX_PLAY = OnSfxPlayEvent().__class__.__name__
        cls.ON_SFX_STOP = OnSfxStopEvent().__class__.__name__
        cls.ON_VOLUME_CHANGE = OnVolumeChangeEvent().__class__.__name__
        cls.ON_ITEM_DROP = OnItemDrop().__class__.__name__
        cls.ON_ITEM_EQUIP = OnItemEquip().__class__.__name__
        cls.ON_NEXT_EVENT_CHANGE = OnNextEventChange().__class__.__name__
        cls.ON_CURRENT_EVENT_CHANGE = OnCurrentEventChange().__class__.__name__
        cls.ON_RECORD_PLAYER_ACTION = OnRecordPlayerAction().__class__.__name__
        cls.ON_PLAYER_STAT_CHANGE = OnPlayerStatChange().__class__.__name__

        return [
            cls.ON_RECORD_PLAYER_ACTION,
            cls.ON_KILL_SELF,
            cls.ON_INVENTORY_DISPLAY,
            cls.ON_PRAY,
            cls.ON_DIE,
            cls.ON_MESSAGE_DISPLAY,
            cls.ON_STAGGERED_MESSAGE_DISPLAY,
            cls.ON_SHOW_AVAILABLE_ACTIONS,
            cls.ON_SHOW_ITEM_ACTIONS,
            cls.ON_INTRO_DISPLAY,
            cls.ON_GAME_START,
            cls.ON_GAME_INITIALIZE,
            cls.ON_PLAYER_ACTION,
            cls.ON_ITEM_PICKUP,
            cls.ON_PLAYER_INVESTIGATE,
            cls.ON_LOCATION_CHANGE,
            cls.ON_MUSIC_TRACK_PLAY,
            cls.ON_SFX_PLAY,
            cls.ON_SFX_STOP,
            cls.ON_ITEM_DROP,
            cls.ON_ITEM_EQUIP,
            cls.ON_VOLUME_CHANGE,
            cls.ON_ITEM_DROP,
            cls.ON_NEXT_EVENT_CHANGE,
            cls.ON_CURRENT_EVENT_CHANGE,
            cls.ON_PLAYER_STAT_CHANGE
        ]

class GameEvent():
    def __init__(self) -> None:
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

class OnShowItemActionsEvent(GameEvent):
    def __call__(self) -> None:
        self.possible_actions = None

class OnMessageDisplayEvent(GameEvent):
    def __init__(self) -> None:
        self.message = None
        self.surface_key = None
        # self.typewriter_delay = None


class OnKillSelfEvent(GameEvent):
    def __init__(self) -> None:
        self.kill_self_message = "\n\nA creeping hollowness begins to edge it's way into your thoughts drilling deeper to hollow out your hopes and dreams. In the span of heartbeats you lose all compulsion to resist the temptation to give up. You draw your blade and gaze longingly into the silver reflection of light in the metal. You watch as the blade thrusts itself into your throat, piercing cartalage and bone. You fall to the ground while the life blood leaks from your wound to form a puddle of hot blood."

class OnDieEvent(GameEvent):
    def __init__(self) -> None:
        self.dead_message = ["\n\nYou wonder if the stories are true, that a soul's death is welcomed by angel song. ", "As your lifeforce seeps away the only sound that greets you is the laughter of Dark Gods", ".", ".", ".", "\n\nGame Over"]

class OnStaggeredMessageDisplayEvent(GameEvent):
    def __init__(self, messages: list[str] = None) -> None:
        self.messages = messages

class OnIntroDisplayEvent(GameEvent):
    def __init__(self) -> None:
        pass

class OnPlayerActionEvent(GameEvent):
    def __init__(self) -> None:
        pass

class OnItemPickupEvent(GameEvent):
    def __init__(self, item = None) -> None:
        self.item = item

class OnPlayerInvestgateEvent(GameEvent):
    def __init__(self) -> None:
        pass

class OnMusicTrackPlayEvent(GameEvent):
    def __init__(self, track_name: str = None) -> None:
        self.track_name = track_name

class OnSfxPlayEvent(GameEvent):
    def __init__(self) -> None:
        self.sfx_name = None
        self.sfx_loops = 0

class OnSfxStopEvent(GameEvent):
    def __init__(self) -> None:
        self.sfx_name = None

class OnVolumeChangeEvent(GameEvent):
    def __init__(self) -> None:
        self.volume_value = None

class OnInventoryDisplay(GameEvent):
    def __init__(self) -> None:
        super().__init__()

class OnPrayEvent(GameEvent):
    def __init__(self) -> None:
        super().__init__()

class OnItemDrop(GameEvent):
    def __init__(self) -> None:
        super().__init__()
        self.item = None
        
class OnItemEquip(GameEvent):
    def __init__(self) -> None:
        super().__init__()
        self.item = None
        self.slot = None

class OnGameInitializeEvent(GameEvent):
    def __init__(self) -> None:
        super().__init__()

class OnNextEventChange(GameEvent):
    def __init__(self) -> None:
        super().__init__()
        self.next_event = None

class OnCurrentEventChange(GameEvent):
    def __init__(self) -> None:
        super().__init__()
        self.current_event = None

class OnRecordPlayerAction(GameEvent):
    def __init__(self) -> None:
        super().__init__()
        self.action = None
        self.scene = None

class OnPlayerStatChange(GameEvent):
    def __init__(self) -> None:
        super().__init__()
        self.stat_type = None
        self.stat_value = None
