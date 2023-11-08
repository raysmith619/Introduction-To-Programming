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
line_pat = re.compile(r"^\s*(\d\d)\s+([a-z]+)"
                      r"\s+(\d+)\s+(\d+)",
                      re.I)
line_no = 0
with open(data_file) as finp:
    for line in finp:
        line = line[:-1]
        line_no += 1
        if list_input:
            print(f"{line_no:4} {line}")
        result = line_pat.match(line)
        if result is None:
            continue

        mth_day = int(result.group(1))
        mth_name = result.group(2)
        morning_value = int(result.group(3))
        evening_value = int(result.group(4))
        if list_data:
            print(f"{mth_name} {mth_day} {morning_value} {evening_value}")
        data_count += 1
        morning_sum += morning_value
        if morning_low is None or morning_value < morning_low:
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

day_nos = [i for i in range(len(morning_values))]
plt.xlabel('Day number')
plt.ylabel('Measurements')
plt.plot(day_nos, len(evening_values)*[150], c='red')
plt.scatter(day_nos, evening_values, marker='.', label="evening", c='orange')

plt.plot(day_nos, len(morning_values)*[80], c='gray')
plt.plot(day_nos, len(morning_values)*[120], c='gray')
plt.scatter(day_nos, morning_values, marker='o', label="morning", c='blue')
plt.legend()

plt.show()
