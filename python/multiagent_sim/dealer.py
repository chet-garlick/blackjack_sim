import Card
import naive_player
class Dealer(naive_player.Player):

    def __init__(self,aggression):
         
        self.hand.append(Card.Card("2",2))
        self.hand.append(Card.Card("K",10))
        self.aggression_level = aggression
