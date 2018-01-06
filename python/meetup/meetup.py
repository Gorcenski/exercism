from datetime import date
from calendar import monthcalendar


def meetup_day(year, month, day_of_the_week, which):
    day_of_week_map = {'Monday': 0,
                       'Tuesday': 1,
                       'Wednesday': 2,
                       'Thursday': 3,
                       'Friday': 4,
                       'Saturday': 5,
                       'Sunday': 6}

    dow = day_of_week_map[day_of_the_week]
    days = list(map(lambda x: x[dow],
                    filter(lambda x: x[dow] != 0,
                           monthcalendar(year, month))))

    if which == 'last':
        day_of_month = days[-1]
    elif which == 'teenth':
        day_of_month = list(filter(lambda x: x >= 13 and x <= 19, days))[0]
    else:
        if which == '5th' and len(days) < 5:
            raise ValueError("There are only 4 {0} in {1}-{2}"
                             .format(day_of_the_week, month, year))
        day_of_month = days[int(which[0]) - 1]

    return date(year, month, day_of_month)
