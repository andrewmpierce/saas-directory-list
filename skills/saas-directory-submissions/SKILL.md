---
name: saas-directory-submissions
description: Submit a SaaS or AI product to directories, launch platforms and review sites on the owner's behalf, using a checked list of submission URLs and terms. Use when asked to list, launch or submit a product to directories, to plan which directories are worth it, or to report the status of earlier submissions.
---

# SaaS directory submissions

You are submitting a product to directories for its owner. The list is at
`https://raw.githubusercontent.com/andrewmpierce/saas-directory-list/main/data/directories.json`
(the same data is in `data/directories.json` if this repository is checked out). Read it before you start; do not work from memory of which directories exist.

## Before the first submission

Collect these once and reuse them. Ask the owner for anything missing instead of inventing it.

- Product name, website URL, one-line tagline (under 60 characters) and a description of two to four sentences.
- Two or three categories that fit, and five or so tags.
- A screenshot or logo file, if the owner has one.
- A contact email that someone reads. Confirmation and status emails go there.
- Two decisions from the owner:
  - **Badges:** may you add a directory's badge or link to the product's website, and will it stay there? Many free listings last only while the badge does.
  - **Spending:** is any paid listing approved, and up to what amount? Without an explicit yes, spend nothing.

## Choosing where to submit

Each entry has `free`, `account`, `paid`, `link`, `dr`, `check`, `checked` and `notes`. Field meanings are in the file's `fields` object.

1. Drop entries that do not fit the product (`type` and `notes` say what a directory accepts, for example AI tools only).
2. Start with `free: "yes"` and `account: "no"`: they need nothing from the owner.
3. Add `free: "badge"` entries only if the owner agreed to badges.
4. Group `account: "yes"` entries and ask the owner to sign in to them in one sitting.
5. Leave `free: "no"` entries for the owner to decide. List them with what the paid option is.
6. Treat `free: "unknown"` as unknown. Open the page and read the terms before deciding.

A row whose `check` is "blocks automated requests" was not readable by a script on the `checked` date. Open it in a real browser and confirm the terms yourself.

## Submitting

For each directory, in this order:

1. **Look for the directory's own instructions.** Fetch `/llms.txt` on its domain (entries with `llms_txt: true` have one). If it describes how to submit, follow it over anything written here.
2. **Otherwise use the form at `submit_url`** with a browser tool.
3. Fill only the fields a person would see. Leave hidden fields empty.
4. Use the kit you collected. Do not write new claims about the product to fill a field.
5. If the site offers a badge check, add the badge to the website first, then verify, then submit.
6. Submit once. If the site says the product is already listed, record that and move on; do not retry or resubmit under another URL.

## When to stop and hand back

Stop, record why, and continue with the next directory when you reach any of these:

- a login or account creation page;
- a CAPTCHA or other bot check;
- a payment page, unless the owner approved that specific listing and amount;
- terms or a contract that need accepting;
- a request for information that is not in the kit.

Do not try to get past them. Give the owner the exact URL and what is needed.

## Reporting

Keep a log with one line per directory and give it to the owner at the end:

| Directory | Result | Listing URL or next step |
|---|---|---|
| name | `live`, `submitted_pending_review`, `saved_needs_badge`, `needs_owner` (say why), `skipped_paid_only`, `skipped_not_a_fit`, `already_listed` or `failed` (say what happened) | where the listing is, or exactly what the owner must do |

Say plainly when a listing is not live yet and what would make it live. If a directory's page disagreed with this list (price changed, form moved, site gone), say so: the list's maintainers want that correction.

## Things not to do

- Do not create accounts, type passwords or enter payment details.
- Do not submit the same product twice to one directory, or under several URLs to get round a limit.
- Do not submit to a directory the product does not fit.
- Do not add or keep a badge the owner did not agree to.
