"""
Print working days/hours until current date.


USAGE:

$ python main.py
"""
from datetime import date
from datetime import datetime
from datetime import timedelta
import calendar

from pandas.tseries.offsets import BDay
import pandas as pd


# 1 January New Year's Day	Capodanno
# 6 January	Epiphany	Epifania
# A Sunday in spring	Easter	Pasqua
# Monday after Easter	Easter Monday	Lunedì dell'Angelo, Lunedì in Albis or more commonly Pasquetta
# 25 April	Liberation Day	Festa della Liberazione	Liberation of Italy from Nazi Germany, 1945
# 1 May	International Workers' Day	Festa del Lavoro (or Festa dei Lavoratori)
# 2 June	Republic Day	Festa della Repubblica	Birth of the Italian Republic, 1946
# 15 August	Ferragosto/Assumption Day	Ferragosto or Assunzione
# 1 November	All Saints' Day	Tutti i santi (or Ognissanti)
# 8 December	Immaculate Conception	Immacolata Concezione (or just Immacolata)
# 25 December	Christmas Day	Natale
# 26 December	St. Stephen's Day
FESTIVITA_NAZIONALI_ITALIANE = [
    '01-01',  # New Year's Day
    '01-06',  # Epiphany
    '04-25',  # Liberation Day
    '05-01',  # International Workers' Day
    '06-02',  # Republic Day
    '08-15',  # Assumption Day
    '11-01',  # All saints's day
    '12-08',  # Immaculate Conception
    '12-25',  # Christmas
    '12-26',  # St. Stephen's Day
]

HOURS_PER_DAY = 6


def calc_easter(year):
    """
    Returns Easter as a tuple (year, month, day)
    """
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    return date(year, month, day)


def working_days_until(year, month, end_day):
    working_days = []

    easter = calc_easter(year)
    easter_monday = easter + timedelta(1)
    festivi = FESTIVITA_NAZIONALI_ITALIANE + \
        ['{:02d}-{:02d}'.format(x.month, x.day) for x in (easter, easter_monday)]
    festivi.sort()

    _, month_end = calendar.monthrange(year, month)
    business_days = pd.date_range(
        '{yyyy}-{mm:02d}-01'.format(yyyy=year, mm=month),
        '{yyyy}-{mm:02d}-{end:02d}'.format(yyyy=year, mm=month, end=month_end),
        freq=BDay()
    )

    for bday in business_days:
        if bday.isoformat()[5:10] in festivi:
            continue
        working_days.append(bday)

    return working_days


def main():
    working_days = working_days_until(*datetime.today().timetuple()[:3])
    for i, wd in enumerate(working_days, 1):
        is_today = wd.isoformat()[:10] == datetime.today().isoformat()[:10]
        row = '{d}\t{i}\t{h}'.format(d=wd.isoformat()[:10], i=i, h=i * HOURS_PER_DAY)
        if is_today:
            row += ' <'
        print(row)
    ret = len(working_days)
    print('---------------------------')
    print('MONTH TOTAL:\t{}\t{}'.format(ret, ret * HOURS_PER_DAY))


if __name__ == '__main__':
    main()
