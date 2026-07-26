# WAF AI SOC v21.2 STABLE

# AI Processor

## 1. Introducción

El módulo AI Processor es el componente principal del motor de análisis inteligente de WAF AI SOC v21.2 STABLE.

Su función es recibir eventos generados por el pipeline de seguridad, analizar el comportamiento asociado a cada petición, enriquecer la puntuación inicial mediante diferentes motores de evaluación y generar una decisión de seguridad basada en el nivel de riesgo detectado.

El módulo actúa como capa de análisis entre la recopilación de eventos y las acciones SOC posteriores.

## 2. Objetivo del módulo

El objetivo principal de AI Processor es transformar eventos de seguridad básicos en eventos enriquecidos con contexto adicional.

Para ello combina:

- puntuación inicial generada por el sistema WAF,
- detección de patrones de ataque,
- historial de actividad de la dirección IP,
- repetición de comportamientos maliciosos,
- persistencia del atacante,
- contexto de la petición.

El resultado final es una evaluación de riesgo que determina la severidad del evento y la acción correspondiente.

## 3. Ubicación y dependencias

El módulo AI Processor se encuentra dentro del componente de inteligencia artificial del sistema WAF AI SOC v21.2 STABLE.

Ubicación:
/opt/waf-v21.2/ai/processor.py

El módulo depende de varios componentes internos necesarios para realizar el análisis y generar las decisiones de seguridad.

### Base de datos SOC

Utiliza la base de datos SQLite:
/opt/waf-v21.2/db/soc_v21.db

La base de datos es utilizada por el procesador AI para consultar y almacenar información relacionada con los eventos de seguridad.

Funciones principales:

- consulta del historial de ataques asociados a una dirección IP,
- cálculo de la reputación del atacante mediante actividad reciente e histórica,
- almacenamiento del resultado final del análisis AI.

Las consultas realizadas permiten al motor añadir contexto adicional al evento recibido antes de tomar una decisión de seguridad.

### Pipeline de eventos

El módulo recibe los eventos desde:
/opt/waf-v21.2/connectors/events.pipe

### Sistema de logs

El módulo genera registros operativos mediante:
/opt/waf-v21.2/logs/waf-ai-events.log


Este registro almacena los eventos SOC generados durante el análisis.

Cuando el motor determina una acción de bloqueo, genera adicionalmente registros en:
/opt/waf-v21.2/logs/waf-ai-ban.log

### Motor de scoring

El componente AI Processor utiliza el módulo de puntuación:

/opt/waf-v21.2/ai/scoring.py

Este módulo contiene la lógica relacionada con la evaluación de riesgo y cálculo de puntuación utilizada durante el análisis del evento.

Su función es separar la lógica de scoring del flujo principal del procesador, permitiendo mantener una arquitectura modular y facilitar futuras mejoras del motor de análisis.

## 4. Flujo de procesamiento

```text 
Evento WAF
      |
      v
events.pipe
      |
      v
AI Processor
      |
      v
Enriquecimiento SOC
      |
      v
Evaluación del riesgo
      |
      v
Clasificación
      |
      v
Acción final
```

El AI Processor ejecuta una cadena de análisis sobre cada evento recibido desde el pipeline de seguridad.

El proceso comienza con la recepción del evento generado por los componentes WAF y continúa con una serie de fases destinadas a obtener contexto adicional antes de tomar una decisión.

Las etapas principales del procesamiento son:

- recepción del evento de seguridad,
- validación de los datos recibidos,
- consulta de información histórica del atacante,
- enriquecimiento del evento con contexto SOC,
- evaluación del nivel de riesgo,
- clasificación de severidad,
- generación de la acción final.

Durante este proceso, el motor combina la información actual de la petición con datos históricos almacenados en la base de datos SOC para mejorar la precisión del análisis.

El resultado final es un evento enriquecido que permite al sistema determinar si debe registrar, alertar o ejecutar una acción defensiva.

## 5. Entrada de datos

El AI Processor recibe los eventos generados por el Collector mediante el canal interno:

/opt/waf-v21.2/connectors/events.pipe

