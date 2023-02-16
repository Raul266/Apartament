from abc import abstractmethod
class Apartament:
    suprafata_mp = None
    mobilat = None
    balcon = None
    numar_camere = None

    def __init__(self, suprafata_mp,mobilat,balcon,numar_camere):
        self.suprafata_mp = suprafata_mp
        self.mobilat = mobilat
        self.balcon = balcon
        self.numar_camere = numar_camere

    @abstractmethod
    def suprafata_ap(self):
        print(f'Ati achizitionat un ap cu suprafata de {self.suprafata_mp}mp')
    def mobilier(self):
        if self.mobilat.lower() == 'da':
            print('Ati achizitionat un ap mobilat')
        else:
            print('Ati achizitionat un ap nemobilat')
    def are_sau_nu_balcon(self):
        if self.balcon.lower() == 'da':
            print('Ati achizitionat un ap cu balcon')
        else:
            print('Ati achizitionat un ap fara balcon')
    def numarul_de_camere(self):
            print(f'Ati achizitionat un ap cu {self.numar_camere} camere')

    def pret_mp(self):
        if self.suprafata_mp <= 40:
            print('Pretul pe metrul patrat este de 2000$')
        elif self.suprafata_mp > 40 and self.suprafata_mp <= 90:
            print('Pretul pe metrul patrat este de 1800$')
        elif self.suprafata_mp > 90:
            print('Pretul pe metrul patrat este de 1500$')
ap = Apartament(90,'nu','da',2)
print(ap.mobilat)
ap.mobilier()
ap.are_sau_nu_balcon()
ap.numarul_de_camere()
ap.pret_mp()

