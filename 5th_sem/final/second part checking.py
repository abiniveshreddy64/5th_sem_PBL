import pyfirmata
import time
import datetime
board=pyfirmata.Arduino("COM3")
val = pyfirmata.util.Iterator(board)
val.start()
detector3 = board.get_pin('a:2:i')
detector4 = board.get_pin('a:3:i')
flag2=''
count2=0
while 1:
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
            print("in")
            count2=0
            flag2=''
            time.sleep(5)
        if flag2=="outin":
            print("out")
            count2=0
            flag2=''
            time.sleep(5) 
    elif count2==1:
        pass
    else:
        count2=0
    time.sleep(0.01)
    