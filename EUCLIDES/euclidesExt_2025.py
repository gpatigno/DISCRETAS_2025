# Implementación del Algoritmo de Euclides Extendido
def euclides_extendido(a, b):
    # Variables iniciales
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        cociente = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - cociente * x1
        y0, y1 = y1, y0 - cociente * y1
    return a, x0, y0  # MCD, coeficiente para a (d), coeficiente para b (k)

e = int(input("Ingrese el valor entero de e: "))
phi = int(input("Ingrese el valor entero de Phi_n: "))

# Calcular el MCD y los coeficientes d y k
mcd, d, k = euclides_extendido(e, phi)
print(f"MCD: {mcd}, d: {d}, k: {k}")
