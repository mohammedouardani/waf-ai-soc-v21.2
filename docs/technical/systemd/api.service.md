# WAF AI SOC v21.2 STABLE - API Dashboard Service

## 1. Descripción

El servicio `waf-ai-soc-v21.2.service` es el componente encargado de ejecutar la API y el Dashboard del sistema WAF AI SOC v21.2 STABLE.

Su función es iniciar el servidor API encargado de proporcionar la interfaz de comunicación con los datos del sistema y servir el Dashboard web.

---

## 2. Ubicación del servicio

Archivo systemd:

```text
/etc/systemd/system/waf-ai-soc-v21.2.service
```
Directorio de trabajo:

```text
/opt/waf-v21.2/api
```
Entorno Python:

```bash
/opt/waf-v21.2/venv/bin/python
```

Ejecutable asociado:

```bash
/opt/waf-v21.2/api/server.py
```
---

## 3. Configuración systemd

Configuración actual:

```ini
[Unit]
Description=WAF AI SOC v21.2 API Dashboard
After=network.target

[Service]
User=moha
WorkingDirectory=/opt/waf-v21.2/api
ExecStart=/opt/waf-v21.2/venv/bin/python server.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
## 4. Ejecución del servicio

El servicio se ejecuta mediante:

```bash
/opt/waf-v21.2/venv/bin/python server.py
```
## 5. Reinicio y recuperación

El servicio tiene habilitado el reinicio automático mediante:

```bash
Restart=always
```
Si el proceso finaliza, systemd espera:

5 segundos

antes de iniciar nuevamente el servicio.

Esto permite mantener disponible la API y el Dashboard durante la operación normal del sistema.
