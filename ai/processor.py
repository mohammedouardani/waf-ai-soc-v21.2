#!/usr/bin/env python3

import sqlite3
import time

DB = "/opt/waf-v21.2/db/soc_v21.db"
PIPE = "/opt/waf-v21.2/connectors/events.pipe"
BAN_LOG = "/opt/waf-v21.2/logs/waf-ai-ban.log"
EVENT_LOG = "/opt/waf-v21.2/logs/waf-ai-events.log"


def get_ip_reputation(ip):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()


    cur.execute("""
        SELECT COUNT(*)
        FROM attacks
        WHERE ip=?
        AND ts >= datetime('now','-10 minutes')
    """, (ip,))

    events_10m = cur.fetchone()[0]


    cur.execute("""
        SELECT COUNT(*)
        FROM attacks
        WHERE ip=?
        AND ts >= datetime('now','-24 hours')
    """, (ip,))

    events_24h = cur.fetchone()[0]


    cur.execute("""
        SELECT COUNT(*)
        FROM attacks
        WHERE ip=?
    """, (ip,))

    events_total = cur.fetchone()[0]


    conn.close()


    return events_10m, events_24h, events_total



def reputation_score(events_10m, events_24h, events_total):

    if events_10m >= 5:
        return 50, "ACTIVE_ATTACKER"

    elif events_24h >= 10:
        return 30, "BAD"

    elif events_total >= 20:
        return 10, "SUSPICIOUS"

    else:
        return 0, "NORMAL"

def detect_pattern(uri):

    uri_lower = uri.lower()


    if any(x in uri_lower for x in [
        "<script",
        "javascript:",
        "onerror=",
        "alert("
    ]):
        return "XSS"


    if any(x in uri_lower for x in [
        "union select",
        "select ",
        "information_schema",
        "sleep(",
        "' or ",
        "\" or "
    ]):
        return "SQLI"


    if any(x in uri_lower for x in [
        "nikto",
        "nmap",
        "zgrab",
        "masscan",
        "acunetix"
    ]):
        return "SCANNER"


    if any(x in uri_lower for x in [
        "../",
        "..\\",
        "/etc/passwd",
        "boot.ini"
    ]):
        return "PATH_TRAVERSAL"


    if any(x in uri_lower for x in [
        "cmd=",
        "shell",
        "r57",
        "eval("
    ]):
        return "RCE"
    if any(x in uri_lower for x in [
        "cmd=",
        "shell",
        "r57",
        "eval("
    ]):
        return "RCE"


    if any(x in uri_lower for x in [
        ".env",
        ".sql",
        ".inc",
        ".bak",
        ".log",
        ".config",
        ".json",
        ".xml",
        ".yml",
        ".yaml",
        ".git",
        "wp-config",
        "config.php",
        "phpinfo.php",
        "install.sh",
        "web.config"
    ]):
        return "SENSITIVE_FILE_SCAN"


    return "UNKNOWN"


    return "UNKNOWN"



def get_pattern_count(ip, pattern):

    if pattern == "UNKNOWN":
        return 0


    signatures = {

        "XSS": [
            "<script",
            "javascript:",
            "onerror=",
            "alert("
        ],

        "SQLI": [
            "union select",
            "information_schema",
            "sleep(",
            "' or ",
            "\" or "
        ],

        "SCANNER": [
            "nikto",
            "nmap",
            "zgrab",
            "masscan",
            "acunetix"
        ],

        "PATH_TRAVERSAL": [
            "../",
            "/etc/passwd",
            "boot.ini"
        ],

        "RCE": [
            "cmd=",
            "shell",
            "r57",
            "eval("
        ]
    }


    if pattern not in signatures:
        return 0


    conn = sqlite3.connect(DB)
    cur = conn.cursor()


    pattern_ids = set()


    for sig in signatures[pattern]:

        cur.execute("""
            SELECT COUNT(*)
            FROM attacks
            WHERE ip=?
            AND uri LIKE ?
            AND ts >= datetime('now','-10 minutes')
        """, (
            ip,
            f"%{sig}%"
        ))

        rows = cur.fetchall()

        for row in rows:
            pattern_ids.add(row[0])


    conn.close()


    return len(pattern_ids)


def save(ip, uri, v19, ai, ts):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO attacks
        (ip, uri, v19_score, ai_score, final_score, ts)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (ip, uri, v19, ai, ai, ts))

    conn.commit()
    conn.close()



def write_decision(ip, uri, score, severity, action, bantime):

    if action != "BLOCK":
        return

    with open(BAN_LOG, "a") as f:

        f.write(
            f"{time.strftime('%Y-%m-%d %H:%M:%S')} "
            f"[AI-DECISION] "
            f"IP={ip} "
            f"SCORE={score} "
            f"SEVERITY={severity} "
            f"ACTION={action} "
            f"BANTIME={bantime} "
            f"URI={uri}\n"
        )



