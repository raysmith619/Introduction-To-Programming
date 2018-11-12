# select_trace.py
"""
trace/logging package
modeled after smTrace.java

Debug Tracing with logging support
"""
from math import log, cos, sin, exp, sqrt, tan, atan, pi, ceil
import re
import os
import atexit

import time
from datetime import datetime
import sys
import traceback

from java_properties import JavaProperties
from test.support import change_cwd

"""
Facilitate execution tracing / logging of execution.
 
@author raysmith
"""

class TraceError(Exception):
    """Base class for exceptions in this module."""
    pass

class SlTrace:
    traceFlagPrefix = "traceFlag"

    """
    Logging Support
    """
    propName = None     # Properties file name None - use script base name
    logName = None # Logfile name
    logExt = "sllog" # Logfile extension (without ".")
    logWriter = None
    logToScreen = True # true - log, additionally to STDOUT
    stdOutHasTs = False # true - timestamp prefix on STDOUT
    lgsString = "" # Staging area for lgs, lgln
    traceObj = None
    defaultProps = None # program properties
    traceAll = False # For "all" trace
    traceFlags = {} # tracing flag/levels
    recTraceFlags = {} # recorded

    @classmethod
    def setup(cls):
        dummy = 0
    
    @classmethod
    def tr(cls, flag, level=1):
    
        cls.setup()        # Insure connection
        return cls.tr1(flag, level=level)

    @classmethod
    def clearFlags(cls):
        """ Clear all trace flags
        """
        cls.traceFlags = {}        # <String, Integer>
        cls.traceAll = 0        # For "all" trace

    
    """
    Setup trace flags from string of the form flag1[=value][,flagN=valueN]* Flags
    are case-insensitive and must not contain ",". Values are optional and
    default to 1 if not present.
    """
    @classmethod
    def setFlags(cls, settings):
        cls.setup() # Insure access
        pat_flag_val = re.compile(r"(\w+)(=(\d+),*)?")
        sets = re.findall(pat_flag_val, settings)
        for setting in sets:
            flag, value = setting[0], setting[2]
            if value is None or value == '':
                value = 1        # Defaule value if no =
            cls.setLevel(flag, value)


    @classmethod
    def setLogExt(cls, logExt):
        """ Setup Logging file default extension This extension is used if no extension
        is provided by user
        """
        cls.logExt = logExt


    @classmethod
    def setLogName(cls, logName):
        """ Setup Logging file name Name without extension is appended with
            "_YYYYMMDD_HHMMSS.tlog"
        """
        cls.logName = logName
        if cls.defaultProps is None:
            propName = os.path.basename(logName)
            propName = os.path.splitext(propName)[0]
            cls.setProps(propName)


    @classmethod
    def setLogToStd(cls, on):
        """ Set logging to stdout
        """
        cls.logToScreen = on

    @classmethod
    def setLogStdTs(cls, on):
        """ Set stdout log to have timestamp prefix
        """
        cls.stdOutHasTs = on


    @classmethod
    def setupLogging(cls, logName=None):
        """
        Setup writing to log file ( via lg(string))
        :logName: name or prefix to log file
        """
            
        if cls.logWriter is not None:
            return cls.logWriter
        
        if logName is not None:
            cls.setLogName(logName)
    
        if cls.logName is None:
            script_name = os.path.basename(sys.argv[0])
            script_name = os.path.splitext(script_name)[0]
            cls.logName = script_name
            
        if not os.path.isabs(cls.logName):
            cwd = os.getcwd()
            dir_base = os.path.basename(cwd)
            if dir_base == "src":
                log_dir = os.path.join("..", "log")  # Place in sister directory
                log_dir = os.path.abspath(log_dir)
            else:
                log_dir = "log"
            cls.logName = os.path.join(log_dir, cls.logName)

        base_file = os.path.abspath(cls.logName)
        directory = os.path.dirname(base_file)
        if not os.path.exists(directory):
            try:
                os.mkdir(directory)
            except:
                raise TraceError("Can't create logging directory %s"
                                     % directory)
                sys.exit(1)
        
            print("Logging Directory %s  created\n"
                  % os.path.abspath(directory))

        if "." not in cls.logName:
            if not cls.logName.endswith("_"):
                cls.logName += "_"
            ts = cls.getTs()
            cls.logName = cls.logName + ts
            cls.logName += "." + cls.logExt  # Default extension

        fw = None
        try:
            abs_logName = os.path.abspath(cls.logName)
            fw = open(abs_logName, "w")
            cls.logWriter = fw
        except IOError as e:
            print("Can't open logWriter %s - %s" % (abs_logName, e))
            sys.exit(1)
        cls.lg("Creating Log File Name: %s" % abs_logName)

        return fw


    @classmethod
    def select_all(cls, level=1):
        """ Trace all known flags at level 1
        """
        for flag in cls.getAllTraceFlags():
            cls.setTraceFlag(flag, level)

    


    @classmethod
    def select_none(cls, level=0):
        """ Trace all known flags at level 0
        """
        for flag in cls.getAllTraceFlags():
            cls.setTraceFlag(flag, level)


    @classmethod
    def lg(cls, msg="", trace_flag=None, level=1, to_stdout=True):
        """
        Log string to file, and optionally to console STDOUT display is based on
        trace info
        @param msg
                   - message to output
        @param trace_flag
                   - when to trace - None - always
        @param level
                   - level to trace - default 1
        @throws IOException
       
        @throws IOException
        """
        if not SlTrace.trace(trace_flag, level):
            return
        
        try:
            cls.setupLogging()
        except:
            print("IOException in lg setupLogging")
            return
 
        ts = cls.getTs()
        if to_stdout:
            prefix = ""
            if cls.stdOutHasTs:
                prefix += " " + ts
            print(prefix + " " + msg)
            sys.stdout.flush()   # Force output
        if cls.logWriter is None:
            print("Can't write to log file")
            return

        try:
            print(" %s %s"  % (ts, msg),
                file=cls.logWriter)
            cls.logWriter.flush()    # Force output
        except IOError as e:
            print("IOError in lg write %s" % str(e))
            


    """
    Append string to log to be logged via next lgln() call
    
    @throws IOException
    """
    @classmethod
    def lgs(cls, msg):
        if cls.lgsString is None:
            lgsString = msg
        else:
            lgsString += msg

    """
    Output staged string to log
    
    @throws IOException
    """
    @classmethod
    def lgln(cls):
        if cls.lgsString is None:
            cls.lgsString = ""

        cls.lg(cls.lgsString)
        cls.lgsString = None # Flush pending

    
    @classmethod
    def onexit(cls):
        try:
            if cls.defaultProps is not None:
                abs_propName = cls.defaultProps.get_path()
                cls.lg("Saving properties file %s"
                    % abs_propName)
                outf = open(abs_propName, "w")
                cls.defaultProps.store(outf, abs_propName)
                cls.defaultProps = None     # Flag as no longer available
        except IOError as e:
            tbstr = traceback.extract_stack()
            cls.lg("Shutdown propName %s store failed %s - %s"
                    % (abs_propName, tbstr), str(e))
        try:
            if cls.logWriter is not None:
                abs_logName = os.path.abspath(cls.logName)
                cls.lg("Closing log file %s"
                    % abs_logName)
                cls.logWriter.close()
                cls.logWriter = None        # Flag as not available
        except IOError as e:
            tbstr = traceback.extract_stack()
            print("Close logfile %s failed %s - %s"
                    % (abs_logName, tbstr), str(e))

    @classmethod
    def getTs(cls):
        """
        Get / generate time stamp Format: YYYYMMDD_HHMMSS
        """
        tsfmt = "%Y%m%d_%H%M%S"
        ts = datetime.now().strftime(tsfmt)
        return ts


    @classmethod
    def setProps(cls, propName=None):
        """
        Set up based on Java style properties file
        
        @throws IOException
        """
        if propName is not None:
            cls.propName = propName
    
        if cls.propName is None:
            script_name = os.path.basename(sys.argv[0])
            script_name = os.path.splitext(script_name)[0]
            cls.propName = script_name
            
        if os.path.splitext(cls.propName)[1] == "":
            cls.propName += ".properties"
            
        if not os.path.isabs(cls.propName):
            cwd = os.getcwd()
            dir_base = os.path.basename(cwd)
            if dir_base == "src":
                prop_dir = os.path.dirname(cwd)
                cls.propName = os.path.join(prop_dir, cls.propName)
            else:
                cls.propName = os.path.abspath(cls.propName)
            
        cls.defaultProps = JavaProperties(cls.propName)

        cls.loadTraceFlags()        # Populate flags from properties
                                     
        atexit.register(cls.onexit)
        # Write out updated properties file


    @classmethod
    def getLogPath(cls):
        """ Returns absolute log file path name
        """
        return os.path.abspath(cls.logName)


    @classmethod
    def getPropKeys(cls):
        """
        get properties keys
        """
        props = cls.defaultProps.get_properties()
        return sorted(props.keys())
    

    @classmethod
    def getPropPath(cls):
        """ Returns absolute Properties file path name
        """
        abs_propName = cls.defaultProps.get_path()
        return abs_propName
    
    
    @classmethod
    def getLevel(cls, trace_name):
        cls.recordTraceFlag(trace_name)
        try:
            v = cls.traceFlags[trace_name]
        except:
            v = 0
            cls.traceFlags[trace_name] = v
        if v is None or v == '':
            return 0            # Not there == 0
        if isinstance(v, str):
            v = int(v)
        return v



    @classmethod
    def setLevel(cls, trace_name, level=1):
        trace_name = trace_name.lower()
        cls.recordTraceFlag(trace_name, level=level)
        if trace_name == "all":
            cls.traceAll = level
        else:
            cls.traceFlags[trace_name] = level


    @classmethod
    def traceVerbose(cls, level=1):
        return cls.trace("verbose", level=level)


    @classmethod
    def getTraceFlags(cls):
        """
        return array of set trace flags
        """
        return cls.traceFlags.keys()

    
    
    """
    Record flag for saving
    Note value may change
    """
    @classmethod
    def recordTraceFlag(cls, flag, level=1):
    ###    if flag in cls.recTraceFlags:
    ###       return                # Already here - don't
        
        cls.recTraceFlags[flag] =  level
        flag_key = cls.getTraceFlagKey(flag)
        cls.setProperty(flag_key, level)


    @classmethod
    def getTraceValueFromProp(cls, name):
        """
        Return flag value, -1 if none
        """
        flagstr = cls.getProperty(cls.getTraceFlagKey(name))
        if flagstr == "":
            return -1

        return int(flagstr)


    @classmethod
    def loadTraceFlags(cls):
        """
        load trace flags from properties
        """
        props = cls.defaultProps.get_properties()
        pattern = cls.traceFlagPrefix + r"\.(.*)"
        r = re.compile(pattern)
        name_list = {}
        ### TBD I need to think about what is going on here
        for name in props.keys():
            if name.startswith(cls.traceFlagPrefix + "."):
                while True:
                    ms = re.findall(r, name)    # unwrap traceFlag.traceFlag....
                    if len(ms) == 0:
                        break
                    name = ms[0]        # stuff after prefix
                    value = "1"
                    mn = re.match(r'(\w+)\s*=\s*(\S.*)', name)
                    if mn:
                        name = mn[1]
                        value = mn[2]

                cls.recordTraceFlag(name, value)

        all_flags = cls.getAllTraceFlags()
        all_flags_str = ",".join(all_flags)
        cls.lg("loadTraceFlags: %s" % all_flags_str)

    
    @classmethod
    def getAllTraceFlags(cls):
        return cls.recTraceFlags.keys()
    
    
    @classmethod
    def getTraceFlagKey(cls, name):
        key = cls.traceFlagPrefix + "." + name
        return key


    @classmethod
    def setDebug(cls, level=1):
        """
        @param debug
                   to set
        """
        cls.setLevel("debug", level)


    @classmethod
    def setVerbose(cls, level=1):
        """
        @param level
        """
        cls.setLevel("verbose", level)


    @classmethod
    def getVerbose(cls):
        """
        @return the verbose
        """
        return cls.getLevel("verbose")


    """
    Trace if at or above this level
    """
    @classmethod
    def trace(cls, flag=None, level=None):
        if flag is None:
            return True
        
        if level is None:
            level = 1
        if level < 1:
            return False # Don't even look

        return cls.traceLevel(flag) >= level


    """
    Return trace level
    """
    @classmethod
    def traceLevel(cls, flag):
        traceLevel = cls.getLevel(flag)
        return traceLevel


    @classmethod
    def getProperty(cls, key):
        """    
        @param key
                   - property key
        ###@return property value, "" if none
        """
        return cls.defaultProps.getProperty(key, "")


    @classmethod
    def setProperty(cls, key, value):
        cls.defaultProps.setProperty(key, value)


    @classmethod
    def getSourcePath(cls, fileName):
        """
        Get source absolute path Get absolute if fileName is not absolute TBD handle
        chain of paths like C include paths
        
        @param fileName
        @return absolute file path
        """
        if not os.path.isabs(fileName):
            dirs = cls.getAsStringArray("source_files")
            searched = []
            for pdir in dirs:
                inf = os.path.join(pdir, fileName)
                if os.path.exists(inf) and os.path.isdir(inf):
                    try:
                        return os.path.realpath(inf)
                    except IOError as e:
                        print("Problem with path %s,%s" % (dir, fileName), file=sys.stderr)
                searched.append(os.path.realpath(inf))

            print("%s was not found\n" % fileName, file=sys.stderr)
            if len(dirs) > 0:
                print("Searched in:\n", file=sys.stderr)
                for dirp in dirs:
                    dirpath = os.path.abspath(dirp)
                    print("\t%s\n" % dirpath, file=sys.stderr)
            return fileName # Return unchanged

        return fileName # Already absolute path

    @classmethod
    def getIncludePath(cls, fileName):
        """
        Get include absolute path Get absolute if fileName is not absolute TBD handle
        chain of paths like C include paths
        
        @param fileName
        @return absolute file path, "" if not found
        """
        if not os.path.isabs(fileName):
            dirs = cls.getAsStringArray("include_files")
            searched = []
            for dirp in dirs:
                inf = os.path.join(dir, fileName)
                if os.path.exists(inf) and not os.path.isdir(inf):
                    try:
                        return os.path.realpath(inf)
                    except IOError as e:
                        print("Problem with path %s,%s" % (dirp, fileName), file=sys.stderr)
      
            print("%s was not found\n" % fileName, file=sys.stderr)
            if len(dirs) > 0:
                print("Searched in:\n")
                for dirp in dirs:
                    dirpath = os.path.realpath(dirp)
                    print("\t%s\n" % dirpath)
            return "" # Indicate as not found

        return fileName # Already absolute path


    @classmethod
    def getAsStringArray(cls, propKey):
        """
        Get default properties key with value stored as comma-separated values as an
        array of those values If propKey not found, return an empty array
        
        @param propKey
        @return array of string values
        """
        valstr = cls.getProperty(propKey)
        vals = valstr.split(',')
        return vals


    @classmethod
    def setTraceFlag(cls, trace_name, level=1):
        """
        Fast, lowlevel trace level setting
        Used for interactive trace changes
        @param trace_name
        @param level
        """
        cls.traceFlags[trace_name] = level

            
    
