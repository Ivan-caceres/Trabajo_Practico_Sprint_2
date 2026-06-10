from validaciones import (
    validar_caracteres_flotantes,
    validar_puntos,
    validar_longitud_minima,
    validar_numeros_negativos,
    validar_inicio_fin,
    validar_rango,
    validar_lista
)

# INGRESO DE DATOS NUMERICOS
def pedir_numero(mensaje:str, minimo:float, maximo:float) -> float:
    """Solicita un número y valida que sea un valor numérico dentro del rango indicado.
        - Que el ingreso no esté vacío.
        - Que contenga solo caracteres numéricos.
        - Que tenga como máximo un punto decimal.
        - Que no sea negativo.
        - Que no comience ni termine con un punto.
        - Que se encuentre dentro del rango indicado.

    Args:
        mensaje (str): Texto que se mostrará al usuario para solicitar el dato.
        minimo (float): Valor mínimo permitido.
        maximo (float): Valor máximo permitido.

    Returns:
        float: Número validado dentro del rango especificado.
    """

    numero = input(mensaje)
    ingreso_valido = False

    while ingreso_valido == False:

        bandera_validada = True

        if validar_longitud_minima(numero,1) == False:
            print("NO PUEDE ESTAR VACIO")
            bandera_validada = False
        
        if validar_caracteres_flotantes(numero) == False:
            print("SE DEBEN INGRESAR NUMEROS")
            bandera_validada = False

        if validar_puntos(numero) == False:
            print("MAS DE UN PUNTO DECIMAL")
            bandera_validada = False
        
        if validar_numeros_negativos(numero) == False:
            print("FUERA DE RANGO, NO SE PERMITEN NEGATIVOS")
            bandera_validada = False
        
        if validar_inicio_fin(numero) == False:
            print("FORMATO INCORRECTO")
            bandera_validada = False

        if bandera_validada and validar_rango (numero,minimo,maximo) == False:
            print(f"FUERA DE RANGO.({minimo}/{maximo})")
            bandera_validada = False
        
        if bandera_validada:
            ingreso_valido = True
        else:
            print("-----------INVALIDO-----------")
            numero = input("Reingrese un número válido: ")

    return float(numero)
#ingresar numeros con REUTILIZACION DE LA FUNCION POR PARAMETROS PARA PEDIR NUMERO
def ingresar_uso_cpu() -> float:
    """Solicita el porcentaje de uso actual del CPU.

    Returns:
        float: Porcentaje de uso del CPU entre 0 y 100.
    """
    return pedir_numero("Ingrese uso de CPU (%): ", 0, 100)

def ingresar_uso_ram() -> float:
    """Solicita el porcentaje de uso actual de la memoria RAM.

    Returns:
        float: Porcentaje de uso de RAM entre 0 y 100.
    """
    return pedir_numero("Ingrese uso de RAM (%): ", 0, 100)

def ingresar_espacio_libre() -> float:
    """Solicita el espacio libre disponible en disco.

    Returns:
        float: Cantidad de espacio libre en GB.
    """   
    return pedir_numero("Ingrese espacio libre en disco (GB): ", 0, 1000)

def ingresar_usuarios_conectados() -> float:
    """Solicita la cantidad de usuarios conectados al servidor.

    Returns:
        float: Cantidad de usuarios conectados.
    """   
    return pedir_numero("Ingrese cantidad de usuarios conectados: ",1,100)

def ingresar_procesos_activos() -> float:
    """Solicita la cantidad de procesos activos del servidor.

    Returns:
        float: Cantidad de procesos activos.
    """
    return pedir_numero("Ingrese Cantidad de procesos activos: ",0,1000)


# INGRESO DE OPCIONES CERRADAS 
def pedir_opcion (mensaje:str,lista_opciones:list) -> str: 
    """Solicita al usuario el ingreso de una opción y repite la petición de forma iterativa hasta que el valor ingresado 
    sea una opción válida.

    Args:
        mensaje (str): Mensaje indicativo que se le muestra al usuario para solicitar el dato.
        opciones (list): Conjunto cerrado de valores strings permitidos 

    Returns:
        str: La opción validada que coincide con uno de los elementos de la lista.
    """

    opcion = input(mensaje)

    while validar_lista(opcion, lista_opciones) == False:

        print("INVÁLIDA")

        opcion = input(f"Re{mensaje}")

    return opcion
#ingresar opciones con REUTILIZACION DE LA FUNCION POR PARAMETROS PARA PEDIR OPCION
def ingresar_sistema_operativo() -> str:
    """Solicita el sistema operativo del servidor.

    Returns:
        str: Sistema operativo seleccionado.
    """

    opciones = ["Linux", "Windows Server"]
    return pedir_opcion("Ingrese sistema operativo (Linux / Windows Server): ",opciones)

def ingresar_estado_firewall() -> str:
    """Solicita el estado actual del firewall.

    Returns:
        str: Estado del firewall seleccionado.
    """

    opciones = ["Activo", "Inactivo"]
    return pedir_opcion("Ingrese estado del firewall (Activo / Inactivo): ",opciones)

def ingresar_tipo_servidor() -> str:
    """Solicita el tipo de servidor.

    Returns:
        str: Tipo de servidor seleccionado.
    """

    opciones = ["Web", "Base de datos", "Archivos"]
    return pedir_opcion("Ingrese tipo de servidor (Web / Base de datos / Archivos): ",opciones)



