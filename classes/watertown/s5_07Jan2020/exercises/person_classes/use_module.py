#use_module.py  20Oct2020  crs, Author
"""
Show use of modules person, person_group
"""
from person_group import PersonGroup    # Import one member
import person   # Import whole module

pgrp = PersonGroup()

per = person.Person("Ray", address="Watertown, MA.")
print(per.name,per)
pgrp.add(per)

per = person.Person("Arlene", is_family=True, address="Watertown, MA.")
print(per.name,per)
pgrp.add(per)

per = person.Person("Rich", is_friend=True)
print(per.name,per)
pgrp.add(per)

pgrp.list("Group Listing")
