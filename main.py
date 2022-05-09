from claseConjunto import Conjunto
from claseMenu import Menu
def test(conjuntouno,conjuntodos):
    conjuntouno.agregar(1)
    conjuntouno.agregar(2)
    conjuntouno.agregar(3)
    conjuntodos.agregar(3)
    conjuntodos.agregar(2)
    conjuntodos.agregar(4)

if __name__ == '__main__':
    unconjunto=Conjunto()
    otroconjunto=Conjunto()
    test(unconjunto,otroconjunto)
    bandera = False
    while not bandera:
        print("\nMENU DE OPCIONES")
        print("0 Salir")
        print("1 ITEM 8.1: La unión de dos conjuntos, para ello sobrecargue el operador binario suma (+)..")
        print("2 ITEM 8.2: La diferencia de dos conjuntos, para ello sobrecargue el operador binario resta (-).")
        print("3 ITEM 8.3:  Verificar si dos conjuntos son iguales, para ello sobrecargue el operador “==”")

        opcion = int(input('Ingrese una opcion:'))
        unmenu=Menu()
        unmenu.opcion(opcion,unconjunto,otroconjunto)
        bandera = int(opcion)== 0





