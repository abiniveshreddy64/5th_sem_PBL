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
def in_or_out(a,b):
    if a[0]<b[0]:
        return "in"
    elif a[0]>b[0]:
        return "out"
    else:
        if a[1]<b[1]:
            return "in"
        elif a[1]>b[1]:
            return "out"
        else:
            if a[1]<b[1]:
                return "in"
            elif a[1]>b[1]:
                return "out"
            else:
                if a[2]<b[2]:
                    return "in"
                elif a[2]>b[2]:
                    return "out"
                return "nothing"
flag1='first second'
flag2='thrid fourth'
for i in range(0,500):#while loop
    first=detector1.read()
    second=detector2.read()
    third=detector3.read()
    fourth=detector4.read()
    if flag1 in 'second':
        if first!=None and first<0.2:
            times=datetime.datetime.now()
            val1=[times.minute,times.second, times.microsecond, time.time_ns()]
            flag1="first"
            continue
            print(val1)
        else:
            flag1="first second"
    if flag1 in 'first':
        if second!= None and second<0.2:
            times=datetime.datetime.now()
            val2=[times.minute,times.second, times.microsecond, time.time_ns()]
            flag2="second"
            continue
            print(val2)
        else:
            flag2="first second"
    if flag2=='fourth' or flag2=='start':
        if third != None and third<0.2:
            times=datetime.datetime.now()
            val3=[times.minute,times.second, times.microsecond, time.time_ns()]
            flag3="detected"
        else:
            flag3="light_reaching"
    '''if flag2=='third' or flag2=='start':
        if fourth!=None and fourth<0.2:
            times=datetime.datetime.now()
            val4=[times.minute,times.second, times.microsecond, time.time_ns()]
            flag4="detected"
        else:
           flag4="light_reaching"
    if flag1!="light_reaching" and flag2!='light_reaching':
        print(in_or_out(val1,val2))
        flag1='light_reaching'
        flag2='light_reaching''''
    '''if flag3!="light_reaching" or flag4!='light_reaching':
        print(in_or_out(val3,val4))'''
    message = 'ALert!! found an animal entered at position {}'.format(1)
    yag.send("shashwatkr0@gmail.com","first",message)
    print("message successfully sent")
    #time.sleep(0.1)
