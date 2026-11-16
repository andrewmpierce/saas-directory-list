# Contributing

Corrections matter more than additions. If a row is out of date, fix it.

## What belongs here

A place where the owner of a SaaS or AI product can list it, and that is taking submissions now. Not agencies, link sellers or sites that only accept paid placements with no listing.

## How to change a row

1. Edit `data/directories.json`. Do not edit the tables in `README.md`; they are generated.
2. Open the submission page yourself and set the fields from what it says today:
   - `free`: `yes`, `badge` (free only with their badge or a link on your site), `no` or `unknown`.
   - `account`: `yes`, `no` or `unknown`.
   - `paid`: the paid option in a few words. Give a price only if the page shows it.
   - `check`: `page loaded` or `blocks automated requests`, with today's date in `checked`.
   - `terms_reviewed`: today's date, if you read the terms.
   - `notes`: one or two factual sentences. No recommendations.
3. Use `unknown` when you could not confirm something. A guess is worse than a gap.
4. Run `python3 scripts/build.py` and commit the JSON, the CSV and the README together.

## If you run the directory

You are welcome to add or correct your own entry. Say so in the pull request, and describe the directory in the same plain terms as the others.
