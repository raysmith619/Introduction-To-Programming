#cards_hand.py   07Aug2021   crs, From cards_mod.py
#
"""
A cards_hand "module"
Manipulates hands of cards (CardsCard)
"""
from cards_card import CardsCard

class CardsHand:
    """ Supports operations on a hand of cards
    """

    def __init__(self):
        self.cards = []     # Setup empty hand

    def __str__(self):
        st = "CardsHand:["
        nf = 0
        for card in self.cards:
            if nf > 0:
                st += ","
            st += card
            nf += 1
        st += "]"
        return st
        
    def list_hand(self, prefix=None):
        """ list cards in hand
        :prefix: optional prefix for identification
                default: no prefix
        """
        if prefix is not None:
            print(prefix, end=" ")
        nf = 0                          # Count of number listed so far
        print(f"hand({self}): ", end="")
        for card in self.cards:
            if nf > 0:
                print(", ", end="")     # Separate after first
            print(f"{card}", end="")       # On one line
            nf += 1
        print()         # Add newline end of list
            
    def add_one_card(self, card):
        """ Adds one card to our list
        :card: if str - convert to CardsCard
               else - treat as CardsCard
        """
        if card is str:
            card = CardsCard(str)   # Convert str to Card
        print("add_one_card(",
              card, ")", sep="")
        self.cards.append(card)     # Add to list (no check to insure
                                    # not here already)
        self.list_hand()

    def add_cards(self, *cards):
        """ Add zero or more cards
        :*cards: zero or more card names
        """
        print("\nadd_cards(", *cards, ")")    # passing on list to print
        for card in cards:  # comma separated args become list
            self.add_one_card(card)

    def has_card(self, ck_card):
        """ Check if card is in my_hand
        :ck_card: if str - convert to CardsCard
                  else - accept CardsCard
        :returns: True if new_card is in my_hand
        """
        for card in self.cards:
            if ck_card == card:
                return True         # possible is in list
        return False                # Not in list

"""
Do testing
"""    
def test_add_one_card():    
    """ Test, or atleast exercise, add_one_card function
    """
    print("\ntest_add_one_card")
    my_hand = CardsHand()             # Start test with empty list
    my_hand.add_one_card("S:9")
    my_hand.add_one_card("S:A")
    my_hand.list_hand()

def test_add_cards():    
    """ Test, or atleast exercise, add_cards function
    """
    print("\ntest_add_cards()")
    my_hand = CardsHand()             # Start test with empty list
    my_hand.add_cards("S:9")
    my_hand.list_hand(prefix='After add_cards("S:9")')
    my_hand.add_cards("S:A", "H:K", "D:J")
    my_hand.list_hand(prefix='After add_cards("S:A", "H:K", "D:J")')

def test_has_card_ck(hand, possible, expect=True):
    """ Helper function check if test passes
    :hand: card hand (CardsHand) to check
    :possible: possible card
    :expect: expected value (True,False)
        default: True if not present
    """
    print("test_has_card_ck:", possible, " expect=", expect, end="")
    result = hand.has_card(possible)
    if result == expect:
        print(" Passed Test")
    else:
        print(" FAILED Test result=", result, "expected=", expect)
        
def test_has_card():
    """ Test has_card function
    """
    print("\ntest_has_card()")
    print("Set up my_hand list")
    my_hand = CardsHand()        # Start test with empty list
    my_hand.add_cards("S:A", "H:K", "D:J")
    print("Check function")
    test_has_card_ck(my_hand, "S:A")    # Check if True as expected
    test_has_card_ck(my_hand, "S:10", expect=False)    # Check if False
    test_has_card_ck(my_hand, "H:K", expect=True)      # Ck if True explicit
    print("Test the testing - this should fail the test.")
    test_has_card_ck(my_hand, "C:Q")               # Should fail this!

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
