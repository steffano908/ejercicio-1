import random


def crearLista(cantidad, lista):
    if cantidad == 0:
        return lista
    numero = random.randint(10, 99)
    lista.append(numero)
    return crearLista(cantidad - 1, lista)


def sumarMultiplos(lista, pos, suma):
    if pos == len(lista):
        return suma
    if lista[pos] % 3 == 0:
        suma = suma + lista[pos]
    return sumarMultiplos(lista, pos + 1, suma)


cantidad = int(input('Ingrese cantidad de elementos: '))

lista = []
crearLista(cantidad, lista)

print(f'Lista generada: {lista}')

resultado = sumarMultiplos(lista, 0, 0)

print(f'Suma de multiplos de 3: {resultado}')