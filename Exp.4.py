import datetime
from datetime import datetime 
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_year = now.strftime("%Y")
current_month=now.strftime("%B")
current_day = now.strftime("%a")
current_date = now.strftime("%d")
print("Todays date is:")
print("{} {} {} {} IST {}".format(current_day,current_month,current_date,current_time,current_year))
