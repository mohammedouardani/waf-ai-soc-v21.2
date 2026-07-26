# API Server

---

## Descripción

El componente **API Server** constituye el punto central de acceso a la información generada por WAF AI SOC v21.2 STABLE. Su función es exponer una API REST para el Dashboard Web y proporcionar información sobre el estado del sistema, las estadísticas de seguridad y los eventos almacenados en la base de datos.

Además de ofrecer los servicios REST, este componente sirve directamente los archivos estáticos del Dashboard, actuando como servidor web para la interfaz gráfica de la aplicación.

El API Server no realiza tareas de análisis de amenazas ni procesamiento de eventos. Su responsabilidad se limita a consultar información ya procesada por otros componentes del sistema y presentarla mediante respuestas JSON o contenido web estático.

---

## Ubicación

```
/opt/waf-v21.2/api/server.py
```

---

## Funciones principales

El servidor API desarrolla las siguientes funciones:

- Exponer la API REST utilizada por el Dashboard.
- Consultar la base de datos SQLite.
- Obtener estadísticas de los ataques registrados.
- Consultar el estado de los servicios del sistema.
- Mostrar información de salud del sistema.
- Publicar las últimas direcciones IP bloqueadas.
- Servir la interfaz web del Dashboard.
- Entregar archivos estáticos (HTML, CSS y JavaScript).

---

## Dependencias

El componente utiliza las siguientes bibliotecas:

| Biblioteca | Función |
|------------|---------|
| Flask | Servidor web y API REST |
| sqlite3 | Acceso a la base de datos SQLite |
| psutil | Información del sistema |
| subprocess | Consulta del estado de servicios mediante systemctl |
| time | Cálculo del tiempo de actividad |

No utiliza ORM, SQLAlchemy ni sistemas de almacenamiento externos.

---

## Configuración

Durante la inicialización se configura Flask con los siguientes parámetros:

- Directorio del Dashboard:

```
/opt/waf-v21.2/dashboard
```

- Base de datos:

```
/opt/waf-v21.2/db/soc_v21.db
```

Estas rutas se encuentran definidas directamente dentro del código fuente.

---

## Arquitectura del componente

```
                API Server (Flask)
                       │
      ┌────────────────┼────────────────┐
      │                │                │
      ▼                ▼                ▼
  SQLite          Sistema Linux     Dashboard
  soc_v21.db      psutil/systemctl  HTML/CSS/JS
```

El servidor centraliza la presentación de la información, mientras que el procesamiento de eventos y el análisis de inteligencia artificial se realizan en componentes independientes.

---
## Acceso a la base de datos SQLite

El acceso a la información almacenada en la base de datos se realiza mediante una función auxiliar denominada `query()`.

Su funcionamiento es el siguiente:

1. Abre una conexión con la base de datos SQLite.
2. Crea un cursor de ejecución.
3. Ejecuta la consulta SQL recibida.
4. Recupera todos los registros mediante `fetchall()`.
5. Cierra la conexión.
6. Devuelve los resultados al componente solicitante.

Este diseño mantiene el código sencillo y evita mantener conexiones abiertas de forma permanente. Cada consulta utiliza una conexión independiente a la base de datos.

---

## Consulta del estado de servicios

El servidor implementa una función denominada `service_status()` cuya finalidad es consultar el estado operativo de distintos servicios del sistema.

Para ello ejecuta internamente el comando:

```bash
systemctl is-active <servicio>
```

El resultado obtenido se devuelve posteriormente al endpoint `/api/system`.

Los servicios consultados son:

- waf-ai-soc-v21.2
- waf-ai-soc-v21.2-collector
- waf-ai-soc-v21.2-processor
- nginx
- fail2ban

En caso de producirse un error durante la ejecución del comando, la función devuelve el estado:

```
unknown
```

---

## Endpoints implementados

El servidor implementa varios endpoints REST destinados a suministrar información al Dashboard Web y a otras herramientas de administración.

Todos los endpoints responden en formato JSON, excepto aquellos destinados a servir la interfaz web y los archivos estáticos.

### Endpoints disponibles

| Endpoint | Descripción |
|----------|-------------|
| `/api/stats` | Estadísticas generales |
| `/api/top` | Top de direcciones IP |
| `/api/live` | Últimos eventos registrados |
| `/api/dashboard` | Información agregada para el Dashboard |
| `/api/system` | Estado del sistema |
| `/api/blocked` | Últimas direcciones IP bloqueadas |
| `/` | Dashboard Web |
| `/<path:path>` | Archivos estáticos |

## Endpoint `/api/stats`

Este endpoint proporciona un resumen estadístico de los ataques almacenados en la base de datos.

La información se obtiene directamente de la tabla `attacks` mediante consultas SQL independientes.

### Información devuelta

- Número total de ataques registrados.
- Número de direcciones IP únicas.
- Puntuación máxima (`final_score`) registrada.
- Puntuación media (`final_score`) de todos los ataques.

La respuesta se devuelve en formato JSON para su consumo por el Dashboard.

---

