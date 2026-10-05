def maximoMultiplo(n1, n2, actual):
    if n1 == n2:
        return actual
    if n1 % 3 == 0:
        actual = n1
    return maximoMultiplo(n1 + 1, n2, actual)


def minimoMultiplo(n1, n2, actual):
    if n1 == n2:
        return actual
    if n1 % 3 == 0:
        actual = n1
    return minimoMultiplo(n1 - 1, n2, actual)


n1 = int(input('Ingrese numero de inicio: '))
n2 = int(input('Ingrese numero de fin: '))

if n1 < n2:
    resultado = maximoMultiplo(n1, n2, -1)
    if resultado == -1:
        print(f'De {n1} hacia {n2}, no hay multiplos de 3')
    else:
        print(f'De {n1} hacia {n2}, el maximo multiplo de 3 es: {resultado}')
else:
    resultado = minimoMultiplo(n1, n2, -1)
    if resultado == -1:
        print(f'De {n1} hacia {n2}, no hay multiplos de 3')
    else:
        print(f'De {n1} hacia {n2}, el minimo multiplo de 3 es: {resultado}')