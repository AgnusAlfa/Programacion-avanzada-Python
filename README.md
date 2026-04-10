# Programacion-avanzada-Python

#ACTIVIDAD MÓDULO 4, LECCIÓN 1

Mi reflexión:
Lo que más me llamó la atención fue el cambio de chip. Venía acostumbrado a programar de forma más estructurada (pensando solo en el orden de las funciones y la lógica suelta) y pasar a la POO te obliga a organizar todo de una manera mucho más real, como si estuvieras armando piezas de un sistema.
Me pareció especialmente interesante el tema del encapsulamiento. Antes dejaba todas las variables expuestas, pero el hecho de usar el prefijo "_" para proteger los datos y manejar la información solo a través de métodos como "mostrar_info()" hace que el código se vea mucho más profesional y ordenado. Es una forma distinta de ver los datos, ya no son solo variables, es el "estado" de un objeto que tiene su propia lógica.


#ACTIVIDAD MÓDULO 4, LECCIÓN 1

Mi reflexión:
Personalmente, la relación que me resultó más fácil de implementar fue la colaboración. Me pareció muy intuitivo crear el objeto del autor (en este caso Roberto Bolaño) de forma independiente y luego simplemente "pasárselo" al libro como un parámetro más.

La composición me tomó un poco más de trabajo mental al principio, sobre todo por el hecho de tener que generar la editorial directamente dentro del constructor del libro. Pero una vez que lo ejecutas, entiendes la lógica: la editorial pertenece a la existencia de ese libro en particular dentro del programa. Aunque la colaboración es más sencilla de escribir, la composición me parece una forma más ordenada de asegurar que ciertos datos no queden "volando" sueltos si el objeto principal desaparece.