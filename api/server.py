from flask import Flask, jsonify, send_from_directory
import sqlite3
import psutil
import subprocess
import time

app = Flask(
    __name__,
    static_folder="/opt/waf-v21.2/dashboard",
    static_url_path=""
)

DB = "/opt/waf-v21.2/db/soc_v21.db"
def service_status(name):
    try:
        r = subprocess.run(
            ["systemctl", "is-active", name],
            capture_output=True,
            text=True
        )
        return r.stdout.strip()
    except:
        return "unknown"


def query(sql):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows


# ----------------------------------------------------
# API - Total de ataques
# ----------------------------------------------------
@app.route("/api/stats")
def stats():

    total = query("SELECT COUNT(*) FROM attacks")[0][0]
    max_score = query("SELECT MAX(final_score) FROM attacks")[0][0] or 0
    unique_ips = query("SELECT COUNT(DISTINCT ip) FROM attacks")[0][0]
    avg_score = query("SELECT AVG(final_score) FROM attacks")[0][0] or 0

    return jsonify({
        "total_attacks": total,
        "max_score": max_score,
        "unique_ips": unique_ips,
        "avg_score": round(avg_score, 2)
    })
# ----------------------------------------------------
# API - Top IPs
# ----------------------------------------------------
@app.route("/api/top")
def top():

    data = query("""
        SELECT ip, MAX(final_score) AS score
        FROM attacks
        GROUP BY ip
        ORDER BY score DESC
        LIMIT 5
    """)

    return jsonify(data)


# ----------------------------------------------------
# API - Últimos eventos
# ----------------------------------------------------
@app.route("/api/live")
def live():

    data = query("""
        SELECT
            ip,
            uri,
            final_score,
            ts
        FROM attacks
        ORDER BY id DESC
        LIMIT 20
    """)

    return jsonify(data)


# ----------------------------------------------------
# API - Dashboard completo (v21.1 STABLE)
# ----------------------------------------------------
@app.route("/api/dashboard")
def dashboard_api():

    total = query("""
        SELECT COUNT(*)
        FROM attacks
    """)[0][0]

    unique_ips = query("""
        SELECT COUNT(DISTINCT ip)
        FROM attacks
    """)[0][0]

    max_score = query("""
        SELECT COALESCE(MAX(final_score),0)
        FROM attacks
    """)[0][0]

    avg_score = query("""
        SELECT COALESCE(ROUND(AVG(final_score),2),0)
        FROM attacks
    """)[0][0]

    top = query("""
        SELECT
            ip,
            COUNT(*) AS hits
        FROM attacks
        GROUP BY ip
        ORDER BY hits DESC
        LIMIT 5
    """)

    live = query("""
        SELECT
            ip,
            uri,
            final_score,
            ts
        FROM attacks
        ORDER BY ts DESC
        LIMIT 20
    """)

    return jsonify({
        "status": "online",
        "total_attacks": total,
        "unique_ips": unique_ips,
        "max_score": max_score,
        "avg_score": avg_score,
        "top": top,
        "live": live
    })

# ----------------------------------------------------
# API - Estado del sistema
# ----------------------------------------------------
@app.route("/api/system")
def system():

    cpu = psutil.cpu_percent(interval=0.5)

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage("/").percent

    boot_time = psutil.boot_time()
    uptime = int(time.time() - boot_time)

    return jsonify({

        "status": "online",

        "services": {

            "api": service_status("waf-ai-soc-v21.2"),

            "collector": service_status("waf-ai-soc-v21.2-collector"),

            "processor": service_status("waf-ai-soc-v21.2-processor"),

            "nginx": service_status("nginx"),

            "fail2ban": service_status("fail2ban")
        },
        "defense": {

            "modsecurity": "active",

            "crs": "active",

            "sqlite": "active",

            "ufw": "active"

        },

        "system": {

            "cpu": cpu,

            "ram": ram,

            "disk": disk,

            "uptime_seconds": uptime
        }

    })


# ----------------------------------------------------
# API - Últimas IP bloqueadas
# ----------------------------------------------------
@app.route("/api/blocked")
def blocked():

    log = "/opt/waf-v21.2/logs/waf-ai-ban.log"

    blocked = []

    try:
        with open(log, "r") as f:
            lines = f.readlines()[-100:]

        for line in reversed(lines):

            if "ACTION=BLOCK" not in line:
                continue

            parts = {}

            for item in line.split():
                if "=" in item:
                    k, v = item.split("=", 1)
                    parts[k] = v

            ip = parts.get("IP")

            if ip and not any(x["ip"] == ip for x in blocked):

                blocked.append({
                    "ip": ip,
                    "score": parts.get("SCORE"),
                    "severity": parts.get("SEVERITY"),
                    "uri": parts.get("URI")
                })

            if len(blocked) == 3:
                break

    except Exception:
        pass

    return jsonify({
        "blocked": blocked
    })


# ----------------------------------------------------
# Dashboard Web
# ----------------------------------------------------
@app.route("/")
def dashboard():

    return send_from_directory(
        app.static_folder,
        "index.html"
    )


# ----------------------------------------------------
# Archivos estáticos
# ----------------------------------------------------
@app.route("/<path:path>")
def static_proxy(path):

    return send_from_directory(
        app.static_folder,
        path
    )


# ----------------------------------------------------
# MAIN
# ----------------------------------------------------
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5051,
        debug=False
    )
