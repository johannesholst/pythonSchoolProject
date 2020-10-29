import random


class Leader:
    def __init__(self, name=None, fire=None, shock=None, maneuver=None):
        names = ["Robert E. Lee", "George G. Meade", "John F. Reynolds", "Ulysses S. Grant"]
        if name is None:
            name = random.choice(names)
        if fire is None:
            fire = random.randint(0, 6)
        if shock is None:
            shock = random.randint(0, 6)
        if maneuver is None:
            maneuver = random.randint(0, 6)

        self.name = name
        self.fire = fire
        self.shock = shock
        self.maneuver = maneuver

general = Leader(None, None, None, None)


class LeaderAI(Leader):
    pass

generalAI = LeaderAI(None, None, None, None)
