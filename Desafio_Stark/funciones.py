import os
import re

def extraer_iniciales(nombre:str) -> str:
    """extrae las iniciales de las palabras que pases, exceptuando si está el articulo "the", y en caso de haber - se reemplaza por un espacio

    Args:
        nombre (str): palabras para extraer iniciales

    Returns:
        str: inicales
    """
    iniciales = ""
    if not nombre:
        return "N/A"
    if re.search("-", nombre):
        nombre = re.sub("-", " ", nombre)
    nombre = re.split(" ", nombre)
    for i in nombre:
        if i.lower() == "the":
            continue
        else:
            iniciales += i[0].upper() + "."
    
    return iniciales

def definir_iniciales_nombre(dicc:dict) -> bool:
    """recibe un diccionario y si este tiene la key "nombre" se extraen las iniciales y se agregan a una nueva key. 

    Args:
        dicc (dict): diccionario para extraer iniciales

    Returns:
        bool: False en caso de error, True en caso de correcto
    """
    if not dicc or not "nombre" in dicc:
        return False
    else:
        dicc["iniciales"] = extraer_iniciales(dicc["nombre"])
        return True




##############################################################

def sumar(a: int, b: int)->int:
    """suma dos numeros enteros

    Args:
        a (int): primer numero entero a sumar
        b (int): segundo numero entero a sumar

    Returns:
        int: resultado de la suma
    """
    rta = a + b
    return rta

def mostrar_lista(lista:list, titulo:str):
    """muestra una lista

    Args:
        lista (list): lista a mostrar
        titulo (string): titulo
    """
    print(f"--- {titulo} ---")
    for item in lista:
        print(item)

def mostrar_nombre(lista:list, titulo:str):
    """muestra el nombre de los elementos de una lista

    Args:
        lista (lista): lista a mostrar
        titulo (string): titulo
    """
    print(f"*** {titulo} ***")
    for item in lista:
        print(f"{item['nombre']:15s}")

def mostrar_item(lista:list, item:str) -> None:
    """recorre una lista y muestra el dato que pidas

    Args:
        lista (list): lista a recorrer
        item (str): dato a mostrar
    """
    for elemento in lista:
        print(f"{elemento[item]}")

def calcular_altura_min_max(lista:list, condicion:str) -> dict:
    """calcula la altura maxima o minima de los elementos de una lista

    Args:
        lista (list): lista 
        condicion (str): "max" o "min"

    Returns:
        dict: personaje mas alto o mas bajo
    """
    altura_max = 0
    bandera_altura_max = True
    personaje_altura_max = None
    altura_min = 0
    bandera_altura_min = True
    personaje_altura_min = None
    retorno = None
    if condicion == "min":
        for personaje in lista:
            altura = float(personaje["altura"])
            if bandera_altura_min or altura < altura_min:
                altura_min = altura
                personaje_altura_min = personaje["nombre"]
                bandera_altura_min = False
                retorno = personaje_altura_min
    elif condicion == "max":
        for personaje in lista:
             altura = float(personaje["altura"])
             if bandera_altura_max or altura > altura_max:
                altura_max = altura
                personaje_altura_max = personaje["nombre"]
                bandera_altura_max = False
                retorno = personaje_altura_max
    return retorno
    
def calcular_alt_promedio(lista:list) -> float:
    """calcula la altura promedio de una lista

    Args:
        lista (list): lista a calcular

    Returns:
        float: valor de la altura promedio
    """
    acumulador_altura = 0
    promedio_altura = 0
    for personaje in lista:
                altura = float(personaje["altura"])
                acumulador_altura += altura
                promedio_altura = acumulador_altura / len(lista)
    return promedio_altura

def calcular_heroe_peso_max_min(lista:list, condicion:str) -> dict:
    """calcula el peso maximo o minimo de un elemento de la lista

    Args:
        lista (list): lista a iterar
        condicion (str): "max" o "min" segun el peso que quiere buscar

    Returns:
        dict: personaje mas o menos pesado
    """
    bandera_peso_min = True
    personaje_peso_min = None
    bandera_peso_max = True
    personaje_peso_max = None
    retorno = None
    if condicion == "max":
        for heroe in lista:
            peso = float(heroe["peso"])
            if bandera_peso_max or peso > peso_max:
                peso_max = peso
                personaje_peso_max = heroe["nombre"]
                bandera_peso_max = False
                retorno = personaje_peso_max
    else:
        for heroe in lista:
            peso = float(heroe["peso"])
            if bandera_peso_min or peso < peso_min:
                peso_min = peso
                personaje_peso_min = heroe["nombre"]
                bandera_peso_min = False
                retorno = personaje_peso_min
        
    return retorno

