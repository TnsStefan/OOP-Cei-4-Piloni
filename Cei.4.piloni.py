from abc import ABC, abstractmethod

# ABSTRACTION
# Clasa abstracta FormaGeometrica
# Contine un field PI=3.14
# Contine o metoda abstracta aria (optional)
# Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’


class FormaGeometrica(ABC):

    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descrie(cls):
        print('cel mai probabil am colturi')


# INHERITANCE
# Clasa Patrat - mosteneste FormaGeometrica
# constructor pt latura
# ENCAPSULATION
# latura este proprietate privata
# Implementati getter, setter, deleter pt latura
# Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura * self.__latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: Noua latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura = None


# Clasa Cerc - mosteneste FormaGeometrica
# constructor pt raza
# raza este proprietate privata
# Implementati getter, setter, deleter pt raza
# Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)
#
# POLYMORPHISM
# Definiti o noua metoda descrie - printati ‘Eu nu am colturi’


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza cercului este: {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Noua valoarea a razei este: {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Am sters valoarea razei')
        self.__raza = 0

    def aria(self):
        aria_cercului = self.PI * self.__raza * self.__raza
        return aria_cercului

    def descrie(self):
        print(f'Eu nu am colturi')



cercul = Cerc(5)
print(cercul.aria())
cercul.descrie()
print(cercul.raza)
del cercul.raza
print(cercul.raza)
cercul.raza = 7
print(cercul.raza)


print(100 *'*')

patratul = Patrat(10)
print(patratul.aria())
patratul.descrie()
print(patratul.latura)
del patratul.latura
print(patratul.latura)
patratul.latura = 15
print(patratul.latura)
