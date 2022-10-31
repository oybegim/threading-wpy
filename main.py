import threading as th
import time
from name import *
from surname import *
from sh import *
from poll import *

t1 = th.Thread(target=ism)
t2 = th.Thread(target=familiya)
t3 = th.Thread(target=ochistva)
t4 = th.Thread(target=jinsi)

t1.start()
t2.start()
t3.start()
t4.start()  
     