## Endpoint `/api/top`

Este endpoint devuelve las cinco direcciones IP con mayor puntuación registrada.

Para ello agrupa los registros por dirección IP, obtiene el valor máximo de `final_score` para cada una de ellas y ordena los resultados de mayor a menor puntuación.

El resultado se limita a las cinco primeras posiciones.

Su finalidad es identificar rápidamente las direcciones IP asociadas a los ataques con mayor impacto.

---

## Endpoint `/api/live`

Este endpoint proporciona los veinte eventos más recientes registrados en la base de datos.

Para cada evento devuelve los siguientes campos:

- Dirección IP.
- URI solicitada.
- Puntuación final (`final_score`).
- Marca temporal (`ts`).

La información es utilizada por el Dashboard para mostrar la actividad reciente del sistema.

---

## Endpoint `/api/dashboard`

Este endpoint reúne en una única respuesta la información principal necesaria para el funcionamiento del Dashboard.

Entre los datos incluidos se encuentran:

- Estado general del sistema.
- Número total de ataques.
- Número de direcciones IP únicas.
- Puntuación máxima registrada.
- Puntuación media.
- Top de direcciones IP.
- Últimos eventos registrados.

Este diseño reduce el número de peticiones HTTP necesarias para actualizar la interfaz web, mejorando la eficiencia de la comunicación entre el Dashboard y la API.

## Endpoint `/api/system`

Este endpoint proporciona información sobre el estado operativo del sistema y de los principales servicios utilizados por WAF AI SOC v21.2 STABLE.

La información se obtiene en tiempo real mediante la biblioteca `psutil` y consultas al gestor de servicios `systemd`.

### Información del sistema

El endpoint devuelve las siguientes métricas:

- Uso de CPU.
- Uso de memoria RAM.
- Uso del sistema de archivos.
- Tiempo de actividad del servidor (`uptime`).

### Estado de los servicios

El servidor consulta el estado de los siguientes servicios mediante `systemctl is-active`:

- API Server.
- Collector.
- Processor.
- Nginx.
- Fail2Ban.

El resultado permite al Dashboard mostrar el estado operativo de cada servicio.

### Estado de la pila defensiva

Además de los servicios, el endpoint devuelve un bloque informativo con los principales componentes de la defensa:

- ModSecurity.
- OWASP Core Rule Set (CRS).
- SQLite.
- UFW.

Esta información se utiliza para representar el estado general de la plataforma de protección.

---

## Endpoint `/api/blocked`

Este endpoint muestra las direcciones IP bloqueadas más recientemente por el sistema.

La información no se obtiene desde la base de datos SQLite.

El servidor analiza directamente el archivo de registro:

```
/opt/waf-v21.2/logs/waf-ai-ban.log
```

Durante el procesamiento del fichero:

- Se revisan las últimas líneas del registro.
- Se seleccionan únicamente los eventos con `ACTION=BLOCK`.
- Se extraen los campos IP, SCORE, SEVERITY y URI.
- Se eliminan direcciones IP duplicadas.
- Se devuelven las tres IP bloqueadas más recientes.

Este endpoint permite al Dashboard mostrar las acciones de bloqueo aplicadas por el sistema en tiempo real.

---

## Dashboard Web

El servidor API también actúa como servidor web para la interfaz gráfica de WAF AI SOC v21.2 STABLE.

La ruta raíz:

```
/
```

entrega el archivo:

```
index.html
```

ubicado en:

```
/opt/waf-v21.2/dashboard/
```
De esta forma, el mismo proceso Flask proporciona tanto la API REST como la interfaz web del Dashboard.

---

## Archivos estáticos

El endpoint:

```
/<path:path>
```

permite servir automáticamente los recursos estáticos del Dashboard.

Entre los archivos publicados se encuentran:

- HTML
- CSS
- JavaScript
- Imágenes
- Otros recursos necesarios para la interfaz web

La función utiliza `send_from_directory()` para localizar y entregar los archivos solicitados desde el directorio configurado como `static_folder`.

---

## Ejecución del servidor

Cuando el fichero `server.py` se ejecuta como programa principal, Flask inicia el servidor con la siguiente configuración:

| Parámetro | Valor |
|-----------|-------|
| Host | `0.0.0.0` |
| Puerto | `5051` |
| Debug | `False` |

La escucha en `0.0.0.0` permite aceptar conexiones desde cualquier interfaz de red disponible en el servidor.

---

## Resumen técnico

El componente **API Server** constituye la capa de presentación de WAF AI SOC v21.2 STABLE.

Sus responsabilidades se limitan a exponer información ya existente mediante una API REST y servir la interfaz web del Dashboard. No implementa lógica de inteligencia artificial, correlación de eventos ni procesamiento de ataques, funciones que recaen sobre otros componentes del sistema.

Su diseño es ligero y modular, basado en Flask y SQLite, proporcionando una interfaz sencilla para consultar estadísticas, eventos, estado del sistema y acciones de bloqueo, además de publicar los recursos estáticos necesarios para el funcionamiento del Dashboard.

