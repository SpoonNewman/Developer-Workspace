Adding a new room:
1. Add the room to the `room_config.json`
2. Add the event handler event sequence object ot our `story_sequences_registry.py`
    - this will require creating an event sequence and adding it to the registry.
    - The following functions are required:
        - `handle_sequence`
        - `trigger_event_sequence`

