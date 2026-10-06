def multClasica(u, v):
    return u * v


def mult(u, v):
    n = max(len(str(u)), len(str(v)))
    if n <= 2:
        return multClasica(u, v)
    s = n // 2
    potencia = 10 ** s
    w = u // potencia
    x = u % potencia
    y = v // potencia
    z = v % potencia
    return (mult(w, y) * (10 ** (2 * s))) + ((mult(w, z) + mult(x, y)) * (10 ** s)) + mult(x, z)

u = int(input('Ingrese primer numero: '))
v = int(input('Ingrese segundo numero: '))

resultado = mult(u, v)

print(f'{u} x {v} = {resultado}')