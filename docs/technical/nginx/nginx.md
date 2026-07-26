# WAF AI SOC v21.2 STABLE - Nginx Web Server

## 1. Descripción

Nginx es el componente encargado de recibir las conexiones HTTP/HTTPS externas y actuar como punto de entrada del sistema WAF AI SOC v21.2 STABLE.

Su función es gestionar el tráfico web, aplicar la configuración de seguridad, comunicarse con ModSecurity y servir como proxy inverso hacia la API del Dashboard.

---

## 2. Ubicación

Servicio:

```text
nginx.service
```
Configuración principal:

```text
/etc/nginx/nginx.conf
```

Configuraciones adicionales:

```text
/etc/nginx/sites-enabled/
```

Servidor web protegido:

```text
HTTPS :443
``` 

---

## 3. Funcionamiento general

Nginx recibe las peticiones del usuario y las dirige hacia las capas internas del sistema.

Flujo:

```text
Cliente
   |
   v
Nginx HTTPS
   |
   v
ModSecurity
   |
   v
Aplicación protegida
```
Para el Dashboard:

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
```

---

## 4. Integración con ModSecurity

Nginx utiliza el módulo:

ModSecurity-nginx v1.0.3

La protección WAF se encuentra activa mediante:

SecRuleEngine On

El tráfico HTTP procesado por Nginx es analizado por ModSecurity antes de llegar a la aplicación.

---

## 5. Proxy inverso API Dashboard

Nginx publica la API del sistema mediante proxy inverso.

Destino interno:

```text
http://127.0.0.1:5051
```
Servicio asociado:

```text
waf-ai-soc-v21.2.service
```

La API Flask escucha internamente en el puerto 5051 y Nginx actúa como intermediario entre el usuario y el servicio interno.

Flujo:
```text
HTTPS :443
      |
      v
Nginx
      |
      v
Proxy inverso
      |
      v
Flask API :5051
      |
      v
Dashboard
```

El acceso directo al puerto interno de la API no forma parte de la exposición pública del sistema.

---

## 6. Seguridad HTTPS

El sistema utiliza HTTPS mediante certificado válido.

Configuración:

Puerto HTTPS:
443

El acceso HTTP es redirigido hacia HTTPS:

```text
HTTP
 |
 v
301 Redirect
 |
 v
HTTPS
```
---

## 7. Restricciones de acceso

Nginx aplica restricciones adicionales:

- Bloqueo de acceso directo por IP HTTPS.
- Separación entre tráfico público y servicios internos.
- Proxy controlado hacia la API.

---

## 8. Integración dentro del sistema

Nginx representa la primera capa del WAF AI SOC:

```text
Internet
    |
    v
Nginx
    |
    v
ModSecurity + OWASP CRS
    |
    v
Collector
    |
    v
AI Processor
    |
    v
SQLite
    |
    v
API
    |
    v
Dashboard
```

---

## 9. Estado operativo

La disponibilidad de Nginx es necesaria para:

- Recepción del tráfico HTTPS.
- Funcionamiento del WAF.
- Acceso al Dashboard.
- Comunicación con la API.

Estado comprobado mediante:

```bash
systemctl status nginx
```


