# sugar_plotting.py
"""
Sugar Tracking / Plotting program
Data file format:
lines: dd mmmm ddd ddd
Examples:
26 July 109 231
17 Aug 110 149

day of month: decimal 1-31
Month: aaaa
morning value: decimal
eavining: decimal
comments: #....
Ignore anything else
"""
import re
import statistics
from matplotlib import pyplot as plt

list_input = True       # True - list input
list_input = False
list_data = True        # True - list data
list_data = False
data_file = "sugar_01.data"
morning_low = None      # low moring value
morning_high = None     # high morning value
morning_sum = 0         # Sum of morning values
evening_low = None      # low evening value
evening_high = None     # high evening value
evening_sum = 0         # Sum of evening values
data_count = 0          # Count of measured days
morning_values = []       # list of morning values

evening_values = []       # list of evening values
class Smeasure:
    def __init__(self, dayno=0, date=None,
               mtype=None,
               value=None):
        self.dayno = dayno  # day from beginning
        self.date = date    # string ddmmmyyyy
        self.mtype = mtype    # 'm'- morning, 'e'-evening
        self.value = value
smeasures = []    
comment_pat = re.compile(r"^(.*)#.*")
blank_line_pat = re.compile(r'\s*$')
line_pat = re.compile(r"^\s*(\d\d)\s+([a-z]+)"
                      r"\s+(\S+)\s+(\d+)",
                      re.I)
line_no = 0
morning_value = 0     # Initialize incase missing
evening_value = 0
with open(data_file) as finp:
    for line in finp:
        line = line[:-1]
        line_no += 1
        if list_input:
            print(f"{line_no:4} {line}")
        res = comment_pat.match(line)
        if res is not None:
            line = result.group(1)
        if blank_line_pat.match(line) is not None:
            continue        # Ignore blank lines
        if re.match(r'\d+$', line):
            year = int(line)    # New current year
        
        res = line_pat.match(line)
        if res is  None:
            continue        # Ignore if not likely
        
        mth_day = int(res.group(1))
        mth_name = res.group(2)
        morning_val = res.group(3)
        if morning_val == "?" or morning_val == "night":
            pass        # Use previous morning
        else:
            morning_value  = int(morning_val)
            
        evening_val = res.group(4)
        if evening_val is None or evening_val == "?":
            pass        # Use previous evening
        else:
            evening_value = int(evening_val)
        if list_data:
            print(f"{mth_name} {mth_day} {morning_value} {evening_value}")
        data_count += 1
        sme = Smeasure(dayno=data_count,
                       date=f"{mth_day:02}{mth_name}{year:4d}",
                       mtype='m',
                       value=morning_value)
        smeasures.append(sme)              
        sme = Smeasure(dayno=data_count,
                       date=f"{mth_day:02}{mth_name}{year:4d}",
                       mtype='e',
                       value=evening_value)
        smeasures.append(sme)              
        morning_sum += morning_value
        if morning_low is None or morning_value < morning_low:
            if morning_value > 0:
                morning_low = morning_value
        if morning_high is None or morning_value > morning_high:
            morning_high = morning_value
        morning_values.append(morning_value)
        evening_sum += evening_value
        evening_values.append(evening_value)
        if evening_low is None or evening_value < evening_low:
            evening_low = evening_value
        if evening_high is None or evening_value > evening_high:
            evening_high = evening_value
            
print(f"Number of days: {data_count}")
morning_median = statistics.median(morning_values) if len(morning_values) > 0 else 0

morning_avg = morning_sum/data_count if data_count > 0 else 0
print(f"Morning low: {morning_low:3}   high: {morning_high:3}"
      f"   avg: {morning_avg:5.1f}   median: {morning_median:5.1f}")

evening_median = statistics.median(evening_values) if len(evening_values) > 0 else 0
evening_avg = evening_sum/data_count if data_count > 0 else 0
print(f"Evening low: {evening_low:3}   high: {evening_high:3}"
      f"   avg: {evening_avg:5.1f}   median: {evening_median:5.1f}")

day_nos = [i for i in range(1, len(morning_values)+1)]
plt.xlabel('Day number')
plt.ylabel('Measurements')
plt.plot(day_nos, len(evening_values)*[150], c='red')
# Out of bounds evening values
ev_hi = 150
ev_low = 80
ev_ob = []  # values
ev_ob_days = []  # days
ev_ib = []  # values
ev_ib_days = []  # days
for sme in smeasures:
    if sme.mtype == 'e':
        if sme.value > ev_hi or sme.value < ev_low:
            ev_ob.append(sme.value)
            ev_ob_days.append(sme.dayno)
        else:
            ev_ib.append(sme.value)
            ev_ib_days.append(sme.dayno)
plt.scatter(ev_ob_days, ev_ob, marker='x', label="ev ob", c='red')
plt.scatter(ev_ib_days, ev_ib, marker='.', label="ev in", c='purple')

###plt.scatter(day_nos, evening_values, marker='.', label="evening", c='purple')

mo_hi = 120
mo_low = 80
mo_ob = []  # values
mo_ob_days = []  # days
mo_ib = []  # values
mo_ib_days = []  # days
plt.plot(day_nos, len(morning_values)*[mo_low], c='gray')
plt.plot(day_nos, len(morning_values)*[mo_hi], c='gray')

for sme in smeasures:
    if sme.mtype == 'm':
        if sme.value > mo_hi or sme.value < mo_low:
            mo_ob.append(sme.value)
            mo_ob_days.append(sme.dayno)
        else:
            mo_ib.append(sme.value)
            mo_ib_days.append(sme.dayno)
plt.scatter(mo_ob_days, mo_ob, marker='x', label="morn ob", c='pink')
plt.scatter(mo_ib_days, mo_ib, marker='.', label="morn in", c='blue')



###plt.scatter(day_nos, morning_values, marker='o', label="morning", c='blue')
plt.legend()

plt.show()
