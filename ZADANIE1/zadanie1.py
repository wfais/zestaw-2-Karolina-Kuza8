def dodaj_element(wejscie):

    def max_depth(obj, depth=0):
        """
        Zwraca maksymalną głębokość list w strukturze.
        """
        if isinstance(obj, list):
            d = depth
            for el in obj:
                d = max(d, max_depth(el, depth + 1))
            return d
        elif isinstance(obj, tuple):
            d = depth
            for el in obj:
                d = max(d, max_depth(el, depth + 1))
            return d
        elif isinstance(obj, dict):
            d = depth
            for v in obj.values():
                d = max(d, max_depth(v, depth + 1))
            return d
        else:
            return depth

    max_d = max_depth(wejscie)

    def add_at_depth(obj, depth=0):
        """
        Modyfikuje obiekt, dodając nowy element do list na maksymalnej głębokości.
        """
        if isinstance(obj, list):
            if depth == max_d:
                # Dodaj nowy element: len(list) + 1
                obj.append(len(obj) + 1)

            for el in obj:
                add_at_depth(el, depth + 1)

        elif isinstance(obj, tuple):
            for el in obj:
                add_at_depth(el, depth + 1)

        elif isinstance(obj, dict):
            for v in obj.values():
                add_at_depth(v, depth + 1)

    add_at_depth(wejscie)
    return wejscie


if __name__ == '__main__':
    input_list = [
        1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
        "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(output_list)
