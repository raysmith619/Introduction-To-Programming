# java_properties.py    20Sep2018
"""
Java properties file processing
Simple single name.name.... = value
"""
import os
import sys

class JavaProperties:
    
    def __init__(self, filename):
        self.props = self.load(filename)
        
    def load(self, filename):
        sep = "="
        if "." not in(filename):
            filename += ".properties"   # Default extension
        if not os.path.isabs(filename):
            filename = os.path.abspath(filename)
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, "w") as fout:
                abs_filename = os.path.abspath(filename)
                print("Creatng empty file %s" % abs_filename)
                print("# %s Empty - created" % filename, file=fout)
                fout.close()
        with open(filename) as fin:
            props = {}
            for line in fin:
                if "#" in line:
                    ic = line.index("#")
                    line = line[ic:]
                if sep not in line:
                    continue
                            # Find the name and value by splitting the string
                name, value = line.split(sep, 1)
    
                # Assign key value pair to dict
                # strip() removes white space from the ends of strings
                props[name.strip()] = value.strip()
        return props


    def getProperty(self, key, default):
        """ Get property, returning default if none
        """
        try:
            value = self.props.get(key, default)
        except:
            value = default
        return value
    
        
    def get_properties(self):
        """ Return dictionary of keys and value text strings
        """
        return self.props


    def setProperty(self, key, value):
        """ Set property(key) value
        """
        self.props[key] = value


    def store(self, fp, title):
        """ Store properties file
        :fp: Output file
        :title: Optional comment line
        """
        try:
            if title is not None:
                print("# %s" % title, file=fp)
            for key in self.props:
                print("%s=%s" % (key, self.props[key]), file=fp)
            fp.close()
        except IOError as ioex:
            print("Error in storing Properties file %s" % title)
            print("errno: %d" % ioex.errno)
            print("err code: %d" % ioex.errorcode[ioex.errno])
            print("err message: %s" % os.strerror(ioex.errno))

    
    def get_path(self):
        """ Get full path to properties file
        """
        return self.filename        

    
if __name__ == "__main__":
    propfile = "test"
    pr = JavaProperties(propfile)
    dp = pr.get_properties()
    
    for key in dp:
        print("dp[%s] = %s" % (key, dp[key]))
    
    pr2 = JavaProperties(propfile)
    pk = "new_key"
    default_val = "check_val"
    pval = pr2.getProperty(pk, default_val)
    if pval == default_val:
        print("Got expected default %s value %s" % (pk, pval))
    else:
        print("Got %s NOT the EXPECTED %s" % (pval, default_val))
        print("Quitting")
        sys.exit(1)
        
    new_value = "New VALUE"   
    pr2.setProperty(pk, new_value)
    
    propfile2 = "test2.properties"
    abs_propfile2 = os.path.abspath(propfile2)
    print("\nWriting new properties file %s" % abs_propfile2)    
    with open(propfile2, "w") as p2f:
        pr2.store(p2f, "# %s properties file 2" % propfile2)
        p2f.close()

    print("Loading new properties file %s" % propfile2)    
    pr2b = JavaProperties(propfile2)
    pk2 = pk
    pval2 = pr2b.getProperty(pk2, None)
    if pval2 is None:
        print("Property %s not found" % pk2)
        sys.exit(1)
        
    print("pval=%s" % pval2)
    print("new_value=%s" % new_value)
    if pval2 != pval2:
        print("pval2 Not Equal to pval")
        print("Property key:%s: %s was NOT the EXPECTED %s"
               % (pk2, pval2, pval))
        print("Quitting")
        sys.exit
    print("End of Test")        
        