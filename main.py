import time
import random

from leader import general, generalAI
from soldier import infantry, infantryAI


def terrain():
    if general.maneuver is generalAI.maneuver:
        TP = 0
        TAI = 0
        return TP, TAI
    elif generalAI.maneuver > general.maneuver:
        TP = -2
        TAI = 2
        return TP, TAI
    elif general.maneuver > generalAI.maneuver:
        TP = 2
        TAI = -2
        return TP, TAI


def phases():
    TP, TAI = terrain()

    phaseF = (general.fire - generalAI.fire) + infantry.fire + TP
    phaseS = (general.shock - generalAI.shock) + infantry.shock + TP

    phaseAIF = generalAI.fire - general.fire + infantryAI.fire + TAI
    phaseAIS = generalAI.shock - general.shock + infantryAI.shock + TAI

    if phaseF < 1:
        phaseF = 1

    if phaseAIF < 1:
        phaseAIF = 1

    if phaseS < 1:
        phaseS = 1

    if phaseAIS < 1:
        phaseAIS = 1

    return phaseF, phaseS, phaseAIF, phaseAIS


def main():
    phaseF, phaseS, phaseAIS, phaseAIF = phases()
    T, TAI = terrain()

    print("-----------------------------------------------------------")
    print("General name and stats:", general.name, general.fire, general.shock, general.maneuver)
    print("AI general name and stats:", generalAI.name, generalAI.fire, generalAI.shock, generalAI.maneuver)

    print("-----------------------------------------------------------")
    print("player Fire phase and Shock phase:", phaseF, phaseS)
    print("AI Fire phase and Shock phase:", phaseAIF, phaseAIS)

    print("-----------------------------------------------------------")
    print("terrain advantage for player: ", T)
    print("terrain advantage for AI: ", TAI)

    print("-----------------------------------------------------------")
    regiments = int(input("Enter number of player and enemy regiments: "))
    print("-----------------------------------------------------------")

    army = regiments * infantry.size
    armyAI = regiments * infantryAI.size

    print("starting player army:", army)
    print("starting AI army:", armyAI)
    print("starting morale:", infantry.morale)
    print("starting AI morale:", infantryAI.morale)

    while army > 0 and armyAI > 0 and infantry.morale > 0 and infantryAI.morale > 0:
        randroll = random.randint(0, 6)
        randrollAI = random.randint(0, 6)

        result = regiments*(infantry.size * 0.001)
        resultAI = regiments*(infantryAI.size * 0.001)

        '''Fire phase'''

        damageF = (result * phaseF) * randroll
        damageAIF = (resultAI * phaseAIF) * randrollAI

        army -= damageAIF
        print("-----------------------------------------------------------")
        print("player Army", int(army), "    -  AI Army", int(armyAI))
        print("Player Fire cas:", int(damageAIF), " -  AI Fire cas:", int(damageF))
        armyAI -= damageF

        morFP = (infantry.morale*0.01)*randroll
        morFAI = (infantryAI.morale*0.01)*randrollAI

        infantry.morale -= morFAI
        infantryAI.morale -=morFP

        print("-----------------------------------------------------------")
        print("player morale:", int(infantry.morale), "     -   AI morale:", int(infantryAI.morale))
        print("-----------------------------------------------------------")


        '''shock phase'''

        damageS = (result * phaseS) * randroll
        damageAIS = (resultAI * phaseAIS) * randrollAI

        army -= damageAIS
        print("-----------------------------------------------------------")
        print("player Army", int(army), "     -  AI Army", int(armyAI))
        print("Player Shock cas:", int(damageAIS), " -  AI Shock cas:", int(damageS))
        armyAI -= damageS

        morSP = (infantry.morale * 0.01) * randroll
        morSAI = (infantryAI.morale * 0.01) * randrollAI

        infantry.morale -= morSAI
        infantryAI.morale -= morSP

        print("-----------------------------------------------------------")
        print("player morale:", int(infantry.morale), "     -   AI morale:", int(infantryAI.morale))
        print("-----------------------------------------------------------")

        time.sleep(1)
        print('\n' * 50)

    if army > armyAI or infantry.morale > infantryAI.morale:
        print("Victory")
    else:
        print("Defeat")


if __name__ == '__main__':
    main()




