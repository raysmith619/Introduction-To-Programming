#sometime.py    24Feb2022  crs
# Some available date/time functions
import datetime
import time

print("Today is ", datetime.date.today())
print("...including time", time.asctime())

sleep_time = 5
print("Sleeping for", sleep_time, "seconds")
time.sleep(sleep_time)
print("Time's up\a")    # \a for beep
print("The time is", time.strftime("%I:%M:%S %p"))
