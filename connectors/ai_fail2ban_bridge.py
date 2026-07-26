#!/usr/bin/env python3

import time
import re
from pathlib import Path
from datetime import datetime

SOURCE = "/opt/waf-v21.2/logs/waf-ai-ban.log"
DEST = "/opt/waf-v21.2/logs/waf-ai-events.log"

seen = set()

def process(line):
    if "ACTION=BLOCK" not in line:
        return

    match = re.search(r"IP=([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", line)

    if match:
        ip = match.group(1)

        if ip not in seen:
            seen.add(ip)

            with open(DEST, "a") as f:
                f.write(
                    f"{datetime.now()} BLOCK IP={ip}\n"
                )

def main():

    with open(SOURCE, "r") as f:
        f.seek(0,2)

        while True:
            line = f.readline()

            if line:
                process(line)
            else:
                time.sleep(1)


if __name__ == "__main__":
    main()
