# WAF AI SOC v21.2 STABLE

## Sobre el proyecto

WAF AI SOC v21.2 STABLE es una plataforma de seguridad diseñada para integrar diferentes capas de protección web en una arquitectura SOC (Security Operations Center).

El proyecto combina tecnologías Open Source para crear una arquitectura de análisis, detección y respuesta automática ante eventos de seguridad.

La arquitectura integra:

- Protección WAF mediante ModSecurity.
- Reglas de seguridad mediante OWASP Core Rule Set (CRS).
- Recolección de eventos mediante Collector.
- Procesamiento y clasificación mediante un motor AI.
- Almacenamiento de eventos en SQLite.
- API Flask para comunicación interna.
- Dashboard web para monitorización.
- Respuesta automática mediante Fail2Ban y UFW.

El objetivo principal del proyecto es estudiar, comprender y documentar cómo diferentes componentes de seguridad pueden trabajar juntos dentro de una arquitectura WAF AI SOC real.

---

## Filosofía del proyecto

Este proyecto nace del aprendizaje continuo, la experimentación práctica y la colaboración con herramientas y comunidades Open Source.

Su objetivo es servir como plataforma de estudio, comprensión y evolución de una arquitectura WAF AI SOC real, permitiendo analizar cómo diferentes tecnologías de seguridad pueden integrarse en un sistema completo de defensa.

> El conocimiento crece cuando se comparte.

---

## Arquitectura

```text
Internet
    |
    v
Nginx HTTPS
    |
    v
ModSecurity + OWASP CRS
    |
    v
Collector
    |
    v
AI Processor
    |
    v
SQLite Database
    |
    v
Flask API
    |
    v
Dashboard
    |
    v
Fail2Ban + UFW
```
Esta arquitectura representa el flujo general del sistema WAF AI SOC v21.2 STABLE, donde cada componente cumple una función dentro del ciclo de detección, análisis y respuesta ante eventos de seguridad.

---

## Componentes principales

### Nginx

Servidor web encargado de recibir las conexiones HTTP/HTTPS y actuar como punto de entrada del sistema.

Funciones principales:

- Gestión del tráfico web.
- Terminación HTTPS.
- Proxy inverso hacia la API.
- Integración con ModSecurity.


### ModSecurity + OWASP CRS

Capa WAF encargada de analizar las peticiones web mediante reglas de seguridad.

Funciones principales:

- Detección de ataques web.
- Aplicación de reglas OWASP Core Rule Set.
- Generación de eventos de seguridad.


### Collector

Componente encargado de recoger los eventos generados por ModSecurity.

Funciones principales:

- Lectura del Audit Log.
- Extracción de información relevante.
- Preparación de eventos para el pipeline.


### AI Processor

Motor de análisis y clasificación del sistema.

Funciones principales:

- Análisis de patrones.
- Cálculo de puntuación de riesgo.
- Clasificación de eventos.
- Generación de decisiones de respuesta.


### SQLite

Base de datos utilizada para almacenar la información del SOC.

Funciones principales:

- Persistencia de eventos.
- Historial de ataques.
- Datos utilizados por la API y Dashboard.


### Flask API

Capa de comunicación interna del sistema.

Funciones principales:

- Exposición de datos del SOC.
- Comunicación con el Dashboard.
- Consulta del estado del sistema.


### Dashboard

Interfaz web de monitorización.

Funciones principales:

- Visualización de eventos.
- Estado del sistema.
- Métricas de seguridad.


### Fail2Ban + UFW

Capa de respuesta automática.

Funciones principales:

- Aplicación de bloqueos.
- Integración con decisiones AI.
- Protección activa mediante firewall.

---

## Instalación

Actualmente WAF AI SOC v21.2 STABLE está orientado a entornos de laboratorio, aprendizaje y experimentación con tecnologías de seguridad Open Source.

Requisitos principales:

- Sistema Linux Debian/Ubuntu.
- Python 3.
- Nginx.
- ModSecurity.
- OWASP Core Rule Set (CRS).
- SQLite.

La instalación completa, configuración y puesta en marcha del sistema se encuentra documentada en:

```text
docs/
```
---

## Documentación

La documentación del proyecto está organizada para separar la visión general del sistema y los detalles técnicos de implementación.

Estructura principal:

```text
docs/
├── 00-README.md
├── 01-Arquitectura.md
├── 02-Componentes.md
├── 03-Estructura-del-proyecto.md
├── 04-Nginx.md
├── 05-ModSecurity.md
├── 06-Connectors.md
├── 07-Event-Pipeline.md
├── 08-AI-Engine.md
├── 09-Base-de-datos.md
├── 10-API.md
├── 11-Dashboard.md
├── 12-Fail2Ban.md
├── 13-UFW.md
├── 14-Systemd.md
├── 15-Backup-y-Restore.md
├── 16-Troubleshooting.md
├── 17-Changelog-v21.2.md
├── 18-Roadmap.md
├── 19-Glosario.md
├── 20-Scripts.md
└── technical/
```
La documentación técnica contiene información detallada sobre la implementación real de cada componente del sistema.

---

## Estado del proyecto

WAF AI SOC v21.2 STABLE representa una versión estable y documentada del proyecto.

Estado actual:

- Arquitectura WAF AI SOC implementada.
- ModSecurity y OWASP CRS integrados.
- Collector operativo para eventos de seguridad.
- AI Processor funcional con clasificación y puntuación de riesgo.
- Base de datos SQLite integrada.
- API Flask operativa.
- Dashboard web disponible.
- Integración Fail2Ban + UFW para respuesta automática.
- Documentación técnica completada.

La versión v21.2 STABLE queda establecida como base de referencia para futuras evoluciones del proyecto.

---

## Roadmap

La evolución del proyecto continuará orientada a mejorar las capacidades de análisis, correlación y automatización de seguridad.

Próximas líneas de evolución:

- Mejora del motor de correlación de eventos.
- Integración de nuevas fuentes de información de seguridad.
- Ampliación de capacidades SOC.
- Investigación de integración con análisis de red.
- Mejoras de visualización y monitorización.
- Evolución hacia una arquitectura SOC AI más completa.

Las futuras versiones se desarrollarán manteniendo la filosofía del proyecto: aprendizaje, documentación y colaboración Open Source.

---

## Licencia

El proyecto está publicado bajo la licencia MIT.

Esta licencia permite estudiar, utilizar, modificar y distribuir el software, manteniendo la referencia original del proyecto.

Consulta el archivo:

```text
LICENSE
```
