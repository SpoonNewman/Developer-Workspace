from Controllers.base_controller import BaseController
from constants import GameConstants
from pygame import mixer

class MusicSoundRegistry():
    BOOK_PAGE = "book-page-turn.wav"
    PLAYER_DEATH_CRY = "player-death-cry.mp3"

class MusicController(BaseController):
    music_path = "./Game/assets/music/"
    sfx_path = "./Game/assets/sfx/"
    music_library = [
        "The-Road-Home.mp3",
        "a-really-dark-alley.mp3",
        "Come-Out-And-Play.mp3",
        "Labyrinth-of-Lost-Dreams.mp3",
    ]

    default_track = "a-really-dark-alley.mp3"
    default_music_volume = 0.6
    default_music_fadeout_time = 2200
    default_fade_in_time = 1600

    @classmethod
    def initialize_music(cls, **kwargs):
        if kwargs.get("play_audio"):
            mixer.init()
            cls.play_default_music()

    @classmethod
    def play_default_music(cls, **kwargs):
        cls.play_music_by_track(track_name=cls.default_track)

    @classmethod
    def play_music_by_track(cls, **kwargs):
        track_name = kwargs.get("track_name")
        if track_name in cls.music_library:
            if mixer.music.get_busy():
                mixer.music.fadeout(cls.default_music_fadeout_time)
            mixer.music.load(f"{cls.music_path}{track_name}")
            mixer.music.set_volume(cls.default_music_volume)
            mixer.music.play(loops=-1, fade_ms=cls.default_fade_in_time)

    @classmethod
    def play_sfx(cls, event):
        if not event.sfx_name in MusicSoundRegistry.__dict__.values():
            raise ValueError("The sound effect you attempted to play is not registered in the Music Sound Registry.")
        sound = f"{cls.sfx_path}{event.sfx_name}"
        item_sfx = mixer.Sound(sound)
        mixer.Sound.play(item_sfx)