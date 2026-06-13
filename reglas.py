# 1) alerta_critica
def evaluar_regla_alerta_critica(uso_cpu:float, uso_ram:float, carga_total:float) -> bool:
    """Evalúa si el servidor se encuentra en una situación crítica de carga.

    Args:
        uso_cpu (float): Porcentaje de uso del CPU.
        uso_ram (float): Porcentaje de uso de la memoria RAM.
        carga_total (float): Promedio de utilización entre CPU y RAM.

    Returns:
        bool: True si se superan los umbrales críticos de CPU, RAM y carga total, False en caso contrario.
    """

    retorno = False

    if uso_cpu > 85 and uso_ram > 80 and carga_total > 82:
        retorno = True

    return retorno

# 2) alerta_mantenimiento
def evaluar_regla_alerta_mantenimiento(espacio_libre:float, procesos_activos:int) -> bool:
    """Evalúa si el servidor requiere tareas de mantenimiento.

    Args:
        espacio_libre (float): Espacio libre disponible en disco.
        procesos_activos (int): Cantidad de procesos activos.

    Returns:
        bool: True si el espacio libre es insuficiente o la cantidad de procesos supera el límite establecido, False en caso contrario.
    """

    retorno = False

    if espacio_libre < 10 or procesos_activos > 250:
        retorno = True

    return retorno

# 3) alerta_seguridad
def evaluar_regla_alerta_seguridad(estado_firewall:str) -> bool:
    """Evalúa si existe un riesgo de seguridad asociado al firewall.

    Args:
        estado_firewall (str): Estado actual del firewall.

    Returns:
        bool: True si el firewall no se encuentra activo, False en caso contrario.
    """

    retorno = False

    if not estado_firewall == "Activo":
        retorno = True

    return retorno

# 4) alerta_normal
def evaluar_regla_alerta_normal (uso_cpu:float, uso_ram:float) -> bool:
    """Evalúa si el servidor opera dentro de parámetros normales.

    Args:
        uso_cpu (float): Porcentaje de uso del CPU.
        uso_ram (float): Porcentaje de uso de la memoria RAM.

    Returns:
        bool: True si CPU y RAM se encuentran dentro de los rangos normales, False en caso contrario.
    """
    
    retorno = False

    if 40 <= uso_cpu <= 70 and 40 <= uso_ram <= 70:
        retorno = True
    
    return retorno
   
# 5) alerta_web
def evaluar_regla_alerta_web (tipo_servidor:str,usuarios_conectados:float, uso_cpu:float) -> bool:
    """Evalúa una posible sobrecarga en servidores de tipo Web.

    Args:
        tipo_servidor (str): Tipo de servidor configurado.
        usuarios_conectados (float): Cantidad de usuarios conectados.
        uso_cpu (float): Porcentaje de uso del CPU.

    Returns:
        bool: True si el servidor es de tipo Web y presenta una carga elevada
        de usuarios y CPU, False en caso contrario.
    """

    retorno = False

    if tipo_servidor == "Web" and usuarios_conectados > 100 and uso_cpu > 75:
        retorno = True
    
    return retorno

# 6) alerta_proceso
def evaluar_regla_alerta_proceso(uso_por_proceso:float, uso_cpu:float, uso_ram:float ) -> bool:
    """Evalúa si los procesos activos generan una carga excesiva.

    Args:
        uso_por_proceso (float): Carga promedio asociada a cada proceso activo.
        uso_cpu (float): Porcentaje de uso del CPU.
        uso_ram (float): Porcentaje de uso de la memoria RAM.

    Returns:
        bool: True si la carga por proceso es elevada y existe alta utilización de CPU o RAM, False en caso contrario.
    """
     
    retorno = False

    if uso_por_proceso > 3 and (uso_cpu > 70 or uso_ram > 70):
        retorno = True
    
    return retorno
     
# 7) alerta_recursos
def evaluar_regla_alerta_recursos(recursos_disponibles:float, ratio_usuario:float,nivel_riesgo:str) -> bool:
    """Evalúa la disponibilidad general de recursos del servidor.

    Args:
        recursos_disponibles (float): Porcentaje de recursos libres.
        ratio_usuario (float): Relación entre usuarios conectados y recursos disponibles.
        nivel_riesgo (str): Nivel de riesgo calculado para el sistema.

    Returns:
        bool: True si los recursos disponibles son bajos, la demanda de usuarios es alta y el nivel de riesgo es Alto o Crítico, False en caso contrario.
    """
    
    retorno = False
    
    if (recursos_disponibles < 20 and ratio_usuario > 5 and nivel_riesgo in ("Alto", "Critico")) :
        retorno = True
    
    return retorno

# 8) alerta_disco
def evaluar_regla_alerta_disco(sistema_operativo:str, espacio_libre:float) -> bool:
    """Evalúa si un servidor Windows dispone de espacio suficiente en disco.

    Args:
        sistema_operativo (str): Sistema operativo del servidor.
        espacio_libre (float): Espacio libre disponible en disco.

    Returns:
        bool: True si el servidor utiliza Windows Server y dispone de menos de 20 GB libres, False en caso contrario.
    """
    
    retorno = False
    
    if sistema_operativo == "Windows Server" and espacio_libre < 20:
        retorno = True
    
    return retorno

