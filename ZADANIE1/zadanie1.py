def dodaj_element(wejscie):
    def znajdz_listy(obj, poziom=0, wynik=None):
        if wynik is None:
            wynik = []
        if isinstance(obj, list):
            if not any(isinstance(el, (list, tuple, dict)) for el in obj):
                wynik.append((obj, poziom))
            for el in obj:
                znajdz_listy(el, poziom + 1, wynik)
        elif isinstance(obj, tuple):
            for el in obj:
                znajdz_listy(el, poziom + 1, wynik)
        elif isinstance(obj, dict):
            for v in obj.values():
                znajdz_listy(v, poziom + 1, wynik)
        return wynik

    listy_z_poziomem = znajdz_listy(wejscie)
    if not listy_z_poziomem:
        if isinstance(wejscie, list):
            najwiekszy = max(wejscie) if wejscie else 0
            wejscie.append(najwiekszy + 1)
        return wejscie

    max_poziom = max(poziom for _, poziom in listy_z_poziomem)
    najglebsze_listy = [lst for lst, poziom in listy_z_poziomem if poziom == max_poziom]

    for lst in najglebsze_listy:
        if lst:
            lst.append(max(lst) + 1)
        else:
            lst.append(1)
    return wejscie


if __name__ == '__main__':
    input_list = [
        1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
        "hello", 3, [4, 5], (5, (6, (1, [7, 8])))
    ]
    output_list = dodaj_element(input_list)
    print(output_list)
