# WAF AI SOC v21.2 STABLE

# Estructura del Proyecto

## Introducción

WAF AI SOC v21.2 STABLE organiza sus componentes mediante una estructura de directorios diseñada para facilitar el desarrollo, la administración y el mantenimiento de la plataforma.

Cada componente dispone de una ubicación específica que agrupa los archivos relacionados con una misma función, manteniendo una separación clara entre configuración, procesamiento, almacenamiento, interfaz y documentación.

La organización del proyecto permite localizar fácilmente cada elemento del sistema y simplifica las tareas de actualización, copia de seguridad y resolución de incidencias.

---

## Organización general

La estructura del proyecto agrupa los diferentes componentes de WAF AI SOC v21.2 STABLE en directorios independientes según su función dentro del sistema.

Esta organización facilita la separación de responsabilidades entre los distintos módulos, mejora la mantenibilidad del proyecto y simplifica las tareas de administración, desarrollo y evolución de la plataforma.

Cada directorio contiene los recursos necesarios para un componente específico, manteniendo una estructura coherente y fácilmente identificable.

---

## Directorio raíz

El directorio raíz del proyecto contiene la estructura principal de WAF AI SOC v21.2 STABLE.

Desde esta ubicación se organizan los diferentes componentes que forman la plataforma, agrupando la configuración, el procesamiento de eventos, los servicios de inteligencia artificial, la interfaz web, la base de datos, las copias de seguridad, los registros y la documentación.

Esta organización proporciona un punto central de trabajo y facilita la administración y el mantenimiento del sistema.

---

## Directorio ai/

El directorio `ai/` contiene los componentes responsables del análisis y procesamiento inteligente de los eventos de seguridad.

En esta ubicación se encuentran los módulos encargados de clasificar los eventos recibidos, aplicar el análisis correspondiente y generar la información utilizada por el resto de la plataforma.

Su contenido constituye el núcleo del motor de inteligencia artificial de WAF AI SOC v21.2 STABLE.

---

## Directorio api/

El directorio `api/` contiene los componentes que implementan la interfaz de programación de aplicaciones (API) de WAF AI SOC v21.2 STABLE.

Su función es proporcionar acceso controlado a la información generada por el sistema, permitiendo la consulta de datos por parte del Dashboard Web y de otros componentes autorizados.

La organización de este directorio facilita el mantenimiento y la evolución de los servicios expuestos por la plataforma.

---

## Directorio backup/

El directorio `backup/` almacena las copias de seguridad generadas por WAF AI SOC v21.2 STABLE.

Su contenido permite conservar la información necesaria para la recuperación del sistema, incluyendo los archivos y datos definidos por la política de copias de seguridad del proyecto.

La organización de este directorio facilita la gestión y restauración de la información cuando resulta necesario.

---

## Directorio config/

El directorio `config/` contiene los archivos de configuración utilizados por los distintos componentes de WAF AI SOC v21.2 STABLE.

En esta ubicación se almacenan los parámetros necesarios para el funcionamiento de la plataforma, permitiendo centralizar la configuración y facilitar su administración y mantenimiento.

La separación de la configuración respecto al resto de componentes contribuye a mejorar la organización y la gestión del sistema.

---

## Directorio connectors/

El directorio `connectors/` contiene los componentes responsables de recopilar y transferir los eventos generados por las distintas fuentes de información hacia el flujo de procesamiento del sistema.

Su función es facilitar la integración entre los diferentes orígenes de datos y el resto de la plataforma, garantizando un tratamiento uniforme de los eventos recibidos.

La organización de este directorio permite mantener separados los mecanismos de adquisición de información del resto de componentes de WAF AI SOC v21.2 STABLE.

---

## Directorio dashboard/

El directorio `dashboard/` contiene la interfaz web de WAF AI SOC v21.2 STABLE.

En esta ubicación se encuentran los recursos necesarios para la visualización de la información generada por el sistema, permitiendo consultar el estado de la plataforma y los eventos registrados mediante una interfaz centralizada.

