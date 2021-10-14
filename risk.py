import numpy as np
debug = False

def random_number():
    return np.random.randint(1,6)

def setup_attacker(units):
    die_total = 0
    if (units >= 3):
        die_total = 3
    else:
        die_total = units

    dice = []
    for numbers in range(die_total):
        dice.append(random_number())

    return dice

def setup_defender(units):
    die_total = 0
    if (units >= 2):
        die_total = 2
    else:
        die_total = units

    dice = []
    for numbers in range(die_total):
        dice.append(random_number())

    return dice

def compare(attacker, defender):
    if attacker > defender:
        return True
    return False

def match_round(attacker_units, defender_units, max_loses):

    attacker_loses = 0
    while (attacker_units > 0 and defender_units > 0 and max_loses > attacker_loses):
        attacker_dice = setup_attacker(attacker_units)
        defender_dice = setup_defender(defender_units)
        attacker_dice.sort(reverse=True)
        defender_dice.sort(reverse=True)
        
        while (attacker_dice and defender_dice):
            if debug: print ('Attacker Dice: {}'.format(attacker_dice))
            if debug: print ('Defender Dice: {}'.format(defender_dice))
            outcome = compare(attacker_dice[0], defender_dice[0])
            if outcome:
                if debug: print ('attacker wins')
                defender_units -= 1
                attacker_loses += 1
            else:
                if debug: print ('defender wins')
                attacker_units -= 1

            attacker_dice.pop(0)
            defender_dice.pop(0)
    
    print ("Attacker: {} remaining; Defender: {} remaining".format(attacker_units, defender_units))
    if debug: print (attacker_loses)

def ask_user():
    attack_units = int(input("Number of attackers: "))
    defender_units = int(input("Number of defenders: "))
    acceptable_loses = int(input("Number attack stops at: "))

    return attack_units, defender_units, acceptable_loses

attack_units, defender_units, acceptable_loses = ask_user()
match_round(attack_units, defender_units, acceptable_loses)