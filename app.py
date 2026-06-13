from inputs import (
    ingresar_uso_cpu,
    ingresar_uso_ram,
    ingresar_espacio_libre,
    ingresar_usuarios_conectados,
    ingresar_procesos_activos,
    ingresar_sistema_operativo,
    ingresar_estado_firewall,
    ingresar_tipo_servidor,
    ingresar_nombre_servidor,
    ingresar_nombre_administrador
)

from calculos import (
    calcular_carga_total,
    calcular_recursos_disponibles,
    calcular_uso_por_proceso,
    calcular_ratio_usuario,
    determinar_nivel_riesgo,
    determinar_estado_general
)

from reglas import(
    evaluar_regla_alerta_critica,
    evaluar_regla_alerta_mantenimiento,
    evaluar_regla_alerta_seguridad,
    evaluar_regla_alerta_normal,
    evaluar_regla_alerta_web,
    evaluar_regla_alerta_proceso,
    evaluar_regla_alerta_recursos,
    evaluar_regla_alerta_disco
)

from output import(
    mostrar_encabezado,
    mostrar_diagnostico,
    mostrar_problemas_detectados,
    generar_problemas_detectados,
    mostrar_recomendaciones,
    generar_recomendaciones
)

def ejecutar_sistema() -> None:

    mostrar_encabezado()

    # ingresos

    uso_cpu = ingresar_uso_cpu()
    uso_ram = ingresar_uso_ram()
    espacio_libre = ingresar_espacio_libre()
    usuarios_conectados = ingresar_usuarios_conectados()
    procesos_activos = ingresar_procesos_activos()

    sistema_operativo = ingresar_sistema_operativo()
    estado_firewall = ingresar_estado_firewall()
    tipo_servidor = ingresar_tipo_servidor()

    nombre_servidor = ingresar_nombre_servidor()
    nombre_administrador = ingresar_nombre_administrador()

    # calculos

    carga_total = calcular_carga_total(uso_cpu,uso_ram)
    recursos_disponibles = calcular_recursos_disponibles(carga_total)
    uso_por_proceso = calcular_uso_por_proceso(uso_cpu,uso_ram,procesos_activos)
    ratio_usuario = calcular_ratio_usuario(usuarios_conectados,recursos_disponibles)
    nivel_riesgo = determinar_nivel_riesgo(carga_total,espacio_libre)
    estado_general = determinar_estado_general(nivel_riesgo)

    # reglas

    alerta_critica = evaluar_regla_alerta_critica(uso_cpu,uso_ram,carga_total)
    alerta_mantenimiento =  evaluar_regla_alerta_mantenimiento(espacio_libre,procesos_activos)
    alerta_seguridad = evaluar_regla_alerta_seguridad(estado_firewall)
    alerta_normal = evaluar_regla_alerta_normal (uso_cpu,uso_ram)
    alerta_web = evaluar_regla_alerta_web (tipo_servidor,usuarios_conectados,uso_cpu)
    alerta_proceso = evaluar_regla_alerta_proceso(uso_por_proceso,uso_cpu,uso_ram)
    alerta_recursos = evaluar_regla_alerta_recursos(recursos_disponibles,ratio_usuario,nivel_riesgo)
    alerta_disco = evaluar_regla_alerta_disco(sistema_operativo,espacio_libre)

    # diagnostico

    mostrar_diagnostico(nombre_servidor,nombre_administrador,estado_general,nivel_riesgo)
    problemas = generar_problemas_detectados(alerta_critica,alerta_mantenimiento,alerta_seguridad,alerta_normal,alerta_web,alerta_proceso,alerta_recursos,alerta_disco)
    mostrar_problemas_detectados(problemas)
    recomendaciones = generar_recomendaciones(alerta_critica,alerta_mantenimiento,alerta_seguridad,alerta_normal,alerta_web,alerta_proceso,alerta_recursos,alerta_disco)
    mostrar_recomendaciones(recomendaciones)


