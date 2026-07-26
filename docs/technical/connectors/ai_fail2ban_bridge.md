# WAF AI SOC v21.2 STABLE - AI Fail2Ban Bridge Connector

## 1. Descripción

El script `ai_fail2ban_bridge.py` es un componente encargado de conectar las acciones de bloqueo generadas por el sistema WAF AI SOC v21.2 STABLE con el registro interno de eventos defensivos.

Su función es monitorizar el log de bloqueos generado por la capa de defensa y transformar las acciones `BLOCK` en eventos registrados dentro del sistema.

Este componente actúa como puente entre la respuesta automática mediante Fail2Ban/UFW y el sistema de monitorización SOC.

---

## 2. Ubicación

Código fuente:

```text
/opt/waf-v21.2-github/connectors/ai_fail2ban_bridge.py
```
Logs utilizados:

Origen:
```text
/opt/waf-v21.2/logs/waf-ai-ban.log
```

Destino:

```text
/opt/waf-v21.2/logs/waf-ai-events.log
```
---

## 3. Funcionamiento general

El Bridge mantiene una lectura continua del log de bloqueos.

Flujo:

```text
Evento AI BLOCK
        |
        v
waf-ai-ban.log
        |
        v
ai_fail2ban_bridge.py
        |
        v
Detección ACTION=BLOCK
        |
        v
Extracción IP
        |
        v
Registro SOC Event
```
---

## 4. Procesamiento del evento

La función principal es:

`process(line)`

Realiza las siguientes acciones:

Comprueba si la línea contiene:

```text
ACTION=BLOCK
```
Extrae la dirección IP mediante expresión regular.

Evita registrar varias veces la misma IP mediante:

`seen = set()`

Genera una entrada en el log de eventos.

---

## 5. Registro generado

Cuando se detecta un bloqueo válido se añade una entrada:

```text
TIMESTAMP BLOCK IP=x.x.x.x
```
El registro queda almacenado en:

```text
waf-ai-events.log
```
---

## 6. Monitorización continua

La función:

`main()`

abre el log origen y se posiciona al final del archivo:

`seek(0,2)`

Después mantiene una lectura continua esperando nuevos eventos.

Cuando no existen nuevas líneas, realiza una espera:

`time.sleep(1)`

---

## 7. Integración dentro del sistema

```text
AI Processor
      |
      v
Decisión BLOCK
      |
      v
Fail2Ban + UFW
      |
      v
waf-ai-ban.log
      |
      v
AI Fail2Ban Bridge
      |
      v
waf-ai-events.log
      |
      v
Dashboard / SOC
```
---

## 8. Diferencia con events.pipe

Este componente no utiliza el canal FIFO:

```text
events.pipe
```
El FIFO se utiliza para comunicación entre Collector y AI Processor.

`ai_fail2ban_bridge.py` trabaja con logs de defensa y eventos de bloqueo.

