#!/usr/bin/env python3
"""Rebuild the tables in README.md and data/directories.csv from data/directories.json.

Run from the repository root:  python3 scripts/build.py
"""
import csv
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "data" / "directories.json").read_text())
rows = data["directories"]

SECTIONS = [
    ("Review sites and company databases", ("review site", "company database")),
    ("Launch platforms and communities", ("launch platform", "community")),
    ("General directories", ("directory",)),
    ("Badge-exchange directories", ("badge-exchange directory",)),
    ("AI directories", ("AI directory",)),
]
FREE = {"yes": "Yes", "badge": "With badge", "no": "No", "unknown": "Unknown"}
ACCOUNT = {"yes": "Yes", "no": "No", "unknown": "Unknown"}
CHECK = {"page loaded": "Loaded", "blocks automated requests": "Blocked"}


def cell(text):
    return str(text).replace("|", "\\|")


def table(kinds):
    out = [
        "| Directory | DR | Free? | Paid | Account | Link | Submit | Checked | Notes |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    picked = sorted((r for r in rows if r["type"] in kinds), key=lambda r: (-r["dr"], r["name"].lower()))
    for r in picked:
        name = f"[{r['name']}]({r['url']})" + (" ◆" if r.get("operator") else "")
        out.append("| " + " | ".join(cell(x) for x in (
            name, f"~{r['dr']}", FREE[r["free"]], r["paid"] or "–", ACCOUNT[r["account"]], r["link"].capitalize(),
            f"[Submit]({r['submit_url']})", f"{CHECK[r['check']]} {r['checked']}", r["notes"] or "–",
        )) + " |")
    return "\n".join(out)


body = []
for title, kinds in SECTIONS:
    body += [f"### {title}", "", table(kinds), ""]
block = "\n".join(body).rstrip() + "\n"

readme = ROOT / "README.md"
text = readme.read_text()
text = re.sub(r"(<!-- TABLES:START -->\n).*?(<!-- TABLES:END -->)", lambda m: m.group(1) + block + m.group(2), text, flags=re.S)
loaded = sum(1 for r in rows if r["check"] == "page loaded")
text = re.sub(r"(<!-- COUNT:START -->).*?(<!-- COUNT:END -->)",
              lambda m: f"{m.group(1)}{len(rows)} directories · {loaded} loaded on the last check · updated {data['updated']}{m.group(2)}", text, flags=re.S)
readme.write_text(text)

fields = ["name", "url", "submit_url", "type", "dr", "free", "paid", "account", "link", "check", "checked", "terms_reviewed", "operator", "notes"]
with (ROOT / "data" / "directories.csv").open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    for r in sorted(rows, key=lambda r: (-r["dr"], r["name"].lower())):
        writer.writerow({k: r.get(k, "") for k in fields})
print(f"{len(rows)} directories written to README.md and data/directories.csv")
