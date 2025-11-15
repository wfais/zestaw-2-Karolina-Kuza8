def rzymskie_na_arabskie(rzymskie):
    if not isinstance(rzymskie, str):
        raise ValueError("Liczba rzymska musi być łańcuchem znaków.")

    rzymskie = rzymskie.upper()

    wartości = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    # sprawdzenie poprawności znaków
    for ch in rzymskie:
        if ch not in wartości:
            raise ValueError(f"Niepoprawny znak w liczbie rzymskiej: {ch}")

    # niedozwolone powtórzenia
    niedozwolone = ["IIII", "VV", "LL", "DD"]
    for nd in niedozwolone:
        if nd in rzymskie:
            raise ValueError("Niepoprawny format liczby rzymskiej.")

    # dozwolone odejmowania
    dozwolone_pary = {"IV", "IX", "XL", "XC", "CD", "CM"}

    i = 0
    wynik = 0
    while i < len(rzymskie):
        # sprawdzamy parę odejmującą
        if i + 1 < len(rzymskie):
            para = rzymskie[i] + rzymskie[i+1]
            if para in dozwolone_pary:
                wynik += wartości[rzymskie[i+1]] - wartości[rzymskie[i]]
                i += 2
                continue

            # niedozwolone odejmowanie typu IC, XM, IL itd.
            if wartości[rzymskie[i]] < wartości[rzymskie[i+1]]:
                raise ValueError("Niepoprawny format liczby rzymskiej.")

        wynik += wartości[rzymskie[i]]
        i += 1

    if not (1 <= wynik <= 3999):
        raise ValueError("Wynik poza zakresem 1-3999.")

    return wynik


def arabskie_na_rzymskie(arabskie):
    if not isinstance(arabskie, int):
        raise ValueError("Liczba arabska musi być typu int.")

    if not (1 <= arabskie <= 3999):
        raise ValueError("Liczba musi być w zakresie 1–3999.")

    mapowanie = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    wynik = ""
    for wartość, symbol in mapowanie:
        while arabskie >= wartość:
            wynik += symbol
            arabskie -= wartość

    return wynik


if __name__ == '__main__':
    try:
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")

        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")

    except ValueError as e:
        print(e)
