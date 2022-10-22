from abc import abstractmethod


class BaseItemRegistry():
    @classmethod
    @abstractmethod
    def get_registered_items(cls):
        raise NotImplementedError("")

class GameItem():
    def __init__(self) -> None:
        self.name = "unknown item"
        self.inv_socket_weight = 0
        self.description = ""
        self.on_pickup_sfx_name = None