Cada evento recibido representa una detección de seguridad previamente recopilada y reconstruida por el componente Collector.

El AI Processor no realiza lectura directa del Audit Log de ModSecurity. Su procesamiento comienza cuando el Collector entrega un evento válido al pipeline interno.

Los datos recibidos contienen la información necesaria para realizar el análisis:

- dirección IP origen,
- información del evento WAF,
- tipo de detección,
- datos asociados a la petición,
- información temporal del evento.

Flujo de entrada:

```text
Collector
      |
      v
events.pipe
      |
      v
AI Processor
```
## 6. Análisis y enriquecimiento del evento

El AI Processor realiza un proceso de enriquecimiento sobre cada evento recibido desde el pipeline de seguridad.

El objetivo de esta fase es añadir contexto adicional al evento original antes de realizar la evaluación de riesgo.

Durante esta etapa el motor ejecuta diferentes consultas y análisis internos:

- consulta del historial de actividad asociado a la dirección IP,
- cálculo de reputación del atacante,
- detección del patrón de ataque,
- análisis de repetición del comportamiento detectado.


### Reputación de IP

El procesador utiliza la función:

```python
get_ip_reputation(ip)
```
Esta función consulta la base de datos SOC:

/opt/waf-v21.2/db/soc_v21.db

para obtener información histórica asociada a la dirección IP analizada.

Los valores calculados son:

- eventos detectados en los últimos 10 minutos,
- eventos detectados en las últimas 24 horas,
- número total de eventos registrados para la dirección IP.

Estos datos permiten al motor determinar el nivel de actividad asociado al atacante.

La información obtenida se utiliza posteriormente por el sistema de reputación y por el motor de evaluación de riesgo.

### Detección de patrones

El procesador utiliza la función:

```python
detect_pattern(uri)
```
Esta función analiza la URI de la petición para identificar indicadores asociados a diferentes tipos de ataques.

Los patrones reconocidos actualmente son:

- XSS,
- SQL Injection,
- Scanner,
- Path Traversal,
- RCE,
- Sensitive File Scan.

El patrón detectado se incorpora al evento y se utiliza posteriormente durante la evaluación de riesgo.

### Repetición del patrón

El procesador utiliza la función:

```python
get_pattern_count(ip, pattern)
```
Esta función consulta la actividad histórica asociada a una dirección IP para determinar cuántas veces se ha detectado un patrón concreto.

La información obtenida permite al motor diferenciar entre:

- una detección aislada,
- actividad repetitiva,
- comportamiento persistente del atacante.

El resultado final de esta fase es un evento enriquecido con información adicional preparado para el sistema de puntuación de riesgo.

## 7. Sistema de puntuación de riesgo

El sistema de puntuación de riesgo es el mecanismo encargado de evaluar el nivel de peligrosidad asociado a cada evento analizado por el AI Processor.

La puntuación final se obtiene combinando diferentes factores de seguridad recopilados durante el procesamiento del evento.

Los principales elementos considerados son:

- puntuación inicial generada por el sistema WAF,
- tipo de ataque detectado,
- severidad del evento,
- comportamiento histórico de la dirección IP,
- número de eventos asociados al atacante,
- repetición de actividad maliciosa,
- contexto adicional obtenido desde la base de datos SOC.

El motor utiliza esta información para generar una valoración de riesgo que representa la probabilidad de que el evento corresponda a una actividad maliciosa.

La puntuación obtenida permite clasificar el evento y determinar la respuesta adecuada del sistema.

Los valores de riesgo sirven como base para las siguientes acciones:

- registro del evento,
- generación de alerta SOC,
- aplicación de medidas defensivas,
- bloqueo automático cuando el nivel de riesgo supera los límites establecidos.

Este proceso permite que el sistema no tome decisiones únicamente basadas en una petición individual, sino considerando también el comportamiento global asociado al atacante.

## 8. Clasificación de severidad

La clasificación de severidad es la fase encargada de transformar la puntuación de riesgo obtenida por el AI Processor en un nivel operativo comprensible para el sistema SOC.

El motor analiza el resultado de la evaluación de riesgo junto con el contexto del evento para determinar la importancia de la amenaza detectada.

