# 1. Exploración teórica

# ¿Qué es la programación orientada a objetos?
# Es un paradigma de programación que utiliza "objetos" para diseñar aplicaciones y programas informáticos. 
# Estos objetos agrupan datos (atributos) y las funciones que operan sobre esos datos (métodos) en una sola unidad.

# ¿En qué se diferencia de la programación estructurada?
# Mientras que la programación estructurada se centra en la lógica de los procedimientos y el flujo de control 
# mediante funciones y bloques, la POO se centra en la organización de los datos y la interacción entre objetos. 
# En la POO, los datos y las funciones están estrechamente vinculados dentro de las clases.

# Ejemplo de la vida cotidiana:
# Un "Smartphone" puede verse como un objeto. 
# Tiene atributos (marca, modelo, color, nivel de batería) y métodos o comportamientos 
# (hacer una llamada, tomar una foto, enviar un mensaje).



# 2. Definición de una clase simple 

# Creamos la clase llamada Perro 
class Perro:
    # El método __init__ se usa para inicializar los atributos: nombre, edad y raza 
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    # Definimos el método ladrar() que imprime "¡Guau!" 
    def ladrar(self):
        print("¡Guau!")

# Creamos una instancia de la clase Perro 
mi_perro = Perro("Boby", 3, "Labrador")

# Llamamos al método ladrar() de la instancia creada 
mi_perro.ladrar()



# 3. Diferenciar conceptos

# Diferencia entre Clase, Instancia y Objeto:
# - Clase: Es el plano, molde o "blueprint" que define las reglas (atributos y métodos).
# - Objeto: Es la entidad creada a partir de la clase que ocupa un lugar en memoria.
# - Instancia: Es el proceso de creación de un objeto específico o el objeto mismo en relación a su clase. 
#   Por ejemplo, 'Perro' es la clase y 'mi_perro' es una instancia/objeto de esa clase.

# Diferencia entre Atributo y Estado:
# - Atributo: Es la variable definida dentro de la clase (nombre, edad, raza).
# - Estado: Es el valor actual de esos atributos en un momento específico para un objeto determinado.
#   Ejemplo: El estado de 'mi_perro' es {nombre: "Boby", edad: 3, raza: "Labrador"}.

# Diferencia entre Método y Comportamiento:
# - Método: Es la función definida dentro de la clase (ladrar()).
# - Comportamiento: Es la acción o reacción que el objeto realiza cuando se ejecuta el método.
#   En nuestro ejemplo, el comportamiento es la impresión de "¡Guau!" en la consola.



# 4. Principios de POO

class Perro:
    # Modificamos los atributos para que estén encapsulados usando el prefijo _
    def __init__(self, nombre, edad, raza):
        self._nombre = nombre
        self._edad = edad
        self._raza = raza

    def ladrar(self):
        print("¡Guau!")

    # Agregamos el método mostrar_info() que devuelve el estado como texto
    def mostrar_info(self):
        return f"Perro: {self._nombre}, Edad: {self._edad}, Raza: {self._raza}"

# Abstracción:
# La abstracción consiste en enfocarse en las características esenciales de un objeto 
# ocultando los detalles complejos de su implementación. En este ejemplo, el usuario 
# de la clase solo necesita saber que puede llamar a 'mostrar_info()' para obtener 
# los datos, sin preocuparse por cómo están almacenados internamente los atributos.

# Probamos la modificación
mi_perro_mejorado = Perro("Boby", 3, "Labrador")
print(mi_perro_mejorado.mostrar_info())