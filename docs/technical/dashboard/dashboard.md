# WAF AI SOC v21.2 STABLE - Dashboard

## 1. Descripción

El Dashboard es la interfaz web de visualización del sistema WAF AI SOC v21.2 STABLE.

Su función es mostrar el estado operativo del SOC, estadísticas de ataques, eventos procesados por el motor AI y estado de los componentes de defensa.

El Dashboard obtiene la información mediante la API Flask del sistema.

---

## 2. Ubicación

Directorio principal:

```text
/opt/waf-v21.2/dashboard
```
---

## 3. Servidor del Dashboard

El Dashboard es servido mediante la API Flask:

Código asociado:

```bash 
/opt/waf-v21.2/api/server.py
```

Configuración:

```python
static_folder="/opt/waf-v21.2/dashboard"
```
Servicio systemd asociado:

```ini
waf-ai-soc-v21.2.service
```
---

## 4. Funcionamiento general

El Dashboard no procesa directamente eventos de seguridad.

Su función es consumir datos proporcionados por la API.

Flujo:

```text

Usuario
   |
   v
Nginx HTTPS
   |
   v
Flask API :5051
   |
   v
Dashboard
   |
   v
API Endpoints
   |
   v
SQLite Database
```
---

## 5. Comunicación con la API

El JavaScript del Dashboard consulta los endpoints internos de la API.

Endpoints utilizados:

```text
/api/dashboard
/api/stats
/api/top
/api/live
/api/system
/api/blocked
```
---

## 6. Información mostrada

El Dashboard muestra los siguientes módulos:

### Estadísticas principales

- Total de ataques.
- IPs únicas detectadas.
- Mayor puntuación AI.
- Puntuación media.

### System Health

Estado de los servicios:

- API
- Collector
- Processor
- Nginx
- Fail2Ban

Información del sistema:

- CPU
- RAM
- DISK
- Uptime

### Defense Stack

Estado de los componentes de defensa:

- ModSecurity
- OWASP CRS
- SQLite
- UFW

### Eventos en tiempo real

El Dashboard muestra los últimos eventos almacenados en la base de datos.

Datos mostrados:

- IP
- URI
- Final Score
- Timestamp

### IP bloqueadas

El Dashboard consulta las últimas acciones:

```text
ACTION=BLOCK
```
---

## 7. Integración dentro del sistema

El Dashboard representa la última capa de visualización:

```text
ModSecurity
      |
      v
Collector
      |
      v
AI Processor
      |
      v
SQLite Database
      |
      v
API Flask
      |
      v
Dashboard
```
---

## 8. Estado operativo

El Dashboard forma parte del servicio:

waf-ai-soc-v21.2.service

Su disponibilidad depende de:

API activa

Base de datos disponible

Nginx operativo


