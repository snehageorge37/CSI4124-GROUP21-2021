#pip3 install psycopg2

import psycopg2
import csv

con = psycopg2.connect(database="group_21", user="sgeor006", password="******", host="www.eecs.uottawa.ca",
                       port="15432")

print("Database opened successfully")

with open('mobility_dimension.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        line_count += 1
        cur = con.cursor()
        query_format = "INSERT INTO mobility (mobility_id,metro_area,sub_region,retail_and_rec,grocery_and_pharma,parks,transit_stations,workplaces,residential,date) VALUES ({}, '{}', '{}', {}, {}, {}, {},{}, {}, '{}')".format(row[1], row[3], row[2], row[5], row[6], row[7], row[8], row[9], row[10], row[4])
        cur.execute(query_format)
        con.commit()
con.close()
print("Database closed successfully")
