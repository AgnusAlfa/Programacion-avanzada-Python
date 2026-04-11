# 1. Definición de la Clase Base (Persona)
class Persona:
    def __init__(self, nombre, apellido, cedula, correo):
        # Usamos visibilidad protegida como en el diagrama
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._correo = correo

    # Método que usaremos para demostrar Polimorfismo más adelante
    def mostrar_datos(self):
        return f"Nombre: {self._nombre} {self._apellido} | CI: {self._cedula}"

# 2. Herencia: Clase Alumno
class Alumno(Persona):
    def __init__(self, nombre, apellido, cedula, correo, matricula, nivel):
        # Llamamos al constructor de la clase padre (Persona)
        super().__init__(nombre, apellido, cedula, correo)
        self.__matricula = matricula  # Privado
        self.__promedio_notas = 0.0
        self._nivel = nivel

    # Polimorfismo: Redefinimos el método mostrar_datos
    def mostrar_datos(self):
        base = super().mostrar_datos()
        return f"{base} | Matrícula: {self.__matricula} | Nivel: {self._nivel}"

# 3. Herencia: Clase Profesor
class Profesor(Persona):
    def __init__(self, nombre, apellido, cedula, correo, id_empleado, especialidad):
        super().__init__(nombre, apellido, cedula, correo)
        self.__id_empleado = id_empleado
        self._especialidad = especialidad

    # Polimorfismo: También redefinimos aquí
    def mostrar_datos(self):
        base = super().mostrar_datos()
        return f"{base} | ID: {self.__id_empleado} | Especialidad: {self._especialidad}"



# 4. Clase Asignatura
class Asignatura:
    def __init__(self, nombre_materia, codigo, horario):
        self.__nombre_materia = nombre_materia
        self.__codigo = codigo
        self.__horario = horario
        self.__alumnos_inscritos = [] # Lista para interacción entre objetos

    def obtener_detalle(self):
        return f"Asignatura: {self.__nombre_materia} [{self.__codigo}] - Horario: {self.__horario}"

    # Sobrecarga de métodos (Simulada con argumentos opcionales)
    # Requerimiento de la actividad 
    def inscribir(self, estudiante, beca=None):
        self.__alumnos_inscritos.append(estudiante)
        if beca:
            print(f"Inscripción exitosa: {estudiante._nombre} con beca del {beca}%.")
        else:
            print(f"Inscripción regular: {estudiante._nombre} registrado en {self.__nombre_materia}.")

# --- PROGRAMA PRINCIPAL (Interacción entre objetos)  ---

if __name__ == "__main__":
    # 1. Instanciar objetos
    profe_pablo = Profesor("Pablo", "Neruda", "12.345.678-9", "pablo@poesia.cl", 101, "Literatura")
    alumno_lucia = Alumno("Lucila", "Godoy", "11.222.333-4", "lucila@escuela.cl", 202401, "3er Año")
    mate_base = Asignatura("Poesía Chilena", "LIT101", "Lunes 09:00")

    print("ESTADO INICIAL DEL SISTEMA")
    
    # 2. Polimorfismo en acción 
    # Ambos objetos usan 'mostrar_datos' pero responden distinto
    personas = [profe_pablo, alumno_lucia]
    for p in personas:
        print(p.mostrar_datos())

    print("\nGESTIÓN DE ASIGNATURAS")
    
    # 3. Interacción y Sobrecarga [cite: 70, 72]
    print(mate_base.obtener_detalle())
    
    # Uso de sobrecarga: llamada sin parámetro extra
    mate_base.inscribir(alumno_lucia) 
    
    # Uso de sobrecarga: llamada con parámetro extra (beca)
    alumno_dos = Alumno("Jorge", "Teillier", "9.888.777-6", "jorge@sur.cl", 202402, "1er Año")
    mate_base.inscribir(alumno_dos, beca=50)