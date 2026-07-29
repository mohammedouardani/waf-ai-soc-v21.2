from pathlib import Path

file = Path("/opt/waf-v21/ai/processor.py")

data = file.read_text()


insert_after = """def save(ip, uri, v19, ai):
"""


new_functions = r'''

def get_ip_reputation(ip):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        SELECT COUNT(*)
        FROM attacks
        WHERE ip=?
        AND ts >= datetime('now','-10 minutes')
    """, (ip,))

    count = cur.fetchone()[0]

    conn.close()

    return count



def reputation_score(events):

    if events >= 20:
        return 50, "ATTACKER"

    elif events >= 10:
        return 30, "BAD"

    elif events >= 3:
        return 10, "SUSPICIOUS"

    else:
        return 0, "NORMAL"

'''


if "def get_ip_reputation" not in data:

    data = data.replace(
        insert_after,
        new_functions + "\n" + insert_after
    )


old = """    ai_score = score
"""


new = """    ai_score = score


    # ----------------------------
    # IP Reputation Engine
    # ----------------------------

    events = get_ip_reputation(ip)

    rep_bonus, reputation = reputation_score(events)

    ai_score += rep_bonus
"""


data = data.replace(old, new)


old_print = """        f"AI={ai_score} "
        f"SEVERITY={severity} "
        f"ACTION={action}"
"""


new_print = """        f"AI={ai_score} "
        f"REP={reputation} "
        f"EVENTS={events} "
        f"SEVERITY={severity} "
        f"ACTION={action}"
"""


data = data.replace(old_print, new_print)


file.write_text(data)

print("IP Reputation Engine añadido correctamente")
