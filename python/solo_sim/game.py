import Card
import random

deck = []
player_hand = []
dealer_hand = []


def create_deck():
    new_deck = []
    for j in range(52):
        if( j < 4 ): card = Card.Card('2',2)
        elif( j >= 4 and j < 8): card = Card.Card('3',3)
        elif (j >= 8 and j < 12): card = Card.Card('4',4)
        elif (j >= 12 and j < 16): card = Card.Card('5',5)            
        elif (j >= 16 and j < 20): card = Card.Card('6',6)
        elif (j >= 20 and j < 24): card = Card.Card('7',7)
        elif (j >= 24 and j < 28): card = Card.Card('8',8)
        elif (j >= 28 and j < 32): card = Card.Card('9',9)
        elif (j >= 32 and j < 36): card = Card.Card('T',10) 
        elif (j >= 36 and j < 40): card = Card.Card('J',10)
        elif (j >= 40 and j < 44): card = Card.Card('Q',10)
        elif (j >= 44 and j < 48): card = Card.Card('K',10)
        elif (j >= 48 and j < 52): card = Card.Card('A',11)

        new_deck.append(card) 
            
    random.shuffle(new_deck)

    return new_deck


def new_hand(deck,player_hand, dealer_hand):

    deck.clear()
    deck = create_deck()

    player_hand.clear()
    dealer_hand.clear() 
    player_hand.append( deck.pop() )
    dealer_hand.append( deck.pop() ) 
    player_hand.append( deck.pop() )
    dealer_hand.append( deck.pop() )
    
    game_state = player_decision(player_hand,dealer_hand[1],deck)
    player_hand = game_state[0]
    player_score = score_hand(player_hand)
    
    if(not player_score > 21):
        deck = game_state[1]
        dealer_state = dealer_decision(dealer_hand,player_score, deck)
        dealer_score = dealer_state[0]
        dealer_hand = dealer_state[1]

        
        print("The dealer's hand was: ")
        for c in dealer_hand:
            print(c.get_face_value())

        if(dealer_score > 21):
            print("You win, the dealer busted.")
 
        elif(dealer_score > player_score):  
            print("You lose, the dealer was closer to 21.")
        elif(dealer_score < player_score):
            print("You win, you were closer to 21.")
        elif(dealer_score == player_score):
            print("You push, you and the dealer had an equal score,")

def score_hand(hand):
    score = 0
    has_high_ace = False
    for c in hand:
        score += c.get_point_value()
        if(c.get_point_value() == 11):
            has_high_ace = True

    if(score > 21 and has_high_ace):
        for c in hand:
            if (c.get_point_value() == 11):
                c.swap_ace_value()
                score = score - 10
                break


    return score


def player_decision(hand,dealer_show_card,deck):
    playing = True
    print("The dealer is showing a " + dealer_show_card.get_face_value())
 
    print("Your hand is: ")
    for i in range(len(hand)):
        print(hand[i].get_face_value())
    
    hit = hit_prompt()
    if(hit):
        hand.append(deck.pop())
        if(score_hand(hand) > 21):
            print("You busted. You lose.")
            print("Your bust card was: " + hand[len(hand) - 1].get_face_value())
        else:
            player_decision(hand,dealer_show_card,deck)
    else:
        playing = False

    return (hand,deck)
    

def hit_prompt():
    print("Do you want to hit?")
    hit = input("Y/N \n")
    if (hit == "N" or hit == "n"):
        return False
    elif (hit == "Y" or hit == 'y'):
        return True
    else:
        return hit_prompt()


def play_again_prompt():
    print("Do you want to play again?")
    play_again = input("Y/N \n")
    if (play_again == "N" or play_again == "n"):
        return False
    elif (play_again == "Y" or play_again == 'y'):
        print("----------------------------")
        return True
    else:
        return play_again_prompt()


def dealer_decision(d_hand, p_score, deck):
    dealer_score = 0

    dealer_score = score_hand(d_hand)
    still_playing = True
    dealer_wins = False
    while(dealer_score < 17 and still_playing):
        if(dealer_score > p_score):
            still_playing = False
        else:
            d_hand.append(deck.pop())
            dealer_score = score_hand(d_hand)

    return (dealer_score, d_hand)


def main():
    deck = []
    player_hand = []
    dealer_hand = []
    playing = True
    while(playing):
        new_hand(deck,player_hand,dealer_hand)
        playing = play_again_prompt()
            

def hand_to_string(hand):
    output = ""
    for c in hand:
        output += c.get_face_value()
    return output

main()





