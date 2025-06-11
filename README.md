# Urava Frontend

This is a minimal and user friendly front end to search the Urava Zotero library.

It fetches zotero items with all fields through a python script which uses pyzotero. This fetching happens once a day, automatically. It is saved as json.

The frontend is HTML+JS which loads the json, does a fuzzy search, and renders it as a table, paginated.
