n = [10, 13, 16, 22, 9, 4, 37]
nums = {'evens': [], 'odds': []}

for val in n:
    if val % 2 == 0:
        nums['evens'].append(val)
    else:
        nums['odds'].append(val)
print(nums)

############
numbers = '1 2 3 4 5 6 7 8'

mynum = [int(x) for x in numbers.strip().split()]

print(mynum)

############

from itertools import groupby

n = [10, 13, 16, 22, 9, 4, 37]
nums = {'evens': [], 'odds': []}

# data = sorted(n, key=nums)
for k, g in groupby(n, lambda x: x % 2):
    if k:
        nums['odds'].extend(g)
    else:
        nums['evens'].extend(g)
print(nums)

#######

import os

for root, dir, files in os.walk("."):
    path = root.split(os.sep)
    print((len(path) - 1) * '┗━', os.path.basename(root))
    for file in files:
        if file.endswith(".py"):
            print(len(path) * '┃', file)

##########


from datetime import date, timedelta


def all_sundays(year):
    # January 1st of the given year
    dt = date(year, 1, 1)
    # First Sunday of the given year
    dt += timedelta(days=6 - dt.weekday())
    while dt.year == year:
        yield dt
        dt += timedelta(days=7)


for s in all_sundays(2020):
    print(s)

import calendar

tc = calendar.TextCalendar(firstweekday=0)
# print(tc.pryear(2019))


########

import calendar

year = 2019
month = 3
day_to_count = calendar.SUNDAY

print(day_to_count)

for i in range(1, 13):
    matrix = calendar.monthcalendar(year, i)
    print(matrix)
    num_days = sum(1 for x in matrix if x[day_to_count] != 0)
    print("Number of sundays:" + str(num_days) + " Month:" + str(i))
