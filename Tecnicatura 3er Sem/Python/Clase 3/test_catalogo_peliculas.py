from servicio.CatalogoPeliculas import CatalogoPeliculas
from dominio.Pelicula import Pelicula
import os
def mostrar_menu():
    
 print('\n Menu del catalogo de Peliculas')
 print('1)Agregar pelicula')
 print('2)Listar peliculas')
 print('3)Eliminar archivo de Peliculas')
 print('4)Salir')
while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion :")
    catalogoPeliculas = CatalogoPeliculas()
    
    if opcion == "1":
        nombre_pelicula = input('Nombre de la pelicula que va agregar: ')
        pelicula = Pelicula(nombre_pelicula)
        catalogoPeliculas.agregar_pelicula(pelicula)
    elif opcion == '2':
        catalogoPeliculas.listar_peliculas()
    elif opcion == "3":
      nombre_pelicula = input('Nombre de la pelicula que va eliminar: ')
      catalogoPeliculas.eliminar(nombre_pelicula)
    elif opcion ==  '4':
        
        print('Cerrando el catalogo de Peliculas')
        break
    else:

     print('Opcion no valida')