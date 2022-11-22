#Classes pour représenter un personnage.

import random

import utils


class Weapon:
    """
    Une arme dans le jeu.

    :param name: Le nom de l'arme
    :param power: Le niveau d'attaque
    :param min_level: Le niveau minimal pour l'utiliser
    """

    def __init__(self, name, power, min_level):
        self.__name = name
        self.power = power
        self.min_level = min_level
    @property
    def name(self):
        return self.__name


    UNARMED_POWER = 20
    @staticmethod
    def make_unarmed():
        return Weapon('unarmed', Weapon.UNARMED_POWER, 1)



class Character:
    """
    Un personnage dans le jeu

    :param name: Le nom du personnage
    :param max_hp: HP maximum
    :param attack: Le niveau d'attaque du personnage
    :param defense: Le niveau de défense du personnage
    :param level: Le niveau d'expérience du personnage
    """
    def __init__(self, name, max_hp, attack, defense, level):
        self.__name = name
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.level = level
        self.__weapon = None
        self.__hp = self.max_hp

    @property
    def name(self):
        return self.__name

    @property
    def weapon (self, weapon) :
        return self.__weapon

    @weapon.setter
    def weapon (self, weapon):
        if weapon is None :
            self.__weapon = Weapon.make_unarmed()
        elif self.level >= weapon.min_level:
            self.__weapon = weapon
        else :
            raise ValueError('Mauvais niveau darme' )




    @property
    def main(self): #acceder mais pas modifier
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = utils.clamp(hp, 0, self.max_hp)

    @staticmethod
    def compute_damage_output(attacker_lvl, weapon_power, attack, defense, crit_prob, variability ):
        level_factor = 2 * attacker_lvl / 5 + 2
        attack_factor = attack / defense
        rand_factor = random.uniform(1.0 - variability, 1.0)
        crit = 2.0 if random.random() < crit_prob else 1.0;
        modifier = rand_factor * crit
        dmg = ((level_factor * weapon_power * attack_factor)/ 50 + 2 ) * modifier
        return dmg


def deal_damage(attacker : Character, defender : Character):
    # TODO: Calculer dégâts
    dmg, crit = Character.compute_damage_output(
        attacker.level,
        attacker.weapon.power,
        attacker.attack,
        defender.defense,
        1.0/16,
        0.15
    )
    defender.hp -= dmg
    print(f'{attacker.name} used {attacker.weapon.name} on {defender.name}')
    if crit :
        print('critical hit !')
    print(f'{dmg} dealt to {defender.name}')


def run_battle(c1, c2):
    # TODO: Initialiser attaquant/défendeur, tour, etc.
    attacker = c1
    defender = c2
    while True :
        deal_damage(attacker, defender)
        if defender.hp == 0 :
            print(f'{defender.name} is dead !!')
            break

    print('combat endeddd')