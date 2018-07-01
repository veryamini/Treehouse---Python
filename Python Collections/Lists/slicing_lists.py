def first_4(items):
    return items[:4]

def first_and_last_4(items):
    new_items = items[:4] + items[len(items) - 4:]
    return new_items

def odds(items):
    return items[1::2]

def reverse_evens(items):
    if (len(items) - 1) % 2 == 0:
        return items[len(items) - 1::-2]
    else:
        return items[len(items) - 2::-2]
