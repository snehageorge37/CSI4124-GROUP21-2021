import datetime
import csv

y = 2020
m = 4
d = 1

summer_start = datetime.datetime(year=2020, month=6, day=20)
holidays = ['10/04/20', '13/04/20', '23/04/20', '18/05/20', '01/07/20']
dates = []
frame = [['id', 'day', 'month', 'year', 'season', 'isWeekend', 'isHoliday']]

counter = 0
while y <= 2020:
    while m <= 7:

        while d <= 31:
            try:
                date = datetime.datetime(year=y, month=m, day=d)
                print(date.strftime('%d/%m/%y'))
                frame.append([counter, d, m, y, 'summer' if date >= summer_start else 'spring', not date.weekday(), date.strftime('%d/%m/%y') in holidays])
                d += 1
                counter += 1
            except:
                d += 1

        d = 1
        m += 1
    y += 1


with open('dates.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in frame:
        writer.writerow(row)

