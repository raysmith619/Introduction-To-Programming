#person_1.py  22Dec2020  crs
"""
Simplest example of a class
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
    
# Selftest
if __name__ == "__main__":
    per = Person("Ray")
    print(per.name)

    per = Person("Arlene")
    print(per.name)

    per = Person("Rich")
    print(per.name,per)
