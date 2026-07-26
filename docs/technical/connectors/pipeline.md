# WAF AI SOC v21.2 STABLE - Pipeline Connector

## 1. Descripción

El script `pipeline.py` es el componente encargado de procesar eventos dentro del pipeline interno del sistema WAF AI SOC v21.2 STABLE.

Su función es combinar la puntuación generada por el sistema V19 con la evaluación realizada por el motor AI para obtener una puntuación final de riesgo.

---

## 2. Ubicación

Código fuente:

```text
/opt/waf-v21.2/connectors/pipeline.py
```

Dependencia utilizada:
```text
/opt/waf-v21.2/ai/scoring.py
```
---

## 3. Funcionamiento general

El Pipeline recibe un evento en formato JSON, ejecuta la evaluación AI y genera una puntuación final.

Flujo:

```text

Evento JSON
      |
      v
pipeline.py
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

Conversión de la línea JSON recibida a un objeto evento.

Evaluación mediante:

`ai_score(event)`

Inserción del resultado:

`event["ai_score"]`

---

## 5. Cálculo de puntuación final

El Pipeline calcula:

final_score = (v19_score * 0.4) + (ai_score * 0.6)

La puntuación final combina:

40%  Sistema V19

60%  Motor AI

---

## 6. Resultado generado

El evento procesado contiene:

v19_score
ai_score
final_score

y es devuelto como evento enriquecido para las siguientes etapas del sistema.

---

## 7. Integración dentro del sistema

El Pipeline actúa como capa de combinación entre el análisis tradicional y el motor AI:

```text
V19 Score
     |
     v
Pipeline Connector
     |
     +------ AI Scoring
     |
     v
Final Score
```

