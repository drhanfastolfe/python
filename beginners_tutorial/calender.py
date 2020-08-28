import calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2019, 3))

print(calendar.monthcalendar(2019, 3))

print(calendar.calendar(2019))

day_of_week = calendar.weekday(2019, 3, 8)
print(day_of_week)
print()

is_leap = calendar.isleap(2019)
print(is_leap)
print()

is_leap = calendar.isleap(2020)
print(is_leap)

how_many_leap_days = calendar.leapdays(2000, 2021)
print(how_many_leap_days)
