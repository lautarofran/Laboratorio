from data_stark import lista_personajes
from funciones import *

# Crear la función ‘stark_generar_codigos_heroes’ la cual recibirá como parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá iterar la lista de personajes y agregarle el código a cada uno de los personajes.
# El código del héroe (id_heore) surge de la posición del mismo dentro de la lista_heroes (comenzando por el 1).
# Reutilizar la función agregar_codigo_heroe pasándole como argumentos el héroe que se está iterando y el id_heroe
# Una vez finalizado imprimir por pantalla un mensaje como el siguiente:
# (# representa la cantidad de códigos generados):
# Se asignaron # códigos
# * El código del primer héroe es: M-00000001
# * El código del del último héroe es: M-00001224
# La función deberá validar::
# ● La lista contenga al menos un elemento
# ● Todos los elementos de la lista sean del tipo diccionario
# ● Todos los elementos contengan la clave ‘genero’
# En caso de encontrar algún error, informar por pantalla: ‘El origen de datos no contiene el formato correcto’
# La función no retorna ningún valor.




stark_normalizar_datos(lista_personajes)

stark_generar_codigos_heroes(lista_personajes)


# stark_marvel_app(lista_personajes)