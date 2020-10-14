import random


class Leader:
    def __init__(self, fire=None, shock=None, maneuver=None):
        if fire is None:
            fire = random.randint(0, 6)
        if shock is None:
            shock = random.randint(0, 6)
        if maneuver is None:
            maneuver = random.randint(0, 6)
        self.fire = fire
        self.shock = shock
        self.maneuver = maneuver

general = Leader(None, None, None)
print(general.fire, general.shock, general.maneuver)


class LeaderAI(Leader):
    pass

generalAI = LeaderAI(None, None, None)

print(generalAI.fire, generalAI.shock, generalAI.maneuver)