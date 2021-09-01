#cards_mod.py   07Aug2021   crs, From friends_mod.py
#               23Jun2020   crs, Adapted from friends_3.py
"""
A cards "module" which can be used by other programs
via from cards_mod import *
card := (S|H|D|C) ":" A|K|Q|J|10|9..1
        # e.g., "S:A" for Ace of Spades
"""
my_hand = []     # Initialize empty card hand as an empty list

def list_hand(prefix=None):
    """ list cards in hand
    :prefix: optional prefix for identification
            default: no prefix
    """
    if prefix is not None:
        print(prefix, end=" ")
    nf = 0                          # Count of number listed so far
    print("my_hand: ", end="")
    for card in my_hand:
        if nf > 0:
            print(", ", end="")     # Separate after first
        print(card, end="")       # On one line
        nf += 1
    print()         # Add newline end of list
        
def add_one_card(card):
    """ Adds one card to our list
    :card: card's name
    """
    global my_hand           # REQUIRED to allow us to modify
                                # variable outside function
    print("add_one_card(",
          card, ")", sep="")
    my_hand.append(card)   # Add to list (no check to insure
                                # not here already)
    list_hand()

def add_cards(*cards):
    """ Add zero or more cards
    :*cards: zero or more card names
    """
    print("\nadd_cards(", *cards, ")")    # passing on list to print
    for card in cards:  # comma separated args become list
        add_one_card(card)

def has_card(ck_card):
    """ Check if card is in my_hand
    :ck_card: name of card
    :returns: True if new_card is in my_hand
    """
    for card in my_hand:
        if ck_card == card:
            return True         # possible is in list
    return False                # Not in list

"""
Do testing
"""    
def test_add_one_card():    
    """ Test, or atleast exercise, add_one_card function
    """
    global my_hand           # REQUIRED to allow us to modify
                                # variable outside function
    print("\ntest_add_one_card")
    my_hand = []             # Start test with empty list
    add_one_card("S:9")
    add_one_card("S:A")

def test_add_cards():    
    """ Test, or atleast exercise, add_cards function
    """
    global my_hand           # REQUIRED to allow us to modify
                                # variable outside function
    print("\ntest_add_cards()")
    my_hand = []             # Start test with empty list
    add_cards("S:9")
    list_hand(prefix='After add_cards("S:9")')
    add_cards("S:A", "H:K", "D:J")
    list_hand(prefix='After add_cards("S:A", "H:K", "D:J")')

def test_has_card_ck(possible, expect=True):
    """ Helper function check if test passes
    :possible: possible card
    :expect: expected value (True,False)
        default: True if not present
    """
    print("test_has_card_ck:", possible, " expect=", expect, end="")
    result = has_card(possible)
    if result == expect:
        print(" Passed Test")
    else:
        print(" FAILED Test result=", result, "expected=", expect)
        
def test_has_card():
    """ Test has_card function
    """
    global my_hand           # REQUIRED to allow us to modify
                                # variable outside function
    print("\ntest_has_card()")
    print("Set up my_hand list")
    my_hand = []             # Start test with empty list
    add_cards("S:A", "H:K", "D:J")
    print("Check function")
    test_has_card_ck("S:A")    # Check if True as expected
    test_has_card_ck("S:10", expect=False)    # Check if False
    test_has_card_ck("H:K", expect=True)      # Ck if True explicit
    print("Test the testing - this should fail the test.")
    test_has_card_ck("C:Q")               # Should fail this!

"""
This type of test can be placed
in a module to facilitate "self-testing"
because it gets executed if/when the file gets
run by itself
"""
if __name__ == "__main__":
    print("Self test", __file__) 
    test_add_one_card()
    test_add_cards()
    test_has_card()
