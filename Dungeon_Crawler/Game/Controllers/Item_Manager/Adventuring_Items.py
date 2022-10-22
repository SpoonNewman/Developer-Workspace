from Controllers.Item_Manager.BaseItem import BaseItemRegistry, GameItem


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
        self.name = "book"

class TorchItem(AdventuringItem):
    pass

class ChestItem(AdventuringItem):
    pass

class ChainItem(AdventuringItem):
    pass

class RopeItem(AdventuringItem):
    pass