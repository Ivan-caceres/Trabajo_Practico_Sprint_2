## Trabajo Practico Integrador Sprint 2
### Grupo 2
- Fabricio Maidana
- Fleitas Agustín
- Lourdes Luna Privitera
- Ivan Caceres
***
# Sistema de Diagnóstico y Configuración de Servidor Basado en Reglas 
## Modalidad 

- Trabajo grupal. 
- Desarrollo incremental por sprints. 
- Defensa oral obligatoria. 
- Evaluación por proceso y producto final. 

## Objetivo General 

### Evolucionar el sistema desarrollado en el Sprint 1 incorporando: 

- Validación robusta de datos de entrada 
- Modularización del código 
- Uso obligatorio de funciones propias 
- Organización lógica del sistema en múltiples archivos 
- Reutilización de código [principio DRY (Don't Repeat Yourself o "No te repitas")] 
- Mejora en mantenibilidad y legibilidad 
*** 
### El objetivo principal de este sprint es transformar un programa funcional en un sistema estructurado, reutilizable y escalable. 
***
## SPRINT 2 – Motor de decisiones 

## Objetivo técnico 

### Evolucionar el sistema del Sprint 1 incorporando: 

- Validación robusta de entradas 
- Separación en funciones 
- Modularización del sistema 
- Mejora en mantenibilidad y escalabilidad 

**En otras palabras: pasar de “script que funciona” → “mini-sistema bien diseñado”.** 
***
## Requerimientos obligatorios 

> ###  1. Validaciones de datos 
- Todos los inputs deben validarse antes de usarse.  

### Tipos de validación esperados

> ### Validación de datos numéricos 

El sistema deberá validar datos numéricos, aceptando valores que representen correctamente números enteros o decimales (flotantes) dentro de un rango permitido. 
#### *Ejemplo*:
    Uso de CPU (%):

### Comportamiento esperado: 
- Si el usuario ingresa 50 → válido 
- Si ingresa 50.5 → válido 
- Si ingresa 0 o 100 → válido (si están dentro del rango definido) 
- Si ingresa -10 → inválido (fuera de rango, si no se permiten negativos) 
- Si ingresa 150 → inválido (fuera de rango) 
- Si ingresa 5. o .5 → inválido (formato incorrecto) 
- Si ingresa 50.5.2 → inválido (más de un punto decimal) 
- Si ingresa abc, 5a o vacío → inválido 

### En caso de error, el sistema deberá: 
- Mostrar un mensaje de error 
- Volver a solicitar el dato 
- Repetir hasta obtener un valor numérico válido (entero o decimal) dentro del rango establecido 
***
> ### Validación de datos de tipo texto 

El sistema deberá validar datos de tipo texto, es decir, cadenas de caracteres que representen información válida y no vacía, solo espacios y tener más de 5 caracteres. 
#### *Ejemplo*:
    Nombre del servidor:

### Comportamiento esperado: 
- Si el usuario ingresa Servidor01 → válido 
- Si ingresa Main Server → válido 
- Si ingresa Admin01 → válido 
- Si ingresa A → Inválido 
- Si ingresa abc → Inválido 
- Si ingresa vacío ("") → inválido 
- Si ingresa solo espacios (" ") → inválido 

### En caso de error, el sistema deberá: 
- Mostrar un mensaje de error 
- Volver a solicitar el dato 
- Repetir hasta obtener un texto válido (no vacío y con al menos un carácter distinto de espacio) 

> ### Validación de opciones cerradas. Categóricas. 

El sistema deberá validar opciones cerradas, es decir, valores que solo pueden pertenecer a un conjunto predefinido. 

### *Ejemplo:*
    Sistema operativo (Linux / Windows Server):

### Comportamiento esperado: 
- Si el usuario ingresa Linux → válido 
- Si ingresa Windows Server → válido 
- Si ingresa linux, Windows, Mac u otro valor → inválido 

### En caso de error, el sistema deberá: 
- Mostrar un mensaje de error 
- Volver a solicitar el dato 
- Repetir hasta obtener un valor correcto 
***
> ### 2. Modularización mediante funciones obligatoria 

- El sistema deberá dividirse en funciones desarrolladas por el grupo. 

### Requisitos mínimos 
- Implementar al menos 6 funciones propias 
- Cada función debe tener una responsabilidad específica 
- No se permite repetir lógica innecesariamente 
- Las validaciones deben reutilizarse mediante funciones 

### *Ejemplos válidos:*
```python
def pedir_numero(...):
    pass
def validar_opcion(...):
    pass
def calcular_carga(...):
    pass
def evaluar_reglas(...):
    pass
def mostrar_resultados(...):
    pass
```
***
> ### 3. Modularización obligatoria 

- El proyecto deberá separarse en múltiples archivos .py. 

### *Estructura mínima sugerida:*
    /proyecto
    |
    |-- main.py
    |-- validaciones.py
    |-- inputs.py
    |-- reglas.py
    |-- calculos.py
    |-- output.py

### Requisitos:

- main.py debe actuar únicamente como punto de entrada del sistema 
- La lógica principal no debe estar completamente dentro de main.py 
- Cada módulo debe tener responsabilidades claras 
- Se deberá utilizar import correctamente 

> ### Reglas 

- Se deberán conservar e integrar las reglas implementadas en el Sprint 1. 

### Requisitos mínimos 

### Mantener al menos 8 reglas  

### Incluir:  
- Reglas con AND  
- Reglas con OR  
- Reglas con NOT  
- Reglas que evalúen rangos  
- Reglas que utilicen múltiples variables 

### Recomendación 

- Las reglas deberán encapsularse en funciones. 

### *Ejemplo:*

```python
def reglas_sobrecarga(cpu, ram):
    return cpu > 85 and ram >80
```
***
> ### 4. Uso algorítmico de listas 

- En este sprint se permite utilizar listas únicamente de forma algorítmica. 

### Esto significa que: 

### Se permite: 
- Crear listas  
- Recorrer listas mediante índices  
- Acceder a posiciones específicas  
- Modificar elementos mediante índices 
- Crear funciones propias para manipulación de listas 

### No se permite: 

- Métodos incorporados de listas (append(), remove(), sort(), etc) 

### *Ejemplo válido:*
```python
alerta = ["", "", "", ""]
alerta[0] = "CPU critica"
alerta[1] = "RAM elevada"

i = 0

while i < len(alertas):
    if alertas[i] != "":
        print(alertas[i])
    i = i + 1
```
***
> ### Restricciones 
### Las reglas: 
- Deben ser explícitas y no redundantes. 
- No deben depender solo de una variable. 
- No deben ser triviales. 
- Deben utilizar la mayor cantidad posible de datos ingresados o calculados. 
***
> ### Evaluación de reglas 
### Debe definirse claramente: 
- Orden de evaluación. 
- Si el sistema: 
  - Devuelve la primera regla válida. 
  - Acumula múltiples alertas y recomendaciones. 
#### La decisión debe estar documentada. 
***
> ### Salida 
### La salida debe: 
- Ser explicativa y amigable para el usuario. 
- Utilizar tabulaciones, colores (colorama) NO OBLIGATORIO, separación visual, etc. 
- Justificar cada diagnóstico realizado. 
- No ser un simple print() aislado. Siempre utilizar f-string. 
***
### Entregables: 
- Código funcional. 
- Documento con listado de reglas implementadas. 
- Breve explicación del flujo de decisión. 
- Ejemplo de ejecución real. 
### Resultado esperado (ejemplo)
"AGREGAR foto de ejemplo"
***
### Flujo esperado del sistema 
    main()
    |-- solicitud y validación de datos
    |-- cálculos y métricas
    |-- evaluacion de reglas
    |-- generación de alertas
    |-- visualización del diagnóstico
***
### Errores graves (penalización importante) 
- No validar entradas  
- Código completamente en main.py  
- Uso de métodos de listas  
- Repetición excesiva de lógica 
- Reglas triviales o redundantes  
- Variables sin nombres descriptivos  
- Funciones excesivamente largas 
