#!/usr/bin/env python3
"""Request every submit_url and report what came back. Does not edit the data file.

Run from the repository root:  python3 scripts/check_links.py
A 403 or 429 usually means the site blocks automated requests, not that it is down;
record those as "blocks automated requests" and confirm them in a browser.
"""
import concurrent.futures
import json
import pathlib
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
rows = json.loads((ROOT / "data" / "directories.json").read_text())["directories"]
AGENT = "Mozilla/5.0 (compatible; saas-directory-list link check; +https://github.com/andrewmpierce/saas-directory-list)"


def check(row):
    request = urllib.request.Request(row["submit_url"], headers={"User-Agent": AGENT})
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return row, response.status, response.geturl()
    except urllib.error.HTTPError as error:
        return row, error.code, row["submit_url"]
    except Exception as error:  # DNS failure, timeout, TLS error
        return row, 0, type(error).__name__


with concurrent.futures.ThreadPoolExecutor(8) as pool:
    for row, status, final in pool.map(check, rows):
        moved = "" if final.rstrip("/") == row["submit_url"].rstrip("/") else f"  -> {final}"
        print(f"{status:>3}  {row['name']:<26} {row['submit_url']}{moved}")
