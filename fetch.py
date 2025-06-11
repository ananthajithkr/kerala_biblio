# fetch_zotero.py

import os
import json
import time
from pyzotero import zotero

API_KEY = os.environ.get("API_KEY")
GROUP_ID = os.environ.get("GROUP_ID")

# Initialize Zotero client for a group library
zot = zotero.Zotero(GROUP_ID, 'group', API_KEY)

all_items = []
start = 0
limit = 100

while True:
    items = zot.items(limit=limit, start=start)
    if not items:
        break
    all_items.extend(items)
    start += limit
    time.sleep(1)  # ⏱️ Pause 1 second between requests

with open("zotero_items.json", "w") as f:
    json.dump(all_items, f, indent=2)
