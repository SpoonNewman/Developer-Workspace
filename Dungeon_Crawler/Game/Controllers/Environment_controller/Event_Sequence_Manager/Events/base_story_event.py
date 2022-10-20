from abc import abstractmethod


class BaseStoryEvent():
    @classmethod
    @abstractmethod
    def handle_event(cls):
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @classmethod
    @abstractmethod
    def trigger_next_scene(cls):
        raise NotImplementedError("This is using base class abstract property, please make your own!")
