import random
import Card
import naive_player as player
import dealer as d
import time
import csv

class Game:

    shoe = []
    players = []
    dealer = d.Dealer(17)
    results_filepath = "results.txt"
    csv_file = "results.csv"

    def __init__(self, num_players, default_aggression, num_decks_in_shoe, num_simulated_rounds):
        self.num_players = int(num_players)
        self.default_aggression = int(default_aggression)
        self.num_decks_in_shoe = int(num_decks_in_shoe)
        self.num_simulated_rounds = int(num_simulated_rounds)
        for i in range(self.num_players):
            self.players.append(player.Player(self.default_aggression))

        self.start_sim()

    def new_shoe(self):
        new_shoe = []
        for i in range(self.num_decks_in_shoe):
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

                new_shoe.append(card) 
        random.shuffle(new_shoe)

        self.shoe = new_shoe


    def new_hand(self):

        for p in self.players:
            tmp_hand = []
            tmp_hand.append(self.shoe.pop())
            tmp_hand.append(self.shoe.pop())
            p.new_hand(tmp_hand)

        dealer_hand = []
        dealer_hand.append(self.shoe.pop())
        dealer_hand.append(self.shoe.pop())
        self.dealer.new_hand(dealer_hand)

        for p in self.players:
            while(p.get_playing()):
                if(p.decision()):
                    p.hit(self.shoe.pop())

        while(self.dealer.get_playing()):
            if(self.dealer.decision()):
                self.dealer.hit(self.shoe.pop())

        if(self.dealer.is_busted()):
            for play in self.players:
                if(not play.is_busted()):
                    play.wins += 1
                    play.set_result("Win. Dealer bust.")
        else:
            for player in self.players:
                if(not player.is_busted()):
                    if(player.get_hand_value() > self.dealer.get_hand_value() ):
                        player.wins += 1
                        player.set_result("Win. Closer to 21 than dealer.")
                    elif(player.get_hand_value() < self.dealer.get_hand_value() ):
                        self.dealer.wins += 1
                        player.set_result("Loss. Dealer had better hand.")
                    else:
                        player.set_result("Push. Same score as dealer.")
                else:
                    self.dealer.wins += 1

        self.report_hand()


    def report_hand(self):
        results_file = open(self.results_filepath,"a")
        results_file.write("===== New Hand =====\n")
        results_file.write("Number of players: " + str(self.num_players) + " \n" )
        i=0
        for p in self.players:
            i += 1
            results_file.write("Player: " + str(i) + " " )
            results_file.write(p.get_result())
            results_file.write(p.hand_to_string())
        results_file.write("Dealer hand: " + self.dealer.hand_to_string())
        results_file.write("\n===== End of Hand =====\n")
        results_file.close()




    def start_sim(self):

        for i in range(self.num_simulated_rounds):
            if(len(self.shoe) < 50):
                self.new_shoe()
            self.new_hand()

        results_file = open(self.results_filepath, "a")
        dealer_result_string = ("Dealer won " + str(self.dealer.wins) + " hands.")
        print(dealer_result_string)
        results_file.write(dealer_result_string)
        j=0
        for p in self.players:
            j+=1
            tmp_player_res_string = ("Player " + str(j) + " won  " + str(p.wins) + " hands. ")
            print(tmp_player_res_string)
            results_file.write(tmp_player_res_string)
        print("\n")
        results_file.close()






    

