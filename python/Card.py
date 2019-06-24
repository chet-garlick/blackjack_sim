class Card:
    def __init__ (self, value, point_value):
        self.value = value
        self.point_value = point_value

    def get_point_value(self):
        return self.point_value


card = Card('2',2)
print(card.get_point_value())
