"""
Print working days/hours until current date.


USAGE:

$ python main.py
"""
from datetime import datetime
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

def working_days_until(year, month, end_day):
    working_days = []

    month_start, month_end = calendar.monthrange(year, month)
    # momth_start should be always 1, obviously
    assert month_start == 1, 'Unexpexted month start day: {}'.format(month_start)
    _, month_end = calendar.monthrange(year, month)
    business_days = pd.date_range(
        '{yyyy}-{mm:02d}-01'.format(yyyy=year, mm=month),
        '{yyyy}-{mm:02d}-{end:02d}'.format(yyyy=year, mm=month, end=month_end),
        freq=BDay()
    )

    for bday in business_days:
        if bday.isoformat()[5:10] in FESTIVITA_NAZIONALI_ITALIANE:
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