def calcular_inteligencia(lista:list) -> dict:
    """cuenta los personajes de una lista que hay con cada tipo de inteligencia

    Args:
        lista (list): lista a iterar

    Returns:
        dict: la cantidad de personajes en cada tipo de inteligencia
    """
    conteo = {}
    for heroe in lista:
        if heroe["inteligencia"] == "":
            heroe["inteligencia"] = "No tiene"
        inteligencia = heroe["inteligencia"]
        if inteligencia in conteo:
            conteo[inteligencia] += 1
        else:
            conteo[inteligencia] = 1
    return conteo

def contar_color_pelo(lista:list) -> dict:
    """cuenta la cantidad de personajes que hay con cada color de pelo

    Args:
        lista (list): lista a recorrer

    Returns:
        dict: cantidad de personajes con cada color de pelo
    """
    conteo = {}
    for heroe in lista:
        color_pelo = heroe["color_pelo"]
        if color_pelo in conteo:
            conteo[color_pelo] += 1
        else:
            conteo[color_pelo] = 1
    return conteo

def contar_color_ojos(lista:list) -> dict:
    """cuenta la cantidad de personajes que hay con cada color de ojos

    Args:
        lista (list): lista a recorrer

    Returns:
        dict: cantidad de personajes con cada color de ojo
    """
    conteo = {}
    for heroe in lista:
        color_ojos = heroe["color_ojos"]
        if color_ojos in conteo:
            conteo[color_ojos] += 1
        else:
            conteo[color_ojos] = 1
    return conteo

def listar_heroes_genero(lista:list, genero:str) -> list:
    """recibe una lista y la separa por genero

    Args:
        lista (list): lista a recorrer
        genero (str): "F" o "M" segun quiera saber

    Returns:
        list: lista con heroes F o M segun necesite
    """
    nueva_lista = []
    for heroe in lista:
        if heroe["genero"] == genero:
            nueva_lista.append(heroe)
        elif heroe["genero"] == genero:
            nueva_lista.append(heroe)
    return nueva_lista

def agrupar_por_color_pelo(lista:list) -> dict:
    agrupados = {}
    for heroe in lista:
        color_pelo = heroe["color_pelo"]
        if color_pelo in agrupados:
            agrupados[color_pelo].append(heroe["nombre"])
        else:
            agrupados[color_pelo] = [heroe["nombre"]]
    return agrupados    

def mostrar_por_color_pelo(dicc:dict):
    for color_pelo, superheroes in dicc.items():
        print("Superheroes con color de pelo:", color_pelo)
        for heroe in superheroes:
            print("- ", heroe)
            
def agrupar_por_inteligencia(lista:list) -> dict:
    agrupados = {}
    for heroe in lista:
        inteligencia = heroe["inteligencia"]
        if inteligencia in agrupados:
            agrupados[inteligencia].append(heroe["nombre"])
        else:
            agrupados[inteligencia] = [heroe["nombre"]]
    return agrupados                

def mostrar_por_inteligencia(dicc:dict):
    for inteligencia, superheroes in dicc.items():
        print("Superheroes con inteligencia:", inteligencia)
        for heroe in superheroes:
            print("- ", heroe)

def agrupar_por_color_ojos(lista:list):
    agrupados = {}
    for heroe in lista:
        color_ojos = heroe["color_ojos"]
        if color_ojos in agrupados:
            agrupados[color_ojos].append(heroe["nombre"])
        else:
            agrupados[color_ojos] = [heroe["nombre"]]
    return agrupados  
    
def mostrar_por_color_ojos(dicc:dict):
    for color_ojos, superheroes in dicc.items():
        print("Superheroes con ojos color:", color_ojos)
        for heroe in superheroes:
            print("- ", heroe)

def mostrar_heroe_fila(heroe: dict) -> None:
    print(f"{heroe[ 'nombre']} {heroe['identidad']} {heroe['empresa']} {float(heroe['altura']):.2f} {float(heroe['peso']):.2f} {heroe['genero']} {heroe['color_ojos']} {heroe['color_pelo']} {heroe['fuerza']} {heroe['inteligencia']} ")
  
def listar_heroes(lista: list) -> None:
    print("   Lista Heroes")
    print("nombre identidad ---------------------")
    for heroe in lista:
        mostrar_heroe_fila(heroe)

