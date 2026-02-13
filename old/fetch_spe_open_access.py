#!/usr/bin/env python3
import requests
import csv
import time

JOURNAL_ISSN = "0038-0644"  # Software: Practice and Experience
OUTPUT_FILE = "software_practice_experience_open_access.csv"

def is_open_access(licenses):
    if not licenses:
        return False
    for lic in licenses:
        url = lic.get("URL", "").lower()
        if "creativecommons.org" in url or "cc-by" in url:
            return True
    return False

def fetch_open_access_articles():
    url = "https://api.crossref.org/journals/{}/works".format(JOURNAL_ISSN)
    rows = []
    cursor = "*"
    total = 0
    print("Fetching open-access articles from CrossRef...")

    while True:
        params = {
            "filter": "type:journal-article",
            "rows": 100,
            "cursor": cursor,
            "mailto": "your_email@example.com",  # optional for polite use
        }
        r = requests.get(url, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()["message"]
        items = data.get("items", [])
        cursor = data.get("next-cursor")
        if not items:
            break

        for item in items:
            licenses = item.get("license", [])
            if not is_open_access(licenses):
                continue
            title = " ".join(item.get("title", [""])).strip()
            doi = item.get("DOI", "")
            link = f"https://doi.org/{doi}"
            issued = item.get("issued", {}).get("date-parts", [[None]])[0][0]
            license_urls = [lic.get("URL", "") for lic in licenses]
            rows.append([title, doi, link, issued, "; ".join(license_urls)])
            total += 1

        print(f"Fetched {total} open-access entries so far...")
        time.sleep(1)  # be polite to API

        if not data.get("next-cursor"):
            break

    # Write to CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "DOI", "URL", "Published", "License"])
        writer.writerows(rows)

    print(f"\n✅ Done! Saved {len(rows)} open-access articles to {OUTPUT_FILE}")

if __name__ == "__main__":
    fetch_open_access_articles()
