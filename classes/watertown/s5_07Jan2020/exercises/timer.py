# timer.py  26-Jul-2018
"""
Write a "Timer" program.
The program ACCEPTS A TIME AND COUNTS DOWN AND ANNOUNCES WHEN DONE
Test:

"""
import time
import sys
import winsound     # sounds
duration = 60
test_inc = .1       # Testing increment in seconds
inp = input("Enter duration in seconds[" + str(duration) + "]: ")
if inp == "":
    inp = duration
duration = float(inp)
time_start = time.time()
time_end = time_start + duration
time_cur = time_start           # Don't use name time, conflicts with module
while time_cur < time_end:
    time_cur = time.time()
    tsin = time_cur - time_start
    tleft = time_end - time_cur
    if tleft < .0001:
        tleft = 0
    print("time left: {0:.1f}\r".format(tleft), end='')
    ###print()         ### Hack for IDLE shell presentation
    sys.stdout.flush()
    time.sleep(test_inc)
sound_inc = 10
low_freq = 340
hi_freq = low_freq + 200
sound_duration = int(1000/sound_inc)
for freq in range(low_freq, hi_freq, sound_inc):
    winsound.Beep(freq, sound_duration)    
for freq in range(hi_freq, low_freq, -sound_inc):
    winsound.Beep(freq, sound_duration)    
