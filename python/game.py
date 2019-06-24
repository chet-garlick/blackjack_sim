from random import shuffle

NUM_PLAYERS = 4
LOW_AGGRESSION = 13
VERY_LOW_AGGRESSION = 12
MEDIUM_AGGRESSION = 14
HIGH_AGGRESSION = 15
VERY_AGGRESSION = 16
NUM_DECKS_IN_SHOE = 6
DECK_SIZE = 52

SHOE = []

def init_shoe():
    for i in range(NUM_DECKS_IN_SHOE):
        for j in range(52):
            if( j < 4 ): card = Card('2',2)
            elif( j >= 4 and j < 8): card = Card('3',3)
            elif (j >=8 and j < 12): card = Card('4',4)
            elif (j >=8 and j < 12): card = Card('5',5)            
            elif (j >=8 and j < 12): card = Card('6',6)
            elif (j >=8 and j < 12): card = Card('7',7)
            elif (j >=8 and j < 12): card = Card('8',8)
            elif (j >=8 and j < 12): card = Card('9',9)
            elif (j >=8 and j < 12): card = Card('T',10) 
            elif (j >=8 and j < 12): card = Card('J',10)
            elif (j >=8 and j < 12): card = Card('Q',10)
            elif (j >=8 and j < 12): card = Card('K',10)
            elif (j >=8 and j < 12): card = Card('A',11)

            SHOE.append(card) 
            SHOE.shuffle()


def new_round():
    pass
