#person_group_startup.py    23Dec2020 crs setup exercise
#                   23Dec2020  crs, case insensitive
#                   14Oct2020  crs
"""
With code stripped out for student to add

Group of Person
"""
class PersonGroup:
    """
    Embodies a group of people (Person)
    """

    # Class instance (object) setup
    def __init__(self):
        self.people = {}    # Initialize as an empty  group
                            # A dictionary by name

    def add(self, person):
        """ Add person to group
        :person: person(Person) to add to group
        """
        key = person.name.lower() # Case insensitive key
        
    def is_family(self, name):
        """ Check if name is a family
        :name: of potential family
        :returns: True if name is a family
        """
                      # Check if in group
        return False    # Not in group

    def is_friend(self, name):
        """ Check if name is a friend
        :name: of potential friend
        :returns: True if name is a friend
        """
        return False

    def get_people(self):
        """ Return list of people in group
        :returns: list of people(Person)
        """
        pers = []       # Build into list

        return pers
    
    def get_person(self, name):
        """ Get person, if in this group
        :name: name of possible member
        :returns: person(Person) if in group
                    else None
        """
        
        return None


    def is_in_group(self, name):
        """ Test if name is in group
        :name: name of candidate member
        :returns: True if in group
        """
        key = name.lower()  # Case insensitive

        return False
    
                    
    def list(self, heading=None):
        """ List people in group
        :heading: optional heading to listing
        """
        if heading is not None:
            print(f"\n{heading}")
            
# Selftest
if __name__ == "__main__":
    from person import Person

    print(f"{__file__} self test")
    
    def test_group(group, name):
        """ Do assorted tests with name for group
        :group: group to test
        :name: name to test
        """
        print(f"\n===============\nTest {name}")
        if group.is_in_group(name):
            print(f"{name} is in group")
        else:
            print(f"{name} is not in group")

        if group.is_friend(name):
            print(f"{name} is a friend")
        else:
            print(f"{name} is not friend")

        if group.is_family(name):
            print(f"{name} is one of the family")
        else:
            print(f"{name} is not one of the family")

    t_group = PersonGroup()    
    p1 = Person("Ray", address="Watertown, MA.")
    t_group.add(p1)
    t_group.list()
    
    p1a = Person("Arlene", is_family=True, address="Watertown, MA.")
    t_group.add(p1a)
    t_group.list(f"After {p1a}")
    
    p2 = Person("Rich", is_friend=True)
    t_group.add(p2)
    t_group.list(f"After {p2}")
    
    p3 = Person("Igor")
    t_group.add(p3)
    t_group.list(f"After {p3}")

    print("Testing Group")
    for person in t_group.get_people():
        test_group(t_group, person.name)
    
