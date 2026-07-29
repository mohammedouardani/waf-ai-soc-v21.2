## Objetivos

- Proteger aplicaciones web frente a ataques HTTP/HTTPS.
- Inspeccionar el tráfico mediante ModSecurity y OWASP CRS.
- Procesar y clasificar los eventos de seguridad con el motor AI.
- Registrar los eventos para su análisis y auditoría.
- Aplicar respuestas automáticas mediante Fail2Ban cuando corresponda.
- Centralizar la información en un Dashboard web.
- Mantener una arquitectura modular, estable y documentada.

## Componentes principales

WAF AI SOC v21.2 STABLE está compuesto por los siguientes componentes:

- Nginx
- ModSecurity
- OWASP Core Rule Set (CRS)
- AI Processor
- Event Collector
- API REST
- Dashboard Web
- SQLite
- Fail2Ban

## Flujo general del sistema

Internet
    │
    ▼
Nginx
    │
    ▼
ModSecurity
    │
    ▼
OWASP CRS
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
    ├────────► API REST ───────► Dashboard Web
    │
    └────────► Fail2Ban


## Estructura de la documentación

La documentación de WAF AI SOC v21.2 STABLE se organiza en documentos independientes, cada uno dedicado a un componente o aspecto específico del sistema.

Cada documento describe exclusivamente el componente correspondiente, evitando duplicar información y manteniendo una separación clara entre arquitectura, instalación, configuración, funcionamiento y mantenimiento.


## Información de versión

- Proyecto: WAF AI SOC
- Versión: v21.2 STABLE
- Estado: Congelado tras OPERACIÓN CLEAN
- Tipo de documentación: Documentación técnica del sistema estable
