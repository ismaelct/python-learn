import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='php.glez.cloud', user='root', password='root', port=3306)

with connection.cursor() as cursor:
    # Read a single record
    sql = "use sys"
    cursor.execute(sql)
    sql = "SELECT * FROM user_summary"
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
