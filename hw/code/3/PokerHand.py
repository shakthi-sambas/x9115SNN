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
        #TODO
        pass

    def has_straightflush(self):
        #TODO
        pass
    
if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(2):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print 'Has Flush: %s' % hand.has_flush()
        print 'Has One Pair: %s' % hand.has_pair()
        print 'Has Two Pairs: %s' % hand.has_twopair()
        print 'Has Three of a Kind: %s' % hand.has_threeofakind()
        print 'Has Four of a Kind: %s' % hand.has_fourofakind()
        print 'Has Full House: %s' % hand.has_fullhouse()
        print ''
