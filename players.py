class Players():
    def __init__(self, position, units):
        self.position = position
        self.units = units
        if (position == "attacker"):
            self.max_die = 3
        else:
            self.max_die = 2

    def get_die_count(self):
        if (self.units >= self.max_die):
            return self.max_die
        return self.units

    def lost_unit(self):
        self.units -= 1

    def won_unit(self):
        self.units += 1

    def allowed_loses(self, loses):
        self.loses = loses
    
