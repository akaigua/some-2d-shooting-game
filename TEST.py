    SUIT_NAMES = {0 : 'Hearts', 1 : 'Diamonds', 2 : 'Clubs', 3 : 'Spades'}
    NUMBER_NAMES = {1 : 'Ace', 2 : 'Two', 3 : 'Three', 4 : 'Four',
                    5 : 'Five', 6 : 'Six', 7 : 'Seven', 8 : 'Eight',
                    9 : 'Nine', 10 : 'Ten', 11 : 'Jack', 12 : 'Queen',
                    13 : 'King'}
	for a in SUIT_NAMES:
    	for b in NUMBER_NAMES:
            print(NUMBER_NAMES[b + 1], 'of', SUIT_NAMES[a])
