def dodaj_element(structure):

    def process(node):
        
        # Jeśli lista:
        if isinstance(node, list):
            max_depth = 1
            contains_list = False
            new_list = []
            
            for el in node:
                new_el, depth, has_list = process(el)
                if depth + 1 > max_depth:
                    max_depth = depth + 1
                if has_list:
                    contains_list = True
                new_list.append(new_el)
            
            # Jeśli wewnątrz NIE ma list — to jest najgłębsza lista
            if not contains_list:
                new_list.append(len(new_list) + 1)

            return new_list, max_depth, True
        
        # Jeśli słownik:
        if isinstance(node, dict):
            max_depth = 0
            contains_list = False
            out = {}
            for k, v in node.items():
                new_v, depth, has_list = process(v)
                out[k] = new_v
                if depth > max_depth:
                    max_depth = depth
                if has_list:
                    contains_list = True
            return out, max_depth, contains_list
        
        # Jeśli tuple:
        if isinstance(node, tuple):
            max_depth = 0
            contains_list = False
            new_items = []
            for el in node:
                new_el, depth, has_list = process(el)
                new_items.append(new_el)
                if depth > max_depth:
                    max_depth = depth
                if has_list:
                    contains_list = True
            return tuple(new_items), max_depth, contains_list
        
        # Inne typy
        return node, 0, False

    return process(structure)[0]
