import random


class Person:
    def __init__(self, force=1, dex=1, cons=1, inte=1, per=1, wp=0, fa=0, br=0, mag=0, ale=0, st=0, pa=0, dro=0):
        self.force = force
        self.dex = dex
        self.cons = cons
        self.inte = inte
        self.per = per
        self.wp = wp
        self.fa = fa
        self.br = br
        self.mag = mag
        self.ale = ale
        self.st = st
        self.pa = pa
        self.dro = dro

    def __str__(self):
        return f'Seus atributos são:' \
               f'\nStrength: {self.force}' \
               f'\nDexterity: {self.dex}' \
               f'\nConstituition: {self.cons}' \
               f'\nIntelligence: {self.inte}' \
               f'\nPerception: {self.per}'

    def update_force(self, force):
        self.force += force

    def update_dex(self, dex):
        self.dex += dex

    def update_cons(self, cons):
        self.cons += cons

    def update_inte(self, inte):
        self.inte += inte

    def update_per(self, per):
        self.per += per

    def update_wp(self, wp):
        self.wp += wp

    def update_fa(self, fa):
        self.fa += fa

    def update_br(self, br):
        self.br += br

    def update_mag(self, mag):
        self.mag += mag

    def update_ale(self, ale):
        self.ale += ale

    def update_st(self, st):
        self.st += st

    def update_pa(self, pa):
        self.pa += pa

    def update_dro(self, dro):
        self.dro += dro

    def sheet_atributtes(self, race):
        if race == 1:
            self.force += 2
            self.cons += 2
        elif race == 2:
            self.dex += 2
            self.inte += 1
            self.per += 1
        elif race == 3:
            self.inte += 1
        elif race == 4:
            self.force += 2
            self.cons += 1
        elif race == 5:
            self.force += 2
            self.cons += 2

        person_atributtes = {'Strength': self.force, 'Dexterity': self.dex, 'Constituition': self.cons,
                             'Intelligence': self.inte, 'Perception': self.per}

        return '\n'.join([f"{i} = {person_atributtes[i]}" for i in person_atributtes])

    def sheet_skills(self, classe):
        if classe == 1:
            self.dro = 3
            self.st = 2
            self.fa = 2
        elif classe == 2:
            self.mag = 4
            self.fa = 1
            self.wp = 1
        elif classe == 3:
            self.br = 4
            self.pa = 3
        elif classe == 4:
            self.wp = 3
            self.pa = 3
            self.fa = 1
        elif classe == 5:
            self.mag = 3
            self.st = 2
            self.fa = 1
            self.wp = 1
        elif classe == 6:
            self.fa = 4
            self.pa = 2
            self.br = 1

        person_skills = {'White Weapons': self.wp, 'Firearms': self.fa, 'Brawl': self.br,
                         'Magic': self.mag, 'Alertness': self.ale, 'Strategic Attack': self.st,
                         'Power Attack': self.pa, 'Drones': self.dro}
        return '\n'.join([f"{i} = {person_skills[i]}" for i in person_skills])

    def sheet_status(self, class_person):
        _class = 0
        _mana = 0
        if class_person in 'Street Samurai':
            _class += 8
        elif class_person in 'Fusor':
            _class += 5
        elif class_person in 'Uraban Xaman':
            _class += 4
        elif class_person in 'Mage':
            _class += 4
        elif class_person in 'Martial Adept':
            _class += 7
        elif class_person in 'Weapon Adept':
            _class += 6
        else:
            _class = 5

        if class_person in 'Xaman':
            _mana = 2
        elif class_person in 'Mage':
            _mana = 3
        else:
            _mana = 1

        life = (self.force + (self.cons * 2)) * _class
        mana = (self.inte * 5) * _mana
        return f'Total Life: {life}' \
               f'\nTotal Mana: {mana}'


class NPC:
    def __init__(self, force=1, dex=1, cons=1):
        self.force = force
        self.dex = dex
        self.cons = cons

    def update_npc_force(self, force):
        self.force = force

    def update_npc_dex(self, dex):
        self.dex = dex

    def update_npc_cons(self, cons):
        self.cons = cons

    def create_npc(self):
        self.force = random.randint(1, 5)
        self.dex = random.randint(1, 5)
        self.cons = random.randint(1, 5)

        npc_atributtes = {'Strength': self.force, 'Dexterity': self.dex, 'Constituition': self.cons}
        print('==' * 15)
        return '\n'.join([f"{i} = {npc_atributtes[i]}" for i in npc_atributtes])
