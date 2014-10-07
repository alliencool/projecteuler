import sys

class Hand(object):

    RANKS = [
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
        self.cards_by_rank = []
        self._get_rank()
        
    def __str__(self):
        return str(self.cards) + " " + str(self.cards_by_rank) + " " + str(self.rank)

    def _value_map(self, card_value):
        
        if card_value <= "9":
            return int(card_value)
        
        return {"T":10, "J":11, "Q":12, "K":13, "A":14}[card_value]

    def _get_rank(self):

        all_equal = lambda x: x == ([x[0]] * len(x))
        consequtive = lambda x: all_equal([(x[i + 1] - x[i]) for i in xrange(len(x)-1)] + [1])
        get_suites = lambda pairs: [pair[1] for pair in pairs]
        get_values = lambda pairs: [pair[0] for pair in pairs]

        values = get_values(self.cards)
        suites = get_suites(self.cards)

        if values == [10, 11, 12, 13, 14] and all_equal(suites):
            self.rank = self.RANKS[9]
            self.cards_by_rank = [values[-1::-1]]
        elif consequtive(values) and all_equal(suites):
            self.rank = self.RANKS[8]
            self.cards_by_rank = [values[-1::-1]]
        elif all_equal(values[:4]) or all_equal(values[1:]):
            self.rank = self.RANKS[7]
            if all_equal(values[:4]):
                self.cards_by_rank = [values[3::-1], [values[4]]]
            else:
                self.cards_by_rank = [values[-1:0:-1], [values[0]]]
        elif (all_equal(values[:2]) and all_equal(values[2:])) or\
             (all_equal(values[:3]) and all_equal(values[3:])):
            self.rank = self.RANKS[6]
            if (all_equal(values[:2]) and all_equal(values[2:])):
                self.cards_by_rank = [values[2:], values[:2]]
            else:
                self.cards_by_rank = [values[:3], values[3:]]
        elif all_equal(suites):
            self.rank = self.RANKS[5]
            self.cards_by_rank = [values[-1::-1]]
        elif consequtive(values):
            self.rank = self.RANKS[4]
            self.cards_by_rank = [values[-1::-1]]
        elif all_equal(values[:3]) or all_equal(values[1:4]) or all_equal(values[2:]):
            self.rank = self.RANKS[3]
            if all_equal(values[:3]):
                self.cards_by_rank = [values[:3], values[4:2:-1]]
            elif all_equal(values[1:4]):
                self.cards_by_rank = [values[1:4], [values[4], values[0]]]
            else:
                self.cards_by_rank = [values[2:], values[1::-1]]
        elif (all_equal(values[:2]) and (all_equal(values[2:4]) or all_equal(values[3:]))) or\
             (all_equal(values[1:3]) and all_equal(values[3:])):
            self.rank = self.RANKS[2]
            if all_equal(values[:2]) and all_equal(values[2:4]):
                self.cards_by_rank = [values[2:4], values[:2], [values[4]]]
            elif all_equal(values[:2]) and all_equal(values[3:]):
                self.cards_by_rank = [values[3:], values[:2], [values[2]]]
            else:
                self.cards_by_rank = [values[3:], values[1:3], [values[0]]]
        elif all_equal(values[:2]) or all_equal(values[1:3]) or all_equal(values[2:4]) or all_equal(values[3:]):
            self.rank = self.RANKS[1]
            if all_equal(values[:2]):
                self.cards_by_rank = [values[:2], values[4:1:-1]]
            elif all_equal(values[1:3]):
                self.cards_by_rank = [values[1:3], values[4:2:-1] + [values[0]]]
            elif all_equal(values[2:4]):
                self.cards_by_rank = [values[2:4], [values[4]] + values[1::-1]]
            else:
                self.cards_by_rank = [values[3:], values[2::-1]]
        else:
            self.rank = self.RANKS[0]
            self.cards_by_rank = [values[-1::-1]]

    def __gt__(self, other_hand):

        if self.rank > other_hand.rank:
            return True
        elif other_hand.rank > self.rank:
            return False

        if self.rank == other_hand.rank:
            for i in xrange(len(self.cards_by_rank)):
                for j in xrange(len(self.cards_by_rank[i])):
                    if self.cards_by_rank[i][j] > other_hand.cards_by_rank[i][j]:
                        return True
                    elif self.cards_by_rank[i][j] < other_hand.cards_by_rank[i][j]:
                        return False
        print "Something wrong!"

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
                print "Shit! Something wrong with these hands:\n", first_hand, second_hand

    print "First win = ", first_win
    print "Second win = ", second_win

if __name__ == "__main__":
    task54(sys.argv[1])