def filtrar_heroes(lista: list, key: str, color: str) -> list:
    lista_filtrada = []
    for heroe in lista:
        if (heroe[key] == color):
            lista_filtrada.append(heroe)
    return lista_filtrada  

def filtrar_heroes(lista:list, key:str, value:str) -> list:
    lista_filtrada = []
    for heroe in lista:
        if(heroe[key] == value):
            lista_filtrada.append(heroe)
    return lista_filtrada


##############################################################

def stark_normalizar_datos(lista:list) -> None:
    datos_modificados = False
    if not lista:
        print("ERROR. La lista esta vacia.")
        return lista
    else:
        for heroe in lista:
            for key, valor in heroe.items():
                if type(valor) == int or type(valor) == float:
                    continue
                elif re.match(r'^\d+\.?\d*$', str(valor)):
                    if "." in valor:
                        heroe[key] = float(valor)
                        datos_modificados = True
                    else:
                        heroe[key] = int(valor)
                        datos_modificados = True
    if datos_modificados:
        print("Datos normalizados.")
        
def obtener_nombre(heroe: dict) -> str:
    nombre = heroe['nombre']
    return f"Nombre: {nombre}"

def imprimir_dato(dato:str) -> None:
    print(dato)

def esta_vacia(lista):
    if not lista:
        print("ERROR. La lista esta vacia.")
        return 1
    else:
        return 0

def stark_imprimir_nombres_heroes(lista):
    if not esta_vacia(lista):
        for heroe in lista:
            imprimir_dato(obtener_nombre(heroe))
    else:
        return -1

def obtener_nombre_y_dato(dict: dict, key: str) -> str:
    if key in dict:
        return f"Nombre: {dict['nombre']} | {key}: {dict[key]}"
    else:
        print(f"No se encontro {key}")

def stark_imprimir_nombres_alturas(lista:list) -> int or str:
    if lista:
        for heroe in lista:
            nombre_y_altura = obtener_nombre_y_dato(heroe, "altura")
            print(nombre_y_altura)
    else:
        return -1

def calcular_max(lista:list, key:str) -> list:
    """calcula cual es el maximo en una lista de los siguientes datos: peso, altura o fuerza_maxima y retorna el heroe que tenga el dato mas alto

    Args:
        lista (list): lista para buscar el dato
        key (str): dato a buscar
    """
    if not lista or key not in lista[0]:
        print("La lista de heroes esta vacia o la key no existe")
        return []
    bandera_mayor = True
    mayor = None
    heroe_max = []
    for heroe in lista:
        if bandera_mayor or heroe[key] > mayor:
            mayor = heroe[key]
            bandera_mayor = False
            heroe_max = [heroe]
        elif heroe[key] == mayor:
            heroe_max.append(heroe)
    return heroe_max

def calcular_min(lista:list, key:str) -> list:
    """calcula cual es el minimo en una lista de los siguientes datos: peso, altura o fuerza y retorna el heroe que tenga el dato mas bajo

    Args:
        lista (list): lista para buscar el dato
        key (str): dato a buscar
    """
    if not lista or key not in lista[0]:
        print("La lista de heroes esta vacia o la key no existe")
        return []
    bandera_menor = True
    menor = None
    heroe_min = []
    for heroe in lista:
        if bandera_menor or heroe[key] < menor:
            menor = heroe[key]
            bandera_menor = False
            heroe_min = [heroe]
        elif heroe[key] == menor:
            heroe_min.append(heroe)
    return heroe_min

def calcular_max_min_dato(lista:list, tipo:str, key:str) -> list:
    if not lista or key not in lista[0]:
        print("La lista de heroes esta vacia o la key no existe")
        return []
    heroe_calculado = []
    if tipo == "maximo":
        heroe_calculado = calcular_max(lista, key)
    elif tipo == "minimo":
        heroe_calculado = calcular_min(lista, key)
    else:
        print("ERROR. El tipo debe ser mayor o menor.")
    return heroe_calculado

def stark_calcular_imprimir_heroe(lista: list, tipo: str, key: str) -> None:
    if not lista:
        print("La lista de heroes esta vacia")
        return -1
    
    heroe_calculado = calcular_max_min_dato(lista, tipo, key)
    
    if not heroe_calculado:
        print(f"No se pudo calcular el {tipo} {key}")
        return -1
    
    dato_a_imprimir = obtener_nombre_y_dato(heroe_calculado[0], key)
    
    if dato_a_imprimir:
        print(f"{tipo.capitalize()} {key}: {dato_a_imprimir}")
    else:
        return -1

