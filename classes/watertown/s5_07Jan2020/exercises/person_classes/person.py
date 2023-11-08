#person.py  14Oct2020  crs
"""
A simple example of a class
Embodies a person's information
"""
class Person:
    """
    Embodies a person's information
    """

    # Class instance (object) setup function
    def __init__(self,      # Reference to us
                 name,      # Person's name: required
                 is_friend=False,   # default - not
                 is_family=False,
                 address=None,      # default Unknown
                 ):
                            #Saving setup info
        self.name = name
        self.is_friend = is_friend
        self.is_family = is_family
        self.address = address

    def __str__(self):
        """ Give object's string representation
        """
        ret = f"Person: {self.name}"
        if self.is_friend:
            ret += " friend"
        if self.is_family:
            ret += " family"
        if self.address is not None:
            ret += f" address: {self.address}"
        return ret
    
# Selftest
if __name__ == "__main__":
    per = Person("Ray", address="Watertown, MA.")
    print(per.name,per)

    per = Person("Arlene", is_family=True, address="Watertown, MA.")
    print(per.name,per)

    per = Person("Rich", is_friend=True)
    print(per.name, per)
    
    if per.is_friend:
        print(f"{per.name} is a friend")
