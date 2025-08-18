# Respuesta Dia 2 Advent of Code 2024 "Informes de Nariz Roja"

# Parte 1 version 2
def verificar_informe(lista):
    if int(lista[0]) < int(lista[1]): # Es Creciente
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
    
    # --- Parte 2: aplicar amortiguador real ---
    if resultado == "Inseguro":
        # Probar eliminando un número en cada posición
        seguro_con_amortiguador = False
        for i in range(len(informe)):
            nuevo = informe[:i] + informe[i+1:]   # copia sin el i-ésimo
            if verificar_informe(nuevo) == "Seguro":
                seguro_con_amortiguador = True
                break
        if seguro_con_amortiguador:
            resultado = "Seguro"
            
    print(f"{informe} es: {resultado}")
    if resultado == "Seguro":
        informes_Seguros = informes_Seguros + 1
        
print(f" La cantidad de informes seguros es: {informes_Seguros}")
        
archivo.close()
