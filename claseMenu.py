from claseConjunto import Conjunto

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            0:self.salir
                          }
    def opcion(self,op,unconjunto,otroconjunto):
        print(op)
        func=self.__switcher.get(op,lambda: print("Opción no válida"))
        func(unconjunto,otroconjunto)

    def salir(self,unconjunto,otroconunto):
        print('Usted salio del programa')
    def opcion1(self,unconjunto,otroconjunto):
        c=unconjunto+otroconjunto
        print(c)


    def opcion2(self,unconjunto,otroconjunto):
        c=unconjunto-otroconjunto
        print(c)


    def opcion3(self,unconjunto,otroconjunto):
        unconjunto==otroconjunto

        
