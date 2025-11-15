def dodaj_element(wejscie):
    max_depth = 0
    deepest_items = []
    
    def find_deepest(items, depth=0):
        nonlocal max_depth, deepest_items
        
        if isinstance(items, list):
            if depth > max_depth:
                max_depth = depth
                deepest_items = [items]
            elif depth == max_depth:
                deepest_items.append(items)
            
            for item in items:
                find_deepest(item, depth + 1)
                
        elif isinstance(items, tuple):
            for item in items:
                find_deepest(item, depth + 1)
                
        elif isinstance(items, dict):
            for value in items.values():
                find_deepest(value, depth + 1)
    
    def add_to_deepest(items, depth=0):
        nonlocal max_depth
        
        if isinstance(items, list):
            if depth == max_depth:
                if items not in added_items:
                    items.append(next_value)
                    added_items.add(id(items))
                return
            
            for item in items:
                add_to_deepest(item, depth + 1)
                
        elif isinstance(items, tuple):
            for item in items:
                add_to_deepest(item, depth + 1)
                
        elif isinstance(items, dict):
            for value in items.values():
                add_to_deepest(value, depth + 1)
    
    # Znajdź najgłębsze zagnieżdżenie
    find_deepest(wejscie)
    
    # Jeśli nie ma żadnych list, dodaj na końcu głównej listy
    if max_depth == 0:
        if isinstance(wejscie, list):
            return wejscie + [1]
        return wejscie
    
    # Oblicz następną wartość do dodania
    next_value = max_depth + 1
    
    # Dodaj element do najgłębszych list
    added_items = set()
    add_to_deepest(wejscie)
    
    return wejscie

if __name__ == '__main__':
    input_list = [
        1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
        "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(output_list)