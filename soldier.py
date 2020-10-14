class Soldier:
    def __init__(self, morale, fire, shock, size):
        self.morale = morale
        self.fire = fire
        self.shock = shock
        self.size = size

infantry = Soldier(10, 2, 4, 1000)


class SoldierAI(Soldier):
    pass

infantryAI = SoldierAI(10, 2, 4, 1000)

