def dodaj_element(wejscie):

    # znajdowanie maksymalnej głębokości zagnieżdżeń LIST
    def max_glebokosc(x, poziom=1):
        max_g = poziom
        if isinstance(x, list):
            for e in x:
                g = max_glebokosc(e, poziom + 1)
                if g > max_g:
                    max_g = g
        elif isinstance(x, tuple):
            for e in x:
                g = max_glebokosc(e, poziom + 1)
                if g > max_g:
                    max_g = g
        elif isinstance(x, dict):
            for v in x.values():
                g = max_glebokosc(v, poziom + 1)
                if g > max_g:
                    max_g = g
        return max_g

    maks = max_glebokosc(wejscie)

    # dodawanie elementu do list na maksymalnej głębokości
    def dodaj(x, poziom=1):
        if isinstance(x, list):
            if poziom == maks:
                x.append(len(x) + 1)
            else:
                for i in range(len(x)):
                    x[i] = dodaj(x[i], poziom + 1)
            return x

        elif isinstance(x, tuple):
            nowa = []
            for e in x:
                nowa.append(dodaj(e, poziom + 1))
            return tuple(nowa)

        elif isinstance(x, dict):
            for k in x:
                x[k] = dodaj(x[k], poziom + 1)
            return x

        return x

    return dodaj(wejscie)
