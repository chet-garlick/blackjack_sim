class Card:
    def __init__ (self, value, point_value):
        self.value = value
        self.point_value = point_value

    def get_point_value(self):
        return self.point_value

    def get_face_value(self):
        return self.value
    
    def swap_ace_value(self):
        if(Card.get_face_value == "A"):
            self.point_value = 1

