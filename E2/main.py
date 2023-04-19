
from funciones import listaa, cuadrada

file = open("my_files/notas.txt", "a+")
file.close()

listaa("my_files/notas.txt")
cuadrada("my_files/notas.txt")
