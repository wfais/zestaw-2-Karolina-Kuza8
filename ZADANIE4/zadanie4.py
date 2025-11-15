import os
import time
import threading
import sys

# Stałe konfiguracyjne
LICZBA_KROKOW = 80_000_000
LICZBA_WATKOW = sorted({1, 2, 4, os.cpu_count() or 4})


def policz_fragment_pi(pocz: int, kon: int, krok: float, wyniki: list[float], indeks: int) -> None:
    """Oblicza część sumy przybliżenia liczby pi metodą prostokątów."""
    suma = 0.0
    for i in range(pocz, kon):
        x = (i + 0.5) * krok
        suma += 4.0 / (1.0 + x * x)
    wyniki[indeks] = suma


def main():
    print(f"Python: {sys.version.split()[0]}  "
          f"(tryb bez GIL? {getattr(sys, '_is_gil_enabled', lambda: None)() is False})")
    print(f"Liczba rdzeni logicznych CPU: {os.cpu_count()}")
    print(f"LICZBA_KROKOW: {LICZBA_KROKOW:,}\n")

    krok = 1.0 / LICZBA_KROKOW

    # Wstępne uruchomienie w celu stabilizacji środowiska wykonawczego
    wyniki = [0.0]
    w = threading.Thread(target=policz_fragment_pi, args=(0, LICZBA_KROKOW, krok, wyniki, 0))
    start_time = time.perf_counter()
    w.start()
    w.join()
    czas_jednowatkowy = time.perf_counter() - start_time
    print(f"1 wątek: π ≈ {krok * wyniki[0]:.12f}, czas {czas_jednowatkowy:.4f} s")

    # Wielowątkowe obliczenia
    for n_watkow in LICZBA_WATKOW[1:]:
        wyniki = [0.0] * n_watkow
        watki = []
        # Wyznaczenie zakresów dla każdego wątku
        podstawa = LICZBA_KROKOW // n_watkow
        start_idx = 0
        zakresy = []
        for k in range(n_watkow):
            end_idx = start_idx + podstawa + (1 if k < (LICZBA_KROKOW % n_watkow) else 0)
            zakresy.append((start_idx, end_idx))
            start_idx = end_idx

        # Utworzenie wątków
        for idx, (pocz, kon) in enumerate(zakresy):
            t = threading.Thread(target=policz_fragment_pi, args=(pocz, kon, krok, wyniki, idx))
            watki.append(t)

        # Pomiar czasu
        t0 = time.perf_counter()
        for t in watki:
            t.start()
        for t in watki:
            t.join()
        t1 = time.perf_counter()

        pi_watek = krok * sum(wyniki)
        przyspieszenie = czas_jednowatkowy / (t1 - t0)
        print(f"{n_watkow} wątki: π ≈ {pi_watek:.12f}, czas {t1 - t0:.4f} s, przyspieszenie {przyspieszenie:.2f}x")


if __name__ == "__main__":
    main()
