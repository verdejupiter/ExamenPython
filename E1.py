import random


def numberamdon():
    lista = []
    for item in range(0, 10):
        lista.append(random.randint(0, 100))
    return lista


def almacena(listini):
    lista = []
    for item in listini:
        if item not in lista:
            lista.append(item)
    return lista


def asdescende(lista):
    print("Lista ordenada de menor a mayor {}".format(sorted(lista)))
    print("Lista ordenada de mayor a menor {}".
          format(sorted(lista, reverse=True)))


def mayor(lista):
    return print("El número mayor de la lista es: {}".format(max(lista)))


lista1 = numberamdon()
print("La lista random es: {}".format(lista1))
lista2 = almacena(lista1)
asdescende(lista2)
mayor(lista2)
