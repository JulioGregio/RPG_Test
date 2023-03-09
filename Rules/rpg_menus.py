from Rules import rpg_choices
from time import sleep


'''
Neste ponto eu poderia ter feito mais simples e direto ao ponto, para evitar de ficar rolando
terminal pra saber algo, e de certa forma eu já poderia tirar a escolha de raça na sequência
sem precissar fazer outras funções apenas por estilo ou desejo de algo melhor, mas poderia ser
feito assim também. Talvez fosse útil para uma interface gráfica.

At this point I could have made it simpler and more to the point, to avoid scrolling
terminal to know something, and in a way I could already remove the choice of race in the sequence
without having to do other functions just for style or desire for something better, but it could be
done like that too. Perhaps it would be useful for a GUI.

def start_menu():
    print('==' * 18)
    print('Welcome!'
          '\nYour journey starts here...'
          '\nYour first choice will be your Race.'
          '\nYour second choice will be your Class.')
    while True:
        print('==' * 18)
        show1 = int(input('[1] - Dwarf'
                          '\n[2] - Elf'
                          '\n[3] - Human'
                          '\n[4] - Ork'
                          '\n[5] - Troll'
                          '\n[0] - Next Step'
                          '\nWhich option do you want to see: '))
        if show1 == 1:
            print('==' * 18)
            print(rpg_choices.Dwarf())
        elif show1 == 2:
            print('==' * 18)
            print(rpg_choices.Elf())
        elif show1 == 3:
            print('==' * 18)
            print(rpg_choices.Human())
        elif show1 == 4:
            print('==' * 18)
            print(rpg_choices.Ork())
        elif show1 == 5:
            print('==' * 18)
            print(rpg_choices.Troll())
        elif show1 == 0:
            print('==' * 18)
            print("Are you ready to choose your class? I hope so! Let's go!")
            break
        else:
            print('Incorrect option. Try again.')
'''


def race_menu():
    print('Welcome!'
          '\nYour journey starts here...'
          '\nYour first choice will be your Race.'
          '\nYour second choice will be your Class.')
    print('==' * 60)
    sleep(1)
    print("Let's go to the first stage, the choice of race you will have the following options:")
    sleep(1)
    print("\n"
          "\n[1] - DWARF - They are strong and resistant, they have low and wide bodies, "
          "\nthey have great discharge with metals and technology. Stubborn and headstrong, "
          "\nmale dwarves like to grow long beards.")
    sleep(1)
    print("\n"
          "\n[2] - ELF - They are tall and slender, with slender bodies and delicate details,"
          "\nwhich gives them great body dexterity. They have pointed ears and eyes that can see far away."
          "\nThey tend to be a little cold and distant.")
    sleep(1)
    print('\n'
          '\n[3] - HUMAN - They are the species with the greatest dominance, they have '
          '\nevolved a lot in the field of intelligence and are great in everything that is available,'
          '\nthe ambition to always want more is what moves them forward.')
    sleep(1)
    print("\n"
          "\n[4] - ORK - A little taller than humans, broad and with large fangs protruding from its mouth. "
          "\nOrks have a rough, violent appearance and don't do much to change that stereotype. "
          "\nTo some they are just troublemakers and rioters, but among their kind there is a strong "
          "\nbond of honor.")
    sleep(1)
    print("\n"
          "\n[5] - TROLL - Standing nearly 10 feet tall and weighing around 400 pounds, Trolls have "
          "\ntrouble finding their place in the world. They have an intimidating appearance and if "
          "\nit weren't enough to be big and massive, they still have large horns, fangs and bone "
          "\nplates spread throughout their body.")

    print('==' * 60)

    while True:
        choice1 = int(input("What number do you choose? "))
        if choice1 == 1:
            sleep(1)
            print(rpg_choices.Dwarf())
            break
        elif choice1 == 2:
            sleep(1)
            print(rpg_choices.Elf())
            break
        elif choice1 == 3:
            sleep(1)
            print(rpg_choices.Human())
            break
        elif choice1 == 4:
            sleep(1)
            print(rpg_choices.Ork())
            break
        elif choice1 == 5:
            sleep(1)
            print(rpg_choices.Troll())
            break
        else:
            print('Invalid Option. Try again.')
    return choice1


def classe_menu():
    print('==' * 60)

    print("Let's go to your second choice, choose your class from the following options:")
    sleep(1)
    print("\n"
          "\n[1] - FUSOR - He is highly skilled in operating, repairing and customizing all types of vehicles "
          "\nand/or drones, offering surveillance, transport and remote firepower to his team. If you have a "
          "\ncontrol spindle they can become your vehicles.")
    sleep(1)
    print("\n"
          "\n[2] - MAGE - He manipulates and channels mana, an energy field that is the essence of magic. "
          "\nMana can be manipulated in many different ways, allowing for different types of casters. "
          "\nMages follow a more logical and orderly system of magic.")
    sleep(1)
    print("\n"
          "\n[3] - MARTIAL ADEPT - He manipulates the body to be a weapon, expert in unarmed combat. "
          "\nIt uses powerful blows and practically superhuman abilities resulting from its hard training.")
    sleep(1)
    print("\n"
          "[4] - STREET SAMURAI - He can take massive amounts of damage and remain on his feet, dealing "
          "\ndevastating damage to his enemies. He is typically augmented with hefty amounts of cyberware "
          "\nand bionics, which makes him exceptionally tough and dangerous in physical and armed combat. "
          "\nAlthough he is fierce and deadly, he often has a code of honor: it may be a code understandable "
          "\nonly to him.")
    sleep(1)
    print("\n"
          "\n[5] - URBAN XAMAN - He manipulates and channels mana, an energy field that is the essence of magic. "
          "\nMana can be manipulated in many different ways, allowing for different types of casters. "
          "\nXamans rely more on their instincts and their intuition.")
    sleep(1)
    print("\n"
          "\n[6] - WEAPON ADEPT - He handles firearms with mastery, being adept at physical combat if necessary. "
          "\nThey are quite versatile.")
    print('==' * 60)

    while True:
        choice2 = int(input("What number do you choose? "))
        if choice2 == 1:
            sleep(1)
            print(rpg_choices.Fusor())
            break
        elif choice2 == 2:
            sleep(1)
            print(rpg_choices.Mage())
            break
        elif choice2 == 3:
            sleep(1)
            print(rpg_choices.MartialAdept())
            break
        elif choice2 == 4:
            sleep(1)
            print(rpg_choices.StreetSamurai())
            break
        elif choice2 == 5:
            sleep(1)
            print(rpg_choices.UrbanXaman())
            break
        elif choice2 == 6:
            sleep(1)
            print(rpg_choices.WeaponAdept())
            break
        else:
            print('Invalid Option. Try again.')
    return choice2
