from abc import abstractmethod


class BaseSequence():
    @classmethod
    @abstractmethod
    def handle_sequence():
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @classmethod
    @abstractmethod
    def get_player_input():
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @classmethod
    @abstractmethod
    def trigger_event_sequence():
        raise NotImplementedError("This is using base class abstract property, please make your own!")