def classify(score):

    if score >= 120:

        return (
            "CRITICAL",
            "BLOCK"
        )


    elif score >= 80:

        return (
            "HIGH",
            "ALERT"
        )


    elif score >= 30:

        return (
            "MEDIUM",
            "MONITOR"
        )


    elif score > 0:

        return (
            "LOW",
            "LOG"
        )


    else:

        return (
            "NORMAL",
            "IGNORE"
        )

def calculate_bantime(ai_score):

    if ai_score >= 150:
        return 604800      # 7 días

    elif ai_score >= 120:
        return 86400       # 24 horas

    elif ai_score >= 80:
        return 21600       # 6 horas

    elif ai_score >= 30:
        return 3600        # 1 hora

    return 0

def analyze(line):

    parts = line.strip().split("|")


    if len(parts) != 4:
        return


    ip, uri, score, ts = parts


    try:

        score = int(score)

    except ValueError:

        return



    ai_score = score

    # ----------------------------
    # Pattern Memory Engine v21.1
    # ----------------------------

    pattern = detect_pattern(uri)

    pattern_count = get_pattern_count(
        ip,
        pattern
    )


    if pattern == "XSS":
        ai_score += 5


    elif pattern == "SQLI":
        ai_score += 25


    elif pattern == "SCANNER":
        ai_score += 15


    elif pattern == "RCE":
        ai_score += 40


    elif pattern == "PATH_TRAVERSAL":
        ai_score += 20
    
    elif pattern == "SENSITIVE_FILE_SCAN":
        ai_score += 30



    # Repetition bonus

    if pattern_count >= 3:

        ai_score += 20


    if pattern_count >= 5:

        ai_score += 40

    # ----------------------------
    # IP Reputation Engine
    # ----------------------------

    events_10m, events_24h, events_total = get_ip_reputation(ip)

    rep_bonus, reputation = reputation_score(
        events_10m,
        events_24h,
        events_total
    )

    ai_score += rep_bonus


    if reputation == "ACTIVE_ATTACKER" and pattern != "UNKNOWN":

        ai_score += 10



    # ----------------------------
    # Persistent Attack Escalation
    # ----------------------------

    if events_10m >= 10:
        ai_score += 10

    if events_10m >= 20:
        ai_score += 20

    if events_10m >= 40:
        ai_score += 30

    if events_10m >= 80:
        ai_score += 40


    if events_total >= 100:
        ai_score += 10

    if events_total >= 250:
        ai_score += 20

    if events_total >= 500:
        ai_score += 30


    # ----------------------------
    # AI enrichment
    # ----------------------------

    uri_lower = uri.lower()


    if any(x in uri_lower for x in [
        "wp-",
        "admin",
        "login"
    ]):

        ai_score += 20



    if any(x in uri_lower for x in [
        "shell",
        "cmd",
        "r57"
    ]):

        ai_score += 50



    severity, action = classify(ai_score)
    bantime = calculate_bantime(ai_score)


    if action == "IGNORE":
        return

    # Todos los eventos SOC
    with open(EVENT_LOG, "a") as f:
        f.write(
            f"{time.strftime('%Y-%m-%d %H:%M:%S')} "
            f"[AI] "
            f"IP={ip} "
            f"URI={uri} "
            f"PATTERN={pattern} "
            f"REPEAT={pattern_count} "
            f"V19={score} "
            f"AI={ai_score} "
            f"REP={reputation} "
            f"10M={events_10m} "
            f"24H={events_24h} "
            f"TOTAL={events_total} "
            f"SEVERITY={severity} "
            f"ACTION={action}\n"
        )

    

        # Todos los eventos SOC
    with open(EVENT_LOG, "a") as f:

        f.write(
            f"{time.strftime('%Y-%m-%d %H:%M:%S')} "
            f"[AI] "
            f"IP={ip} "
            f"URI={uri} "
            f"PATTERN={pattern} "
            f"REPEAT={pattern_count} "
            f"V19={score} "
            f"AI={ai_score} "
            f"REP={reputation} "
            f"10M={events_10m} "
            f"24H={events_24h} "
            f"TOTAL={events_total} "
            f"SEVERITY={severity} "
            f"ACTION={action}\n"
        )


    # Solo BLOCK va a Fail2Ban
    if action == "BLOCK":

        write_decision(
            ip,
            uri,
            ai_score,
            severity,
            action,
            bantime
        )

    
    save(
        ip,
        uri,
        score,
        ai_score,
        ts
    )



def run():

    print("V21 AI Processor STARTED")


    with open(PIPE, "r") as f:


        while True:


            line = f.readline()


            if not line:

                time.sleep(0.5)

                continue


            analyze(line)



if __name__ == "__main__":

    run()
