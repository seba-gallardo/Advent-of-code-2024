# Respuesta Dia 2 Advent of Code 2024 "Informes de Nariz Roja"

# Parte 1
def verificar_creciente(lista):
    for pos in range(len(lista) - 1): 
        if int(lista[pos]) < int(lista[pos+1]): 
            niveles = int(lista[pos+1]) - int(lista[pos])
            if niveles < 1 or niveles > 3:
                return "Inseguro" 
        else:
            return "Inseguro"
    return "Seguro"
    
def verificar_decreciente(lista):
    for pos in range(len(lista) - 1):
        if int(lista[pos]) > int(lista[pos+1]):
            niveles = int(lista[pos]) - int(lista[pos+1])
            if niveles < 1 or niveles > 3:
                return "Inseguro" 
        else:
            return "Inseguro"
    return "Seguro"

# Main
# Paso 1 Separar los informes por linea y evaluar
archivo = open("informes.txt") # Leer los datos de entrada
informes_Seguros = 0
for linea in archivo:
    informe = linea.split() # input
    # Comprobamos si es creciente o decreciente y validamos restricciones
    if int(informe[0]) < int(informe[1]):
        resultado = verificar_creciente(informe)   
    else:
        resultado = verificar_decreciente(informe)
    # Contamos la cantidad de informes seguros
    if resultado == "Seguro":
        informes_Seguros = informes_Seguros + 1
        
print(f" La cantidad de informes seguros es: {informes_Seguros}")
        
archivo.close()
