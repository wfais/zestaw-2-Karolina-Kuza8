import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

# Funkcja rysująca wykres na podstawie eval()
def rysuj_wielomian(wejscie):
    # Wejście ma format: "funkcja, x_min x_max"
    funkcja, zakres = wejscie.split(",", 1)
    funkcja = funkcja.strip()
    x_min, x_max = map(float, zakres.split())

    # Generowanie x
    x_val = np.linspace(x_min, x_max, 200)

    # Bezpieczny eval – definiujemy tylko x
    local_dict = {"x": x_val, "np": np}
    y_val = eval(funkcja, {"__builtins__": {}}, local_dict)

    # Rysowanie wykresu
    plt.plot(x_val, y_val)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Wykres wielomianu (eval)")
    plt.grid(True)

    # Zwracamy wartości brzegowe
    return float(y_val[0]), float(y_val[-1])


# Funkcja rysująca wykres na podstawie SymPy
def rysuj_wielomian_sympy(wejscie):
    funkcja, zakres = wejscie.split(",", 1)
    funkcja = funkcja.strip()
    x_min, x_max = map(float, zakres.split())

    x = symbols('x')
    wzor = sympify(funkcja)

    # Zamiana na funkcję numeryczną
    f_num = lambdify(x, wzor, 'numpy')

    # Generowanie x
    x_val = np.linspace(x_min, x_max, 200)
    y_val_sympy = f_num(x_val)

    # Rysowanie wykresu
    plt.plot(x_val, y_val_sympy)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Wykres funkcji (SymPy)")
    plt.grid(True)

    return float(y_val_sympy[0]), float(y_val_sympy[-1])


if __name__ == '__main__':
    wejscie1 = "x**3 + 3*x + 1, -10 10"
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)

    wejscie2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Wynik (SymPy):", wynik_sympy)

    plt.show()
    