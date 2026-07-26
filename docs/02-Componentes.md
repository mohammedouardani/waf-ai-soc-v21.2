# WAF AI SOC v21.2 STABLE

# Componentes del Sistema

## Introducción

WAF AI SOC v21.2 STABLE está formado por diferentes componentes independientes que trabajan conjuntamente para proporcionar protección web, análisis de eventos y monitorización del sistema.

## Nginx

Nginx es el componente encargado de recibir y gestionar las conexiones HTTP/HTTPS que llegan al sistema.

Actúa como punto de entrada del tráfico web y permite la integración con la capa de protección mediante ModSecurity.

## ModSecurity

ModSecurity es el motor de seguridad web encargado de inspeccionar las peticiones recibidas por Nginx.

Su función es analizar el tráfico mediante reglas de seguridad y generar eventos cuando detecta patrones que requieren revisión o acción.

## OWASP Core Rule Set (CRS)

OWASP Core Rule Set (CRS) proporciona el conjunto de reglas de seguridad utilizado por ModSecurity para detectar patrones de ataque conocidos.

Estas reglas permiten identificar comportamientos asociados a diferentes tipos de amenazas web y generar eventos de seguridad para su posterior análisis.

## Event Collector

Event Collector es el componente encargado de recopilar los eventos generados por la capa de seguridad del sistema.

Su función es recibir la información de los eventos y prepararla para el procesamiento posterior dentro del flujo del SOC.

## AI Processor

AI Processor es el componente encargado de analizar y clasificar los eventos de seguridad recibidos.

Su función es procesar la información de los eventos, aplicar el análisis correspondiente y determinar la clasificación del riesgo dentro del sistema.

## SQLite

SQLite es el sistema de almacenamiento utilizado por WAF AI SOC v21.2 STABLE para guardar la información generada por el sistema.

La base de datos permite conservar los datos necesarios para la consulta, análisis y visualización de los eventos registrados.

## API REST

La API REST proporciona una interfaz de acceso a la información generada por WAF AI SOC v21.2 STABLE.

Su función es permitir la consulta de datos del sistema y servir como enlace entre la información almacenada y el Dashboard Web.

## Dashboard Web

El Dashboard Web proporciona una interfaz visual para consultar el estado del sistema y la información generada por WAF AI SOC v21.2 STABLE.

Permite visualizar los datos disponibles del SOC de forma centralizada.

## Fail2Ban

Fail2Ban es el componente encargado de aplicar acciones de bloqueo cuando se cumplen las condiciones definidas por el sistema.

Su integración permite ejecutar respuestas automáticas frente a eventos de seguridad que requieren intervención.

## UFW

UFW (Uncomplicated Firewall) proporciona la capa de filtrado de red del sistema.

Su función es controlar el tráfico entrante y saliente mediante reglas de firewall que limitan el acceso a los servicios autorizados y complementan las medidas de protección del WAF y de Fail2Ban.

## Servicios Systemd

Los servicios Systemd permiten gestionar el ciclo de vida de los distintos componentes de WAF AI SOC v21.2 STABLE.

Su utilización garantiza el inicio automático, la supervisión y la ejecución controlada de los servicios que forman parte de la plataforma.

## Backup y Restore

El sistema de copias de seguridad permite preservar la configuración, la documentación y los datos necesarios para recuperar la plataforma en caso de incidencia.

Su objetivo es facilitar la restauración del sistema manteniendo la integridad de la información almacenada.

## Logs

El sistema genera registros de actividad que permiten realizar tareas de monitorización, auditoría y análisis forense.

Los diferentes componentes producen información que facilita el seguimiento del funcionamiento de la plataforma y la investigación de eventos de seguridad.

## Documentación

La documentación reúne la información técnica necesaria para la instalación, administración, mantenimiento y evolución de WAF AI SOC v21.2 STABLE.

Su organización facilita la consulta de cada componente de forma independiente, manteniendo una visión global de la arquitectura del sistema.


