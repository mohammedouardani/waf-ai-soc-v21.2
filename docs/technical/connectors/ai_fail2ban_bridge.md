# WAF AI SOC v21.2 STABLE - AI Fail2Ban Bridge Connector

## 1. Descripción

El script `ai_fail2ban_bridge.py` es el conector encargado de enlazar los eventos de bloqueo generados por el sistema WAF AI SOC con el registro de eventos de seguridad.

Su función es monitorizar el log de bloqueos, detectar acciones `BLOCK` y registrar las IP bloqueadas en el log de eventos del sistema.

---

## 2. Ubicación

Código fuente:

```text
/opt/waf-v21.2/connectors/ai_fail2ban_bridge.py
```
Archivo de entrada:

```text
/opt/waf-v21/logs/waf-ai-ban.log
```

Archivo de salida:

```text
/opt/waf-v21/logs/waf-ai-events.log
```
---

## 3. Funcionamiento general

El Bridge mantiene una lectura continua del log de bloqueos.

Flujo:

```text
WAF AI SOC BLOCK Event
          |
          v
waf-ai-ban.log
          |
          v
ai_fail2ban_bridge.py
          |
          v
waf-ai-events.log
```

---

## 4. Procesamiento de eventos

La función `process()` analiza cada línea recibida.

Solo procesa eventos que contienen:

```text
ACTION=BLOCK
```

Las líneas sin esta acción son ignoradas.

---

## 5. Extracción de IP

El Bridge obtiene la dirección IP mediante una expresión regular:

IP=192.168.1.100

Cuando encuentra una IP válida, genera un registro:

`TIMESTAMP BLOCK IP=x.x.x.x`

---

## 6. Control de duplicados

El script mantiene un conjunto interno:

```text
seen
```

para evitar registrar varias veces la misma IP durante la ejecución del proceso.

---

## 7. Lectura continua del log

La función `main()` mantiene una lectura permanente del archivo origen.

El proceso comienza desde el final del archivo:

```python
seek(0,2)
```

y espera nuevas líneas generadas por el sistema.

---

## 8. Integración dentro del sistema

El Bridge forma parte del flujo de defensa activa:

```text 
AI Processor
      |
      v
ACTION=BLOCK
      |
      v
waf-ai-ban.log
      |
      v
AI Fail2Ban Bridge
      |
      v
waf-ai-events.log
```
