# WAF AI SOC v21.2 STABLE

# UFW

## Introducción

UFW (Uncomplicated Firewall) es el componente encargado de gestionar las reglas de filtrado de red utilizadas por WAF AI SOC v21.2 STABLE.

Su función consiste en controlar el tráfico de red permitido o bloqueado de acuerdo con la configuración definida por la plataforma y las acciones aplicadas por los mecanismos de seguridad.

## Objetivo

El objetivo de UFW es proporcionar una capa adicional de protección mediante el control del acceso a los servicios disponibles en el sistema.

Su integración complementa las funciones de detección y respuesta implementadas por el resto de componentes de la plataforma.

## Función dentro del sistema

UFW aplica las reglas de filtrado que determinan qué conexiones pueden acceder a los servicios protegidos.

Estas reglas pueden mantenerse de forma permanente o actualizarse como resultado de las acciones ejecutadas por los mecanismos de respuesta del sistema.

## Flujo de actuación

El funcionamiento general de UFW sigue el siguiente esquema:

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
       UFW
        │
        ▼
Control del tráfico
```

## Integración con Fail2Ban

UFW actúa como mecanismo de aplicación de las acciones de protección solicitadas por Fail2Ban.

Esta integración permite automatizar la restricción del acceso cuando se cumplen las condiciones definidas por la plataforma.

## Gestión de reglas

UFW administra las reglas de filtrado utilizadas para controlar el tráfico de red del sistema.

La configuración de estas reglas permite definir el comportamiento del firewall de acuerdo con las necesidades de la plataforma.

## Protección de servicios

El filtrado realizado por UFW contribuye a proteger los servicios expuestos por WAF AI SOC v21.2 STABLE frente a accesos no autorizados.

Esta protección complementa las funciones desempeñadas por Nginx, ModSecurity y Fail2Ban.

## Trazabilidad

Las acciones aplicadas mediante UFW forman parte del mecanismo de respuesta de la plataforma y permiten realizar el seguimiento de las medidas de protección implementadas.

## Logs

La actividad relacionada con UFW puede generar registros destinados a la monitorización, el diagnóstico y la verificación del correcto funcionamiento del sistema de filtrado de red.
