

# 1. Captura básica de errores

try:
    # Pedimos al usuario que ingrese dos números para dividir
    numerador = float(input("Ingresa el primer número (dividendo): "))
    denominador = float(input("Ingresa el segundo número (divisor): "))
    
    resultado = numerador / denominador
    print(f"Genial, el resultado es: {resultado}")

except ZeroDivisionError:
    # Este mensaje se muestra si el usuario pone un 0 abajo
    print("Oye, recuerda que en matemáticas no se puede dividir por cero. ¡Intenta con otro número!")



# 2. Múltiples excepciones

try:
    # Intentamos convertir la entrada directamente a float
    numerador = float(input("Ingresa el dividendo: "))
    denominador = float(input("Ingresa el divisor: "))
    
    resultado = numerador / denominador
    print(f"Resultado: {resultado}")

except ZeroDivisionError:
    # Se ejecuta si el denominador es 0
    print("Error: No puedes dividir por cero.")

except ValueError:
    # Se ejecuta si el usuario ingresa letras o símbolos en lugar de números
    print("Error: Por favor, ingresa solo valores numéricos.")


# 3. Excepciones personalizadas

# Definimos nuestra propia clase de error heredando de Exception
class EdadInvalidaError(Exception):
    """Excepción lanzada cuando la edad es negativa."""
    pass

def validar_edad(edad):
    # Si la edad es menor a 0, "lanzamos" nuestra alarma personalizada
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser un número negativo.")
    else:
        print(f"Edad validada correctamente: {edad} años.")

# --- Prueba del Ítem 3 ---
try:
    valor_edad = int(input("Por favor, ingresa tu edad: "))
    validar_edad(valor_edad)

except EdadInvalidaError as e:
    # Capturamos nuestra propia excepción y mostramos el mensaje que definimos
    print(f"Error de validación: {e}")

except ValueError:
    print("Error: La edad debe ser un número entero.")



# 4. Limpieza de recursos

def procesar_archivo():
    try:
        # Simulamos la apertura de un archivo
        print("Intentando abrir el archivo de datos...")
        
        # Simulamos un error durante el procesamiento
        opcion = input("¿Quieres simular un error de lectura? (s/n): ")
        if opcion.lower() == 's':
            raise Exception("Error inesperado al leer el archivo.")
        
        print("Archivo procesado con éxito.")

    except Exception as e:
        print(f"Se capturó un problema: {e}")

    finally:
        # Este bloque se ejecuta SIEMPRE, haya error o no
        print("Cerrando archivo y liberando memoria...")
        print("Limpieza de recursos completada.")

# Prueba del Ítem 4
procesar_archivo()