def dodaj_element(wejscie):

    # Tu szukamy maksymalnej głębokości LIST, nie całej struktury
    def znajdz_maks_list(x, poziom=0):
        max_g = -1  # -1 oznacza: jeszcze nie znaleziono żadnej listy na tym poziomie

        if isinstance(x, list):
            # znaleźliśmy listę – aktualny poziom jest ważny
            max_g = poziom
            for el in x:
                max_g = max(max_g, znajdz_maks_list(el, poziom + 1))

        elif isinstance(x, tuple):
            # tuple tylko przenosi zagłębienie dalej
            for el in x:
                max_g = max(max_g, znajdz_maks_list(el, poziom + 1))

        elif isinstance(x, dict):
            # wartości słownika też są zagłębione
            for v in x.values():
                max_g = max(max_g, znajdz_maks_list(v, poziom + 1))

        return max_g

    maks = znajdz_maks_list(wejscie)

    # specjalny przypadek: nie znaleziono ŻADNYCH list zagnieżdżonych
    if maks == -1:
        wejscie.append(len(wejscie) + 1)
        return wejscie

    # Dodajemy element do list na poziomie maksymalnym
    def dodaj(x, poziom=0):
        if isinstance(x, list):
            if poziom == maks:
                x.append(len(x) + 1)
            else:
                for el in x:
                    dodaj(el, poziom + 1)

        elif isinstance(x, tuple):
            for el in x:
                dodaj(el, poziom + 1)

        elif isinstance(x, dict):
            for v in x.values():
                dodaj(v, poziom + 1)

    dodaj(wejscie)
    return wejscie


if __name__ == '__main__':
    input_list = [
     1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
     "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(input_list)
