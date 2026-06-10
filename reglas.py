def regla_sobrecarga(uso_cpu, uso_ram):
    return uso_cpu > 85 and uso_ram > 80
#PASAR TODAS LAS REGLAS A FUNCIONES
'''
    #alerta_critica
    if uso_cpu > 85 and uso_ram > 80 and carga_total > 82:
        alerta_critica = True
        mensaje_critica = f"CPU al {uso_cpu}%, RAM al {uso_ram}% y {cant_procesos} procesos activos superan los umbrales seguros."
    #alerta_mantenimiento
    if espacio_libre < 10 or cant_procesos > 250:
        alerta_mantenimiento = True
        mensaje_mantenimiento = (
            f"Espacio libre: {espacio_libre} GB. Procesos activos: {cant_procesos}."
        )
    #alerta_seguridad
    if firewall == "Inactivo":
        alerta_seguridad = True
        mensaje_seguridad = f"Firewall en estado '{firewall}', servidor expuesto."
    #alerta_normal
    if 40 <= uso_cpu <= 70 and 40 <= uso_ram <= 70:
        alerta_normal = True
        mensaje_normal = (
            f"CPU al {uso_cpu}% y RAM al {uso_ram}% dentro de parámetros saludables."
        )
    #alerta_web
    if tipo_serv == "Web" and usuarios_conectados > 100 and uso_cpu > 75:
        alerta_web = True
        mensaje_web = f"{usuarios_conectados} usuarios conectados con CPU al {uso_cpu}% en servidor Web."
    #alerta_proceso
    if presion_por_proceso > 3 and (uso_cpu > 70 or uso_ram > 70):
        alerta_proceso = True
        mensaje_proceso = (
            f"Cada proceso consume en promedio {presion_por_proceso} unidades de carga."
        )
    #alerta_recursos
    if (
        recursos_disponibles < 20
        and ratio_usuarios > 5
        and nivel_riesgo in ("Alto", "Critico")
    ):
        alerta_recursos = True
        mensaje_recursos = f"Solo {recursos_disponibles}% de recursos libres para {usuarios_conectados} usuarios."
    #alerta_disco
    if so == "Windows Server" or so == "windows server" and espacio_libre < 20:
        alerta_disco = True
        mensaje_disco = f"Windows Server con solo {espacio_libre} GB libres. Mínimo recomendado: 20 GB."

'''