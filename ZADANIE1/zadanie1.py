def dodaj_element(wejscie):
   
    def znajdz_maks_glebokosc(x, poziom=0):
        max_g = poziom
        if isinstance(x, list):
            for el in x:
                max_g = max(max_g, znajdz_maks_glebokosc(el, poziom + 1))
        elif isinstance(x, tuple):
            for el in x:
                max_g = max(max_g, znajdz_maks_glebokosc(el, poziom + 1))
        elif isinstance(x, dict):
            for v in x.values():
                # wartości słownika traktujemy jak dodatkowe zagnieżdżenie
                max_g = max(max_g, znajdz_maks_glebokosc(v, poziom + 1))
        return max_g

    maks = znajdz_maks_glebokosc(wejscie)

    # Teraz dodam elementy do wszystkich list na tym poziomie
    def dodaj_w_maks(x, poziom=0):
        if isinstance(x, list):
            if poziom == maks:
                x.append(len(x) + 1)
            else:
                for el in x:
                    dodaj_w_maks(el, poziom + 1)

        elif isinstance(x, tuple):
            for el in x:
                dodaj_w_maks(el, poziom + 1)

        elif isinstance(x, dict):
            for v in x.values():
                dodaj_w_maks(v, poziom + 1)

    dodaj_w_maks(wejscie)
    return wejscie


if __name__ == '__main__':
    input_list = [
        1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
        "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(input_list)
