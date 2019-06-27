import random
import Card
import naive_player
import dealer
import time


NUM_PLAYERS = 4
LOW_AGGRESSION = 13
VERY_LOW_AGGRESSION = 12
MEDIUM_AGGRESSION = 14
HIGH_AGGRESSION = 15
VERY_HIGH_AGGRESSION = 16
DEALER_AGGRESSION = 17
NUM_DECKS_IN_SHOE = 6
DECK_SIZE = 52
NUM_SIMULATED_ROUNDS = 10000
SHOE = []
PLAYERS = []
DEALER = dealer.Dealer(DEALER_AGGRESSION) 
def init_shoe():
    new_shoe = []
    for i in range(NUM_DECKS_IN_SHOE):
        for j in range(52):
            if( j < 4 ): card = Card.Card('2',2)
            elif( j >= 4 and j < 8): card = Card.Card('3',3)
            elif (j >=8 and j < 12): card = Card.Card('4',4)
            elif (j >=8 and j < 12): card = Card.Card('5',5)            
            elif (j >=8 and j < 12): card = Card.Card('6',6)
            elif (j >=8 and j < 12): card = Card.Card('7',7)
            elif (j >=8 and j < 12): card = Card.Card('8',8)
            elif (j >=8 and j < 12): card = Card.Card('9',9)
            elif (j >=8 and j < 12): card = Card.Card('T',10) 
            elif (j >=8 and j < 12): card = Card.Card('J',10)
            elif (j >=8 and j < 12): card = Card.Card('Q',10)
            elif (j >=8 and j < 12): card = Card.Card('K',10)
            elif (j >=8 and j < 12): card = Card.Card('A',11)

            new_shoe.append(card) 
            
    random.shuffle(new_shoe)

    return new_shoe

def first_round(SHOE):


    for i in range( NUM_PLAYERS ) :

        tmp_hand = []
        tmp_hand.append(SHOE.pop())
        tmp_hand.append(SHOE.pop())
        player = naive_player.Player(tmp_hand, MEDIUM_AGGRESSION)
        PLAYERS.append(player)

    tmp_hand = []
    tmp_hand.append(SHOE.pop())
    tmp_hand.append(SHOE.pop())
    #dealer = dealer.Dealer(tmp_hand, DEALER_AGGRESSION)
    DEALER.new_hand(tmp_hand)

def new_round(SHOE):
    
    if(len(SHOE) < 30):
        SHOE = init_shoe()
     
    #DEAL HANDS
    for p in PLAYERS:
        tmp_hand = []
        tmp_hand.append(SHOE.pop())
        tmp_hand.append(SHOE.pop())
        p.new_hand(tmp_hand)
        

    dealer_hand = []
    dealer_hand.append(SHOE.pop())
    dealer_hand.append(SHOE.pop())
    DEALER.new_hand(dealer_hand)

    #GAME LOOP
    for p in PLAYERS:
        if ( p.decision() ):
            p.hit(SHOE.pop())

    DEALER.decision()

    if(DEALER.is_busted()):
        for p in PLAYERS:
            if(not p.is_busted()):
                p.wins+=1
            else:
                DEALER.wins += 1
    else:
        for p in PLAYERS:
            if(not p.is_busted()):
                if ( p.get_hand_value() > DEALER.get_hand_value() ):
                    p.wins+=1
                elif ( p.get_hand_value() < DEALER.get_hand_value() ):
                    DEALER.wins+=1
            else:
                DEALER.wins+=1





def main():
    start = time.time()
    SHOE = init_shoe()
    first_round(SHOE)
    for i in range(NUM_SIMULATED_ROUNDS):
        new_round(SHOE)
    for j in range(NUM_PLAYERS):
        print("player " + str(j) + " won " + str(PLAYERS[j].wins) + " rounds.")

    print("The dealer won " + str(DEALER.wins) + " rounds.")
    end = time.time()
    print(str( end - start ) + " seconds elapsed for this simulation.")


main()
