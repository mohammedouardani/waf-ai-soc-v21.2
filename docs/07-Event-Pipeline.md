# WAF AI SOC v21.2 STABLE

# Event Pipeline

## Introducción

El Event Pipeline es el flujo interno encargado de gestionar el recorrido de los eventos de seguridad desde su generación hasta su almacenamiento y posterior consulta dentro de WAF AI SOC v21.2 STABLE.

Su diseño permite que cada componente desempeñe una función específica dentro del proceso de análisis, manteniendo una arquitectura modular y facilitando el tratamiento uniforme de la información.

## Objetivo del pipeline

El objetivo del Event Pipeline es garantizar que todos los eventos generados por la plataforma sean procesados de forma ordenada y consistente antes de su almacenamiento y visualización.

Esta organización facilita el análisis de los eventos, la clasificación del riesgo y la consulta posterior de la información registrada.

## Flujo de procesamiento

El flujo general de procesamiento de eventos sigue el siguiente esquema:

```text
Petición HTTP/HTTPS
        │
        ▼
      Nginx
        │
        ▼
  ModSecurity + CRS
        │
        ▼
 Event Collector
        │
        ▼
    AI Processor
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

Los eventos son generados por los distintos componentes del sistema cuando detectan información relevante para la seguridad o el funcionamiento de la plataforma.

El Event Collector recibe estos eventos y los incorpora al flujo interno de procesamiento.

## Normalización

Durante el procesamiento, los eventos son preparados para mantener un formato uniforme que facilite su tratamiento por el resto de componentes del sistema.

La normalización permite reducir diferencias entre las distintas fuentes de información y mantener la consistencia de los datos.

## Análisis mediante AI Processor

El AI Processor analiza los eventos recibidos para determinar su clasificación dentro del sistema.

Este proceso permite identificar el nivel de riesgo asociado a cada evento y preparar la información para su almacenamiento.

## Clasificación de eventos

Tras el análisis, los eventos son clasificados según los criterios definidos por la plataforma.

Esta clasificación facilita posteriormente las tareas de monitorización, búsqueda y análisis de la información registrada.

## Almacenamiento

Una vez procesados, los eventos se almacenan en la base de datos utilizada por WAF AI SOC v21.2 STABLE.

El almacenamiento permite conservar el historial de actividad para su consulta y análisis posterior.

## Consulta desde la API REST

La API REST proporciona acceso a la información almacenada, permitiendo que otros componentes del sistema consulten los datos de forma controlada.

## Visualización en el Dashboard

El Dashboard Web utiliza la información proporcionada por la API REST para mostrar el estado del sistema y los eventos registrados mediante una interfaz centralizada.

## Trazabilidad

El Event Pipeline mantiene el recorrido lógico de cada evento desde su origen hasta su almacenamiento, facilitando las tareas de auditoría, seguimiento y análisis forense.

## Logs

Los distintos componentes del Event Pipeline pueden generar registros de actividad destinados a la monitorización, el diagnóstico y la verificación del correcto funcionamiento de la plataforma.
