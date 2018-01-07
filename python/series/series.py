def slices(series, length):
    if length == 0:
        raise ValueError("Cannot have zero-length slices")
    if length > len(series):
        raise ValueError("Length longer than input series")

    substrings = [series[i:i + length] for i in range(len(series))]
    return [list(map(lambda y: int(y), s)) for s in substrings
            if len(s) == length]
