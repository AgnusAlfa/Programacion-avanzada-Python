# Programacion-avanzada-Python


ACTIVIDAD MÓDULO 4, LECCIÓN 1

Mi reflexión:
Lo que más me llamó la atención fue el cambio de chip. Venía acostumbrado a programar de forma más estructurada (pensando solo en el orden de las funciones y la lógica suelta) y pasar a la POO te obliga a organizar todo de una manera mucho más real, como si estuvieras armando piezas de un sistema.
Me pareció especialmente interesante el tema del encapsulamiento. Antes dejaba todas las variables expuestas, pero el hecho de usar el prefijo "_" para proteger los datos y manejar la información solo a través de métodos como "mostrar_info()" hace que el código se vea mucho más profesional y ordenado. Es una forma distinta de ver los datos, ya no son solo variables, es el "estado" de un objeto que tiene su propia lógica.



ACTIVIDAD MÓDULO 4, LECCIÓN 2

Mi reflexión:
Personalmente, la relación que me resultó más fácil de implementar fue la colaboración. Me pareció muy intuitivo crear el objeto del autor (en este caso Roberto Bolaño) de forma independiente y luego simplemente "pasárselo" al libro como un parámetro más.

La composición me tomó un poco más de trabajo mental al principio, sobre todo por el hecho de tener que generar la editorial directamente dentro del constructor del libro. Pero una vez que lo ejecutas, entiendes la lógica: la editorial pertenece a la existencia de ese libro en particular dentro del programa. Aunque la colaboración es más sencilla de escribir, la composición me parece una forma más ordenada de asegurar que ciertos datos no queden "volando" sueltos si el objeto principal desaparece.



ACTIVIDAD MÓDULO 4, LECCIÓN 3

Explicación del despliegue del diagrama:
Para este modelo de sistema educacional, decidí estructurar el diseño partiendo de una clase base llamada "Persona". La idea principal fue aprovechar la herencia para que tanto los alumnos como los profesores compartan los datos básicos (nombre, rut, correo) sin tener que repetirlos en cada tabla. 

En el diagrama, se puede ver claramente cómo:
-Los Alumnos y Profesores heredan de Persona (indicado con las flechas de triángulo).
-Apliqué encapsulamiento usando visibilidad protegida (#) en la clase padre y privada (-) en los datos específicos como sueldos o matrículas, para que la información esté segura.
-Las relaciones de "cursa" y "dicta" conectan a los usuarios con las "Asignaturas", que es el núcleo donde se cruza toda la información académica.



ACTIVIDAD MÓDULO 4, LECCIÓN 4

Resumen de la implementación:
En este proyecto pasamos el diagrama del sistema educacional a código funcional. Lo más interesante fue aplicar el polimorfismo, creé una clase base "Persona" para que "Alumno" y "Profesor" compartieran la lógica de mostrar datos, pero cada uno le añade sus propios detalles técnicos de forma automática.

También implementé la sobrecarga en el método de inscripción de materias, permitiendo que el sistema sea flexible si un alumno tiene beca o no. Todo el proyecto está organizado bajo la estructura de carpetas solicitada para asegurar que los objetos interactúen de forma limpia y profesional.



ACTIVIDAD MÓDULO 4, LECCIÓN 5

1.¿Qué tipo de error crees que es más común en programas reales?
En mi opinión, el error más común en programas reales es el relacionado con la entrada de datos del usuario (como ValueError). Es muy frecuente que un usuario ingrese texto cuando se espera un número, o que deje campos vacíos. También son muy comunes los errores de archivos no encontrados o fallos en la conexión a bases de datos, situaciones que el programador no siempre puede controlar directamente pero que debe prever.

2.¿Por qué es importante manejar excepciones?
El manejo de excepciones es fundamental para garantizar la robustez y estabilidad de una aplicación. Sin este control, cualquier error inesperado provocaría que el programa se cerrara abruptamente ("crasheara"), mostrando mensajes técnicos confusos al usuario final. Al capturar excepciones, permitimos que el programa responda de manera controlada, informe del problema de forma amigable y pueda seguir funcionando o cerrarse de forma segura sin pérdida de datos.



ACTIVIDAD MÓDULO 4, LECCIÓN 6

1.¿Qué diferencia notaste entre write() y append()?
La diferencia es crítica para la integridad de los datos. El método write() abre el archivo en modo escritura ('w'), lo que significa que si el archivo ya existe, borrará todo su contenido para empezar desde cero[cite: 57, 58]. Por el contrario, append() abre el archivo en modo anexar ('a'), lo que permite añadir nueva información justo al final de lo que ya existe, sin borrar nada de lo anterior[cite: 65, 66].

2.¿Qué ventaja tiene usar with open(...) frente a abrir y cerrar manualmente?
La ventaja principal es la gestión automática de recursos. Al usar 'with', Python garantiza que el archivo se cierre correctamente al terminar el bloque de código, incluso si ocurre un error durante el proceso[cite: 69]. Esto nos ahorra tener que escribir manualmente archivo.close() y evita que el sistema pierda datos o consuma memoria innecesaria por dejar archivos abiertos por accidente.