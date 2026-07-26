# WAF AI SOC v21.2 STABLE

# Base de datos SQLite

## 1. Introducción

La base de datos SQLite constituye el repositorio central de información del sistema WAF AI SOC v21.2 STABLE.

Su función es almacenar los eventos procesados, mantener el historial de actividad de las direcciones IP y proporcionar la información necesaria para el funcionamiento del AI Processor, la API y el Dashboard.

---

## 2. Objetivo del módulo

El objetivo principal de la base de datos es conservar de forma persistente toda la información generada durante el procesamiento de los eventos de seguridad.

Esta información permite realizar consultas históricas, calcular la reputación de los atacantes, detectar comportamientos repetitivos y suministrar datos al resto de componentes del sistema.

---

## 3. Ubicación

La base de datos principal se encuentra en:

```text
/opt/waf-v21.2/db/soc_v21.db
```

---

## 4. Función dentro del sistema

La base de datos SQLite actúa como repositorio central de información para todos los componentes del WAF AI SOC v21.2 STABLE.

Los diferentes módulos consultan y almacenan información de forma continua durante el funcionamiento del sistema.

Los principales componentes que utilizan la base de datos son:

- Collector.
- AI Processor.
- API.
- Dashboard.

---

## 5. Información almacenada

La base de datos almacena la información generada durante el procesamiento de los eventos de seguridad.

Entre los datos almacenados se incluyen:

- eventos procesados,
- dirección IP origen,
- fecha y hora del evento,
- tipo de ataque detectado,
- puntuación de riesgo,
- severidad asignada,
- acción decidida por el motor AI,
- información utilizada para consultas históricas.

Esta información permite mantener un historial completo de la actividad registrada por el sistema.

---

## 6. Flujo de utilización

La base de datos SQLite participa en varias fases del funcionamiento del WAF AI SOC v21.2 STABLE.

Flujo general:

```text
Collector
      |
      v
AI Processor
      |
      v
SQLite
      |
      +------> API
      |
      +------> Dashboard
```

El AI Processor consulta la información histórica antes de evaluar cada evento y almacena posteriormente el resultado del análisis.

La API utiliza la base de datos para atender las consultas realizadas por el Dashboard y por otros componentes del sistema.

---

## 7. Persistencia de la información

Todos los eventos procesados se almacenan de forma persistente.

La persistencia permite:

- mantener el historial de ataques,
- calcular la reputación de las direcciones IP,
- detectar patrones repetitivos,
- realizar consultas históricas,
- proporcionar información al Dashboard,
- facilitar auditorías de seguridad.

La información almacenada constituye la base para el funcionamiento del motor de análisis y de los componentes de visualización del sistema.


---

## 8. Estructura de la base de datos

La base de datos `soc_v21.db` está organizada en varias tablas utilizadas por los diferentes componentes del WAF AI SOC v21.2 STABLE.

La estructura completa de la base de datos se documenta a partir de la implementación real del sistema.

Para cada tabla se describirán:

- nombre de la tabla,
- finalidad,
- campos almacenados,
- tipo de datos,
- claves primarias,
- índices utilizados,
- relación con el resto de componentes del sistema.

---

## 9. Resumen

La base de datos SQLite constituye el repositorio central de información del WAF AI SOC v21.2 STABLE.

Su función es almacenar de forma persistente los eventos procesados, mantener el historial de actividad y proporcionar la información necesaria para el funcionamiento del AI Processor, la API y el Dashboard.

La información almacenada permite realizar consultas históricas, calcular la reputación de las direcciones IP, detectar patrones de comportamiento y suministrar datos a los distintos componentes del sistema.

La estructura de la base de datos se documenta a partir de las tablas y campos implementados en la versión STABLE del sistema, garantizando que la documentación refleje fielmente el funcionamiento real de WAF AI SOC v21.2 STABLE.


