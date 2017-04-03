def is_leap_year(year):
    return year % 4 == 0 and year % 400 not in [100, 200, 300]
