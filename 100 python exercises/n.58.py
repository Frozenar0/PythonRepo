#convert a date of birth into lived days
from datetime import datetime, date


def findDays(y,m,d):
    d0 = date(y, m, d)
    d1 = date.today()
    delta = d1 - d0
    print(delta.days)

findDays(1991, 4, 21)