def sumar_dato_heroe(lista:list, key:str) -> int:

    """La funcion realiza la suma de todos los datos segun la key pasada por parametro y retorna la misma

    Args:
        lista (list): lista para iterar 
        key (str): dato a sumar

    Returns:
        int: el resultado de la suma
    """
    suma = 0
    for heroe in lista:
        if isinstance(heroe, dict) and heroe:
            if key in heroe:
                suma += heroe[key]
            else:
                print(f"ERROR: El héroe {heroe['nombre']} no tiene el atributo '{key}'")
        else:
            print(f"Error: El héroe {heroe} no es un diccionario válido")
    return suma

def dividir(dividendo:float, divisor:float) -> float:
    if divisor == 0:
        return 0
    else:
        resultado = dividendo/divisor
        return resultado

def calcular_promedio(lista:list, key:str) -> float:
    suma = sumar_dato_heroe(lista, key)
    resultado = dividir(suma, len(lista))
    return resultado

def stark_calcular_imprimir_promedio_altura(lista:list, key:str="altura") -> None | int:
    if not lista:
        print("La lista esta vacia.")
        return -1
    
    dato_a_imprimir = calcular_promedio(lista, key)
    
    if dato_a_imprimir:
        print(f"{key.capitalize()} promedio: {round(dato_a_imprimir, 2)}")

def validar_entero(dato:str) -> bool:
    if re.match("^\d+$", dato):
        return True
    else:
        return False

def imprimir_menu() -> None:
    """muestra un menu
    """
    imprimir_dato("---Menú de opciones---")
    imprimir_dato("Opcion 1: Mostrar nombre de los superheroes")
    imprimir_dato("Opcion 2: Mostrar nombre y altura de los superheroes")
    imprimir_dato("Opcion 3: Superheroe mas alto")
    imprimir_dato("Opcion 4: Superheroe mas bajo")
    imprimir_dato("Opcion 5: Altura promedio de los superheroes")
    imprimir_dato("Opcion 6: Mostrar nombre del superheroe mas alto y mas bajo")
    imprimir_dato("Opcion 7: Mostrar superheroe mas pesado y mas liviano")
    imprimir_dato("Opcion 8: Mostrar nombre de heroes femeninas")
    imprimir_dato("Opcion 9: Mostrar nombre de heroes masculinos")
    imprimir_dato("Opcion 10': Calcular nombre de masculino mas alto")
    imprimir_dato("Opcion 11': Calcular nombre de femenina mas alto")
    imprimir_dato("Opcion 12': Calcular nombre de masculino mas bajo")
    imprimir_dato("Opcion 13': Calcular nombre de femenina mas baja")
    imprimir_dato("Opcion 14': Calcular altura promedio de los heroes masculinos")
    imprimir_dato("Opcion 15': Calcular altura promedio de los heroes femeninos")
    imprimir_dato("Opcion 16': Mostrar opciones 10,11,12,13")
    imprimir_dato("Opcion 17': Determinar cuantos heroes tienen cada tipo de ojos")
    imprimir_dato("Opcion 18': Determinar cuantos heroes tienen cada tipo de pelo")
    imprimir_dato("Opcion 19': Determinar cuántos superhéroes tienen cada tipo de inteligencia")
    imprimir_dato("Opcion 20': Listar todos los superhéroes agrupados por color de ojos")
    imprimir_dato("Opcion 21': Listar todos los superhéroes agrupados por color de pelo")
    imprimir_dato("Opcion 22': Listar todos los superhéroes agrupados por tipo de inteligencia")
    imprimir_dato("Opcion 23: Salir")

def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    if validar_entero(opcion):
        opcion = int(opcion)
        if opcion < 1 or opcion > 23:
            print("ERROR. Opcion no valida")
        else:
            return opcion
    else:
        imprimir_dato("ERROR. Eso no es un numero.")
        return -1

