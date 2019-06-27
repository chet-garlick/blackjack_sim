class Player:

    hand = []
    hand_value = 0
    playing_current_hand = True
    busted = False
    wins = 0

    def __init__(self, hand, aggression_level):      
        self.aggression_level = aggression_level
        self.hand = hand
        self.update_hand_value()

    def new_hand(self, new_hand):
        self.playing_current_hand = True
        self.busted = False
        self.hand = new_hand
        self.update_hand_value()

    def update_hand_value(self):
        self.hand_value = 0
        for card in self.hand:
            self.hand_value += card.get_point_value()

    def get_hand_value(self):
        return self.hand_value

    def decision(self):
        if(self.playing_current_hand):
            if(self.hand_value < self.aggression_level):
                #self.hit()
                return True
            else:
                self.playing_current_hand = False
                return False
        else:
            return False

    def hit(self, new_card):
        self.hand.append(new_card)
        self.update_hand_value()
        if(self.hand_value > 21):
            self.playing_current_hand = False
            self.busted = True
        else:
            self.decision()

    def is_busted(self):
        return self.busted
