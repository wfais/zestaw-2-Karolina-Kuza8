def dodaj_element(wejscie):
    # funkcja która znajdzie maksymalną głębokość
    def znajdz_glebokosc(x, poziom=1):
        max_g = poziom
        if isinstance(x, list) or isinstance(x, tuple):
            for e in x:
                g = znajdz_glebokosc(e, poziom + 1)
                if g > max_g:
                    max_g = g
        elif isinstance(x, dict):
            for v in x.values():
                g = znajdz_glebokosc(v, poziom + 1)
                if g > max_g:
                    max_g = g
        return max_g

    # funkcja która doda elementy w najbardziej zagłębionych listach
    def dodaj(x, poziom, maks):
        if isinstance(x, list):
            # jeśli to najbardziej zagnieżdżona lista → dodaj element
            if poziom == maks:
                # wartość to po prostu kolejny numer (długość + 1)
                x.append(len(x) + 1)
            else:
                for i in range(len(x)):
                    x[i] = dodaj(x[i], poziom + 1, maks)
        elif isinstance(x, tuple):
            # krotki nie można zmieniać, więc tworzę nową
            nowa = []
            for e in x:
                nowa.append(dodaj(e, poziom + 1, maks))
            return tuple(nowa)
        elif isinstance(x, dict):
            for k in x:
                x[k] = dodaj(x[k], poziom + 1, maks)
        return x

    maks_gleb = znajdz_glebokosc(wejscie)
    return dodaj(wejscie, 1, maks_gleb)


if __name__ == '__main__':
    input_list = [
        1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
        "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(input_list)
