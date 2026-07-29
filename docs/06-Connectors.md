# WAF AI SOC v21.2 STABLE

# Connectors

## Introducción

Los Connectors son los componentes encargados de facilitar la comunicación entre las diferentes fuentes de información y el flujo interno de procesamiento de WAF AI SOC v21.2 STABLE.

Su función es recopilar, adaptar y transferir los datos generados por los distintos componentes del sistema hacia las capas encargadas del análisis y gestión de eventos.

La utilización de Connectors permite mantener una arquitectura modular, separando los mecanismos de adquisición de información del resto de componentes de la plataforma.

## Función dentro del sistema

Los Connectors actúan como una capa intermedia entre los componentes generadores de información y los módulos encargados del procesamiento.

Sus principales responsabilidades son:

- Recibir información procedente de diferentes fuentes.
- Normalizar los datos recibidos.
- Preparar los eventos para su procesamiento posterior.
- Mantener desacoplados los componentes internos del sistema.

## Flujo de información

El flujo general de comunicación mediante Connectors sigue el siguiente esquema:

```text
Fuente de información
        │
        ▼
   Connector
        │
        ▼
 Event Collector
        │
        ▼
  AI Processor
        │
        ▼
SQLite / API REST / Dashboard
```


## Integración con Event Collector

Los Connectors entregan la información recopilada al Event Collector, que actúa como punto central de recepción de eventos dentro de WAF AI SOC v21.2 STABLE.

Esta separación permite que las fuentes de información puedan evolucionar sin modificar las capas superiores de análisis.

## Gestión de eventos

Los eventos recibidos mediante Connectors contienen la información necesaria para su posterior clasificación, almacenamiento y consulta.

El sistema mantiene una estructura común de eventos para facilitar el procesamiento interno y la trazabilidad.

## Seguridad y aislamiento

Los Connectors funcionan como una capa controlada de comunicación entre componentes.

Su diseño permite limitar dependencias directas y mantener una arquitectura modular, facilitando la administración y mantenimiento del sistema.

## Logs

La actividad relacionada con los Connectors puede generar información de registro destinada a tareas de monitorización, diagnóstico y análisis del funcionamiento de la plataforma.

