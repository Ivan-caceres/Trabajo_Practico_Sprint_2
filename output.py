def mostrar_encabezado() -> None:

    print("------------------------------------------------------------")
    print("            SISTEMA DE DIAGNOSTICO DE SERVIDORES            ")
    print("------------------------------------------------------------")

def mostrar_diagnostico(nombre_servidor:str, nombre_administrador:str, estado_general:str, nivel_riesgo:str) -> None:

    print("\n------------------------------------------------------------")

    print(f"\n🖥️  Diagnóstico del Servidor: {nombre_servidor}")

    print(f"\n👤  Administrador: {nombre_administrador}")

    print(f"\nEstado general: {estado_general} ({nivel_riesgo})") 
   
def generar_problemas_detectados(alerta_critica:bool, alerta_mantenimiento:bool, alerta_seguridad:bool, alerta_normal:bool,alerta_web:bool, alerta_proceso:bool, alerta_recursos:bool, alerta_disco:bool) -> list:

    lista_problemas = []

    if alerta_critica:
        lista_problemas += ["- Sobrecarga crítica detectada."]
    
    if alerta_mantenimiento:
        lista_problemas += ["- Espacio libre insuficiente o exceso de procesos activos."]

    if alerta_seguridad:
        lista_problemas += ["- Firewall desactivado."]

    if alerta_normal:
        lista_problemas += ["- Sistema operando en rango normal."]

    if alerta_web:
        lista_problemas += ["- Servidor web con alta demanda de usuarios y CPU elevada."]

    if alerta_proceso:
        lista_problemas += ["- Carga excesiva por proceso activo."]

    if alerta_recursos:
        lista_problemas += ["- Recursos disponibles insuficientes para la demanda actual."]

    if alerta_disco:
        lista_problemas += ["- Espacio en disco insuficiente para Windows Server."]

    if len(lista_problemas) == 0:
        lista_problemas += ["- Sin problemas detectados."]    

    return lista_problemas

def mostrar_problemas_detectados(lista_problemas:list) -> None:

    print("\nProblemas detectados:")

    for problema in lista_problemas:
        print(f"{problema}")

def generar_recomendaciones(alerta_critica:bool, alerta_mantenimiento:bool, alerta_seguridad:bool, alerta_normal:bool,alerta_web:bool, alerta_proceso:bool, alerta_recursos:bool, alerta_disco:bool) -> list:

    lista_recomendaciones = []

    if alerta_critica:
        lista_recomendaciones += ["✓ Finalizar procesos no esenciales inmediatamente."]
    
    if alerta_mantenimiento:
        lista_recomendaciones += ["✓ Liberar espacio en disco y revisar procesos activos."]

    if alerta_seguridad:
        lista_recomendaciones += ["✓ Activar el firewall de inmediato."]
    
    if alerta_normal:
        lista_recomendaciones += ["✓ Continuar monitoreo de rutina, no se requiere acción."] 

    if alerta_web:
        lista_recomendaciones += ["✓ Escalar recursos o activar balanceo de carga."] 

    if alerta_proceso:
        lista_recomendaciones += ["✓ Identificar y optimizar los procesos más demandantes."] 

    if alerta_recursos:
        lista_recomendaciones += ["✓ Reducir usuarios conectados o aumentar capacidad."] 

    if alerta_disco:
        lista_recomendaciones += ["✓ Liberar almacenamiento o ampliar el volumen de disco."] 

    if len(lista_recomendaciones) == 0:
        lista_recomendaciones += ["✓ Continuar monitoreo de rutina."]
    
    return lista_recomendaciones

def mostrar_recomendaciones(lista_recomendaciones) -> None:
    
    print("\nRecomendaciones:")

    for recomendacion in lista_recomendaciones:
        print(f"\n{recomendacion}")
        print("\n------------------------------------------------------------")

