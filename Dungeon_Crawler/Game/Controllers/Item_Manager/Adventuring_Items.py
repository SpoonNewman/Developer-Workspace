from Controllers.Item_Manager.BaseItem import BaseItemRegistry, GameItem
from Controllers.Music_Controller import MusicSoundRegistry


class AdventuringItemsRegistry(BaseItemRegistry):
    @classmethod
    def get_registered_items(cls):
        cls.TORCH = TorchItem().__class__.__name__
        cls.CHEST = ChestItem().__class__.__name__
        cls.CHAIN = ChainItem().__class__.__name__
        cls.ROPE = RopeItem().__class__.__name__
        cls.BOOK = BookItem().__class__.__name__

        return [
           cls.TORCH,
           cls.CHEST,
           cls.CHAIN,
           cls.ROPE,
           cls.BOOK
        ]

class AdventuringItem(GameItem):
    def __init__(self) -> None:
        super().__init__()
        self.inv_socket_weight = 1

class BookItem(AdventuringItem):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Book"
        self.on_pickup_sfx_name = MusicSoundRegistry.BOOK_PAGE

class TorchItem(AdventuringItem):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Torch"
        self.description = "A wooden stick with oil and rag. When lit aflame it provides light. Careful in small areas."

class ChestItem(AdventuringItem):
    pass

class ChainItem(AdventuringItem):
    pass

class RopeItem(AdventuringItem):
    pass