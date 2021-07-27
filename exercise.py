#! /usr/bin/env python3
# Purpose: Exercise for Lecture 1
import random

class PlayingCard:
    ''' A standard playing card (singular). It has a suit and a number.'''


    SUIT_NAMES = {0 : 'Hearts', 1 : 'Diamonds', 2 : 'Clubs', 3 : 'Spades'}
    NUMBER_NAMES = {1 : 'Ace', 2 : 'Two', 3 : 'Three', 4 : 'Four',
                    5 : 'Five', 6 : 'Six', 7 : 'Seven', 8 : 'Eight',
                    9 : 'Nine', 10 : 'Ten', 11 : 'Jack', 12 : 'Queen',
                    13 : 'King'}

                    
    def __init__(self, suit, number):
        self.NUMBER_NAMES = number
        self.SUIT_NAMES = suit
        
    
    def __str__(self):
        ''' Make sure you can print a pretty representation of the card.'''
        for a in SUIT_NAMES:
            for b in NUMBER_NAMES:
                print(NUMBER_NAMES[b], 'of', SUIT_NAMES[a])
                
class Deck:
    ''' A container of playing cards.  The deck has 52 total cards.'''

    
    SUIT_NAMES = {0 : 'Hearts', 1 : 'Diamonds', 2 : 'Clubs', 3 : 'Spades'}
    NUMBER_NAMES = {1 : 'Ace', 2 : 'Two', 3 : 'Three', 4 : 'Four',
                    5 : 'Five', 6 : 'Six', 7 : 'Seven', 8 : 'Eight',
                    9 : 'Nine', 10 : 'Ten', 11 : 'Jack', 12 : 'Queen',
                    13 : 'King'}

    
    def __init__(self):
        self.cards = []
        self.rcd = []
        self.flag = []
        self.NUMBER_NAMES = number
        self.SUIT_NAMES = suit
        self.choice = random.choice(card)
        pass
                        
    def shuffle(self):
        pass
                
    def draw(self, num=1):
        ''' Select and return one (or more) of the top card(s) from the deck.  
            A card that has been drawn is no longer in the deck.
            
            num -- the number of cards to be drawn.'''

                    
                
    def __str__(self):
        for a in SUIT_NAMES:
            for b in NUMBER_NAMES:
                card.append[NUMBER_NAMES[b], 'of', SUIT_NAMES[a]]             
        
def main():
    ''' Draw cards from a shuffled deck until you get a duplicate NUMBER.
        For instance, you would stop drawing after you have seen a second Ace.
        
        Print the number of cards drawn and the number of Diamonds seen.
    '''
    d = Deck()
    drawn = 0
    diamonds = 0
    while sum(flag) == 0:
        for i in rcd:
            if i == choice:
                flag.append(a)
            else:
                flag.append(0)
        rcd.append(choice)
        card.remove(choice)
        drawn += 1
        if choice.count('Diamond') > 0:
            diamonds += 1
        
    
    
    # Needs more code here!

    print(f'{drawn} cards were drawn, resulting in {diamonds} Diamonds')    
    
if __name__ == "__main__":
    main()
