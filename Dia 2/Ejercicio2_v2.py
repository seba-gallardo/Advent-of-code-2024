# Respuesta Dia 2 Advent of Code 2024 "Informes de Nariz Roja"

# Parte 1 version 2
def verificar_informe(lista):    
    if int(informe[0]) < int(informe[1]): # Es Creciente
        for pos in range(len(lista) - 1): 
            if int(lista[pos]) < int(lista[pos+1]): 
                niveles = int(lista[pos+1]) - int(lista[pos]) # Obtener nivel
                if niveles < 1 or niveles > 3: # Comprobar niveles
                    return "Inseguro" 
            else:
                return "Inseguro"
    else: # Es Decreciente o Igual
        for pos in range(len(lista) - 1): 
            if int(lista[pos]) > int(lista[pos+1]):
                niveles = int(lista[pos]) - int(lista[pos+1]) # Obtener nivel
                if niveles < 1 or niveles > 3: # Comprobar niveles
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
    # Comprobar si el informe es seguro o inseguro
    resultado = verificar_informe(informe) 
    if resultado == "Seguro":
        informes_Seguros = informes_Seguros + 1
        
print(f" La cantidad de informes seguros es: {informes_Seguros}")
        
archivo.close()
