def dodaj_element(structure):
    """
    Funkcja znajduje wszystkie najgłębsze listy i dodaje do nich element:
    - 1 + max(lista)
    - lub 1 jeśli lista jest pusta
    """

    # Najpierw ustalamy maksymalną głębokość dowolnej listy

    def find_max_depth(x, depth=0):
        max_d = depth
        if isinstance(x, list):
            for el in x:
                max_d = max(max_d, find_max_depth(el, depth + 1))
        elif isinstance(x, dict):
            for el in x.values():
                max_d = max(max_d, find_max_depth(el, depth + 1))
        elif isinstance(x, tuple):
            for el in x:
                max_d = max(max_d, find_max_depth(el, depth + 1))
        return max_d

    max_depth = find_max_depth(structure)

    # Teraz modyfikujemy TYLKO listy na max_depth

    def process(x, depth=0):
        if isinstance(x, list):
            new = []
            for el in x:
                new.append(process(el, depth + 1))

            # jeśli ta lista jest NAJGŁĘBSZA
            if depth == max_depth:
                if new:  # niepusta
                    new.append(max(new) + 1)
                else:    # pusta
                    new.append(1)

            return new

        elif isinstance(x, dict):
            return {k: process(v, depth + 1) for k, v in x.items()}

        elif isinstance(x, tuple):
            return tuple(process(el, depth + 1) for el in x)

        return x  # typ prosty

    return process(structure)
