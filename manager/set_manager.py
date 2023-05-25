class SetManager:

    def __init__(self, stadium_manager):
        self.stadium_manager = stadium_manager

    def __len__(self):
        length = 0
        for s in self.stadium_manager.__iter__():
            length += len(s.equipment_set)
        return length

    def __iter__(self):
        new_set = set()
        for s in self.stadium_manager.__iter__():
            new_set.update(s.equipment_set)
        return iter(new_set)

    def __getitem__(self, key):
        for s in self.stadium_manager.__iter__():
            return s[key]

    def __next__(self):
        for s in self.stadium_manager.__iter__():
            return next(s)