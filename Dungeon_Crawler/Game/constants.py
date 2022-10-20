from enum import Enum


class GameConstants():
    player_starting_area = "Opening of the dungeon."
    
    class typewriter_speeds(Enum):
        SLOW = 0.1
        MEDIUM = 0.065
        FAST = 0.03
        VERY_FAST = 0.01