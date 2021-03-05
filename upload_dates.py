import psycopg2
import csv

con = psycopg2.connect(database="group_21", user="togun062", password="********", host="www.eecs.uottawa.ca",
                       port="15432")

print("Database opened successfully")

with open('dates.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        line_count += 1
        cur = con.cursor()
        query_format = "INSERT INTO date (id,day,month,year,season,is_weekend,is_holiday) VALUES " \
                       "({}, {}, {}, {}, '{}', {}, {})".format(row[0], row[1], row[2], row[3], row[4], row[5].upper(), row[6].upper())
        cur.execute(query_format)
        con.commit()
con.close()
print("Database closed successfully")
