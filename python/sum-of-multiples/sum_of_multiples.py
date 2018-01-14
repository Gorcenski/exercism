def sum_of_multiples(limit, multiples):
    return sum([x for x in range(1, limit)
                if not all([x % y for y in multiples])])
