from collections import Iterable


def flatten(iterable):
    flat_array = []
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, str):
            flat_array.extend(flatten(item))
        elif item is not None:
            flat_array.append(item)
    return flat_array
