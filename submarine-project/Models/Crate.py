class Crate(): 
    def __init__(self, id='', weight=0, height=0, material='', assigned_crewman_id='', load_time_elapsed=0, source_id='', destination_id='', is_volatile=False, is_quarantined=False, required_machinery=[], current_location=''):
        self.id = id
        self.weight = weight
        self.height = height
        self.material = material
        self.assigned_crewman_id = assigned_crewman_id 
        self. load_time_elapsed = load_time_elapsed
        self.source_id = source_id # A Location id
        self.destination_id = destination_id # A location id
        self.is_volatile = is_volatile 
        self.is_quarantined = is_quarantined
        self.required_machinery = required_machinery
        self.current_location = current_location # A Location id