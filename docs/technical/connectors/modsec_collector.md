# WAF AI SOC v21.2 STABLE - ModSecurity Collector Connector

## 1. Descripción

El script `modsec_collector.py` es el conector encargado de recoger eventos generados por ModSecurity y prepararlos para el procesamiento posterior dentro del pipeline WAF AI SOC v21.2 STABLE.

Su función principal es leer el Audit Log de ModSecurity, validar los eventos de seguridad y enviarlos al canal interno de comunicación `events.pipe`.

---

## 2. Ubicación

Código fuente:

```text
/opt/waf-v21.2/connectors/modsec_collector.py
```
Archivo de entrada:

```text
/var/log/modsec_audit.log
```

Canal de salida:

```text
/opt/waf-v21.2/connectors/events.pipe
```
---

## 3. Funcionamiento general

El Collector mantiene una lectura continua del Audit Log de ModSecurity.

Flujo:

```text
ModSecurity Audit Log
        |
        v
modsec_collector.py
        |
        v
Validación del evento
        |
        v
Extracción de datos
        |
        v
events.pipe
```
---

## 4. Extracción del Anomaly Score

La función `extract_score()` analiza los mensajes generados por ModSecurity.

El Collector busca el valor:

Total Score: <valor>

Si existe, utiliza el valor encontrado.

Cuando ModSecurity genera mensajes pero no aparece un Total Score, el Collector asigna un valor inicial:

score = 5

---

## 5. Procesamiento del evento

La función `parse_event()` obtiene:

Dirección IP del cliente.
URI solicitada.
Timestamp del evento.
Mensajes generados por ModSecurity.
Anomaly Score.

Formato de salida generado:

IP|URI|SCORE|TIMESTAMP

Ejemplo:

192.168.1.50|/login|10|2026-07-26T10:00:00

---

## 6. Filtrado de eventos

El Collector descarta eventos que no corresponden a actividad de seguridad.

Se ignoran:

```text
/api/
/favicon.ico
/robots.txt
```

También se descartan eventos sin mensajes de ModSecurity o sin un ruleId válido.

## 7. Comunicación mediante events.pipe

Los eventos válidos son enviados mediante la función `write_pipe()` al canal:

/opt/waf-v21.2/connectors/events.pipe

Cada evento se escribe en una línea independiente.

---

## 8. Ejecución del proceso

El Collector se ejecuta mediante systemd:

waf-ai-soc-v21.2-collector.service

Comando:

```bash
/opt/waf-v21.2/venv/bin/python /opt/waf-v21.2/connectors/modsec_collector.py
```

---

## 9. Gestión del Audit Log

El proceso mantiene una lectura continua del archivo de auditoría.

Incluye detección de rotación del log:

```text
Log rotation detected, resetting
```
---

## 10. Integración dentro del sistema

El Collector actúa como primer componente del pipeline:

```text
ModSecurity
      |
      v
Collector Connector
      |
      v
events.pipe
      |
      v
AI Processor
```
