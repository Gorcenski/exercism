def sieve(limit):
    nums = range(2, limit + 1)
    for n in nums:
        nums = [x if ((x % n != 0) or (x <= n)) else 0 for x in nums]

    return list(filter(lambda x: x > 0, nums))