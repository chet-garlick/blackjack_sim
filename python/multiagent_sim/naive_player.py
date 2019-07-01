class Player:

    hand = []
    hand_value = 0
    playing_current_hand = True
    busted = False
    result = ""
    wins = 0

    def __init__(self, hand, aggression_level):      
        self.aggression_level = aggression_level
        self.hand = hand
        self.update_hand_value()

    def __init__(self, aggression_level):
        self.aggression_level = aggression_level

    def new_hand(self, new_hand):
        self.playing_current_hand = True
        self.busted = False
        self.hand = new_hand
        self.update_hand_value()

    def update_hand_value(self):
        self.hand_value = 0
        has_high_ace = False
        for card in self.hand:
            self.hand_value += card.get_point_value()
            if(card.get_point_value() == 11):
                has_high_ace = True

        if(self.hand_value > 21 and has_high_ace):
            for c in hand:
                if (c.get_point_value() == 11):
                    c.swap_ace_value()
                    self.hand_value = self.hand_value - 10
                    break

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

    def get_result(self):
        return self.result

    def set_result(self, new_res):
        self.result = new_res

    def hand_to_string(self):
        str_hand = ""
        for c in self.hand:
            str_hand.append(c.get_face_value())
