import pymysql
connection = pymysql.connect(host='localhost', user='root',password='Chinnu@123',database='pbl',autocommit=True)
cur = connection.cursor()

count=10
loc="'circle'"
cur.execute(f"update data set count = {count} where location={loc};")
cur.execute("select * from data;")
x=cur.fetchall()
for i in x:
    print(i)