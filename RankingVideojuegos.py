#Henrik Anderson Oloroso Garcia
'''Desarrolle un programa en Python que permita mantener un registro de videojuegos y sus puntuaciones promedio (0–10).
El usuario podrá añadir nuevos títulos, actualizar la puntuación de uno existente, y consultar cuáles son los tres juegos mejor valorados.
Se trata de trabajar con diccionarios donde las claves son los nombres de los juegos y los valores sus puntuaciones.

Objetivo

Practicar la inserción, actualización y ordenamiento de datos en un diccionario.

Requisitos funcionales

    Iniciar un diccionario vacío o con algunos títulos predefinidos.
    Función add_game(name, score) para agregar o actualizar un juego.
    Función top_n(n) que devuelva una lista de tuplas con los n juegos mejor puntuados, en orden descendente.
    Interfaz de consola para: listar todos los juegos, añadir/actualizar puntuación, mostrar Top 3.'''

'''Resultado esperado

Al arrancar, muestra un menú:

    Listar juegos
    Añadir/actualizar juego
    Mostrar Top 3
    Salir

Al elegir Top 3, imprime tres tuplas (juego, puntuación) ordenadas de mayor a menor.'''