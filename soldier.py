class Soldier:
    def __init__(self, morale, fire, shock, size):
        self.morale = morale
        self.fire = fire
        self.shock = shock
        self.size = size

infantry = Soldier(1000, 3, 5, 1000)


class SoldierAI(Soldier):
    pass

infantryAI = SoldierAI(1000, 3, 5, 1000)