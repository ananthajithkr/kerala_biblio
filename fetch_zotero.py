# fetch_zotero.py

import os
import json
from pyzotero import zotero

API_KEY = os.environ.get("API_KEY")
GROUP_ID = os.environ.get("GROUP_ID")

# Initialize Zotero client for a group library
zot = zotero.Zotero(int(GROUP_ID), 'group', API_KEY)

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
