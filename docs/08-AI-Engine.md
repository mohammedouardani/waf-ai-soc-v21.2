# WAF AI SOC v21.2 STABLE

# AI Engine

## Introducción

El AI Engine es el componente encargado de analizar los eventos de seguridad procesados por WAF AI SOC v21.2 STABLE.

Su función consiste en evaluar la información recibida, clasificar los eventos según los criterios definidos por la plataforma y preparar los resultados para su almacenamiento y posterior consulta.

## Objetivo del AI Engine

El objetivo del AI Engine es proporcionar una capa de análisis que permita clasificar los eventos de seguridad de forma consistente, facilitando su interpretación y gestión dentro del sistema.

Esta separación permite mantener desacoplado el proceso de análisis del resto de componentes de la plataforma.

## Función dentro del sistema

El AI Engine recibe los eventos preparados por el Event Pipeline y realiza el procesamiento necesario para determinar su clasificación.

Tras completar el análisis, los resultados son enviados a las capas encargadas del almacenamiento y visualización de la información.

## Flujo de procesamiento

El funcionamiento general del AI Engine sigue el siguiente esquema:

```text
Event Collector
        │
        ▼
    AI Engine
        │
        ▼
 Clasificación
        │
        ▼
    SQLite
        │
        ▼
    API REST
        │
        ▼
 Dashboard Web
```

## Recepción de eventos

El AI Engine recibe los eventos preparados por el Event Pipeline para iniciar su análisis.

Cada evento contiene la información necesaria para que el motor pueda realizar su procesamiento dentro del flujo interno del sistema.

## Análisis y clasificación

Durante el procesamiento, el AI Engine evalúa los eventos y determina su clasificación de acuerdo con los criterios establecidos por la plataforma.

El resultado del análisis facilita las tareas posteriores de monitorización, consulta y gestión de eventos.

## Integración con el Event Pipeline

El AI Engine forma parte del flujo de procesamiento de eventos de WAF AI SOC v21.2 STABLE.

Su integración permite mantener una separación clara entre la recopilación de información, el análisis y el almacenamiento de los resultados.

## Gestión de resultados

Una vez finalizado el análisis, los resultados son preparados para su almacenamiento en la base de datos y su posterior consulta mediante la API REST y el Dashboard Web.

## Trazabilidad

El AI Engine mantiene la continuidad del procesamiento dentro del flujo de eventos, facilitando el seguimiento de la información desde su recepción hasta su almacenamiento.

## Logs

El AI Engine puede generar registros de actividad destinados a la monitorización, el diagnóstico y la verificación del funcionamiento interno del motor de inteligencia artificial.

Estos registros permiten analizar el procesamiento de eventos, comprobar la clasificación realizada por el motor y facilitar las tareas de diagnóstico durante la administración del sistema.

La ubicación y el formato de los registros dependen de la configuración del despliegue y de los componentes habilitados en la instalación.

---

## Documentación técnica relacionada

La documentación detallada del procesamiento interno del motor AI se encuentra en:

- `technical/ai/processor.md`
