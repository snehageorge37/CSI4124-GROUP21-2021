import pandas as pd
# import sklearn
import matplotlib.pyplot as plt
import psycopg2

fact_table_cols = [('Individual_Key', 'Resolved', 'Fatal', 'Special_Measure_Key', 'PHU_Key', 'Weather_Key', 'Onset_Date_Key', 'Reported_Date_Key', 'Test_Date_Key', 'Specimen_Date_Key')]
individual_cols = [('surrogate_key', 'individual_id', 'date', 'age_group', 'gender', 'cause_of_infection', 'outbreak_related', 'reporting_phu_city')]
fact_table = []
individual_table = []

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        return psycopg2.connect(
            host="www.eecs.uottawa.ca",
            database="group_21",
            user="****",
            password="****",
            port="15432"
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


connection = connect()
print('conection established')

cur = connection.cursor()
        
# execute a statement
cur.execute('SELECT * FROM fact_table_v2')
rows = cur.fetchall()
fact_table = fact_table_cols + rows
print(fact_table[:10])


print("\n\n")


cur.execute('SELECT * FROM individuals')
rows = cur.fetchall()
individual_table = individual_cols + rows
print(individual_table[:10])

cur.close()
connection.close()
print('connection terminated')
