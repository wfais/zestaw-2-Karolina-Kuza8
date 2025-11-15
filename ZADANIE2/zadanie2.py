ROMAN_MAP = [
    ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
    ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
    ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
]

def arabskie_na_rzymskie(arabskie):
    if not isinstance(arabskie, int) or not (1 <= arabskie <= 3999):
        raise ValueError("Liczba arabska musi być całkowita w przedziale 1-3999")
    wynik = ""
    for rzym, wart in ROMAN_MAP:
        while arabskie >= wart:
            wynik += rzym
            arabskie -= wart
    return wynik

def rzymskie_na_arabskie(rzymskie):
    if not isinstance(rzymskie, str) or not rzymskie:
        raise ValueError("Liczba rzymska musi być niepustym stringiem")
    
    # Walidacja dozwolonych znaków
    if not all(c in "IVXLCDM" for c in rzymskie):
        raise ValueError("Nieprawidłowe znaki w liczbie rzymskiej")

    i = 0
    wynik = 0
    while i < len(rzymskie):
        # Sprawdzenie par znaków (odejmowanie)
        if i+1 < len(rzymskie) and rzymskie[i:i+2] in dict(ROMAN_MAP):
            wynik += dict(ROMAN_MAP)[rzymskie[i:i+2]]
            i += 2
        elif rzymskie[i] in dict(ROMAN_MAP):
            wynik += dict(ROMAN_MAP)[rzymskie[i]]
            i += 1
        else:
            raise ValueError(f"Nieprawidłowa liczba rzymska: {rzymskie}")
    
    # Dodatkowa weryfikacja: konwersja w drugą stronę powinna dać identyczny string
    if arabskie_na_rzymskie(wynik) != rzymskie:
        raise ValueError(f"Niepoprawna liczba rzymska: {rzymskie}")
    
    return wynik

if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
    except ValueError as e:
        print(e)
