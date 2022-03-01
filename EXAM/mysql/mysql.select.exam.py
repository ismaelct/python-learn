#!/usr/bin/python3

import mysql.connector

try:
    connection = mysql.connector.connect(host='192.168.0.17',
                                         database='employees',
                                         user='root',
                                         password='root')

    sql_select_Query = "select * from employees limit 3;"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("emp_no = ", row[0], )
        print("emp_no = ", row[1])
        print("first_name  = ", row[2])
        print("last_name  = ", row[3])
        print("gender = ", row[4])
        print("hire_date = ", row[5], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")