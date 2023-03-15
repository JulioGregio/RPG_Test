from Rules import rpg_menus
from Rules import rpg_sheet


race = rpg_menus.race_menu()
classe = rpg_menus.classe_menu()
person = rpg_sheet.Person()
print('==' * 60)
print(person.sheet_atributtes(race))
print(person.sheet_skills(classe))
if classe == 1:
    print(person.sheet_status('Fusor'))
elif classe == 2:
    print(person.sheet_status('Mage'))
elif classe == 3:
    print(person.sheet_status('Martial Adept'))
elif classe == 4:
    print(person.sheet_status('Street Samurai'))
elif classe == 5:
    print(person.sheet_status('Urban Xaman'))
elif classe == 6:
    print(person.sheet_status('Weapon Adept'))
list = rpg_menus.upgrade_initial()
person.update_force(list['Strength'])
person.update_dex(list['Dexterity'])
person.update_cons(list['Constitution'])
person.update_inte(list['Intelligence'])
person.update_per(list['Perception'])
print(person.sheet_atributtes())
