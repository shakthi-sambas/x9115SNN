"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *

class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        self.rank = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.rank[card.rank] = self.rank.get(card.rank, 0) + 1
    
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            # print val
            if val >= 5:
                return True
        return False
        
    def has_pair(self):
        self.suit_hist()
        num_pairs = 0
        for val in self.rank.values():
            if val == 2:
                num_pairs = num_pairs + 1
        if num_pairs == 1:
            return True
        else:
            return False
            
    def has_twopair(self):
        self.suit_hist()
        num_pairs = 0
        for val in self.rank.values():
            if val == 2:
                num_pairs = num_pairs + 1
        if num_pairs == 2:
            return True 
        else:
            return False
    
    def has_threeofakind(self):
        self.suit_hist()
        three_of_a_kind = 0
        for val in self.rank.values():
            if val == 3:
                three_of_a_kind = three_of_a_kind + 1
        if three_of_a_kind == 1:
            return True 
        else:
            return False
            
    def has_fourofakind(self):
        self.suit_hist()
        four_of_a_kind = 0
        for val in self.rank.values():
            if val == 4:
                four_of_a_kind = four_of_a_kind + 1
        if four_of_a_kind == 1:
            return True 
        else:
            return False
            
    def has_fullhouse(self):
        self.suit_hist()
        three_of_a_kind = 0
        pair = 0
        for val in self.rank.values():
            if val == 3:
                three_of_a_kind = three_of_a_kind + 1
            if val == 2:
                pair = pair + 1
        if three_of_a_kind == 1 and pair == 1:
            return True
        else:
            return False
        
    def has_straight(self):
        aces_both_sides_rank = self.rank
        aces_both_sides_rank[14] = self.rank.get(1, 0) # copy aces to the end of the dict to cover Ace coming on both sides in a straight hand.
        num_continuous_cards = 0
        for i in range(1, 14):
            if aces_both_sides_rank.get(i, 0) >= 1 and aces_both_sides_rank.get(i+1, 0) >= 1:
                num_continuous_cards = num_continuous_cards + 1
                if num_continuous_cards == 4:
                    return True
            else: 
                num_continuous_cards = 0
        else: 
            return False

    def has_straightflush(self):
        card_dict = {}
        for card in self.cards:
            if card.suit in card_dict:
                card_dict[card.suit].append(card.rank)
                if card.rank == 1:
                    card_dict[card.suit].append(14)
            else:
                card_dict[card.suit] = [card.rank]
                if card.rank == 1:
                    card_dict[card.suit].append(14)
        for key, value in card_dict.iteritems():
            value = sorted(value)
            if len(value) >=5:
                no_continuous_values = 0
                for i in range(len(value)-1):
                    if value[i] == value[i+1] - 1:
                        no_continuous_values = no_continuous_values + 1
                        
                if no_continuous_values >= 4:
                    return True
        return False
                    
    def classify(self, result_list):
        hand_probability_order = ['Straight Flush', '4 of a kind', 'Full House', 'Flush', 'Straight', '3 of a kind', '2 pair', 'Pair']
        for i in range(len(result_list)):
            if result_list[i] == True:
                self.label = hand_probability_order[i]
                return hand_probability_order[i]
        return "No Hand"
        
