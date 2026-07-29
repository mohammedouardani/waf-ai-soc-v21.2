from pathlib import Path
import shutil


FILE = Path("/opt/waf-v21/ai/processor.py")
BACKUP = Path("/opt/waf-v21/ai/processor.py.before-reputation-multilayer-v2")


shutil.copy(FILE, BACKUP)


data = FILE.read_text()


start = data.index("def get_ip_reputation(ip):")
end = data.index("def save(ip, uri, v19, ai):")


new_block = r'''def get_ip_reputation(ip):

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



'''


data = data[:start] + new_block + data[end:]


old = """    events = get_ip_reputation(ip)

    rep_bonus, reputation = reputation_score(events)

    ai_score += rep_bonus
"""


new = """    events_10m, events_24h, events_total = get_ip_reputation(ip)

    rep_bonus, reputation = reputation_score(
        events_10m,
        events_24h,
        events_total
    )

    ai_score += rep_bonus
"""


data = data.replace(old, new)


old_print = """        f"REP={reputation} "
        f"EVENTS={events} "
"""


new_print = """        f"REP={reputation} "
        f"10M={events_10m} "
        f"24H={events_24h} "
        f"TOTAL={events_total} "
"""


data = data.replace(old_print, new_print)


FILE.write_text(data)

print("Reputation Engine Multilayer v21 aplicado")
print("Backup:", BACKUP)
