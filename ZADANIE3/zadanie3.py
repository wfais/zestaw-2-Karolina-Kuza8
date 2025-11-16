import requests, re, time, sys
from collections import Counter

URL = "https://pl.wikipedia.org/api/rest_v1/page/random/summary"
N = 100  # liczba losowań
HEADERS = {
    "User-Agent": "wp-edu-wiki-stats/0.1 (kontakt: twoj-email@domena)",
    "Accept": "application/json",
}

# przygotowanie wyrażenia regularnego wyłapującego słowa (litery)
WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)


def selekcja(text: str):
    # wyciągamy słowa z tekstu
    słowa = WORD_RE.findall(text)
    wynik = []
    for s in słowa:
        s2 = s.lower()
        if len(s2) > 3:
            wynik.append(s2)
    return wynik


def ramka(text: str, width: int = 80) -> str:
    # szerokość pola wewnętrznego
    content_w = width - 2

    # za długie → przyciąć i dodać …
    if len(text) > content_w:
        # zostawiamy content_w - 1 znak (bo jeden to "…")
        text = text[: content_w - 1] + "…"

    # wyśrodkowanie
    centered = text.center(content_w)

    return "[" + centered + "]"


def main():
    cnt = Counter()
    licznik_slow = 0
    pobrane = 0

    # linia statusu
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
    for słowo, ile in cnt.most_common(15):
        print(f"{słowo}: {ile}")


if __name__ == "__main__":
    main()
