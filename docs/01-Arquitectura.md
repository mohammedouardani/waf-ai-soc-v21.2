# WAF AI SOC v21.2 STABLE

# Arquitectura del Sistema

## Visión General

WAF AI SOC v21.2 STABLE está diseñado mediante una arquitectura modular donde diferentes componentes trabajan de forma independiente para realizar la protección, análisis y monitorización de eventos de seguridad.

El sistema integra la capa de protección web, procesamiento de eventos, análisis AI, almacenamiento y visualización mediante Dashboard.

## Capas del Sistema

La arquitectura de WAF AI SOC v21.2 STABLE está formada por varias capas principales:

### Capa Web

Responsable de recibir y gestionar las conexiones HTTP/HTTPS mediante Nginx.

### Capa de Protección

Formada por ModSecurity y OWASP Core Rule Set (CRS), encargada de inspeccionar las peticiones y detectar patrones maliciosos.

### Capa de Análisis

Compuesta por Event Collector y AI Processor, encargada de recopilar, procesar y clasificar los eventos de seguridad.

### Capa de Datos

Utiliza SQLite como sistema de almacenamiento de información generada por el SOC.

### Capa de Visualización

Proporciona acceso mediante API REST y Dashboard Web para consultar el estado y los eventos del sistema.

## Flujo de Datos

El flujo general de información dentro de WAF AI SOC v21.2 STABLE es el siguiente:

1. Una petición llega desde Internet al servidor web Nginx.
2. ModSecurity inspecciona la petición recibida.
3. OWASP CRS aplica las reglas de seguridad configuradas.
4. Los eventos generados son recopilados por Event Collector.
5. AI Processor analiza y clasifica los eventos.
6. La información procesada se almacena en SQLite.
7. La API REST proporciona acceso a los datos.
8. El Dashboard Web muestra la información del sistema.
9. Fail2Ban puede actuar sobre eventos que requieran bloqueo.

## Componentes Principales

### Nginx

Servidor web encargado de recibir y gestionar las conexiones HTTP/HTTPS.

### ModSecurity

Motor de seguridad web encargado de inspeccionar las peticiones y aplicar las reglas de protección.

### OWASP Core Rule Set (CRS)

Conjunto de reglas de seguridad utilizadas por ModSecurity para detectar patrones de ataque conocidos.

### Event Collector

Componente encargado de recopilar los eventos generados por el sistema.

### AI Processor

Motor encargado del análisis y clasificación de los eventos de seguridad.

### SQLite

Base de datos utilizada para almacenar la información del sistema.

### API REST

Servicio que proporciona acceso a la información del SOC.

### Dashboard Web

Interfaz de visualización del estado y eventos del sistema.

### Fail2Ban

Sistema integrado para aplicar acciones de bloqueo cuando corresponde.

## Servicios del Sistema

WAF AI SOC v21.2 STABLE está compuesto por servicios independientes gestionados mediante systemd.

Los servicios principales del sistema son:

- API Dashboard Service
- Event Collector Service
- AI Processor Service

Cada servicio tiene una función específica dentro de la arquitectura y trabaja de forma independiente para mantener la modularidad del sistema.

## Integración entre Componentes

Los componentes de WAF AI SOC v21.2 STABLE trabajan de forma coordinada mediante el siguiente esquema:

- Nginx recibe las conexiones web.
- ModSecurity y OWASP CRS realizan la inspección de seguridad.
- Event Collector recopila la información generada.
- AI Processor analiza los eventos recibidos.
- SQLite almacena los datos procesados.
- API REST permite consultar la información.
- Dashboard Web presenta el estado del sistema.
- Fail2Ban ejecuta acciones de respuesta cuando corresponde.

La separación de componentes permite mantener una arquitectura modular, facilitar la gestión del sistema y simplificar las tareas de mantenimiento.

## Resumen de Arquitectura

WAF AI SOC v21.2 STABLE utiliza una arquitectura modular orientada a la protección web, análisis de eventos y monitorización del sistema.

La separación entre capas permite que cada componente cumpla una función específica dentro del flujo de seguridad, manteniendo un diseño organizado, estable y preparado para tareas de operación y mantenimiento.

Esta arquitectura corresponde al estado estable del proyecto tras la finalización de la OPERACIÓN CLEAN.


