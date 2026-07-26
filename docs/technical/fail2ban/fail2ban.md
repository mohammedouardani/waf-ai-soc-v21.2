# WAF AI SOC v21.2 STABLE - Fail2Ban Integration

## 1. Descripción

Fail2Ban es el componente encargado de aplicar bloqueos activos sobre direcciones IP detectadas como amenazas por el sistema WAF AI SOC v21.2 STABLE.

Su función es monitorizar los eventos de bloqueo generados por el sistema AI y aplicar acciones de defensa mediante el firewall del sistema.

La integración permite transformar una decisión AI:

```text
ACTION=BLOCK
```
en una acción real de protección:

```text
IP bloqueada mediante Fail2Ban
```

---

## 2. Ubicación

Servicio:
```text
fail2ban.service
```

Configuración principal:
```text
/etc/fail2ban/
```

Jail personalizado:

```text
/etc/fail2ban/jail.d/waf-ai-soc.conf
```

Log monitorizado:

```text
/opt/waf-v21.2/logs/waf-ai-ban.log
```

Acción aplicada:

```text
UFW
```

---

## 3. Funcionamiento general

Fail2Ban monitoriza el log generado por WAF AI SOC y detecta eventos de bloqueo.

Flujo:

```text
AI Processor
      |
      v
ACTION=BLOCK
      |
      v
waf-ai-ban.log
      |
      v
Fail2Ban Filter
      |
      v
UFW Ban
      |
      v
IP bloqueada
```
---

## 4. Integración con WAF AI SOC

El sistema AI genera una decisión de defensa cuando un evento supera los umbrales definidos.

Ejemplo:

```text
AI Score >= 120
```

Resultado:

```text
CRITICAL
BLOCK
```

Este evento es registrado en:

```text
/opt/waf-v21.2/logs/waf-ai-ban.log
```

Fail2Ban utiliza este registro como fuente para ejecutar el bloqueo.

---

## 5. Jail WAF AI SOC

Configuración utilizada:

```text
/etc/fail2ban/jail.d/waf-ai-soc.conf
```

Parámetros principales:

```text
maxretry = 1

findtime = 600

bantime = 3600
```

Funcionamiento:

- Una detección BLOCK activa el bloqueo.
- La ventana de análisis es de 600 segundos.
- El bloqueo permanece durante 3600 segundos.

---

## 6. Acción de bloqueo

Fail2Ban utiliza UFW como backend de bloqueo.

Flujo:

```text
Fail2Ban
     |
     v
UFW
     |
     v
iptables/nftables
     |
     v
IP bloqueada
```
---

## 7. Estado operativo

El estado del servicio se comprueba mediante:

```bash
systemctl status fail2ban
```

Los jails activos se pueden consultar mediante:

```bash
fail2ban-client status
```

El jail WAF AI SOC debe aparecer como:

```text
waf-ai-soc
```
---

## 8. Integración dentro del sistema

Fail2Ban representa la capa de respuesta activa:

```text
Internet
    |
    v
Nginx
    |
    v
ModSecurity
    |
    v
Collector
    |
    v
AI Processor
    |
    v
Decision Engine
    |
    v
Fail2Ban
    |
    v
UFW Block
```
---

## 9. Estado de protección

La integración Fail2Ban permite:

- Aplicar bloqueos automáticos.
- Reducir ataques repetitivos.
- Integrar decisiones AI con defensa del sistema.
- Mantener una respuesta automática ante amenazas críticas.


