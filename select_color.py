# select_color.py    03Oct20178
"""
Color control for "select_region" system
"""
from random import seed
from random import randint
import random

from select_trace import SlTrace
from select_error import SelectError
from freq2rgb import freq_lists


def darken(color):
    """ Darken color
    :color: rgb int
    Simple - integer divide each component
    """
    color &= ~0x010101  # clear units to avoid shifting bit
    color >>= 1
    return color

class SelectColor:
    
    SCC_MAX = 255       # Max color 
    SCC_MIN = SCC_MAX/4 # Min color
    
    specs = []
    SCS_FREQ = "freq"
    specs.append(SCS_FREQ)
    SCS_RGB = "rgb"
    specs.append(SCS_RGB)
    SCS_BW = "bw"
    specs.append(SCS_BW)
    SCS_RGB1PRIM = "rgb1prim"
    specs.append(SCS_RGB1PRIM)
    SCS_RGB2PRIM = "rgb2prim"
    specs.append(SCS_RGB2PRIM)
    
    progs = []          # Progression values
    SCP_RANDOM = "random"
    progs.append(SCP_RANDOM)
    SCP_ASCEND = "ascend"
    progs.append(SCP_ASCEND)
    SCP_DESCEND = "descend"
    progs.append(SCP_DESCEND)
    
    
    def __init__(self, ncolor=100, spec=None, prog=None,
                cmax=None, cmin=None,
 
                do_seed=None):
        """ Generate list of colors
        :spec: color specification
            "freq"
            "rgb"
            "bw"
            "rgb1prim" - use only one r,g,b at a time
            "rgb2prim" - use at most 2 r,g,b at a time
        :prog: color progression
                "random" or
                SCP_RANDOM - random colors (DEFAULT)
                "ascend"
                SCP_ASCEND - ascending from SCC_MIN to SCC_MAX
                "descend" or
                SCP_DESCEND - descending from SCC_MAX to SCC_MIN
        :cmax: maximum number interpretation depends on prog
        :cmin: minimum number interpretation depends on prog
        :ncolor: Number of colors
        :do_seed:  If present re-seed random number generator
        
        NOTE: Current implementation creates a list ~ 3 * ncolor in length
        """
        if do_seed is not None:
            seed(do_seed)

        if spec is None:
            spec = "rgb"
        if spec == "frequency":
            spec = "freq"           #Alias
        if spec not in SelectColor.specs:
            raise SelectError("spec %s is not in our implemented specifications %s"
                              % (spec, ", ".join(SelectColor.specs)))
        self.spec = spec
        if prog is None:
            prog = "random"
        if prog not in SelectColor.progs:
            raise SelectError("prog %s is not in our implemented progressions %s"
                              % (prog, ", ".join(SelectColor.progs)))
        self.prog = prog
        if spec == SelectColor.SCS_FREQ:
            if cmin is None:
                cmin = 430      # Visible linght 430 THZ
            if cmax is None:
                cmax = 770
        else:
            if cmin is None:
                cmin = 50
            if cmax is None:
                cmax = 255
        if cmin == 0:
            SlTrace.lg("cmin is 0")
        self.cmax = cmax
        self.cmin = cmin
        self.ncolor = ncolor
        if do_seed is not None:
            seed(do_seed)
        
        if self.spec == SelectColor.SCS_FREQ:
            self.set_freq_lists() 
        elif self.spec == SelectColor.SCS_RGB:
            self.set_rgb_lists()
        elif self.spec == SelectColor.SCS_BW:
            self.set_bw_lists()
        elif self.spec == SelectColor.SCS_RGB1PRIM:
            self.rgb_n_lists(1)
        elif self.spec == SelectColor.SCS_RGB2PRIM:
            self.rgb_n_lists(2)
        else:
            raise SelectError("spec %s is not in our implemented specifications %s"
                  % (self.spec, ", ".join(SelectColor.specs)))

        self.index = 0       # Incremented as colors are provided
        
        
    def get_color(self, index=None):
        """ Get Color
        :index: - color 0-ncolor-1  Default: next color in line
        """
        if index is None:
            index = self.index
            self.index += 1     # Move to next
        
        color = 0
        color |= self.red_colors[index] << 16
        color |= self.green_colors[index] << 8
        color |= self.blue_colors[index]
            
        SlTrace.lg("color:%d(%X)" % (color, color), "get_color")
        return color
    
    
    def get_list(self, ncolor=None, spec=None, prog=None, cmin=None, cmax=None):
        """ Generate a list of values
            See __init__ for parameters
            :Returns:  list of values based on prog between cmin and cmax
        """
        if ncolor is None:
            ncolor = self.ncolor
        if spec is None:
            spec = self.spec
        if prog is None:
            prog = self.prog
        if cmin is None:
            cmin = self.cmin
        if cmax is None:
            cmax = self.cmax
        
        
        clist = []          # List to fill    
        if prog == self.SCP_RANDOM:
            for _ in range(ncolor):
                clist.append(randint(int(cmin), int(cmax)))
        elif prog == self.SCP_ASCEND:
            inc = (cmax-cmin)/ncolor
            val = cmin
            for _ in range(ncolor):
                clist.append(int(val))
                val += inc
        elif prog == self.SCP_DESCEND:
            inc = -(cmax-cmin)/ncolor
            val = cmax
            for _ in range(ncolor):
                clist.append(int(val))
                val += inc
                
        return clist


    def set_freq_lists(self):
        """ Setup color list for frequency specified colors
        """
        ncolor = self.ncolor
        prog = self.prog
        cmin = self.cmin
        cmax = self.cmax
        reds, greens, blues = freq_lists(ncolor, prog=prog, min_f=cmin, max_f=cmax)
        self.red_colors = reds 
        self.green_colors = greens
        self.blue_colors = blues
        
        
    def set_rgb_lists(self):
        """ Setup color lists for rgb specificied colors
        all (r,g,b) at random intensities
        """
        ncolor = self.ncolor
        prog = self.prog
        cmin = self.cmin
        cmax = self.cmax
        self.red_colors = self.get_list(ncolor=ncolor, prog=prog, cmin=cmin, cmax=cmax)
        self.green_colors = self.get_list(ncolor=ncolor, prog=prog, cmin=cmin, cmax=cmax)
        self.blue_colors = self.get_list(ncolor=ncolor, prog=prog, cmin=cmin, cmax=cmax)
        
    def set_bw_lists(self):
        """ Setup black/white lists rgb all at same intensity
        """
        ncolor = self.ncolor
        prog = self.prog
        cmin = self.cmin
        cmax = self.cmax
        self.red_colors = self.get_list(ncolor=ncolor, prog=prog, cmin=cmin, cmax=cmax)
        self.green_colors = self.red_colors
        self.blue_colors = self.red_colors
       
    
    def rgb_n_lists(self, nchoose=1):
        """ Setup color lists for rgb primary with color number restricted to at most n colors
         e.g. 1 (r,g,b) or 2 (r, rg, rb, g, gb, b) all at same intensity
        """
        ncolor = self.ncolor
        prog = self.prog
        cmin = self.cmin
        cmax = self.cmax
        idxs = random.sample(range(3), nchoose)     # Holding indexes of rgb
        clist = self.get_list(ncolor=ncolor, prog=prog, cmin=cmin, cmax=cmax)
        clred = []
        clgreen = []
        clblue = []
        for ic in range(ncolor):
            for clidx in range(3):
                if clidx in idxs:
                    if clidx == 0:
                        clred.append(clist[ic])
                    elif clidx == 1:
                        clgreen.append(clist[ic])
                    elif clidx == 2:
                        clblue.append(clist[ic])
                else:
                    if clidx == 0:
                        clred.append(0)
                    elif clidx == 1:
                        clgreen.append(0)
                    elif clidx == 2:
                        clblue.append(0)
        self.red_colors = clred
        self.green_colors = clgreen
        self.blue_colors = clblue
        
        
#########################################################################
#          Self Test                                                    #
#########################################################################
if __name__ == "__main__":
    ncolor = 10
    ct = SelectColor(ncolor)
    for _ in range(ncolor):
        color = ct.get_color()
        print("color:%d(%X)" % (color, color))
        
    ct = SelectColor(ncolor, use_red=False, use_green=False, prog=SelectColor.SCP_ASCEND)
    for _ in range(ncolor):
        color = ct.get_color()
        print("color:%d(%X)" % (color, color))
        
    ct = SelectColor(ncolor, use_blue=False, use_green=False, prog=SelectColor.SCP_DECEND)
    for _ in range(ncolor):
        color = ct.get_color()
        print("color:%d(%X)" % (color, color))
        
