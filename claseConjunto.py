class Conjunto:
    __numeros=[]


    def __init__(self):
        self.__numeros=[]

    def inicializar(self):
        j=input("Ingrese el numero del conjunto  >> :")
        self.__numeros.append(j)
        op=input("¿Desea ingresar un nuevo numero? \n  Ingrese 1 en caso de querer seguir agregando numeros o 2 en caso de no querer agregar mas numeros >>: ")
        while(int(op)!=2):
            j=input("Ingrese el numero del conjunto  >> :")
            self.__numeros.append(j)
            op=input("¿Desea ingresar un nuevo numero? \n  Ingrese 1 en caso de querer seguir agregando numeros o 2 en caso de no querer agregar mas numeros >>: ")

    def obtenerLista(self):
        return self.__numeros

    def agregar(self,num):
        self.__numeros.append(num)

    def __add__(self, other):
        lista=self.__numeros.copy()
        for i in range(len(other.obtenerLista())):
           j=0
           while((j<len(self.__numeros))and (self.__numeros[j]!=other.obtenerLista()[i])):
               j+=1
           if j>=len(self.__numeros):
               lista.append(other.obtenerLista()[i])
        return lista

    def __sub__(self, other):
        lista=self.__numeros.copy()
        for i in range(len(other.obtenerLista())):
           j=0
           while((j<len(self.__numeros))and (self.__numeros[j]!=other.obtenerLista()[i])):
               j+=1
           if j<len(self.__numeros):
               del lista[j]
        return lista

    def __eq__(self, other):
        print(self.__numeros)
        print(other.obtenerLista())
        print(type(other))
        if len(other.obtenerLista())!=len(self.__numeros):
            print("Los conjuntos  son distintos")
        i=0
        bandera=True
        while(i<len(other.obtenerLista()))and(bandera==True):
            j=0
            while(j<(len(other.obtenerLista())))and(self.__numeros[j]!=other.obtenerLista()[i]):
                j+=1
            if j>=len(other.obtenerLista()):
                print("Los conjuntos  son distintos")
                bandera=False
            i+=1
        print(bandera)
        if bandera==True:
            print("Los conjuntos  son iguales")


















    def mostrarConjunto(self):
        for numero in self.__numeros:
            print(numero)






