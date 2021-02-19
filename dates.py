import datetime
import csv

y = 2020
m = 4
d = 1

holidays = ['10/04/2020', '18/05/2020', '01/07/2020']
dates = []
frame = [['id', 'day', 'month','year', 'season', 'isWeekend', 'isHoliday']]

counter = 0
while y <= 2020:
    while m <= 7:

        while d <= 31:
            try:
                date = datetime.datetime(year=y, month=m, day=d)
                frame.append([counter, d, m, y, 'summer', not date.weekday(), date.strftime('%d/%m/%y') in holidays])
                d += 1
                counter += 1
            except:
                d += 1

        d = 1
        m += 1
        print('done')
    y += 1
print(frame)


with open('dates.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in frame:
        writer.writerow(row)

