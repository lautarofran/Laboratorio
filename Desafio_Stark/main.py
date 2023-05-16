from data_stark import lista_personajes
from funciones import *

# Crear la función ‘agregar_codigo_heroe’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del personaje
# ● id_heroe: un entero que representa el identificador del héroe.
# ○ NOTA: el valor de id_heroe lo vamos a generar recién el punto 2.3. Para probar la función podes pasarle cualquier entero
# La función deberá agregar una nueva clave llamada ‘codigo_heroe’ al diccionario ‘heroe’ recibido como parámetro y asignarle como valor un código utilizando la función ‘generar_codigo_heroe’
# La función deberá validar:
# ● Que el diccionario recibido como parámetro no se encuentre vacío.
# ● Que el código recibido mediante generar_codigo_heroe tenga exactamente 10 caracteres
# En caso de pasar las validaciones correctamente la función deberá retornar True, en caso de encontrarse un error retornar False




dic_hero = {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  }


stark_normalizar_datos(lista_personajes)

print(dic_hero)
agregar_codigo_heroe(dic_hero, 1)
print(dic_hero)

# stark_marvel_app(lista_personajes)