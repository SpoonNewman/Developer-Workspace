from abc import abstractmethod


class BaseSequence():
    @classmethod
    @abstractmethod
    def handle_sequence():
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @classmethod
    def get_player_input(cls):
        return input("\nWhat do you choose?  ")

    @classmethod
    @abstractmethod
    def trigger_event_sequence():
        raise NotImplementedError("This is using base class abstract property, please make your own!")