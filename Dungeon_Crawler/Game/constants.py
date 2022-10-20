from enum import Enum


class GameConstants():
    starting_music = "./Game/assets/The-Road-Home.mp3"
    default_music_volume = 0.6
    class typewriter_speeds(Enum):
        SLOW = 0.1
        MEDIUM = 0.065
        FAST = 0.03
        VERY_FAST = 0.01