def stark_marvel_app(lista:list):
    bandera_lista_inteligencia = False
    bandera_lista_color_pelo = False
    bandera_lista_color_ojos = False
    bandera_c_8 = True
    bandera_c_9 = False
    bandera_c_10 = False
    bandera_c_11 = False
    bandera_c_12 = False
    bandera_c_13 = False
    bandera_c_14 = False
    bandera_c_15 = False
    lista_color_ojos = {}
    lista_color_pelo = {}
    lista_inteligencia = {}
    
    while True:
        opcion = stark_menu_principal()
        match(opcion):
            case 1:
                stark_imprimir_nombres_heroes(lista)
            
            case 2:
                stark_imprimir_nombres_alturas(lista)

            case 3:
                stark_calcular_imprimir_heroe(lista, 'maximo', 'altura')

            case 4:
                stark_calcular_imprimir_heroe(lista, 'minimo', 'altura')

            case 5:
                stark_calcular_imprimir_promedio_altura(lista, "altura")
                
            case 6:
                stark_calcular_imprimir_heroe(lista, 'minimo', 'altura')
                stark_calcular_imprimir_heroe(lista, 'maximo', 'altura')

            case 7:
                stark_calcular_imprimir_heroe(lista, 'minimo', 'peso')
                stark_calcular_imprimir_heroe(lista, 'maximo', 'peso')
            
            case 8:
                bandera_c_8 = True
                mostrar_nombre(listar_heroes_genero(lista, "F"), "Nombre heroes femeninos")
                
            case 9:
                bandera_c_9 = True
                mostrar_nombre(listar_heroes_genero(lista, "M"), "Nombre heroes masculinos")
                
            case 10:
                if bandera_c_9:
                    masculino_alto = calcular_altura_min_max(listar_heroes_genero(lista, "M"), "max")
                    bandera_c_10 = True
                    imprimir_dato("Calculo realizado.")
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion n9.")
                
            case 11:
                if bandera_c_8:
                    femenina_alta = calcular_altura_min_max(listar_heroes_genero(lista, "F"), "max")
                    bandera_c_11 = True
                    imprimir_dato("Calculo realizado.")
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion 8.")
                
            case 12:
                if bandera_c_9:
                    masculino_bajo = calcular_altura_min_max(listar_heroes_genero(lista, "M"), "min")
                    bandera_c_12 = True
                    imprimir_dato("Calculo realizado.")
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcino n9.")
                
            case 13:
                if bandera_c_8:
                    femenina_baja = calcular_altura_min_max(listar_heroes_genero(lista, "F"), "min")
                    bandera_c_13 = True
                    imprimir_dato("Calculo realizado.")
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion n8.")
            
            case 14:
                if bandera_c_9:
                    altura_promedio_masc = calcular_alt_promedio(listar_heroes_genero(lista, "M"))
                    bandera_c_14 = True
                    imprimir_dato("Calculo realizado.")
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion n9.")
                
            case 15:
                if bandera_c_8:
                    altura_promedio_fem = calcular_alt_promedio(listar_heroes_genero(lista, "F"))
                    bandera_c_15 = True
                    imprimir_dato("Calculo realizado.")
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion n8.")
            
            case 16:
                if bandera_c_12 and bandera_c_13 and bandera_c_14 and bandera_c_15:
                    imprimir_dato(f"El heroe masculino mas alto es: {masculino_alto}")
                    imprimir_dato(f"El heroe femenino mas alto es: {femenina_alta}")
                    imprimir_dato(f"El heroe masculino mas bajo es: {masculino_bajo}")
                    imprimir_dato(f"El heroe femenino mas bajo es: {femenina_baja}") 
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a las opciones n12, n13, n14 y n15.")           
            
            case 17:
                lista_color_ojos = agrupar_por_color_ojos(lista)
                bandera_lista_color_ojos = True
                imprimir_dato("Calculo realizado.")
                
            case 18:
                lista_color_pelo = agrupar_por_color_pelo(lista)
                bandera_lista_color_pelo = True
                imprimir_dato("Calculo realizado.")
                
            case 19:
                lista_inteligencia = agrupar_por_inteligencia(lista)
                bandera_lista_inteligencia = True
                imprimir_dato("Calculo realizado.")
                
            case 20:
                if bandera_lista_color_ojos:
                    mostrar_por_color_ojos(lista_color_ojos)
                else:
                    print("ERROR. Primero debes ingresar a la opcion 17.")
            
            case 21:
                if bandera_lista_color_pelo:
                    mostrar_por_color_pelo(lista_color_pelo)
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion n18.")
                
            case 22:
                if bandera_lista_inteligencia:
                    mostrar_por_inteligencia(lista_inteligencia)
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion n19.")
            
            case 23:
                    respuesta = input("Seguro que quieres salir? (s/n): ")
                    if respuesta == "s":
                        break
                    else:
                        continue
        os.system("pause")      
        os.system("cls")              

