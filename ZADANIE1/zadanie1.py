def dodaj_element(structure):
    # 1. Znajdź maksymalny poziom zagnieżdżenia list
    depths = []

    def find_depths(obj, depth):
        if isinstance(obj, list):
            depths.append(depth)
            for el in obj:
                if isinstance(el, (list, tuple, dict)):
                    find_depths(el, depth + 1)
        elif isinstance(obj, tuple):
            for el in obj:
                if isinstance(el, (list, tuple, dict)):
                    find_depths(el, depth + 1)
        elif isinstance(obj, dict):
            for val in obj.values():
                if isinstance(val, (list, tuple, dict)):
                    find_depths(val, depth + 1)

    find_depths(structure, 0)

    if not depths:
        return structure

    max_depth = max(depths)

    # 2. Rekurencyjnie dodawaj elementy tylko do list o maksymalnym poziomie
    def process(obj, depth):
        if isinstance(obj, list):
            new_list = []
            for el in obj:
                if isinstance(el, (list, tuple, dict)):
                    new_list.append(process(el, depth + 1))
                else:
                    new_list.append(el)

            # jeśli to jest lista na maksymalnym poziomie — dodaj nowy element
            if depth == max_depth:
                new_list.append(len(new_list) + 1)

            return new_list

        elif isinstance(obj, tuple):
            new_tuple = []
            for el in obj:
                if isinstance(el, (list, tuple, dict)):
                    new_tuple.append(process(el, depth + 1))
                else:
                    new_tuple.append(el)
            return tuple(new_tuple)

        elif isinstance(obj, dict):
            new_dict = {}
            for k, v in obj.items():
                if isinstance(v, (list, tuple, dict)):
                    new_dict[k] = process(v, depth + 1)
                else:
                    new_dict[k] = v
            return new_dict

        return obj

    return process(structure, 0)
