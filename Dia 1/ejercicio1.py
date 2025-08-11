# Respuesta Dia 1 Advent of Code 2024 "Histeria del historiador"

# Paso 1 Dividir las filas en dos listas
archivo = open("datos.txt")
lista1, lista2 = [], []
for linea in archivo:
    dato = linea.split() # input
    lista1.append(dato[0]) # lista de la izquierda
    lista2.append(dato[1]) # lista de la derecha

# Paso 2 Ordenar las listas de menor a mayor
lista1.sort() 
lista2.sort()

# Paso 3 Calcular las distancias
def calcular_distancia(lista1, lista2):
    distancias = []
    for pos in range(1000):
        if lista1[pos] >= lista2[pos]:
            resultado = int(lista1[pos]) - int(lista2[pos])
        else:
            resultado = int(lista2[pos]) - int(lista1[pos])
        distancias.append(resultado)
    return distancias

resultado_distancias = calcular_distancia(lista1, lista2)

# Paso 4 Calcular la distancia total entre ambas listas
total_distancias = sum(resultado_distancias)
print(f"La distancia total entre ambas listas es: {total_distancias}")
