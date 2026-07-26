# WAF AI SOC v21.2 STABLE

# Fail2Ban

## Introducción

Fail2Ban es el componente encargado de aplicar medidas automáticas de protección cuando se detectan eventos de seguridad que cumplen las condiciones definidas por la plataforma.

Su integración permite reducir la exposición frente a actividades potencialmente maliciosas mediante acciones de bloqueo sobre las direcciones IP identificadas.

## Objetivo

El objetivo de Fail2Ban es complementar la protección proporcionada por WAF AI SOC v21.2 STABLE mediante la aplicación automática de respuestas frente a eventos de seguridad.

Esta integración contribuye a reforzar la defensa del sistema y limitar la repetición de comportamientos considerados no autorizados.

## Función dentro del sistema

Fail2Ban recibe la información necesaria para determinar cuándo debe aplicarse una acción de protección.

Cuando se cumplen las condiciones establecidas por la plataforma, ejecuta las acciones correspondientes para limitar el acceso desde los orígenes afectados.

## Flujo de actuación

El funcionamiento general de Fail2Ban sigue el siguiente esquema:

```text
Evento de seguridad
        │
        ▼
 AI Engine
        │
        ▼
   Fail2Ban
        │
        ▼
 Aplicación del bloqueo
        │
        ▼
      UFW
```

## Integración con el AI Engine

Fail2Ban forma parte del mecanismo de respuesta de WAF AI SOC v21.2 STABLE.

Su actuación se produce como resultado del análisis realizado por el AI Engine y de los criterios definidos por la plataforma.

## Integración con UFW

Fail2Ban utiliza UFW como mecanismo para aplicar las acciones de bloqueo sobre las direcciones IP cuando corresponde.

Esta integración permite mantener separadas las tareas de análisis y las acciones de protección.

## Gestión de bloqueos

Las acciones ejecutadas por Fail2Ban se realizan de acuerdo con la configuración definida para la plataforma.

La gestión de los bloqueos permite responder de forma automática ante determinados eventos de seguridad.

## Trazabilidad

La actividad de Fail2Ban forma parte del flujo de respuesta del sistema, permitiendo realizar el seguimiento de las acciones de protección aplicadas.

## Logs

Fail2Ban puede generar registros de actividad destinados a la monitorización, el diagnóstico y la verificación del correcto funcionamiento del sistema de respuesta automática.
