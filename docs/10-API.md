# WAF AI SOC v21.2 STABLE

# API REST

## Introducción

La API REST es el componente encargado de proporcionar acceso controlado a la información generada por WAF AI SOC v21.2 STABLE.

Su función consiste en facilitar la consulta de los datos almacenados por la plataforma y servir como interfaz de comunicación entre la base de datos y los componentes que requieren acceder a dicha información.

## Objetivo

El objetivo de la API REST es ofrecer un mecanismo uniforme para la consulta de la información del sistema, manteniendo desacopladas las tareas de almacenamiento y presentación de los datos.

Esta arquitectura facilita la integración entre los distintos componentes de la plataforma.

## Función dentro del sistema

La API REST recibe las solicitudes de los componentes autorizados, obtiene la información correspondiente desde la base de datos y devuelve los resultados para su utilización.

Su funcionamiento permite centralizar el acceso a los datos gestionados por WAF AI SOC v21.2 STABLE.

## Flujo de información

El flujo general de acceso a la información sigue el siguiente esquema:

```text
SQLite
    │
    ▼
 API REST
    │
    ▼
Dashboard Web
```

## Consulta de datos

La API REST permite acceder a la información almacenada por la plataforma de forma organizada y controlada.

Las consultas realizadas proporcionan los datos necesarios para la monitorización y visualización del estado del sistema.

## Integración con la Base de Datos

La API REST actúa como interfaz de acceso a la base de datos utilizada por WAF AI SOC v21.2 STABLE.

Esta separación facilita la administración de la información y reduce el acoplamiento entre los distintos componentes.

## Integración con el Dashboard

El Dashboard Web utiliza la API REST para obtener la información necesaria para representar el estado de la plataforma y los eventos registrados.

La utilización de esta interfaz permite mantener una arquitectura modular y organizada.

## Seguridad

El acceso a la información mediante la API REST se realiza dentro de la arquitectura definida por la plataforma.

Su diseño contribuye a mantener una separación clara entre los componentes encargados del almacenamiento y aquellos destinados a la presentación de la información.

## Trazabilidad

La API REST participa en el recorrido de la información desde el almacenamiento hasta su visualización, facilitando el seguimiento del flujo de datos dentro de la plataforma.

## Logs

La actividad relacionada con la API REST puede generar registros destinados a la monitorización, el diagnóstico y la verificación del correcto funcionamiento del sistema.
