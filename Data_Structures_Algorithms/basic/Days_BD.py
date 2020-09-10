#Given your birthday and the current date, calculate your age in days. Compesate for leap days, Assume that the birthday and current date are correct dates.

days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_between_dates(birthday, current_date):
    pass
def days_between_dates(year1, month1, day1, year2, month2, day2):




birthday = {"year": 1988, "month": 9, "day": 15}
current_date = {"year": 2020, "month": 9, "day": 5}

32 0 -10

gregorian Calendar 15 oct 1582



days_between_dates(2012, 12, 7, 2012, 12, 7)
#0
days_between_dates(2012, 12, 7, 2012, 12, 8)
#1
days_between_dates(2012, 12, 8, 2012, 12, 7)
#undefined
days_between_dates(2012, 6, 29, 2013, 6, 29)
#365
days_between_dates(2012, 6, 29, 2013, 6, 31)
#undefined
