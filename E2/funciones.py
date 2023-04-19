import random
import math


def listaa(name):
    var = int(input("Ingrese el tamaño de la lista: "))
    file = open(name, "a+")

    for item in range(0, var):
        file.write(str(random.randint(0, 20)) + "\n")

    file.close()


def cuadrada(name):
    with open(name, "r") as archivo:
        lista = "\n La raíz cuadrada de los números son: \n"
        for linea in archivo:
            a = math.sqrt(int(linea))
            lista = lista + str(a) + "\n"

    file = open(name, "a+")
    file.write(lista)
    file.close()
