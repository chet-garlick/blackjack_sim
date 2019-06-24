class Player:

    __hand__ = []
    __hand_value__ = 0


    def __init__(self, hand, aggression_level):      
        self.aggression_level = aggression_level
        self.hand = hand
        self.update_hand_value()

    def new_hand(self, new_hand):
        self.hand = new_hand
        self.update_hand_value()

    def __update_hand_value__():
        self.hand_value = 0
        for card in hand:
            self.hand_value += card.get_point_value()

    def get_hand_value():
        return self.hand_value

    def decision(self):
        pass

    def hit(self, new_card):
        self.hand.append(new_card)
        self.update_hand_value()