def shuffle_divide_classify_count(num_hands, cards_per_player):
    
    num_straight_flush = 0
    num_four_a_kind = 0
    num_full_house = 0
    num_flush = 0
    num_straight = 0
    num_three_a_kind = 0
    num_two_pair = 0
    num_pair = 0

    for hand in range(num_hands):
        deck = Deck()
        deck.shuffle()
        deck.shuffle()
    
        # deal the cards and classify the hands
        # for i in range(2):
        hand = PokerHand()
        deck.move_cards(hand, cards_per_player)
        hand.sort()
        # print hand
        flush = hand.has_flush()
        if flush:
            num_flush = num_flush+1
        # print 'Has Flush: %s' % flush
        pair =  hand.has_pair()
        if pair:
            num_pair = num_pair+1
        # print 'Has One Pair: %s' % pair
        two_pair = hand.has_twopair()
        if two_pair:
            num_two_pair = num_two_pair+1
        # print 'Has Two Pairs: %s' % two_pair
        three_of_a_kind = hand.has_threeofakind()
        if three_of_a_kind:
            num_three_a_kind = num_three_a_kind + 1
        # print 'Has Three of a Kind: %s' % three_of_a_kind
        four_of_a_kind = hand.has_fourofakind()
        if four_of_a_kind:
            num_four_a_kind = num_four_a_kind+1
        # print 'Has Four of a Kind: %s' % four_of_a_kind
        full_house = hand.has_fullhouse()
        if full_house:
            num_full_house = num_full_house+1
        # print 'Has Full House: %s' % full_house
        straight = hand.has_straight()
        if straight:
            num_straight = num_straight+1
        # print 'Has Straight: %s' % straight
        straight_flush = hand.has_straightflush()
        if straight_flush:
            num_straight_flush = num_straight_flush+1
        # print 'Has Straight Flush: %s' % straight_flush
        result_list = [straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pair, pair]
        hand.classify(result_list)
        # if hand.label:
        #     print "Best hand: %s" % hand.label
        # else:
        #     print "Best hand: None"
        # print ''
    return [num_pair, num_two_pair, num_three_a_kind, num_straight, num_flush, num_full_house, num_four_a_kind, num_straight_flush]


def display_classification_numbers(num_hands_shuffled, classification_list):
    print "Number of Hands shuffled: %s" % num_hands_shuffled
    print "Number of Pairs: %s   Probability : %s %%" % (classification_list[0], float(classification_list[0]) * 100 / num_hands_shuffled)
    print "Number of Two Pairs: %s   Probability : %s %%" % (classification_list[1], float(classification_list[1]) * 100 / num_hands_shuffled)
    print "Number of Three of a Kind: %s   Probability : %s %%" % (classification_list[2], float(classification_list[2]) * 100 / num_hands_shuffled)
    print "Number of Straight: %s   Probability : %s %%" % (classification_list[3], float(classification_list[3]) * 100 / num_hands_shuffled)
    print "Number of Flush: %s   Probability : %s %%" % (classification_list[4], float(classification_list[4]) * 100 / num_hands_shuffled)
    print "Number of Full House: %s   Probability : %s %%" % (classification_list[5], float(classification_list[5]) * 100 / num_hands_shuffled)
    print "Number of Four of a Kind: %s   Probability : %s %%" % (classification_list[6], float(classification_list[6]) * 100 / num_hands_shuffled)
    print "Number of Straight Flush: %s   Probability : %s %%" % (classification_list[7], float(classification_list[7]) * 100 / num_hands_shuffled)
    print ""
     
if __name__ == '__main__':
    # make a deck
    num_hands_shuffled_100 = 100
    num_hands_shuffled_1000= 1000
    num_hands_shuffled_10000= 10000
    
    print "For 5 cards per player: " 
    
    classification_list_100_5 = shuffle_divide_classify_count(num_hands_shuffled_100, 5)
    display_classification_numbers(num_hands_shuffled_100, classification_list_100_5)
    
    classification_list_1000_5 = shuffle_divide_classify_count(num_hands_shuffled_1000, 5)
    display_classification_numbers(num_hands_shuffled_1000, classification_list_1000_5)
    
    classification_list_10000_5 = shuffle_divide_classify_count(num_hands_shuffled_10000, 5)
    display_classification_numbers(num_hands_shuffled_10000, classification_list_10000_5)
    
    print "For 7 cards per player: "
    
    classification_list_100_7 = shuffle_divide_classify_count(num_hands_shuffled_100, 7)
    display_classification_numbers(num_hands_shuffled_100, classification_list_100_7)
    
    classification_list_1000_7 = shuffle_divide_classify_count(num_hands_shuffled_1000, 7)
    display_classification_numbers(num_hands_shuffled_1000, classification_list_1000_7)
    
    classification_list_10000_7 = shuffle_divide_classify_count(num_hands_shuffled_10000, 7)
    display_classification_numbers(num_hands_shuffled_10000, classification_list_10000_7)
