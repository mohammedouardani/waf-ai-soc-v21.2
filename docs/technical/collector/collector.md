# WAF AI SOC v21.2 STABLE
# ModSecurity Collector

## 1. Descripción

El componente `modsec_collector.py` pertenece a la capa de adquisición de eventos de WAF AI SOC v21.2 STABLE.

Su función principal es recoger los eventos generados por ModSecurity, procesarlos y convertirlos en un formato interno compatible con el motor de análisis AI Processor.

El Collector actúa como puente entre ModSecurity y el sistema interno de procesamiento de eventos.

Flujo general:
```
ModSecurity
|
v
Audit Log JSON
|
v
modsec_collector.py
|
v
events.pipe
|
v
AI Processor
```

---

## 2. Ubicación del componente

Código fuente:

/opt/waf-v21.2/connectors/modsec_collector.py


Documentación técnica:

/opt/waf-v21.2/docs/technical/collector/collector.md

---

## 3. Objetivo del Collector

El Collector tiene las siguientes responsabilidades:

- Leer eventos del Audit Log de ModSecurity.
- Analizar únicamente eventos relacionados con seguridad.
- Extraer IP origen, URI, puntuación y timestamp.
- Filtrar eventos internos no relevantes.
- Entregar eventos normalizados al siguiente componente del SOC.

El Collector no realiza clasificación AI ni toma decisiones de bloqueo.

Su responsabilidad es únicamente la recopilación y preparación inicial de datos.

---

## 4. Dependencias Python

El componente utiliza las siguientes librerías estándar:

```python
json
time
re
os
```

## 5. Configuración del componente

El Collector utiliza dos rutas principales:
```python
AUDIT_LOG = "/var/log/modsec_audit.log"
PIPE = "/opt/waf-v21.2/connectors/events.pipe"
```
Archivo de entrada utilizado para leer los eventos generados por ModSecurity.

`AUDIT_LOG` apunta al fichero donde ModSecurity almacena los eventos de auditoría en formato JSON.

`PIPE` define el canal interno utilizado por WAF AI SOC v21.2 STABLE para entregar los eventos procesados al siguiente componente del sistema.

---


## 6. Modelo de funcionamiento

El Collector trabaja en modo monitorización continua del Audit Log de ModSecurity.

Proceso general:

1. Abre el fichero de auditoría de ModSecurity.
2. Se posiciona al final del log actual.
3. Espera nuevas entradas.
4. Procesa cada evento JSON recibido.
5. Valida si el evento corresponde a una detección de seguridad.
6. Genera un evento normalizado.
7. Envía el resultado mediante `events.pipe`.

---

## 7. Filtrado de eventos

Antes de enviar un evento al pipeline interno, el Collector realiza varias validaciones para descartar información no relevante.

El objetivo es evitar que eventos internos o solicitudes sin impacto de seguridad lleguen al procesamiento AI.

El Collector aplica los siguientes filtros:

### Exclusión de llamadas internas del Dashboard

Las peticiones dirigidas a la API interna del sistema son ignoradas:

```python
if uri.startswith("/api/"):
    return None
```

### Exclusión de recursos comunes

También se descartan peticiones hacia recursos estáticos:

```python
"/favicon.ico"
"/robots.txt"
```
Estas rutas no representan actividad maliciosa y no deben entrar en el análisis del SOC.

### Validación de reglas ModSecurity

El Collector comprueba que el evento contiene al menos un `ruleId` válido antes de continuar.

El identificador de regla permite asociar el evento con la detección generada por ModSecurity y conservar la referencia del origen del evento.

Los eventos que no contienen información suficiente de regla no continúan en el proceso normal de análisis.


### Obtención del Anomaly Score

Una vez validado el evento, el Collector obtiene el valor de puntuación de anomalía generado por ModSecurity.

El proceso utiliza la función `extract_score()` para revisar los mensajes asociados a la transacción y localizar el valor `Total Score`.

Si ModSecurity ha generado mensajes pero no existe un valor `Total Score` disponible, el Collector asigna un valor mínimo de puntuación para conservar el evento dentro del flujo de análisis.

El valor obtenido será utilizado posteriormente por el procesamiento AI del WAF AI SOC.

### Construcción del evento de salida

