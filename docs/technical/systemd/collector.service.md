# WAF AI SOC v21.2 STABLE - Collector Service

## 1. Descripción

El servicio `waf-ai-soc-v21.2-collector.service` es el componente encargado de ejecutar el Collector de ModSecurity dentro del sistema WAF AI SOC v21.2 STABLE.

Su función es iniciar el proceso encargado de recoger eventos generados por ModSecurity y preparar los datos para el procesamiento posterior dentro del pipeline del sistema.

---

## 2. Ubicación del servicio

Archivo systemd:
/etc/systemd/system/waf-ai-soc-v21.2-collector.service


Entorno Python:
/opt/waf-v21.2/venv/bin/python

Directorio de trabajo:
/opt/waf-v21.2


---

## 3. Configuración systemd

Configuración actual:

```ini
[Unit]
Description=WAF AI SOC v21.2 ModSecurity Collector
After=network.target

[Service]
Type=simple
User=moha
WorkingDirectory=/opt/waf-v21.2
ExecStart=/opt/waf-v21.2/venv/bin/python /opt/waf-v21.2/connectors/modsec_collector.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
## 4. Ejecución del servicio

El servicio se ejecuta mediante:

```bash
/opt/waf-v21.2/venv/bin/python /opt/waf-v21.2/connectors/modsec_collector.py
```

