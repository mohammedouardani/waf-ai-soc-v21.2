#!/usr/bin/env python3

import json
import time
import re
import os

AUDIT_LOG = "/var/log/modsec_audit.log"
PIPE = "/opt/waf-v21.2/connectors/events.pipe"


def extract_score(event):

    score = 0

    messages = event.get("transaction", {}).get("messages", [])

    for msg in messages:

        message = msg.get("message", "")

        match = re.search(r"Total Score:\s*(\d+)", message)

        if match:
            score = max(score, int(match.group(1)))

    # Si ModSecurity detecta algo pero no aparece el Total Score
    if score == 0 and messages:
        score = 5

    return score


def parse_event(event):

    tx = event.get("transaction", {})

    ip = tx.get("client_ip", "unknown")
    uri = tx.get("request", {}).get("uri", "/")
    ts = tx.get("time_stamp", "")

    messages = tx.get("messages", [])

    # --------------------------------------------------
    # Ignorar llamadas internas del dashboard
    # --------------------------------------------------

    if uri.startswith("/api/"):
        return None

    if uri in (
        "/favicon.ico",
        "/robots.txt",
    ):
        return None

    # --------------------------------------------------
    # Si ModSecurity no ha disparado ninguna regla,
    # no es un evento de seguridad.
    # --------------------------------------------------

    if not messages:
        return None

    # --------------------------------------------------
    # Verificar que exista al menos un ruleId válido
    # --------------------------------------------------

    has_rule = False

    for msg in messages:

        details = msg.get("details", {})

        if details.get("ruleId"):
            has_rule = True
            break

    if not has_rule:
        return None

    # --------------------------------------------------
    # Obtener el Anomaly Score
    # --------------------------------------------------

    score = extract_score(event)

    # Hay reglas pero no aparece Total Score
    if score == 0:
        score = 5

    return f"{ip}|{uri}|{score}|{ts}"

def write_pipe(line):

    with open(PIPE, "a") as f:
        f.write(line + "\n")
        f.flush()

def run():

    print("WAF AI SOC v21.2 ModSecurity Collector STARTED")

    with open(AUDIT_LOG, "r") as f:

        f.seek(0, 2)

        buffer = ""

        while True:

            try:
                if f.tell() > os.path.getsize(AUDIT_LOG):
                    print("[COLLECTOR] Log rotation detected, resetting")
                    f.seek(0)
                    buffer = ""

            except FileNotFoundError:
                time.sleep(1)
                continue


            line = f.readline()

            if not line:
                time.sleep(0.05)
                continue

            buffer += line.strip()

            try:

                event = json.loads(buffer)

                buffer = ""

                output = parse_event(event)

                if output:
                    write_pipe(output)
                    print("[COLLECTOR]", output)

            except json.JSONDecodeError:
                continue



if __name__ == "__main__":
    run()
