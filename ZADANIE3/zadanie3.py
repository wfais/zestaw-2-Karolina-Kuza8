import requests, re, time, sys
from collections import Counter

URL = "https://pl.wikipedia.org/api/rest_v1/page/random/summary"
N = 100  # liczba losowań
HEADERS = {
    "User-Agent": "wp-edu-wiki-stats/0.1 (kontakt: twoj-email@domena)",
    "Accept": "application/json",
}

WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)


def selekcja(text: str):
    # znajdź wszystkie słowa (same litery)
    slowa = WORD_RE.findall(text)
    wynik = []
    for s in slowa:
        s2 = s.lower()
        if len(s2) > 3:
            wynik.append(s2)
    return wynik


def ramka(text: str, width: int = 80) -> str:
    # miejsce na treść = width-2 (bo dwa nawiasy)
    content_w = width - 2
    t = text

    # jeśli za długie, skróć i dodaj …
    if len(t) > content_w:
        # zostaw miejsce na znak … → content_w - 1
        t = t[: content_w - 1] + "…"

    # wyśrodkuj
    centered = t.center(content_w)
    # dołóż nawiasy
    return f"[{centered}]"


def main():
    cnt = Counter()
    licznik_slow = 0
    pobrane = 0

    print(ramka("Start"), end="", flush=True)

    while pobrane < N:
        try:
            data = requests.get(URL, headers=HEADERS, timeout=10).json()
        except Exception:
            time.sleep(0.1)
            continue

        title = data.get("title") or ""
        line = "\r" + ramka(title, 80)
        print(line, end="", flush=True)

        extract = data.get("extract") or ""
        lista = selekcja(extract)

        cnt.update(lista)
        licznik_slow += len(lista)
        pobrane += 1

        time.sleep(0.05)

    print()  # nowa linia po ramce
    print(f"Pobrano wpisów: {pobrane}")
    print(f"Słów (≥4) łącznie: {licznik_slow}")
    print(f"Unikalnych (≥4): {len(cnt)}\n")

    print("Top 15 słów (≥4):")
    for slowo, ile in cnt.most_common(15):
        print(f"{slowo}: {ile}")


if __name__ == "__main__":
    main()
