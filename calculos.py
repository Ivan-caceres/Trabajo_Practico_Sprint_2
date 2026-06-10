from main import (
uso_cpu,
uso_ram,
espacio_libre,
usuarios_conectados,
procesos_activos,
)

#PASAR TODAS LOS CALCULOS FUNCIONES y documentarlas

def calcular_carga_total(uso_cpu:float,uso_ram:float)->float:
    """Promedio de uso entre CPU y RAM. Carga total del sistema.

    Args:
        uso_cpu (float): Porcentaje de uso del CPU, entre 0 y 100.
        uso_ram (float): Porcentaje de uso de la memoria RAM, entre 0 y 100.

    Returns:
        float: _description_
    """
    carga_total = (uso_cpu + uso_ram) / 2
    return carga_total

carga_total = calcular_carga_total

def calcular_recursos_disponibles(recursos_totales:float,recursos_en_uso:float) -> float:
    """Calcular Porcentaje de recursos sin utilizar. Complemento de la carga_total.

    Args:
        recursos_totales (float): 100
        recursos_en_uso (float): Espacio libre en disco expresado en GB, mayor que 0.

    Returns:
        float: _description_
    """
    recursos_disponibles = 100 - carga_total
    return recursos_disponibles
     
recursos_disponibles = calcular_recursos_disponibles

def calcular_uso_por_proceso(uso_cpu:float,uso_ram:float,procesos_activos)-> float:
    """Carga promedio por proceso activo. Cociente de la sumatoria entre uso del CPU y ram, y la cantidad de procesos activos

    Args:
        uso_cpu (float): _description_
        uso_ram (float): _description_
        procesos_activos (_type_): _description_

    Returns:
        float: _description_
    """
    uso_por_proceso = (uso_cpu + uso_ram) / procesos_activos
    return uso_por_proceso
     
uso_por_proceso = calcular_uso_por_proceso

def calcular_ratio_usuario(usuarios_conectados:float, recursos_disponibles:float) -> float:
    """Relación entre los usuarios conectados y los recursos disponibles. Retorna inf(indeterminado) si los recursos disponibles son cero.

    Args:
        usuarios_conectados (float): Cantidad de usuarios conectados, mayor que 0.
        recursos_disponibles (float): Porcentaje de recursos sin utilizar. Complemento de la carga_total.

    Returns:
        float: _description_
    """
    ratio_usuario = usuarios_conectados / recursos_disponibles
    return ratio_usuario
     
ratio_usuario = calcular_ratio_usuario
#------------------------------------------------------------------------------
if procesos_activos > 0:
        uso_por_proceso = (uso_cpu + uso_ram) / procesos_activos
else:
        uso_por_proceso = 0

if recursos_disponibles > 0:
        ratio_usuario = usuarios_conectados / recursos_disponibles
# nivel_riesgo (str): Clasificación de riesgo del sistema, de forma descendente "Critico", "Alto", "Medio, "Bajo".
if carga_total > 85 or espacio_libre < 5:
    nivel_riesgo = "Critico"
elif carga_total > 65 or espacio_libre < 15:
    nivel_riesgo = "Alto"
elif carga_total > 40:
    nivel_riesgo = "Medio"
else:
    nivel_riesgo = "Bajo"
#estado_general (str): Descripción del estado actual del servidor dependiendo del nivel de riesgo que devolvió.
if nivel_riesgo == "Critico":
    estado_general = "Estado del sistema en peligro"
elif nivel_riesgo == "Alto":
    estado_general = "Estado del sistema en grave estres"
elif nivel_riesgo == "Medio":
    estado_general = "Estado del sistema en leve estres"
else:
    estado_general = "Estado del sistema normal"