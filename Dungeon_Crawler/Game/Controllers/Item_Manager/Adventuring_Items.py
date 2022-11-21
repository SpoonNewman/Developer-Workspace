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
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        if not kwargs.get("inv_socket_weight"):
            self.inv_socket_weight = 1

class BookItem(AdventuringItem):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(**kwargs)
        # self.name = "Book"
        if not kwargs.get("type"):
            self.type = "book"
        if not kwargs.get("pickup_sfx_name"):
            self.pickup_sfx_name = MusicSoundRegistry.BOOK_PAGE

class TorchItem(AdventuringItem):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Torch"
        self.description = "A wooden stick with oil and rag. When lit aflame it provides light."
        
        self.is_lit = False
        
        self.actions = {
            "1": "Light",
            "2": "Douse",
            **self.universal_actions,
        }

    def use_item(self, action_input: str):
        if action_input in self.actions.keys():
            action = self.actions[action_input]
            if action == "Light":
                self.light_torch()
            elif action == "Douse":
                self.douse_torch()
            elif action in self.universal_actions.values():

                self.perform_universal_action(action, self)


    def light_torch(self):
        if self.is_lit:
            print("The torch is already blazing with flame, though it does little to light the surroundings.")
        else:
            self.is_lit = True
            print("The torch blazes to life with hot flame.")
            self.play_on_use_sfx(MusicSoundRegistry.MATCH_LIGHT)
            self.play_on_use_sfx(MusicSoundRegistry.FLAME_CRACKLE, sfx_loops=-1)

    def douse_torch(self):
        if not self.is_lit:
            print("The torch is already doused.")
        else:
            self.is_lit = False
            print("You douse the flame of the torch plunging yourself into darkness.")
            self.stop_sfx(MusicSoundRegistry.FLAME_CRACKLE)
            self.play_on_use_sfx(MusicSoundRegistry.FLAME_DOUSE)


class ChestItem(AdventuringItem):
    pass

class ChainItem(AdventuringItem):
    pass

class RopeItem(AdventuringItem):
    pass