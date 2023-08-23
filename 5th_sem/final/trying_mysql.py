import pymysql
import time
connection = pymysql.connect(host='localhost', user='root',password='Chinnu@123',database='pbl',autocommit=True)
cur = connection.cursor()
cur.execute("select email from main;")
for j in cur.fetchall():
    for k in j:
        print(k)
        time.sleep(5)