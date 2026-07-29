# WAF AI SOC v21.2 STABLE

# Base de Datos

## Introducción

La base de datos es el componente encargado de almacenar de forma persistente la información generada por WAF AI SOC v21.2 STABLE.

Su función es conservar los eventos procesados y los datos necesarios para su consulta, monitorización y análisis posterior.

## Objetivo

El objetivo de la base de datos es proporcionar un almacenamiento fiable y organizado para la información gestionada por la plataforma.

Esta organización facilita la consulta de los datos, la generación de informes y el análisis histórico de la actividad del sistema.

## SQLite

WAF AI SOC v21.2 STABLE utiliza SQLite como sistema de almacenamiento de datos.

SQLite proporciona una base de datos ligera, integrada y adecuada para el funcionamiento de la plataforma, simplificando su despliegue y administración.

## Información almacenada

La base de datos almacena la información generada por los distintos componentes del sistema.

Entre los datos almacenados se incluyen los eventos procesados y la información necesaria para su posterior consulta y visualización.

## Integración con el Event Pipeline

La base de datos recibe la información procesada por el Event Pipeline una vez finalizado el análisis de los eventos.

Esta integración permite conservar el historial de actividad generado por la plataforma.

## Consulta de información

Los datos almacenados pueden ser consultados mediante la API REST, que actúa como interfaz de acceso para el resto de componentes del sistema.

Esta separación mantiene desacopladas las tareas de almacenamiento y presentación de la información.

## Integración con el Dashboard

El Dashboard Web obtiene la información necesaria mediante la API REST para representar el estado del sistema y los eventos registrados.

La base de datos actúa como repositorio central de la información utilizada por la plataforma.

## Integridad de los datos

La organización de la información almacenada permite mantener la consistencia de los datos utilizados por WAF AI SOC v21.2 STABLE.

La persistencia de los eventos facilita las tareas de auditoría, monitorización y análisis forense.

## Backup y Restore

La información almacenada puede incluirse en los procedimientos de copia de seguridad y restauración definidos para la plataforma.

Estas operaciones permiten recuperar el estado del sistema en caso de incidencia.

## Logs

La actividad relacionada con la base de datos puede generar registros destinados al diagnóstico, la monitorización y la verificación del correcto funcionamiento del sistema.
