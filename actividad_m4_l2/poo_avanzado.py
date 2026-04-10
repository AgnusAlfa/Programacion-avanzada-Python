

# 1. Definición de una clase con constructor

class Libro:
    # Definimos el constructor para inicializar titulo, autor y anio_publicacion
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    # Método para mostrar la información del libro
    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")

# Ejemplo de uso para probar el ítem 1
mi_libro = Libro("Los detectives salvajes", "Roberto Bolano", 1998)
mi_libro.mostrar_info()



# 2. Métodos accesadores y mutadores

class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        # Usamos el prefijo _ para indicar que son atributos protegidos
        self._titulo = titulo
        self._autor = autor
        self._anio_publicacion = anio_publicacion

    def mostrar_info(self):
        print(f"Título: {self._titulo}")
        print(f"Autor: {self._autor}")
        print(f"Año de publicación: {self._anio_publicacion}")

    # Métodos para el atributo 'titulo' 
    def get_titulo(self):
        return self._titulo

    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    # Métodos para el atributo "anio_publicacion"
    def get_anio_publicacion(self):
        return self._anio_publicacion

    def set_anio_publicacion(self, nuevo_anio):
        self._anio_publicacion = nuevo_anio

# Programa Principal

# Creamos la instancia inicial
mi_libro = Libro("Los detectives salvajes", "Roberto Bolano", 1998)

# Usamos el método mutador (set) para modificar el título
print(f"Título actual: {mi_libro.get_titulo()}")
mi_libro.set_titulo("Los detectives salvajes - Edición Especial")

# Verificamos el cambio con el método accesador (get)
print(f"Título modificado: {mi_libro.get_titulo()}")



# 3. Sobrecarga de métodos (Actualizado con Roberto Bolano)

class Autor:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

class Libro:
    def __init__(self, titulo, autor_obj, anio_publicacion):
        self._titulo = titulo
        self._autor = autor_obj
        self._anio_publicacion = anio_publicacion

    # Método para simular sobrecarga
    def resumen(self, texto=None):
        if texto is None:
            print("Libro sin resumen disponible")
        else:
            print(f"Resumen de '{self._titulo}': {texto}")

# Pruebas del Ítem 3

# Definimos al autor y al libro con tus nuevos datos
autor_bolano = Autor("Roberto Bolano", "Chile")
mi_libro = Libro("Los detectives salvajes", autor_bolano, 1998)

# Prueba 1: Sin pasar parámetros
mi_libro.resumen() 

# Prueba 2: Pasando un resumen real
mi_libro.resumen("Una odisea a través de México y el mundo en busca de una poeta desaparecida.")



# 4. Colaboración entre objetos

# Definimos la clase Autor
class Autor:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

# Modificamos la clase Libro para que el atributo autor sea un objeto de tipo Autor
class Libro:
    def __init__(self, titulo, autor_obj, anio_publicacion):
        self._titulo = titulo
        self._autor = autor_obj  # Recibe un objeto de la clase Autor
        self._anio_publicacion = anio_publicacion

    def mostrar_info(self):
        print(f"Título: {self._titulo}")
        # Accedemos a los atributos del objeto Autor que colabora con Libro
        print(f"Autor: {self._autor.nombre}")
        print(f"País: {self._autor.pais}")
        print(f"Año de publicación: {self._anio_publicacion}")

    # Mantenemos el método resumen del ítem anterior
    def resumen(self, texto=None):
        if texto is None:
            print("Libro sin resumen disponible")
        else:
            print(f"Resumen de '{self._titulo}': {texto}")

# Pruebas del Ítem 4

# 1. Creamos el objeto autor (Roberto Bolaño)
autor_bolano = Autor("Roberto Bolaño", "Chile")

# 2. Creamos el objeto libro pasando el objeto autor como parámetro
mi_libro = Libro("Los detectives salvajes", autor_bolano, 1998)

# 3. Verificamos la colaboración
mi_libro.mostrar_info()



# 5. Composición

class Editorial:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

class Autor:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

class Libro:
    # El constructor ahora recibe también los datos para la editorial
    def __init__(self, titulo, autor_obj, anio, ed_nombre, ed_ciudad):
        self._titulo = titulo
        self._autor = autor_obj
        self._anio_publicacion = anio
        
        # COMPOSICIÓN: Creamos el objeto Editorial AQUÍ ADENTRO
        self._editorial = Editorial(ed_nombre, ed_ciudad)

    def mostrar_info(self):
        print(f"--- Ficha del Libro ---")
        print(f"Título: {self._titulo}")
        print(f"Autor: {self._autor.nombre} ({self._autor.pais})")
        print(f"Año: {self._anio_publicacion}")
        # Accedemos al objeto editorial creado internamente
        print(f"Editorial: {self._editorial.nombre}")
        print(f"Ciudad: {self._editorial.ciudad}")
        print(f"-----------------------")

# Prueba del Ítem 5

# Seguimos con Bolaño
autor_bolano = Autor("Roberto Bolaño", "Chile")

# Al crear el libro, pasamos también los datos de la editorial (Anagrama, Barcelona)
mi_libro_final = Libro(
    "Los detectives salvajes", 
    autor_bolano, 
    1998, 
    "Anagrama", 
    "Barcelona"
)

mi_libro_final.mostrar_info()