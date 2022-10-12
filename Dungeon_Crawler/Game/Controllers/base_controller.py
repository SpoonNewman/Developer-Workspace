class BaseController():
    def __init__(self, event_registry) -> None:
        self.event_registry = event_registry