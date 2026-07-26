# WAF AI SOC v21.2 STABLE - Pipeline Connector

## 1. Descripción

El script `pipeline.py` es un componente encargado de procesar eventos JSON internos del sistema WAF AI SOC v21.2 STABLE.

Su función es combinar una puntuación previa del evento (`v19_score`) con la evaluación realizada por el motor AI para generar una puntuación final de riesgo (`final_score`).

Este componente actúa como una capa de enriquecimiento de eventos dentro del procesamiento interno del sistema.

---

## 2. Ubicación

Código fuente:

```text
/opt/waf-v21.2-github/connectors/pipeline.py
```
Dependencia utilizada:

```bash
/opt/waf-v21.2-github/ai/scoring.py
```
---

## 3. Funcionamiento general

El Pipeline Connector recibe una línea en formato JSON, convierte la información en un objeto evento y ejecuta la evaluación AI.

Flujo:

```text
Evento JSON
      |
      v
pipeline.py
      |
      v
Carga del evento
      |
      v
AI Scoring Engine
      |
      v
Cálculo final_score
      |
      v
Evento enriquecido
```
---

## 4. Procesamiento del evento

La función principal es:

`process_event(line)`

La función realiza:

- Conversión del JSON recibido mediante `json.loads()`.
- Evaluación del evento mediante:
  `ai_score(event)`
- Inserción del resultado AI:
 `event["ai_score"]`
- Cálculo de la puntuación final:
 `event["final_score"]`

---

## 5. Cálculo de puntuación final

El Pipeline combina dos valores:

```text
final_score =
(v19_score * 0.4) +
(ai_score * 0.6)
```

Distribución:

```text
40%  v19_score
60%  AI Score
```
El resultado final se convierte a entero antes de devolver el evento.

---

## 6. Resultado generado

El evento procesado contiene:

```text
v19_score
ai_score
final_score
```
El resultado se devuelve como un evento enriquecido para las siguientes etapas del procesamiento.

---

## 7. Diferencia con events.pipe

Este componente no corresponde al canal FIFO del sistema.

El archivo:

```text
events.pipe
```
es utilizado como mecanismo de comunicación entre Collector y AI Processor.

El Pipeline Connector es una capa interna de procesamiento de eventos JSON.

---

## 8. Integración dentro del sistema

```text
Evento JSON
      |
      v
Pipeline Connector
      |
      +---- AI Scoring
      |
      v
Final Score
```

