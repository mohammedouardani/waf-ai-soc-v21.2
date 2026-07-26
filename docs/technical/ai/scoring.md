# WAF AI SOC v21.2 STABLE

# AI Scoring Engine

## 1. Introducción

El módulo AI Scoring Engine es el componente encargado de calcular la puntuación de riesgo asociada a un evento de seguridad.

Su función consiste en analizar la información recibida por el AI Processor y generar una puntuación que represente el nivel de riesgo detectado.

La puntuación calculada será utilizada posteriormente por el AI Processor para determinar la severidad del evento y la acción correspondiente.

## 2. Objetivo del módulo

El objetivo principal del módulo es incrementar la puntuación inicial del evento mediante la detección de indicadores asociados a diferentes tipos de ataques.

Para ello analiza principalmente la URI de la petición y aplica incrementos de puntuación cuando identifica patrones considerados de riesgo.

El resultado final es una puntuación normalizada que será utilizada durante la evaluación del evento.

## 3. Ubicación

El módulo se encuentra en:

```text
/opt/waf-v21.2/ai/scoring.py
```

El AI Scoring Engine es utilizado por el AI Processor durante la fase de evaluación del riesgo.

## 4. Función principal

El módulo implementa la función:

```python
ai_score(event)
```

Esta función recibe un evento de seguridad y calcula una puntuación de riesgo a partir de la información disponible.

El proceso comienza utilizando la puntuación inicial proporcionada por el sistema WAF.

Posteriormente analiza la URI de la petición para identificar indicadores asociados a diferentes tipos de ataques.

Cada coincidencia detectada incrementa la puntuación del evento según los criterios definidos por el motor de scoring.

## 5. Indicadores evaluados

Durante el cálculo de la puntuación, el motor analiza la URI en busca de diferentes indicadores de riesgo.

Los grupos de indicadores actualmente utilizados son:

- RCE / WebShell.
- Cross-Site Scripting (XSS).
- SQL Injection.
- Reconocimiento de CMS.
- Acceso a ficheros sensibles.
- Riesgo asociado a subida de archivos.

Cada categoría añade una puntuación adicional al evento cuando se detectan coincidencias.

## 6. Criterios de puntuación

El motor incrementa la puntuación inicial del evento cuando detecta determinados indicadores dentro de la URI analizada.

Los incrementos definidos actualmente son:

| Indicador | Incremento |
|-----------|-----------:|
| RCE / WebShell | +40 |
| Cross-Site Scripting (XSS) | +35 |
| SQL Injection | +35 |
| Reconocimiento de CMS | +20 |
| Acceso a ficheros sensibles | +25 |
| Riesgo asociado a subida de archivos | +15 |

Los incrementos se acumulan sobre la puntuación inicial del evento antes de aplicar el límite máximo definido por el motor.

## 7. Límite de puntuación

Una vez finalizado el cálculo, la puntuación obtenida queda limitada a un valor máximo de 100.

Este límite permite mantener una escala homogénea para la evaluación de riesgo realizada por el AI Processor.

## 8. Integración con AI Processor

El AI Scoring Engine no toma decisiones de seguridad de forma independiente.

La puntuación calculada es utilizada por el AI Processor como parte del proceso de evaluación del riesgo.

A partir de este resultado, el AI Processor determina la severidad del evento y la acción correspondiente dentro del sistema WAF AI SOC.

## 9. Flujo de funcionamiento

```text
Evento
      |
      v
Puntuación inicial
      |
      v
AI Scoring Engine
      |
      v
Análisis de la URI
      |
      v
Aplicación de incrementos
      |
      v
Puntuación final
      |
      v
AI Processor
```

## Resumen

El AI Scoring Engine es el módulo encargado de calcular la puntuación de riesgo de cada evento analizado.

Para ello utiliza la puntuación inicial del sistema WAF y la incrementa cuando detecta indicadores asociados a distintos tipos de ataques.

La puntuación resultante es utilizada por el AI Processor para evaluar el nivel de riesgo y determinar la respuesta correspondiente dentro de WAF AI SOC v21.2 STABLE.

---
