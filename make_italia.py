#!/usr/bin/python3
"""Genera una playlist M3U con i soli canali e VOD italiani di Free-TV/IPTV.

Scarica le liste markdown dal repository upstream e le converte con lo stesso
formato usato da make_playlist.py, usando però le sezioni (<h2>) come gruppi.
"""

import argparse
import re
import sys
import urllib.request

RAW_BASE = "https://raw.githubusercontent.com/Free-TV/IPTV/master/"
# (file in lists/, prefisso del gruppo)
SOURCES = [
    ("italy.md", "Italia"),
    ("zz_vod_it.md", "VOD Italia"),
]
COUNTRY_CODE = "IT"
# Ritrasmissioni di terzi (non il CDN dell'emittente): escluse per prudenza.
EXCLUDED_HOSTS = ("netplus.ch",)


def fetch(path):
    """Scarica un file di testo dal repository upstream."""
    with urllib.request.urlopen(RAW_BASE + path, timeout=30) as response:
        return response.read().decode("utf-8")


def epg_header():
    """Costruisce l'intestazione tenendo solo le sorgenti EPG italiane."""
    urls = [line.strip() for line in fetch("epglist.txt").splitlines()
            if re.search(r"_IT\d*\.xml", line)]
    return f'#EXTM3U x-tvg-url="{", ".join(urls)}"\n'


def to_m3u_line(group, md_line):
    """Converte una riga della tabella markdown in una voce #EXTINF + URL."""
    parts = md_line.strip().split("|")
    number = parts[1].strip().replace('"', '')
    name = parts[2].strip().replace('"', '')
    url = parts[3].strip()
    url = url[url.find("(")+1:url.rfind(")")]
    logo = parts[4].strip()
    logo = logo[logo.find('src="')+5:logo.rfind('"')].replace('"', '')
    epg = parts[5].strip().replace('"', '') if len(parts) > 6 else ""

    chno = f' tvg-chno="{number}"' if number and number != "0" else ""
    tvg_id = f' tvg-id="{epg}"' if epg else ""
    # I simboli finali (Ⓖ/Ⓢ/Ⓨ/...) servono al lettore, non al matching EPG.
    tvg_name = re.sub(r'\s*[Ⓐ-ⓩ\s]+$', '', name)
    return (
        f'#EXTINF:-1 tvg-name="{tvg_name}" tvg-logo="{logo}"{tvg_id}{chno}'
        f' tvg-country="{COUNTRY_CODE}" group-title="{group}",{name}\n{url}'
    )


def main():
    """Scarica le liste italiane e scrive la playlist."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("-o", "--output", default="italia.m3u8",
                        help="file di destinazione (default: %(default)s)")
    parser.add_argument("--no-geo", action="store_true",
                        help="escludi i canali geo-bloccati (Ⓖ)")
    parser.add_argument("--no-web", action="store_true",
                        help="escludi le dirette YouTube/Twitch")
    args = parser.parse_args()

    lines = [epg_header()]
    seen = set()
    counts = {}
    for filename, prefix in SOURCES:
        section = ""
        for line in fetch("lists/" + filename).splitlines():
            if "<h2>" in line.lower():
                section = re.sub('<[^<>]+>', '', line.strip())
            # Solo [>] è un link attivo: [x] e la sezione Invalid sono canali morti.
            if "[>]" not in line or section == "Invalid":
                continue
            if args.no_geo and "Ⓖ" in line:
                continue
            if args.no_web and section in ("YouTube Live", "Twitch Live"):
                continue
            group = f"{prefix} - {section}" if section else prefix
            entry = to_m3u_line(group, line)
            url = entry.rsplit("\n", 1)[1]
            if url in seen or any(host in url for host in EXCLUDED_HOSTS):
                continue
            seen.add(url)
            lines.append(entry + "\n")
            counts[group] = counts.get(group, 0) + 1

    with open(args.output, "w", encoding="utf-8") as playlist:
        playlist.writelines(lines)

    for group, count in counts.items():
        print(f"{count:4d}  {group}")
    print(f"{sum(counts.values()):4d}  totale -> {args.output}")


if __name__ == "__main__":
    sys.exit(main())
