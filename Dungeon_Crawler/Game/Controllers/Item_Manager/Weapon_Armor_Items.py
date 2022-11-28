from Controllers.Item_Manager.BaseItem import BaseItemRegistry, GameItem, EquippableItem, HandEquippableItem, BodyEquippableItem
from Controllers.Player_Controller.item_slots import ItemSlots


class WeaponItemsRegistry(BaseItemRegistry):
    @classmethod
    def get_registered_items(cls):
        cls.SWORD = SwordItem().__class__.__name__
        cls.KNIFE = KnifeItem().__class__.__name__
        cls.CLUB = ClubItem().__class__.__name__
        cls.FIREARM = FirearmItem().__class__.__name__

        return [
           cls.SWORD,
           cls.KNIFE,
           cls.CLUB,
           cls.FIREARM
        ]

class ArmorItemsRegistry(BaseItemRegistry):
    @classmethod
    def get_registered_items(cls):
        cls.SHIELD = ShieldItem().__class__.__name__
        cls.CHESTPLATE = ChestPlateItem().__class__.__name__
        
        return [
           cls.SHIELD,
           cls.CHESTPLATE
        ]

class WeaponItem(HandEquippableItem):
    def __init__(self) -> None:
        super().__init__()
        self.inv_socket_weight = 1

class ArmorItem(BodyEquippableItem):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

class ChestPlateItem(ArmorItem):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = "Chest Plate"
        self.description = "A steel chest plate badly dented and rusted."
        self.preferred_slot = ItemSlots.CHEST.value
        self.inv_socket_weight = 4 if not kwargs.get("inv_socket_weight") else kwargs.get("inv_socket_weight")
        if not kwargs.get("type"):
            self.type = "chestplate"
        
        
        self.actions = {
            **self.universal_actions,
        }
    
    def use_item(self, action_input: str):
        if action_input in self.actions.keys():
            action = self.actions[action_input]
            if action in self.universal_actions.values():

                self.perform_universal_action(action, self)

class SwordItem(WeaponItem):
    def __init__(self) -> None:
        self.inv_socket_weight = 2

class KnifeItem(WeaponItem):
    pass

class ClubItem(WeaponItem):
    def __init__(self) -> None:
        self.inv_socket_weight = 2

class ShieldItem(WeaponItem):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Shield"
        self.description = "A wooden shield. Dry rotted and could fall apart at any moment."
        
        
        self.actions = {
            **self.universal_actions,
        }
        
    def use_item(self, action_input: str):
        if action_input in self.actions.keys():
            action = self.actions[action_input]
            if action in self.universal_actions.values():

                self.perform_universal_action(action, self)

class FirearmItem(WeaponItem):
    pass

