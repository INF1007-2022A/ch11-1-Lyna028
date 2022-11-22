class perso:
    max_possible_hp = 10000
    def __init__(self, hp, attack, defense):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.__id = 42  #pour rendre prive

    def print__id(self):
        print(self.__id)

    def compute_dmg(self, target):
        return 10 * self.attack / target.defense


def main () :
    perso1 = perso(20,10,5)
    perso2 = perso(30,15,10)
    print(perso1.hp)
    print(perso2.compute_dmg(perso1)) #tres important en oop
    print(perso1.max_possible_hp)
    print(perso.max_possible_hp) #nom de la classe.nom de ton variable global
    perso1.foo = 42 #ajourter un attribut a la classe
    print(perso1.foo)
    print(type(perso1))


if __name__ == '__main__':
    main()