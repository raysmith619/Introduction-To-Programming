#cards_card.py   07Oct2021   crs, author
#
"""
A cards_card "module" which can be used by other programs
"""
class CardsCard:
    """ Simple playing card class
    """
    rank2str = {14:"A", 13:"K", 12:"Q", 11:"J",
                10:"10", 9:"9", 8:"8", 7:"7", 6:"6",
                5:"5", 4:"4", 3:"3", 2:"2", 1: 1}
    def __init__(self, string):
        """ Setup card
        :str_string: Descriptive sting
        (S|H|D|C) ":" A|K|Q|J|10|9..1
        # e.g., "S:A" for Ace of Spades
        """
        suit, rank_str = string.split(":")
        suit = suit.upper()
        if suit in "SHDC":
            self.suit = suit
        else:
            raise Exception(f"Bad card{string} - suit:{suit}")
        if rank_str in "A|K|Q|J|10|9|8|7|6|5|4|3|2|1":
            if rank_str == "A" or rank_str == 1:
                rank = 14
            elif rank_str == "K":
                rank = 13
            elif rank_str == "Q":
                rank = 12
            elif rank_str == "J":
                rank = 11
            elif rank_str == "10":
                rank = 10
            elif rank_str in "98765432":
                rank = int(rank_str)
            else:
                raise Exception(f"Bad card{string} - rank:{rank_str}")
            self.rank = rank
        

    def __str__(self):
        st = self.suit + ":"
        st += CardsCard.rank2str[self.rank]
        return st
    
"""
Do testing
"""    
if __name__ == "__main__":
    print("Self test", __file__)
    for rank_str in ["A","K","Q","J","10",
                     "9","8","7","6", "5",
                     "4","3","2"]:
        for suit in ["C", "D", "H", "S"]:
                cs = f"{suit}:{rank_str}"
                card = CardsCard(cs)
                print(f" {cs} card: {card}", end="")
        print()
            
