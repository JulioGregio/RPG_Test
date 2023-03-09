class Race:
    def __init__(self, name, attributes, bonuses):
        self.name = name
        self.attributes = attributes
        self.bonuses = bonuses

    def __str__(self):
        return f"Esta é a raça {self.name}. " \
               f"\nSeus bônus de atributos são {self.attributes}. " \
               f"\nSeus bônus de perícias são {', '.join(self.bonuses)}."


class Dwarf(Race):
    def __init__(self):
        name = "Dwarf"
        attributes = "+2 Cons, +2 Str"
        bonuses = ["+1 Machados", "+1 Martelos", "+1 Picaretas", "+1 Rifles Pesados", "+1 Escopetas"]
        super().__init__(name, attributes, bonuses)


class Elf(Race):
    def __init__(self):
        name = "Elf"
        attributes = "+2 Dex, +1 Per, +1 Int"
        bonuses = ["+1 Espada", "+1 Arcos", "+1 Magia", "+1 Rifles", "+1 Pistola", "+1 Rifles Sniper"]
        super().__init__(name, attributes, bonuses)


class Human(Race):
    def __init__(self):
        name = "Human"
        attributes = "+1 Int"
        bonuses = ["+1 Espadas", "+1 Arcos", "+1 Pistolas", "+1 Magia", "+1 Rifles",
                   "+1 Rifles Pesados", "+1 Pistola", "+1 Escopeta"]
        super().__init__(name, attributes, bonuses)


class Ork(Race):
    def __init__(self):
        name = "Ork"
        attributes = "+2 Str, +1 Cons"
        bonuses = ["+1 Espadas", "+1 Pistola", "+1 Rifles Pesados", "+1 Escopeta", "+1 Machado"]
        super().__init__(name, attributes, bonuses)


class Troll(Race):
    def __init__(self):
        name = "Troll"
        attributes = "+2 Str, +2 Cons"
        bonuses = ["+1 Machados", "+1 Martelos", "+1 Rifles Pesados", "+1 Escopeta", "+1 Espadas"]
        super().__init__(name, attributes, bonuses)


class Class:
    """
    Classe base para as classes de personagens do jogo.
    """

    def __init__(self, name, bonus, skills):
        """
        Cria uma nova classe de personagem.

        Args:
            name (str): O nome da classe.
            bonus (str): A descrição dos bônus da classe.
            skills (str): A descrição das habilidades da classe.
        """
        self.name = name
        self.bonus = bonus
        self.skills = skills

    def __str__(self):
        """
        Retorna uma string contendo a descrição da classe.
        """
        return f"Esta é a classe {self.name}. Seus bônus são {self.bonus}. Suas perícias são {self.skills}."


class StreetSamurai(Class):
    """
    Classe de personagem "Street Samurai".
    """

    def __init__(self):
        """
        Cria um novo "Street Samurai".
        """
        name = "Street Samurai"
        bonus = "+5 de dano com katana, multiplicador de vida x8"
        skills = """Perícias:
                     - 3 em Katana
                     - 3 em Ataque Poderoso
                     - 1 em Armas de Fogo"""
        super().__init__(name, bonus, skills)


class Fusor(Class):
    """
    Classe de personagem "Fusor".
    """

    def __init__(self):
        """
        Cria um novo "Fusor".
        """
        name = "Fusor"
        bonus = "+5 de dano quando com seu companheiro Drone, multiplicador de vida x5"
        skills = """Perícias:
                     - 3 em Drones
                     - 2 em Ataque Estratégico
                     - 2 em Armas de Fogo"""
        super().__init__(name, bonus, skills)


class UrbanXaman(Class):
    """
    Classe de personagem "Urban Xaman".
    """

    def __init__(self):
        """
        Cria um novo "Urban Xaman".
        """
        name = "Urban Xaman"
        bonus = "+3 de dano com o companheiro, +3 de dano com Magia, multiplicador de vida x4"
        skills = """Perícias:
                     - 3 em Magia
                     - 2 em Ataque Estratégico
                     - 1 em Armas Brancas
                     - 1 em Armas de Fogo"""
        super().__init__(name, bonus, skills)


class Mage(Class):
    """
    Classe de personagem "Mago".
    """

    def __init__(self):
        """
        Cria um novo "Mago".
        """
        name = "Mage"
        bonus = "+5 de dano em Magia, multiplicador de vida x4"
        skills = """Perícias:
                        - 4 em Magia
                        - 1 em Armas Brancas
                        - 1 em Armas de Fogo"""
        super().__init__(name, bonus, skills)


class MartialAdept(Class):
    """
    Classe de personagem "Martial Adept".
    """

    def __init__(self):
        """
        Cria um novo "Martial Adept".
        """
        name = "Martial Adept"
        bonus = "+5 de dano em combate desarmado, multiplicador de vida x7"
        skills = """Perícias:
                        - 4 em Briga
                        - 3 em Ataque Poderoso"""
        super().__init__(name, bonus, skills)


class WeaponAdept(Class):
    """
    Classe de personagem "Weapon Adept".
    """

    def __init__(self):
        """
        Cria um novo "Weapon Adept".
        """
        name = "Weapon Adept"
        bonus = "+5 de dano em Armas de Fogo, multiplicador de vida x6"
        skills = """Perícias:
                        - 4 em Armas de Fogo
                        - 2 em Ataque Estratégico
                        - 2 em Briga"""
        super().__init__(name, bonus, skills)
