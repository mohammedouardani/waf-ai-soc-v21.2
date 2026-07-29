import json
from ai.scoring import ai_score

def process_event(line):

    # parse V19 line (simplificado)
    event = json.loads(line)

    event["ai_score"] = ai_score(event)

    event["final_score"] = int(
        (event["v19_score"] * 0.4) +
        (event["ai_score"] * 0.6)
    )

    return event
