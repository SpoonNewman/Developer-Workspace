from Controllers.Item_Manager.Adventuring_Items import AdventuringItemsRegistry
from Controllers.Item_Manager.Weapon_Armor_Items import ArmorItemsRegistry, WeaponItemsRegistry


class ItemRegistry():
    def __init__(self) -> None:
        pass

    @classmethod
    def get_registered_items(cls):
        adventuring_items = AdventuringItemsRegistry.get_registered_items()
        weapon_items = WeaponItemsRegistry.get_registered_items()
        armor_items = ArmorItemsRegistry.get_registered_items()

        cls.items = [
            *adventuring_items,
            *weapon_items,
            *armor_items
        ]

        return cls.items