Los niveles de severidad permiten establecer la prioridad del evento y definir la respuesta adecuada del sistema.

Los factores utilizados para la clasificación incluyen:

- puntuación de riesgo calculada,
- tipo de comportamiento detectado,
- impacto potencial del ataque,
- historial asociado a la dirección IP,
- repetición de actividad maliciosa,
- resultado del análisis contextual.

La clasificación permite diferenciar entre eventos informativos, sospechosos y amenazas críticas.

Los niveles de severidad se utilizan como referencia para las acciones posteriores del SOC:

- eventos de bajo riesgo: registro y seguimiento,
- eventos de riesgo medio: generación de alerta y monitorización,
- eventos de alto riesgo: aplicación de medidas defensivas,
- eventos críticos: posible bloqueo automático según la política definida.

Esta capa permite que el sistema mantenga una respuesta proporcional al nivel real de amenaza detectado, evitando decisiones basadas únicamente en un único indicador.

## Tipos de acciones

### LOG

Acción destinada al almacenamiento del evento para auditoría.

Características:

- evento relevante pero sin necesidad de intervención inmediata,
- requiere conservación de información para análisis posterior.

Acción:

- almacenar evento SOC,
- mantener trazabilidad histórica.

---

### MONITOR

Acción aplicada a eventos que requieren seguimiento sin necesidad de bloqueo inmediato.

Características:

- actividad sospechosa con riesgo moderado,
- requiere observación y correlación con eventos posteriores.

Acción:

- registrar el evento,
- mantener monitorización de la dirección IP,
- permitir que futuras detecciones incrementen la evaluación de riesgo.

---

### ALERT

Acción generada cuando existe una probabilidad significativa de actividad maliciosa.

Características:

- comportamiento sospechoso,
- patrones de ataque detectados,
- incremento de riesgo asociado.

Acción:

- registrar el evento de alta prioridad,
- generar una alerta para el sistema SOC,
- mantener seguimiento intensivo de la dirección IP,
- conservar la información para su posterior análisis y correlación.

---

### BLOCK

Acción aplicada cuando el análisis AI determina que la actividad representa una amenaza crítica para el sistema.

Características:

- riesgo crítico confirmado,
- alta probabilidad de ataque,
- requiere respuesta inmediata.

Acción:

- registrar el evento crítico,
- solicitar el bloqueo de la dirección IP,
- conservar la información para auditoría,
- finalizar el tratamiento del evento.

---

## Mapeo de riesgo y severidad

El AI Processor transforma la puntuación de riesgo obtenida durante el análisis en un nivel de severidad y en la acción operativa correspondiente.

Esta decisión permite que todos los componentes del WAF AI SOC trabajen utilizando una clasificación homogénea de los eventos de seguridad.

| Nivel de riesgo | Severidad | Acción |
|-----------------|-----------|--------|
| Bajo            | LOW       | LOG |
| Medio           | MEDIUM    | MONITOR |
| Alto            | HIGH      | ALERT |
| Crítico         | CRITICAL  | BLOCK |

---

## 9. Acciones automáticas del motor AI

Una vez calculada la puntuación de riesgo y determinada la severidad del evento, el AI Processor aplica automáticamente la acción correspondiente.

El proceso se realiza de forma completamente automática y no requiere intervención manual.

Según el nivel de riesgo obtenido, el sistema puede:

- registrar el evento para auditoría,
- mantener la dirección IP bajo observación,
- generar una alerta para el sistema SOC,
- solicitar el bloqueo automático del origen del ataque.

Cada decisión queda asociada al evento procesado y será utilizada por los componentes posteriores del WAF AI SOC para aplicar la respuesta correspondiente.

---

## 10. Flujo general del procesamiento AI

El funcionamiento del AI Processor puede resumirse como una secuencia continua de análisis y toma de decisiones sobre cada evento recibido desde el Collector.

Flujo general:

```text
Collector
      |
      v
events.pipe
      |
      v
AI Processor
      |
      v
Extracción de datos
      |
      v
Evaluación del riesgo
      |
      v
Clasificación de severidad
      |
      v
Selección de acción
      |
      v
SQLite
      |
      v
Dashboard / Fail2Ban
```

