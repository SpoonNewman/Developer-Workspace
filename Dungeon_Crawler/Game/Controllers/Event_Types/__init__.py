from enum import Enum
from events import Events

from Controllers.Player_Controller import PlayerStandardActions

class EventTypes(Enum):
    ON_KILL_SELF = "on_kill_self"
    ON_DIE = "on_die"
    ON_MESSAGE_DISPLAY = "on_message_display"
    ON_INTRO_DISPLAY = "on_intro_display"
    ON_GAME_START = "on_game_start"
    ON_PLAYER_ACTION = "on_player_action"
    ON_ITEM_PICKUP = "on_item_pickup"