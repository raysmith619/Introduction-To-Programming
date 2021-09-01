#person_group.py    23Dec2020  crs, case insensitive
#                   14Oct2020  crs
"""
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
        key = person.name.lower()   # Case insensitive key
        self.people[key] = person
        print(f"add:{person} People:{self.people}")

    def is_family(self, name):
        """ Check if name is a family
        :name: of potential family
        :returns: True if name is a family
        """
        person = self.get_person(name)
        if person is not None:      # Check if in group
            if person.is_family:
                return True

        return False

    def is_friend(self, name):
        """ Check if name is a friend
        :name: of potential friend
        :returns: True if name is a friend
        """
        person = self.get_person(name)
        if person is not None:      # Check if in group
            if person.is_friend:
                return True

        return False

    def get_people(self):
        """ Return list of people in group
        :returns: list of people(Person)
        """
        pers = []   # Build list of (Person)
        for key in self.people:
            pers.append(self.people[key])
        return pers
    
    def get_person(self, name):
        """ Get person, if in this group
        :name: name of possible member
        :returns: person(Person) if in group
                    else None
        """
        key = name.lower()      # Case insensitive
        if key in self.people:
            return self.people[key]
        
        return None


    def is_in_group(self, name):
        """ Test if name is in group
        :name: name of candidate member
        :returns: True if in group
        """
        key = name.lower()  # Case insensitive
        if key in self.people:
            return True

        return False
    
                    
    def list(self, heading=None):
        """ List people in group
        :heading: optional heading to listing
        """
        if heading is not None:
            print(f"\n{heading}")
        ###print(f"list: people:{self.people}")    ### TFD
        for p_name in self.people:
            print(self.people[p_name])
            
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
    