La organización de este directorio facilita el mantenimiento y la evolución de la interfaz de usuario de la plataforma.

---

## Directorio db/

El directorio `db/` contiene la base de datos utilizada por WAF AI SOC v21.2 STABLE para almacenar la información generada por el sistema.

En esta ubicación se conservan los datos necesarios para el registro, consulta y análisis de los eventos procesados por la plataforma.

La organización de este directorio facilita la gestión del almacenamiento y contribuye a mantener la información estructurada y accesible para los distintos componentes del sistema.

---

## Directorio docs/

El directorio `docs/` reúne la documentación técnica de WAF AI SOC v21.2 STABLE.

En esta ubicación se organizan los documentos que describen la arquitectura, los componentes, la instalación, la configuración, la administración y el mantenimiento de la plataforma.

Su estructura facilita la consulta de la información técnica y proporciona una referencia centralizada para el desarrollo, la operación y la evolución del sistema.

---

## Directorio logs/

El directorio `logs/` almacena los registros generados por los distintos componentes de WAF AI SOC v21.2 STABLE.

En esta ubicación se conserva la información necesaria para la monitorización del sistema, la auditoría de eventos y el análisis de incidencias de seguridad.

La organización de este directorio facilita el seguimiento de la actividad de la plataforma y el diagnóstico de su funcionamiento.

---

## Directorio archive/

El directorio `archive/` almacena la información archivada generada por WAF AI SOC v21.2 STABLE.

Su contenido permite conservar datos y recursos que ya no forman parte de la operación diaria del sistema, facilitando su consulta cuando resulta necesario.

La organización de este directorio contribuye a mantener la información histórica de forma ordenada y separada de los componentes activos de la plataforma.

---

## Directorio core/

El directorio `core/` contiene los componentes centrales de WAF AI SOC v21.2 STABLE.

En esta ubicación se agrupan los módulos que proporcionan funcionalidades compartidas y servicios utilizados por los distintos componentes de la plataforma.

La organización de este directorio favorece la reutilización de código y contribuye a mantener una arquitectura modular y coherente.

---

## Directorio models/

El directorio `models/` contiene los modelos utilizados por WAF AI SOC v21.2 STABLE para las tareas de análisis y procesamiento de información.

En esta ubicación se almacenan los recursos necesarios para el funcionamiento de los componentes que requieren modelos específicos dentro de la plataforma.

La organización de este directorio facilita la gestión, actualización y mantenimiento de los modelos empleados por el sistema.

---

## Directorio reports/

El directorio `reports/` contiene los informes generados por WAF AI SOC v21.2 STABLE.

En esta ubicación se almacenan los documentos y resultados producidos por la plataforma para facilitar el análisis, la revisión y el seguimiento de la información generada por el sistema.

La organización de este directorio permite mantener los informes centralizados y disponibles para tareas de auditoría, administración y mantenimiento.

---

## Directorio venv/

El directorio `venv/` contiene el entorno virtual de Python utilizado por WAF AI SOC v21.2 STABLE.

En esta ubicación se almacenan el intérprete, las bibliotecas y las dependencias necesarias para la ejecución de los componentes desarrollados en Python, manteniendo el entorno de la plataforma aislado del sistema operativo.

La utilización de un entorno virtual facilita la gestión de dependencias y contribuye a garantizar la estabilidad y reproducibilidad del proyecto.

---

## Organización del proyecto

La estructura de WAF AI SOC v21.2 STABLE ha sido diseñada para mantener una separación clara entre los distintos componentes de la plataforma.

La organización de los directorios facilita el desarrollo, la administración, el mantenimiento y la evolución del sistema, permitiendo localizar de forma sencilla los recursos asociados a cada funcionalidad.

Esta estructura constituye la base sobre la que se organizan los diferentes componentes documentados en los capítulos posteriores.
