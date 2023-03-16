from Rules import rpg_menus
from Rules import rpg_sheet


def sheet_status_function(clas):
    if clas == 1:
        print(person.sheet_status('Fusor'))
    elif clas == 2:
        print(person.sheet_status('Mage'))
    elif clas == 3:
        print(person.sheet_status('Martial Adept'))
    elif clas == 4:
        print(person.sheet_status('Street Samurai'))
    elif clas == 5:
        print(person.sheet_status('Urban Xaman'))
    elif clas == 6:
        print(person.sheet_status('Weapon Adept'))


race = rpg_menus.race_menu()
classe = rpg_menus.classe_menu()
person = rpg_sheet.Person()
print('==' * 60)
print(person.sheet_atributtes(race))
print(person.sheet_skills(classe))
print(sheet_status_function(classe))
list1 = rpg_menus.upgrade_initial()
person.update_force(list1['Strength'])
person.update_dex(list1['Dexterity'])
person.update_cons(list1['Constitution'])
person.update_inte(list1['Intelligence'])
person.update_per(list1['Perception'])
person.update_wp(list1['White Weapons'])
person.update_fa(list1['Firearms'])
person.update_br(list1['Brawl'])
person.update_mag(list1['Magic'])
person.update_ale(list1['Alertness'])
person.update_st(list1['Strategic Attack'])
person.update_pa(list1['Power Attack'])
person.update_dro(list1['Drones'])
print(person.sheet_atributtes())
print(person.sheet_skills())
print(sheet_status_function(classe))
