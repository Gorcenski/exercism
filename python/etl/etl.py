from functools import reduce
def transform(legacy_data):
    return(reduce(lambda x, y: dict(x, **y),
                  [{v.lower(): key for v in value}
                   for key, value in legacy_data.items()]))
