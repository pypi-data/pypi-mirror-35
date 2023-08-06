# -------------------------------------------------------------------------
# EQUINOX
# Python time utility helper methods.
# -------------------------------------------------------------------------
from datetime import datetime, date
from typing import List

DB_DATE_FORMAT = '%Y-%m-%d'
DB_TIME_FORMAT = '%H-%M-%S'
DB_DATETIME_FORMAT = '%Y-%m-%d %H-%M-%S'

def now() -> datetime:
    return datetime.utcnow()


def today() -> date:
    return now().date()


def now_timestamp() -> str:
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


def convert_date_id_to_date(date_id):
    return datetime.strptime(str(date_id), "%Y%m%d").date()


def convert_date_to_id(date):
    return date.year * 10000 + date.month * 100 + date.day


def create_monthly_date_ranges(date_from, date_to) -> List[List[date]]:
    date_from = convert_date_id_to_date(date_from)
    date_to = convert_date_id_to_date(date_to)

    if date_from >= date_to:
        raise ValueError("date_from must be chronologically before date_to.")

    curr_month = date_from.month
    date_ranges = []
    curr_date = date(date_from.year, date_from.month, date_from.day)

    while curr_date < date_to:
        if curr_date.month < 12:
            next_month = curr_date.month + 1
            next_year = curr_date.year
        else:
            next_month = 1
            next_year = curr_date.year + 1

        next_date = date(next_year, next_month, 1)
        if next_date > date_to:
            next_date = date_to

        date_ranges.append([curr_date, next_date])
        curr_date = date(next_date.year, next_date.month, next_date.day)

    return date_ranges
