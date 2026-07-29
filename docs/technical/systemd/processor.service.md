# WAF AI SOC v21.2 STABLE - Processor Service

## 1. Descripción

El servicio `waf-ai-soc-v21.2-processor.service` es el componente encargado de ejecutar el AI Processor dentro del sistema WAF AI SOC v21.2 STABLE.

Su función es iniciar el proceso de análisis y procesamiento de los eventos recibidos desde el Collector para aplicar la lógica de evaluación AI del sistema.

---

## 2. Ubicación del servicio

Archivo systemd:

```text
/etc/systemd/system/waf-ai-soc-v21.2-processor.service
```
Ejecutable asociado:

```text
/opt/waf-v21.2/ai/processor.py
```

Entorno Python:

```text
/opt/waf-v21.2/venv/bin/python
```

Directorio de trabajo:

```text
/opt/waf-v21.2
```
---

## 3. Configuración systemd

Configuración actual:

```ini
[Unit]
Description=WAF AI SOC v21.2 AI Processor
After=network.target waf-ai-soc-v21.2-collector.service

[Service]
Type=simple
User=moha
WorkingDirectory=/opt/waf-v21.2
ExecStart=/opt/waf-v21.2/venv/bin/python /opt/waf-v21.2/ai/processor.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

## 4. Ejecución del servicio

El servicio se ejecuta mediante:

```bash
/opt/waf-v21.2/venv/bin/python /opt/waf-v21.2/ai/processor.py
```
---

## 5. Dependencias de arranque

El servicio espera a que el Collector esté disponible antes de iniciar:

```ini
After=network.target waf-ai-soc-v21.2-collector.service
```
La relación entre servicios es:

```text
Collector Service
        |
        v
AI Processor Service
```

## 6. Reinicio y recuperación

El servicio tiene habilitado el reinicio automático mediante:


```ini
Restart=always
```

Si el proceso finaliza, systemd espera:

5 segundos

antes de iniciar nuevamente el servicio.

Esto permite mantener el procesamiento AI activo durante la operación normal del sistema.

