import requests, re, time, sys
from collections import Counter

URL = "https://pl.wikipedia.org/api/rest_v1/page/random/summary"
N = 100  # liczba losowań
HEADERS = {
    "User-Agent": "wp-edu-wiki-stats/0.1 (kontakt: twoj-email@domena)",
    "Accept": "application/json",
}

# wyrażenie regularne wyłapujące słowa (tylko litery, Unicode)
WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)


def selekcja(text: str):
    """Zwróć listę słów dłuższych niż 3 znaki, złożonych wyłącznie z liter, małe litery"""
    return [w.lower() for w in WORD_RE.findall(text) if len(w) > 3]


def ramka(text: str, width: int = 80) -> str:
    """Zwraca tekst w ramce o stałej szerokości z wyśrodkowaniem, przycinaniem i wielokropkiem"""
    content_w = width - 2
    t = text.strip()
    if len(t) > content_w:
        t = t[:content_w - 1] + "…"
    return f"[{t.center(content_w)}]"


def main():
    cnt = Counter()
    licznik_slow = 0
    pobrane = 0

    # linia statusu start
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
        words = selekcja(extract)
        cnt.update(words)
        licznik_slow += len(words)
        pobrane += 1
        time.sleep(0.05)

    print()  # zakończ linię statusu
    print(f"Pobrano: {pobrane}")
    print(f"#Słowa:  {licznik_slow}")
    print(f"Unikalne:  {len(cnt)}\n")

    print("Najczęstsze 15 słów:")
    for w, ile in cnt.most_common(15):
        print(f"{w}: {ile}")


if __name__ == "__main__":
    main()
