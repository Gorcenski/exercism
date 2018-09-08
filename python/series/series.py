def slices(series, length):
    if length == 0:
        raise ValueError("Cannot have zero-length slices")
    if length > len(series):
        raise ValueError("Length longer than input series")

    return [series[i:i + length] for i in range(len(series) - length + 1)]
