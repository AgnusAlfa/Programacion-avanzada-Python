

# 1. Escribir en un archivo

# Abrimos (o creamos) el archivo en modo escritura ('w')
# Usamos 'with' que es una buena práctica para asegurar el cierre automático
with open("datos.txt", "w") as archivo:
    archivo.write("Esta es la primera línea de mi archivo.\n")
    archivo.write("En la segunda línea estoy aprendiendo a manejar archivos.\n")
    archivo.write("Y esta es la tercera línea para completar el ejercicio.\n")

print("Archivo 'datos.txt' creado y escrito con éxito.")




# 2. LEER EL ARCHIVO COMPLETO

# Abrimos el archivo en modo lectura ('r')
print("\n--- Leyendo el archivo completo (read) ---")
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()  # Lee todo el contenido de una vez 
    print(contenido)




# 3. LEER LÍNEA POR LÍNEA

print("--- Leyendo línea por línea (readline + for) ---")
with open("datos.txt", "r") as archivo:
    # Usamos readline() para capturar solo la primera línea 
    primera_linea = archivo.readline()
    print(f"Primera línea capturada: {primera_linea.strip()}")
    
    # Luego, usamos un ciclo for para recorrer lo que queda del archivo 
    print("Resto del contenido línea por línea:")
    for linea in archivo:
        print(f"-> {linea.strip()}")




# 4. AÑADIR CONTENIDO (MODO APPEND

# Usamos el modo 'a' (append) para no borrar lo que ya escribimos antes
print("\n--- Añadiendo una línea nueva (modo append) ---")
with open("datos.txt", "a") as archivo:
    archivo.write("Esta es una cuarta línea agregada sin borrar las anteriores.\n")

# Comprobamos la lectura para ver el archivo actualizado
print("Contenido final del archivo:")
with open("datos.txt", "r") as archivo:
    print(archivo.read())



# 5. ATRIBUTOS Y CIERRE

print("\n--- Consultando atributos del archivo ---")

# Abrimos el archivo una última vez para ver sus datos técnicos
with open("datos.txt", "r") as archivo:
    print(f"Nombre del archivo (.name): {archivo.name}")
    print(f"Modo de apertura (.mode): {archivo.mode}")
    print(f"¿Está el archivo cerrado dentro del bloque? (.closed): {archivo.closed}")

# Aquí ya salimos del bloque 'with', por lo que el archivo debería cerrarse solo
print(f"¿Está el archivo cerrado fuera del bloque? (.closed): {archivo.closed}")