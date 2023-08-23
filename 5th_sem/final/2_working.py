import pyfirmata
import time
import datetime
board=pyfirmata.Arduino("COM3")
val = pyfirmata.util.Iterator(board)
val.start()
detector1 = board.get_pin('a:0:i')
detector2 = board.get_pin('a:1:i')
detector3 = board.get_pin('a:2:i')
detector4 = board.get_pin('a:3:i')
flag1="in out"
count=0
while 1:
    first=detector1.read()
    second=detector2.read()
    if count==0:
        if "in" in flag1:
            if first!=None and first<0.2:
                flag1="in"
                count+=1
    else:
        flag1="in out"
        count=0
    if count==0:
        if "out" in flag1:
            if second!= None and second<0.2:
                flag1="out"
                count+=1
            else:
                flag1="in out"
                count=0
    if count==1:
        print(flag1)
    time.sleep(1)

