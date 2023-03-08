from Rules import rpg_choices


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


def initial_menu():
