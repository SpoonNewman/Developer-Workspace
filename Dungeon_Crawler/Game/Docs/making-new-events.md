Inside the `Game/Controllers/game_events.py` is located all the game event classes that can happen within the game. New events will be added here as a class that inherits from `GameEvent`. Game events which perform Below is an example of a new game event class called `OnSomeNewEvent`:

```py
class OnSomeNewEvent(GameEvent):
    def __init__(self):
        pass
```