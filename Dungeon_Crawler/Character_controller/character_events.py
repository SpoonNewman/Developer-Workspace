from enum import Enum

class player_events(Enum):
    ON_ENEMY_ENCOUNTERED = 0
    ON_INACTIVE_CONDITION = 1
    ON_ACTIVE_CONDITION = 2
    ON_LIGHT_ACTIVE = 3
    ON_LIGHT_INACTIVE = 4
    ON_ITEM_PICKUP = 5
    ON_ITEM_DROP = 6

    