import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify


# Funkcja rysująca wykres na podstawie eval()
def rysuj_wielomian(wejscie):
    # wejscie ma format: "funkcja, xmin xmax"
    # przykład: "x**2 + 3*x + 1, -10 10"
    czesci = wejscie.split(",")
    wzor = czesci[0].strip()
    xmin, xmax = czesci[1].split()
    xmin = float(xmin)
    xmax = float(xmax)

    # generowanie X
    x_val = np.linspace(xmin, xmax, 200)

    # obliczanie Y przez eval
    # definiujemy x aby eval mogło go użyć
    x = x_val
    y_val = eval(wzor)

    # rysowanie wykresu
    plt.plot(x_val, y_val)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Wykres wielomianu (eval)")
    plt.grid(True)

    return y_val[0], y_val[-1]


# Funkcja rysująca wykres za pomocą SymPy
def rysuj_wielomian_sympy(wejscie):
    # dzielenie danych wejściowych
    czesci = wejscie.split(",")
    wzor_txt = czesci[0].strip()
    xmin, xmax = czesci[1].split()
    xmin = float(xmin)
    xmax = float(xmax)

    # symbol
    x = symbols('x')

    # konwersja tekstu na funkcję SymPy
    wyrazenie = sympify(wzor_txt)

    # lambdify — tworzy funkcję numeryczną
    funkcja = lambdify(x, wyrazenie, 'numpy')

    # generowanie danych
    x_val = np.linspace(xmin, xmax, 200)
    y_val_sympy = funkcja(x_val)

    # rysowanie wykresu
    plt.plot(x_val, y_val_sympy)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Wykres wielomianu (SymPy)")
    plt.grid(True)

    return y_val_sympy[0], y_val_sympy[-1]


# Kod wykonywany tylko gdy uruchamiamy plik samodzielnie
if __name__ == '__main__':

    wejscie1 = "x**3 + 3*x + 1, -10 10"
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)

    wejscie2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Wynik (SymPy):", wynik_sympy)

    plt.show()
