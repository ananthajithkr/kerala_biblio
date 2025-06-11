# fetch_zotero.py

import os
import json
from pyzotero import zotero

API_KEY = os.environ.get("OW2Fey2B0ogOCnsxDWZzJFjt")
GROUP_ID = os.environ.get("283088")  # Your numeric group ID

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

with open("zotero_items.json", "w") as f:
    json.dump(all_items, f, indent=2)
