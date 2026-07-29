# WAF AI SOC v21.2 STABLE

# Tabla attacks

## 1. Introducción

La tabla `attacks` almacena los eventos de seguridad procesados por WAF AI SOC v21.2 STABLE.

Cada registro representa un evento analizado por el AI Processor y constituye la base para las consultas históricas, el cálculo de reputación y la visualización de información en el Dashboard.

---

## 2. Ubicación

La tabla pertenece a la base de datos:

```text
/opt/waf-v21.2/db/soc_v21.db
```

---

## 3. Definición

La estructura implementada es la siguiente:

```sql
CREATE TABLE attacks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    uri TEXT,
    v19_score INT,
    ai_score INT,
    final_score INT,
    ts DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 4. Campos

| Campo | Tipo | Descripción |
|--------|------|-------------|
| id | INTEGER | Identificador único autoincremental. |
| ip | TEXT | Dirección IP origen del evento. |
| uri | TEXT | URI solicitada por el cliente. |
| v19_score | INT | Puntuación inicial generada por el WAF. |
| ai_score | INT | Puntuación calculada por el AI Scoring Engine. |
| final_score | INT | Puntuación final utilizada por el AI Processor. |
| ts | DATETIME | Fecha y hora del registro. |

---

## 5. Utilización

La información almacenada en esta tabla es utilizada por diferentes componentes del sistema:

- AI Processor (lectura y escritura).
- API (lectura).
- Dashboard (a través de la API).

Los datos permiten realizar consultas históricas, calcular la reputación de las direcciones IP y obtener estadísticas del sistema.

---

## 6. Información almacenada

Cada registro contiene:

- dirección IP origen,
- URI analizada,
- puntuación inicial del WAF,
- puntuación calculada por el motor AI,
- puntuación final,
- fecha y hora del evento.

---

## 7. Flujo de utilización

```text
Collector
      |
      v
AI Processor
      |
      v
Tabla attacks
      |
      +------> API
      |
      +------> Dashboard
```

---

## 8. Resumen

La tabla `attacks` constituye el almacenamiento principal de los eventos procesados por WAF AI SOC v21.2 STABLE.

Su contenido permite mantener el historial de actividad, generar estadísticas, calcular la reputación de los atacantes y suministrar información al resto de componentes del sistema.

