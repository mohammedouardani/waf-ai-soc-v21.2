# WAF AI SOC v21.2 STABLE

# Dashboard Web

## Introducción

El Dashboard Web es la interfaz gráfica de WAF AI SOC v21.2 STABLE destinada a la visualización del estado del sistema y de la información generada durante el funcionamiento de la plataforma.

Su objetivo es proporcionar una visión centralizada de los eventos registrados y facilitar las tareas de monitorización y supervisión.

## Objetivo

El Dashboard Web permite consultar de forma visual la información disponible en la plataforma, facilitando el seguimiento de la actividad del sistema y el análisis de los eventos registrados.

Su diseño ofrece un punto único de acceso a la información presentada por WAF AI SOC v21.2 STABLE.

## Función dentro del sistema

El Dashboard Web obtiene la información mediante la API REST y presenta los datos de forma organizada para facilitar su consulta.

Esta separación mantiene desacopladas las funciones de almacenamiento, procesamiento y presentación de la información.

## Flujo de información

El flujo general de visualización sigue el siguiente esquema:

```text
SQLite
    │
    ▼
 API REST
    │
    ▼
Dashboard Web
    │
    ▼
   Usuario
```

## Visualización de la información

El Dashboard Web presenta la información disponible mediante una interfaz centralizada que facilita la consulta del estado de la plataforma y de los eventos registrados.

La representación de los datos permite obtener una visión general del funcionamiento del sistema.

## Integración con la API REST

El Dashboard Web utiliza la API REST como mecanismo de acceso a la información almacenada por la plataforma.

Esta arquitectura facilita la independencia entre la interfaz de usuario y el sistema de almacenamiento de datos.

## Monitorización

El Dashboard Web facilita las tareas de supervisión mediante la presentación organizada de la información generada por WAF AI SOC v21.2 STABLE.

Su utilización permite realizar un seguimiento continuo del estado de la plataforma.

## Trazabilidad

El Dashboard Web representa la última etapa del flujo de información, mostrando los resultados obtenidos durante el procesamiento de los eventos.

Esta organización facilita la consulta y el seguimiento de la actividad registrada.

## Logs

La actividad relacionada con el Dashboard Web puede generar registros destinados al diagnóstico, la monitorización y la verificación del correcto funcionamiento de la interfaz.
