from datetime import datetime
from datetime import date
from datetime import timedelta
today = datetime.today()
todaydate = date.today()
todaydate.month
todaydate.year
christmas = date(2020, 12, 25)
(christmas - todaydate).days
if (christmas is not todaydate):
    print("There are still " + str((christmas - todaydate).days) + " until Christmas" )
else:
    print("ok") 

t = timedelta(days=4, hours=10)
today = datetime.today()
eta = timedelta(days = 3, hours = 4)
today + t
str(today + eta)