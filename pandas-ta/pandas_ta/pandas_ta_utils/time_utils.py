import calendar
from datetime import date, timedelta, datetime
from typing import Union


def opex_date_of_month(year, month) -> date:
    first_day_of_month = date(year, month, 1)
    first_friday = first_day_of_month + timedelta(days=((4 - calendar.monthrange(year, month)[0]) + 7) % 7)
    return first_friday + timedelta(days=14)


def opex_date_of_date(d: Union[date, datetime]) -> date:
    return opex_date_of_month(d.year, d.month)
