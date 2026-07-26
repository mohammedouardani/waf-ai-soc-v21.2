# WAF AI SOC v21.2 STABLE

# ModSecurity

## Introducción

ModSecurity es el motor de seguridad web integrado en WAF AI SOC v21.2 STABLE encargado de inspeccionar y analizar las peticiones HTTP/HTTPS recibidas por la plataforma.

Su función principal es aplicar reglas de seguridad sobre el tráfico procesado por Nginx, permitiendo detectar patrones asociados a posibles amenazas y generar eventos para su posterior análisis dentro del flujo del SOC.

La integración de ModSecurity proporciona una capa de protección frente a diferentes tipos de ataques web y constituye uno de los componentes principales de la arquitectura de defensa de WAF AI SOC v21.2 STABLE.

---

## Función dentro de la arquitectura

ModSecurity actúa como una capa de inspección de seguridad dentro del flujo de procesamiento de WAF AI SOC v21.2 STABLE.

Su ubicación dentro de la arquitectura permite analizar las peticiones recibidas por Nginx antes de que alcancen los servicios protegidos, aplicando los controles definidos por las políticas de seguridad.

Los eventos generados durante el proceso de inspección son enviados al flujo interno del SOC para su recopilación, análisis y posterior tratamiento por los componentes encargados de la gestión de eventos.

---

## Integración con Nginx

ModSecurity se integra con Nginx como módulo de seguridad para inspeccionar las peticiones HTTP/HTTPS recibidas por la plataforma.

Esta integración permite analizar el tráfico antes de que las solicitudes sean entregadas a los servicios protegidos, aplicando las reglas de seguridad definidas dentro del entorno WAF AI SOC v21.2 STABLE.

La comunicación entre Nginx y ModSecurity permite generar eventos de seguridad cuando una petición coincide con patrones identificados como potencialmente maliciosos.

---

## OWASP Core Rule Set (CRS)

OWASP Core Rule Set (CRS) proporciona el conjunto de reglas de seguridad utilizado por ModSecurity para identificar patrones asociados a diferentes tipos de amenazas web.

Estas reglas permiten detectar comportamientos sospechosos dentro de las peticiones recibidas, generando eventos de seguridad que pueden ser analizados posteriormente por los componentes del SOC.

La integración de CRS dentro de ModSecurity proporciona una base de protección frente a ataques web conocidos y permite mantener una política de inspección estructurada dentro de WAF AI SOC v21.2 STABLE.

---

## Reglas de seguridad

Las reglas de seguridad de ModSecurity definen los criterios utilizados para analizar las peticiones recibidas por la plataforma.

Estas reglas permiten identificar patrones asociados a posibles ataques web, aplicar controles de inspección sobre el tráfico y generar eventos cuando se detectan comportamientos que requieren análisis.

Dentro de WAF AI SOC v21.2 STABLE, las reglas de seguridad forman parte de la capa de detección inicial y proporcionan la información necesaria para el procesamiento posterior dentro del flujo del SOC.

---

## Generación de eventos

ModSecurity genera eventos de seguridad cuando una petición coincide con los criterios definidos por las reglas de inspección configuradas.

Estos eventos contienen la información necesaria para identificar la actividad detectada, facilitar su análisis y permitir su integración dentro del flujo de procesamiento de WAF AI SOC v21.2 STABLE.

La generación de eventos constituye el punto de conexión entre la capa de detección de ModSecurity y los componentes encargados de la recopilación, análisis y gestión de la información de seguridad.

---

## Logs de ModSecurity

Los registros generados por ModSecurity permiten conservar información sobre las inspecciones realizadas y los eventos de seguridad detectados durante el procesamiento del tráfico web.

Estos registros proporcionan datos necesarios para tareas de monitorización, auditoría, análisis de incidencias y revisión del comportamiento de las reglas de seguridad.

La gestión adecuada de los logs de ModSecurity facilita la trazabilidad de los eventos y permite integrar la información generada dentro del flujo de análisis de WAF AI SOC v21.2 STABLE.

---

## Integración con Event Collector

ModSecurity se integra con Event Collector para transmitir los eventos de seguridad generados durante la inspección del tráfico web.

Esta integración permite recopilar la información producida por las reglas de seguridad y prepararla para las siguientes etapas del procesamiento dentro de WAF AI SOC v21.2 STABLE.

El flujo entre ModSecurity y Event Collector garantiza que los eventos detectados sean centralizados, registrados y enviados hacia los componentes encargados del análisis y clasificación de seguridad.

---

## Resumen

ModSecurity constituye uno de los componentes principales de protección dentro de WAF AI SOC v21.2 STABLE.

Su integración con Nginx permite inspeccionar el tráfico HTTP/HTTPS recibido por la plataforma, aplicar reglas de seguridad y generar eventos cuando se detectan patrones asociados a posibles amenazas.

La utilización de OWASP Core Rule Set (CRS), junto con la generación y transferencia de eventos hacia Event Collector, permite incorporar la información de seguridad dentro del flujo de análisis del SOC.

Este componente representa la primera capa de inspección avanzada dentro de la arquitectura de defensa de WAF AI SOC v21.2 STABLE.