Después de procesar y validar la información del evento ModSecurity, el Collector construye una línea de salida con los datos principales de la detección.
El formato generado es:
```
IP_ORIGEN|URI|SCORE|TIMESTAMP
```
Los campos incluidos son:

- IP origen del cliente.
- URI solicitada.
- Anomaly Score calculado.
- Marca temporal del evento.

Esta estructura permite entregar una información simplificada y uniforme al siguiente componente del pipeline WAF AI SOC.

### Escritura del evento en el pipe interno

Una vez generado el evento de salida, el Collector lo escribe en el pipe interno definido por el sistema:

```text
/opt/waf-v21.2/connectors/events.pipe
```
La función `write_pipe()` abre el pipe interno en modo escritura y añade el evento generado por el Collector.

Cada evento se escribe en una nueva línea y se fuerza la descarga del contenido mediante `flush()` para asegurar que la información esté disponible inmediatamente para los componentes posteriores del sistema.

Este mecanismo permite la comunicación entre el Collector y el resto del pipeline WAF AI SOC.

### Inicio del proceso Collector

La función `run()` inicia la ejecución del Collector y muestra el mensaje de arranque del componente:

```text
WAF AI SOC v21.2 ModSecurity Collector STARTED
```
A continuación, el Collector abre el archivo de auditoría de ModSecurity definido en:

```text
/var/log/modsec_audit.log
```
El proceso se posiciona al final del archivo mediante `seek(0, 2)` para comenzar a procesar únicamente los nuevos eventos generados a partir del momento de inicio.

### Lectura continua del Audit Log

Después de abrir el archivo de auditoría, el Collector se posiciona al final del fichero para trabajar en modo seguimiento continuo.

El Collector lee de forma continua las nuevas entradas del Audit Log e intenta procesar cada evento JSON cuando dispone de una estructura válida para su análisis.

El proceso permanece en ejecución mediante un bucle continuo, esperando nuevos eventos generados por ModSecurity.


### Detección de rotación del Audit Log

El Collector comprueba continuamente el tamaño actual del archivo de auditoría para detectar posibles rotaciones del log de ModSecurity.

Si la posición de lectura supera el tamaño actual del archivo, el sistema interpreta que se ha producido una rotación del log.

En ese caso:

- Muestra un mensaje indicando la detección de rotación.
- Reinicia la posición de lectura del archivo.

Este mecanismo permite que el Collector continúe funcionando correctamente después de una rotación del archivo de auditoría.

### Lectura de nuevas líneas del Audit Log

El Collector lee nuevas líneas del archivo de auditoría mediante una lectura continua del fichero.

Cuando no existe una nueva línea disponible, el proceso realiza una pequeña espera antes de volver a comprobar el archivo.

Este comportamiento permite mantener un consumo eficiente de recursos mientras espera nuevos eventos generados por ModSecurity.


## Funcionamiento como servicio permanente

El Collector está diseñado para ejecutarse de forma continua como un componente del WAF AI SOC v21.2.

Su ejecución permanente permite mantener una monitorización constante del Audit Log de ModSecurity sin necesidad de intervención manual.

Como servicio del sistema, el Collector:

- Inicia automáticamente junto al entorno del WAF AI SOC.
- Mantiene activo el proceso de lectura.
- Supervisa nuevos eventos de seguridad.
- Entrega información al siguiente componente del pipeline.
- Permanece operativo durante largos periodos de ejecución.

Flujo de operación:

```text
systemd
   |
   v
Collector
   |
   v
Monitorización Audit Log
   |
   v
Eventos ModSecurity
   |
   v
AI Processor
```
---

## Resumen del componente Collector

El Collector es el componente encargado de actuar como puente entre ModSecurity y el sistema de análisis del WAF AI SOC v21.2.

Su responsabilidad principal es transformar el Audit Log generado por ModSecurity en eventos preparados para el procesamiento posterior.

Funciones principales:

- Apertura y monitorización continua del Audit Log.
- Detección de rotaciones del fichero.
- Lectura incremental de nuevas entradas.
- Procesamiento y validación de eventos JSON del Audit Log.
- Preparación de información para el AI Processor.
- Funcionamiento continuo como servicio del sistema.

Arquitectura del flujo:

```text
ModSecurity
      |
      v
Audit Log JSON
      |
      v
Collector
      |
      v
events.pipe
      |
      v
AI Processor
      |
      v
SQLite
      |
      v
Dashboard
```
---

