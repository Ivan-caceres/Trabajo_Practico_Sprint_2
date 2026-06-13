def calcular_carga_total(uso_cpu:float,uso_ram:float)-> float:
    """Calcula la carga total promedio del sistema.

    Args:
        uso_cpu (float): Porcentaje de uso del CPU.
        uso_ram (float): Porcentaje de uso de la memoria RAM.

    Returns:
        float: Promedio entre el uso de CPU y RAM.
    """

    return (uso_cpu + uso_ram) / 2

def calcular_recursos_disponibles(carga_total:float) -> float:
    """Calcula el porcentaje de recursos disponibles del servidor.

    Args:
        carga_total (float): Porcentaje total de carga del sistema.

    Returns:
        float: Porcentaje de recursos disponibles.
    """

    return 100 - carga_total
     
def calcular_uso_por_proceso(uso_cpu:float, uso_ram:float, procesos_activos)-> float:
    """Calcula la carga promedio generada por cada proceso activo.

    Args:
        uso_cpu (float): Porcentaje de uso del CPU.
        uso_ram (float): Porcentaje de uso de la memoria RAM.
        procesos_activos (int): Cantidad de procesos activos.

    Returns:
        float: Carga promedio por proceso. Devuelve 0 si no existen procesos activos.
    """

    if procesos_activos > 0:
        retorno = (uso_cpu + uso_ram) / procesos_activos
    else:
        retorno = 0

    return retorno
     
def calcular_ratio_usuario(usuarios_conectados:float, recursos_disponibles:float) -> float:
    """Calcula la relación entre usuarios conectados y recursos disponibles.

    Args:
        usuarios_conectados (int): Cantidad de usuarios conectados.
        recursos_disponibles (float): Porcentaje de recursos disponibles.

    Returns:
        float: Ratio usuarios/recursos. Devuelve 0 si no hay recursos disponibles.
    """

    if recursos_disponibles > 0:
        retorno = usuarios_conectados / recursos_disponibles
    else:
        retorno = 0
    return retorno
     
def determinar_nivel_riesgo(carga_total:float, espacio_libre:float) -> str:
    """Determina el nivel de riesgo del servidor.

    Args:
        carga_total (float): Porcentaje de carga total del sistema.
        espacio_libre (float): Espacio libre disponible en disco.

    Returns:
        str: Nivel de riesgo calculado ("Critico", "Alto", "Medio" o "Bajo").
    """

    if carga_total > 85 or espacio_libre < 5:
        retorno = "Critico"

    elif carga_total > 65 or espacio_libre < 15:
        retorno = "Alto"

    elif carga_total > 40:
        retorno = "Medio"

    else:
        retorno = "Bajo"

    return retorno

def determinar_estado_general(nivel_riesgo:str) -> str:
    """Obtiene una descripción general del estado del servidor.

    Args:
        nivel_riesgo (str): Nivel de riesgo calculado para el sistema.

    Returns:
        str: Descripción del estado general del servidor.
    """

    if nivel_riesgo == "Critico":
        retorno = "Estado del sistema en peligro"

    elif nivel_riesgo == "Alto":
        retorno = "Estado del sistema en grave estres"

    elif nivel_riesgo == "Medio":
        retorno = "Estado del sistema en leve estres"

    else:
        retorno = "Estado del sistema normal"

    return retorno
