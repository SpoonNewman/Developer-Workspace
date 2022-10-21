from abc import abstractmethod


class BaseItemRegistry():
    @classmethod
    @abstractmethod
    def get_registered_items(cls):
        raise NotImplementedError("")

class GameItem():
    pass