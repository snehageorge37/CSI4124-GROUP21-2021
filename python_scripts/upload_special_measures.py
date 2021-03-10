import psycopg2
import csv

def format_date(dt: str):
    splt = dt.split('-')
    return f'{splt[1]}/{splt[2]}/{splt[0]}'

con = psycopg2.connect(database="group_21", user="togun062", password="Ad6jyqyv8p", host="www.eecs.uottawa.ca",
                       port="15432")

print("Database opened successfully")

with open('special_measures.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        line_count += 1
        print(row)
        cur = con.cursor()
        query_format = "INSERT INTO special_measures_v2 (id,name,start_date,end_date,includes_toronto,includes_ottawa) VALUES " \
                       "({}, '{}', '{}', '{}', {}, {})".format(row[3], row[4], format_date(row[5]), format_date(row[6]), row[8]=='yes', row[7]=='yes')
        cur.execute(query_format)
        con.commit()
con.close()
print("Database closed successfully")
