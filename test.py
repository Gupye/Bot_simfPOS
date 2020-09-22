import datetime as dt
from datetime import timedelta
from time import sleep

n1=dt.datetime.now()
sleep(2)
n2=dt.datetime.now()

print((n2-n1).total_seconds())
