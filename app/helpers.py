# -*- coding: UTF-8 -*-


def parse_date(date):
    months = {
              'Январь': 1,
              'Февраль': 2,
              'Март': 3,
              'Апрель': 4,
              'Май': 5,
              'Июнь': 6,
              'Июль': 7,
              'Август': 8,
              'Сентябрь': 9,
              'Октябрь': 10,
              'Ноябрь': 11,
              'Декабрь': 12
              }
    try:
        date = date.split()
        str_month = date[1]
        int_month = months[str_month]
        date[1] = str(int_month)
        date[0], date[2] = date[2], date[0]
        formatted_date = '-'.join(date)
        return str(formatted_date)
    except:
        return None

