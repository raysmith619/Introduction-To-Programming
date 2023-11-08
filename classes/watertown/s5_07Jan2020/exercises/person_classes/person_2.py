#person_2.py  22Dec2020  crs
"""
A bit more in example of a class
Embodies a person's information
"""
class Person:
    """
    Embodies a person's information
    """

    # Class instance (object) setup function
    def __init__(self,      # Reference to us
                 name):     # Person's name: required
                            #Saving setup info
        self.name = name

    def __str__(self):      # Used when object accessed
                            # as string
        """ Give object's string representation
        """
        ret = f"Person: {self.name}"
        return ret
    
# Selftest
if __name__ == "__main__":
    per = Person("Ray")
    print(per.name,per)

    per = Person("Arlene")
    print(per.name,per)

    per = Person("Rich")
    print(per.name, per)
