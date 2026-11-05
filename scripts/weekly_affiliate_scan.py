#!/usr/bin/env python3
"""Collect public news leads about affiliate programs; never treats leads as verified offers."""
from __future__ import annotations
import datetime as dt
import html
import os
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

QUERIES = [
    '"programma affiliazione" Italia',
    '"affiliate program" Italy publisher',
    'nuovi programmi affiliazione ecommerce Italia',
]
OUT = Path("reports/weekly-leads.md")
TIMEOUT = 20
MAX_ITEMS_PER_QUERY = 12

def fetch(query: str):
    params = urllib.parse.urlencode({"q": query, "hl": "it", "gl": "IT", "ceid": "IT:it"})
    url = "https://news.google.com/rss/search?" + params
    req = urllib.request.Request(url, headers={"User-Agent": "MoneyEngineResearch/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
        payload = response.read()
    root = ET.fromstring(payload)
    items = []
    for item in root.findall("./channel/item")[:MAX_ITEMS_PER_QUERY]:
        title = html.unescape(item.findtext("title", default="")).strip()
        link = item.findtext("link", default="").strip()
        pub_date = item.findtext("pubDate", default="").strip()
        source = item.findtext("source", default="").strip()
        if title and link:
            items.append((title, link, pub_date, source))
    return items

def main():
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Money Engine — report opportunità affiliate",
        "",
        f"Generato: {now}",
        "",
        "> **Attenzione:** questa scansione raccoglie notizie pubbliche come piste di ricerca. "
        "Non certifica che un programma sia aperto, gratuito o disponibile in Italia. "
        "Non sono ricavi, offerte approvate o raccomandazioni d'investimento.",
        "",
        "## Piste individuate",
        "",
    ]
    total = 0
    errors = []
    seen = set()
    for query in QUERIES:
        lines += [f"### Ricerca: {query}", ""]
        try:
            items = fetch(query)
            fresh = 0
            for title, link, pub_date, source in items:
                if link in seen:
                    continue
                seen.add(link)
                fresh += 1
                total += 1
                meta = " — ".join(x for x in (source, pub_date) if x)
                lines.append(f"- [{title}]({link})" + (f"  \n  <small>{meta}</small>" if meta else ""))
            if fresh == 0:
                lines.append("- Nessun risultato nuovo restituito da questa ricerca.")
        except Exception as exc:
            errors.append(f"{query}: {type(exc).__name__}: {exc}")
            lines.append("- Ricerca non riuscita; nessuna conclusione sull'assenza di opportunità.")
        lines.append("")
    lines += [
        "## Verifiche obbligatorie prima di aderire",
        "",
        "1. Aprire il sito ufficiale del programma, non fermarsi all'articolo.",
        "2. Verificare disponibilità per residenti/publisher italiani e requisiti di ammissione.",
        "3. Verificare commissione, evento remunerato, finestra cookie, resi e storni.",
        "4. Verificare soglia minima, valuta, metodo e calendario effettivo dei pagamenti.",
        "5. Verificare regole su sito, social, email, pubblicità e disclosure affiliate.",
        "6. Controllare privacy, obblighi fiscali e condizioni contrattuali prima di aderire.",
        "",
        f"Totale piste uniche raccolte: **{total}**.",
        "",
    ]
    if errors:
        lines += ["## Problemi di raccolta", ""] + [f"- {e}" for e in errors] + [""]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report scritto in {OUT}; piste uniche: {total}; errori: {len(errors)}")

if __name__ == "__main__":
    main()
