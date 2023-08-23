import yagmail
import pymysql
yag = yagmail.SMTP("Tryingout64@gmail.com","raelgzgecldyogle")
'''connection = pymysql.connect(host='localhost', user='root',password='Chinnu@123',database='pbl',autocommit=True)
cur = connection.cursor()
entered = bool(input('1 for true or 0 for false'))
loc="'circle'"
cur.execute("select count from data where location='loc';")
rows=cur.fetchall()
for i in rows:
    for j in i:
     val=j
     if entered:
        val+=1
        cur.execute(f"update data set count={val} where location={loc};")
    else:
        val-=1
        cur.execute(f"update data set count={val} where location={loc};")
cur.execute(f"select * from data;")
for i in cur.fetchall():
    print(i)'''
message = 'ALert!! found an animal entered at position {}'.format(1)
yag.send("shashwatkr0@gmail.com","first",message)
print("message successfully sent")