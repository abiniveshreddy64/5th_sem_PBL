#4 ldr code
import pyfirmata
import time
import datetime
import yagmail
import pymysql
yag = yagmail.SMTP("Tryingout64@gmail.com","raelgzgecldyogle")
connection = pymysql.connect(host='localhost', user='root',password='Chinnu@123',database='pbl',autocommit=True)
cur = connection.cursor()
table='main'
board=pyfirmata.Arduino("COM3")
val = pyfirmata.util.Iterator(board)
val.start()
detector1 = board.get_pin('a:0:i')
detector2 = board.get_pin('a:1:i')
detector3 = board.get_pin('a:2:i')
detector4 = board.get_pin('a:3:i')
flag1=flag2=''
count1=count2=0
while 1:
    cur.execute("select email from {}".format(table))
    if count1==0:
        first=detector1.read()
        if first!=None and first<0.2:
            flag1+="in"
            count1+=1
    if count1==1 and flag1=="in":
        pass
    if count1==1 and flag1!="in":
        first=detector1.read()
        if first!=None and first<0.2:
            flag1+="in"
            count1+=1
    if count1==0:
        second=detector2.read()
        if second!= None and second<0.2:
            flag1+="out"
            count1+=1
    if count1==1 and flag1=="out":
        pass
    if count1==1 and flag1!="out":
        second=detector2.read()
        if first!=None and first<0.2:
            flag1+="out"
            count1+=1
    if count1==2:
        if flag1=="inout":
            print("in")
            message = 'ALert!!! an animal has entered inside the road'
            for i in cur.fetchall():
                for j in i:
                    yag.send(j,"first",message)
            print(message)
            count1=0
            flag1=''
            time.sleep(3)
        if flag1=="outin":
            print("out")
            message = 'ALert!!! an animal has left the road'
            for i in cur.fetchall():
                for j in i:
                    yag.send(j,"first",message)
            print(message)
            count1=0
            flag1=''
            time.sleep(3) 
    elif count1==1:
        pass
    else:
        count1=0
    time.sleep(0.01)
    #hfjhgjhk
    if count2==0:
        third=detector3.read()
        if third!=None and third<0.2:
            flag2+="in"
            count2+=1
    if count2==1 and flag2=="in":
        pass
    if count2==1 and flag2!="in":
        third=detector3.read()
        if third!=None and third<0.2:
            flag2+="in"
            count2+=1
    if count2==0:
        fourth=detector4.read()
        if fourth!= None and fourth<0.2:
            flag2+="out"
            count2+=1
    if count2==1 and flag2=="out":
        pass
    if count2==1 and flag2!="out":
        fourth=detector4.read()
        if fourth!=None and fourth<0.2:
            flag2+="out"
            count2+=1
    if count2==2:
        if flag2=="inout":
            print("in","2nd")
            message = 'ALert!!! an animal has entered inside the road'
            for i in cur.fetchall():
                for j in i:
                    yag.send(j,"first",message)
            print(message)
            count2=0
            flag2=''
            time.sleep(3)
        if flag2=="outin":
            print("out","2nd")
            message = 'ALert!!! an animal has left the road'
            for i in cur.fetchall():
                for j in i:
                    yag.send(j,"first",message)
            print(message)
            count2=0
            flag2=''
            time.sleep(3) 
    elif count2==1:
        pass
    else:
        count2=0
    time.sleep(0.01)