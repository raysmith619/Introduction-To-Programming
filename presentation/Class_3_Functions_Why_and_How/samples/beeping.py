#beeping.py 06Mar2022  crs
""" beep (sound creation for Windows or Linux)
We use windound on windows else we call the
system function beep
Adapted from Stackoverflow:
Python: what are the nearest Linux and OSX
equivalents of winsound.Beep?
"""
try:
    import winsound
except ImportError:
    import os
    def playsound(frequency,duration):
        #apt-get install beep
        os.system('beep -f %s -l %s' % (frequency,duration))
else:
    def playsound(frequency,duration):
        winsound.Beep(frequency,duration)

if __name__ == '__main__':
    import sys
    print(f"Our platform: {sys.platform}")
    low_freq = 200
    high_freq = 500
    nfreq = 10
    dur = 1000
    freq_inc = int((high_freq-low_freq)/nfreq)
    for i in range(nfreq+1):
        freq = low_freq+i*freq_inc
        print(f"freq:{freq} dur:{dur}")
        playsound(freq, dur)
    for i in range(nfreq,-1,-1):
        dur2 = int(i/nfreq*dur)
        freq = low_freq+i*freq_inc
        print(f"freq:{freq} dur:{dur2}")
        playsound(freq, dur2)
        
