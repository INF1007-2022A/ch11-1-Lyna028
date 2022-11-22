class vehicule :
    def __init__(self, nom, nbderoues, moteur):
        self.__nom = nom
        self.nbderoues = nbderoues
        self.moteur = moteur

    @property
    def nom(self):
        return self.__nom

    def rouler(self, distance_km):
       print(f'{self.nom} roule sur {distance_km} km')


class velo(vehicule) : #fonction heritee qui herite des caracteristiques de la fonctiom mere
    def __init__(self, nom):
        super().__init__(nom,2)

    def rouler(self, distance_km):
        print(f'{self.nom} roule sur {distance_km} km')

class auto(vehicule) :
    def __init__(self, nom, nbrederoues, moteur):
        super().__init__(nom, nbrederoues)
        self.moteur = moteur
        self.est_demarre = False

    def rouler (self, distance_km):
        if self.est_demarre :
            print(f'haha {self.nom} a demarre et roule sur {distance_km} km')
        else :
            print(f'{self.nom} n\'a pas demmrre ')

    def demarrer(self):
        print('lets gooo')
        self.est_demarrer = True

def fn(vehicules : vehicule, distance):
    print(f'j\'ai choisie {vehicules.nom} qui a {vehicules.nbderoues} rouees.')
    vehicule.rouler(distance)


def main () :
    v1 = vehicule("une brouette", 1)
    v2 = auto('mon char', 4, 'moteur VG')
    v3 = velo('mon velo')
    v1.rouler(1)
    v2.demarrer()
    v2.rouler(43)
    v3.rouler(32)


if __name__ == '__main__' :
    main()