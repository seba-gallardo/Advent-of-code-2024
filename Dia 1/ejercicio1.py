# Respuesta Dia 1 Advent of Code 2024 "Histeria del historiador"

# Parte 1
# Paso 1 Dividir las filas en dos listas
archivo = open("datos.txt") # Leer los datos de entrada
lista1, lista2 = [], []
for linea in archivo:
    dato = linea.split() # input
    lista1.append(dato[0]) # lista de la izquierda
    lista2.append(dato[1]) # lista de la derecha
archivo.close()

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

# Parte 2
# Paso 1 Averiguar con qué frecuencia aparece cada número de la lista izquierda en la lista derecha.
def calcular_similitud(lista1, lista2):
    similitudes = []
    for valor in lista1:
        frecuencia = int(valor) * int(lista2.count(valor))
        # print(f"la frecuencia de {valor} es: {frecuencia}")
        similitudes.append(frecuencia)
    return similitudes

# Paso 2 Calcular la similitud total entre ambas listas
resultado_similitudes = calcular_similitud(lista1, lista2)
total_similitud = sum(resultado_similitudes)
print(f"La similitud total entre ambas listas es: {total_similitud}")