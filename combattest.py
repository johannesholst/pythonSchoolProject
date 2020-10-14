from soldier import infantry, infantryAI
from leader import *

import random



def terrain():
    iver = -1
    strait = -2
    amph = -2

    plains = 0
    forest = -1
    hills = -2

    T = forest

    return T



def diceran():
    Randroll = random.randint(0, 9)

    RandrollAI = random.randint(0, 9)

    return Randroll, RandrollAI



def morale():
    C = cas()
    Mdam = C/200*(infantry.morale/2.7)+(0.03)

    print("Morale damage:", Mdam)

    return Mdam


def strength():
    Ustrength = infantry.size - 999

    if Ustrength < 1000:
        print("Unit strength is:", Ustrength)

    UstrengthAI = infantryAI.size - 999

    if UstrengthAI < 1000:
        print("AI Unit strength is:", UstrengthAI)

    return Ustrength, UstrengthAI


def dice():
    Randroll, RandrollAI = diceran()
    T = terrain()

    diceroll = Randroll+(general.shock - generalAI.shock) + infantry.shock + T

    dicerollAI = RandrollAI+generalAI.shock - general.shock + infantryAI.shock + T

    print("diceroll", diceroll)
    print("dicerollAI", dicerollAI)
    print("General.shock", general.shock)
    print("GeneralAI.Shock", generalAI.shock)
    print("RandRoll", Randroll)
    print("RandRollAI", RandrollAI)

    result = general.shock - generalAI.shock

    print("Test", result)

    return diceroll, dicerollAI


def cas():
    diceroll, dicerollAI = dice()
    Ustrength, UstrengthAI = strength()

    Cbase = 15 * diceroll
    Combat = (Cbase*Ustrength*infantry.shock)

    CbaseAI = 15 * dicerollAI
    CombatAI = (CbaseAI*UstrengthAI*infantryAI.shock)

    print("cbase:", Cbase)
    print("cbaseAI", CbaseAI)

    print("combat:", Combat)
    print("combatAI", CombatAI)

    return Combat, CombatAI



cas()
#strength()
#morale()



