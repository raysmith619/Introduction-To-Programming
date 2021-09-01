#test_cards_mod.py  07Aug2021  crs, From friends_4.py
#                   23Jun2020  crs, showing import
"""
Initial testing of cards_mod.py as an imported file
"""
from cards_mod import *
add_cards("S:A", "S:K", "S:Q", "S:J", "S:10")
list_hand()

other_cards = ["H:A", "D:K", "C:Q"]
for card in my_hand + other_cards:
    if has_card(card):
        print(card, "is in hand")
    else:
        print(card, "is NOT in hand")
