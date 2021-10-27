#pgm_time.py  11Oct2021  crs, Author
"""
Time since init, e.g. program time
"""
import time

class PgmTime:
    """ Get elapsed time
    """
    def __init__(self, start_time=None):
        """ Setup elapsed timer
        :start_time: beginning time
            default: current time
        """
        if start_time is None:
            start_time = time.time()
        self.start_time = start_time

    def elapsed(self):
        """Get elapesed time
        :returns: elapsed time in seconds
        """
        now = time.time()
        return now-self.start_time

    def pt(self,fmt=7.5):
        """ Program time formatted
        :fmt: format string
            defalut: .5
        """
        return f"{self.elapsed():{fmt}}"
    
if __name__ == "__main__":
    pt = PgmTime()
    for i in range(5):
        now = time.time()
        print(f"{pt.pt()} time:{now} {now-pt.start_time:.6}")
        time.sleep(1)
    print("End Test")
