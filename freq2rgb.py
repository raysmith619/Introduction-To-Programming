# freq2rgb.py
"""
Conversions between frequency and RGB colors
Initial wav2RGB from R.L.

"""
import random
from select_trace import SlTrace


c = 299792458       # m/sec
c_nm = c * 1.0E9    # nm/sec
c_nm_th = c_nm/1.0E12
def freq_to_wav(freq):
    """ freq in THZ(10**12) to wave length in nano meters 10**-9
    """
    if freq == 0:
        SlTrace.lg("Zero frequency - set to 1")
        freq = 1
    return c_nm_th/freq 

def wav_to_freq(wav):
    """ wav in nano meters(1E-9) to frequency in THZ(10**12)
    """
    if wav == 0:
        SlTrace.lg("Zero wave length - set to 1")
        wav = 1
    return c_nm_th/wav
 
    
def wav2RGB(wavelength):
    w = int(wavelength)

    # colour
    if w >= 380 and w < 440:
        R = -(w - 440.) / (440. - 350.)
        G = 0.0
        B = 1.0
    elif w >= 440 and w < 490:
        R = 0.0
        G = (w - 440.) / (490. - 440.)
        B = 1.0
    elif w >= 490 and w < 510:
        R = 0.0
        G = 1.0
        B = -(w - 510.) / (510. - 490.)
    elif w >= 510 and w < 580:
        R = (w - 510.) / (580. - 510.)
        G = 1.0
        B = 0.0
    elif w >= 580 and w < 645:
        R = 1.0
        G = -(w - 645.) / (645. - 580.)
        B = 0.0
    elif w >= 645 and w <= 780:
        R = 1.0
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0

    # intensity correction
    if w >= 380 and w < 420:
        SSS = 0.3 + 0.7*(w - 350) / (420 - 350)
    elif w >= 420 and w <= 700:
        SSS = 1.0
    elif w > 700 and w <= 780:
        SSS = 0.3 + 0.7*(780 - w) / (780 - 700)
    else:
        SSS = 0.0
    SSS *= 255

    return [int(SSS*R), int(SSS*G), int(SSS*B)]


def freq_to_rgb(freq):
    """ Return RGB list given frequency in THZ 10**6*MHZ
    """
    wav = freq_to_wav(freq)
    return wav2RGB(wav)


def min_freq():
    """ Minimum visible frequency
    """
    return wav_to_freq(700)


def max_freq():
    """ Minimum visible frequency
    """
    return wav_to_freq(390)


def freq_lists(ncolor=100, prog="ascend", min_f=None, max_f=None):
    """ Return R,G,B lists, each of ncolor entries of colors
    :ncolor: number of color entries
    :prog: progression default: ascend
        "random" - random list between min and max
        "ascend" - ascending min to max
        "descend" - decending max to min
    :min: minimum frequncy default: lowest visible
    :max: maximum frequency default: Highest visible
    :Returns: three lists of R, G, B - newly created each call
    From Wikipedia:
        When the wavelength is within the visible spectrum
        (the range of wavelengths humans can perceive,
        approximately from 390 nm to 700 nm), it is known
        as "visible light".
    
        Color             Wavelength interval    Frequency interval
        Red               ~ 700635 nm           ~ 430480 THz
        Orange            ~ 635590 nm           ~ 480510 THz
        Yellow            ~ 590560 nm           ~ 510540 THz
        Green             ~ 560520 nm           ~ 540580 THz
        Cyan              ~ 520490 nm           ~ 580610 THz
        Blue              ~ 490450 nm           ~ 610670 THz
        Violet or Purple  ~ 450400 nm           ~ 670750 THz
    """
    if min_f is None:
        min_f = min_freq()
    if max_f is None:
        max_f = max_freq()
    
    reds = []
    greens = []
    blues = []
    for i in range(1, ncolor+1):
        if prog == "random":
            freq = random.uniform(min_f, max_f)
        elif prog == "ascend":
            freq = i * (max_f-min_f)/ncolor + min_f
        elif prog == "descend":
            freq = (ncolor-i)*(max_f-min_f)/ncolor + min_f
        else:
            freq = random.uniform(min_f, max_f)     # Treat others as random
            
        red, green, blue = freq_to_rgb(freq)
        if red == 0:
            SlTrace.lg("red zero", "red_zero")
        reds.append(red)
        greens.append(green)
        blues.append(blue)
        
    return reds, greens, blues

 
if __name__ == '__main__':
    SlTrace.lg("minimum visible frequency %f THZ" % min_freq())
    SlTrace.lg("maximum visible frequency %f THZ" % max_freq())
    
    ncolor = 8
    reds, greens, blues = freq_lists(ncolor)
    SlTrace.lg("reds:   %s" % ("\t".join([str(x) for x in reds])))
    SlTrace.lg("greens: %s" % ("\t".join([str(x) for x in greens])))
    SlTrace.lg("blues:  %s" % ("\t".join([str(x) for x in blues])))
    