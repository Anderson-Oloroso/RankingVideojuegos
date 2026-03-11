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

def menu():
   global op
   print("\n=========== Menu ==========")
   print("1. Añadir juegos")
   print("2. Actualizar puntuación")
   print("3. Juegos mejor valorados")
   print("4. Salir")


   op = int(input("Opción: "))
   return op

videojuegos = {
       "call of duty": 9.5,
       "blood strike": 7.6,
       "clash royale": 8.9,
       "minecraft": 7.3
   }
global a

def add_game(nombre, puntuacion):
   
   videojuegos[nombre] = puntuacion
   
   print("Videojuego agregado correctamente\n")
   return videojuegos

def actualizarPuntuacion():
   print("\n=========== Actualizar puntuacion ==========")
   name = input("Videojuego al que se actualizara la puntuacion: ")
   while name not in videojuegos:
    name = input("Videojuego al que se actualizara la puntuacion: ")

   puntos = float(input("Nueva puntuación: "))
   videojuegos[name] = puntos
  
def top_n():
    print("\n=========== Top 3 mejores juegos ==========")
    ordenJuegos = sorted(videojuegos.items(), key=lambda x: x[1], reverse= True)
    i = 0
    for nombre, puntuacion in ordenJuegos:
        i += 1
        print(f"{i}. {nombre}: {puntuacion}")
        if i == 3:
            break

def main():
   
   while True:
    menu()
    if op == 1:
       print("Agregar videojuego")
       nombre = input("Nombre del videojuego: ")
       puntuacion = float(input("Puntuación: "))
       add_game(nombre, puntuacion)
    elif op == 2:
        actualizarPuntuacion()
    elif op == 3:
       top_n()
    elif op == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida")
   


main()