if __name__ == "__main__":
    quit_on_first_fail = True      # True - stop testing on first failure
    show_passes = True
    show_passes = False
    def test_fail(msg):
        """ Show error and quit if quit_on_first_error
        """
        SlTrace.lg("FAIL: %s" % msg)
        if quit_on_first_fail:
            SlTrace.lg("Quitting of first fail")
            sys.exit(1)

            
    def test_pass(msg):
        """ Show pass if show_passes
        """
        print_msg = "Pass: %s" % msg
        if show_passes:
            print(print_msg)
        SlTrace.lg(print_msg, to_stdout=False)
            
    logName = "sltest"
    SlTrace.setLogName(logName)     # Setup default log name
    SlTrace.setProps("SlTrace")
    SlTrace.lg("setupTest()")
    flag = "sf1"
    SlTrace.setLevel(flag)
    level_got = SlTrace.getLevel(flag)
    if level_got != 1:
        print("level_got: %d != 1" % level_got)
        sys.exit(1)
    flag = "sf2"
    level = 3
    SlTrace.setLevel(flag, level)
    level_got = SlTrace.getLevel(flag)
    if level_got != level:
        test_fail("level_got: %d != %d" % (level_got, level))

    
    if SlTrace.trace(flag, level):
        test_pass("traced %s(%s) with trace(%d)" % (flag, level_got, level))
    else:
        test_fail("FAILED trace %s(%s) with trace(%d)" % (flag, level_got, level))
    
    if SlTrace.trace(flag, level_got-1):
        test_pass("Correctly traced %s(%s) with trace(%d)" % (flag, level_got, level_got-1))
    else:
        test_fail("ERRONEOUSLY skipped trace %s(%s) with trace(%d)" % (flag, level_got, level_got-1))
    
    if SlTrace.trace(flag, level_got+1):
        test_fail("ERRONEOUSLY traced %s(%s) with trace(%d)" % (flag, level_got, level_got+1))
    else:
        test_pass("Correctly skipped trace %s(%s) with trace(%d)" % (flag, level_got, level_got+1))
        
    SlTrace.setFlags("f1=1,f2=2,f3=3,fnone")
    tdict = {"f1" : 1, "f2" : 2, "f3" : 3, "fnone" : None}
    for flag, level in tdict.items():
        if level is None:
            level = 1           # Default setting
        trace_level = level
        if SlTrace.trace(flag, trace_level):
            if trace_level is None:
                test_pass("flag %s(%d) traced(None)" % (flag, level))
            else:
                test_pass("flag %s(%d) traced(%d)" % (flag, level, trace_level))
                
        else:
            if trace_level is None:
                test_fail("flag %s(%d) skipped(None)" % (flag, level))
            else:
                test_fail("flag %s(%d) skipped(%d)" % (flag, level, trace_level))
    
    SlTrace.lg("End of Test")
