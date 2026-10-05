def recorrer(n1, n2):
    if n1 < n2:
        lista = list(range(n1, n2))
        multiplos = [x for x in lista if x % 3 == 0]
        if len(multiplos) == 0:
            return None
        return max(multiplos)
    else:
        lista = list(range(n1, n2, -1))
        multiplos = [x for x in lista if x % 3 == 0]
        if len(multiplos) == 0:
            return None
        return min(multiplos)


n1 = int(input('Ingrese numero de inicio: '))
n2 = int(input('Ingrese numero de fin: '))

resultado = recorrer(n1, n2)

if n1 < n2:
    print(f'De {n1} hacia {n2}, el maximo multiplo de 3 es: {resultado}')
else:
    print(f'De {n1} hacia {n2}, el minimo multiplo de 3 es: {resultado}')