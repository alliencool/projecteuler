import sys

class Hand(object):

    ranks = [
                (1, "High card"),
                (2, "One pair"),
                (3, "Two pairs"),
                (4, "Three of a Kind"),
                (5, "Straight"),
                (6, "Flush"),
                (7, "Full house"),
                (8, "Four of a Kind"),
                (9, "Straight flush"),
                (10, "Royal flush"),
            ]
    
    def __init__(self, init_list):

        self.init_list = init_list
        self.cards = [(self._value_map(x[0]), x[1]) for x in self.init_list]
        self.cards = sorted(self.cards)
        
    def __str__(self):
        return str(self.init_list)

    def _value_map(self, card_value):
        
        if card_value <= "9":
            return int(card_value)
        
        return {"T":10, "J":11, "Q":12, "K":13, "A":14}[card_value]

def task54(filename):

    first_win = 0
    second_win = 0
    with open(filename) as poker:
        for line in poker:
            first_hand = Hand(line.split()[:5])
            second_hand = Hand(line.split()[5:])
            if first_hand > second_hand:
                first_win += 1
            elif second_hand > first_hand:
                second_win += 1
            else:
                print "Something wrong!\n", first_hand, second_hand

if __name__ == "__main__":
    task54(sys.argv[1])