Cada evento es procesado de forma independiente, aplicando las reglas de evaluación y clasificación definidas por el motor AI antes de almacenarlo y ponerlo a disposición del resto de componentes del WAF AI SOC.

---


## Registro de decisiones

Todas las acciones generadas por el AI Processor quedan registradas para permitir:

- auditoría de decisiones automáticas,
- análisis histórico de amenazas,
- revisión del comportamiento del motor AI,
- mejora futura de las políticas de seguridad.

El resultado final del procesamiento contiene la información necesaria para que los componentes SOC posteriores puedan actuar sobre el evento.

## 11. Persistencia del resultado SOC

Después de completar el análisis del evento y determinar la acción correspondiente, el AI Processor almacena el resultado final dentro del sistema SOC.

La persistencia permite conservar la información generada durante el análisis para futuras consultas, auditorías y correlaciones de seguridad.

El resultado almacenado contiene tanto los datos originales del evento como la información añadida durante el proceso de análisis inteligente.

## Información persistida

Los registros SOC pueden incluir:

- fecha y hora del análisis,
- dirección IP origen,
- tipo de evento detectado,
- patrón de ataque identificado,
- puntuación de riesgo calculada,
- nivel de severidad asignado,
- acción decidida por el motor AI,
- información contextual obtenida durante el enriquecimiento.

## Base de datos SOC

El almacenamiento principal utiliza:
/opt/waf-v21.2/db/soc_v21.db


La base de datos permite mantener un historial de actividad asociado a los eventos procesados por el motor AI.

Este historial es utilizado para:

- consultas posteriores del comportamiento de una dirección IP,
- análisis de repetición de ataques,
- cálculo de reputación del atacante,
- generación de información para el SOC.

## Registro de eventos

Además de la persistencia en base de datos, el sistema mantiene registros operativos mediante:
/opt/waf-v21.2/logs/waf-ai-events.log


## Objetivo de la persistencia

La conservación de resultados permite que WAF AI SOC v21.2 STABLE no analice cada evento de forma aislada.

El sistema utiliza la información histórica acumulada para mejorar la evaluación futura, detectar comportamientos repetitivos y proporcionar una visión completa de la actividad del atacante.

## 12. Integración con Dashboard y Alertas

El resultado generado por el AI Processor es utilizado por los componentes SOC superiores para la visualización, monitorización y gestión de eventos de seguridad.

El objetivo de esta integración es proporcionar una representación clara del estado de las amenazas detectadas y permitir una respuesta rápida por parte del operador.

## Flujo de integración

El resultado del análisis AI sigue el siguiente flujo:

```text
AI Processor
      |
      v
Resultado SOC
      |
      v
Persistencia
      |
      +------> Dashboard
      |
      +------> SOC Response
```
---

## Resumen del AI Processor

El AI Processor constituye el núcleo del motor de análisis de WAF AI SOC v21.2 STABLE.

Su función consiste en analizar los eventos recibidos desde el Collector, enriquecerlos con contexto adicional y generar una decisión de seguridad basada en el nivel de riesgo detectado.

Funciones principales:

- Recepción de eventos desde `events.pipe`.
- Enriquecimiento del evento con información contextual.
- Evaluación de la puntuación de riesgo.
- Clasificación de la severidad del evento.
- Selección de la acción correspondiente.
- Registro de decisiones y persistencia del resultado.
- Generación de información para los componentes posteriores del WAF AI SOC.

Arquitectura del flujo:

```text
Collector
      |
      v
events.pipe
      |
      v
AI Processor
      |
      v
Evaluación del riesgo
      |
      v
Clasificación
      |
      v
Acción
      |
      v
SQLite
      |
      +------> Dashboard
      |
      +------> Fail2Ban
```

El AI Processor permite que WAF AI SOC v21.2 STABLE tome decisiones de seguridad de forma automática, uniforme y basada en el contexto de cada evento, proporcionando una respuesta proporcional al nivel de riesgo detectado.

---
