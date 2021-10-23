import numpy as np
from die import Die
from players import Players


debug = True

def random_number():
    return np.random.randint(1,7)

def setup_dice(player):
    dice = []
    for numbers in range(player.get_die_count()):
        die = Die(6)
        dice.append(die.roll())

    return dice

def compare(attacker, defender):
    if attacker > defender:
        return True
    return False

def match_round(attacker, defender):

    attacker_loses = 0
    while (attacker.units > 0 and defender.units > 0 and attacker.loses > attacker_loses):
        attacker_dice = setup_dice(attacker)
        defender_dice = setup_dice(defender)
        attacker_dice.sort(reverse=True)
        defender_dice.sort(reverse=True)

        
        while (attacker_dice and defender_dice and attacker.loses > attacker_loses):
            if debug: print ('Attacker Dice: {}'.format(attacker_dice))
            if debug: print ('Defender Dice: {}'.format(defender_dice))
            outcome = compare(attacker_dice[0], defender_dice[0])
            if outcome:
                if debug: print ('attacker wins')
                defender.lost_unit()
                attacker.won_unit()
                
            else:
                if debug: print ('defender wins')
                attacker.lost_unit()
                defender.won_unit()
                attacker_loses += 1

            attacker_dice.pop(0)
            defender_dice.pop(0)
    
    print ("Attacker: {} remaining; Defender: {} remaining".format(attacker.units, defender.units))
    if debug: print (attacker_loses)

def ask_user():
    attack_units = int(input("Number of attackers: "))
    defender_units = int(input("Number of defenders: "))
    acceptable_loses = int(input("Number attack stops at: "))
    attacker = Players("attacker", attack_units)
    attacker.allowed_loses(acceptable_loses)
    defender = Players("defender", defender_units)
    return attacker, defender


def main():
    attacker, defender = ask_user()
    match_round(attacker, defender)

if __name__ == "__main__":
    main()