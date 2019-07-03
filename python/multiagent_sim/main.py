import time
import Game

def main():

    default_aggression = 14
    num_decks_in_shoe = 6
    num_players = num_players_prompt()
    print("Default aggression level: " + str(default_aggression))
    num_rounds = num_rounds_prompt()
    print("Default number of decks in shoe: " + str(num_decks_in_shoe))
    start = time.time()
    new_game = Game.Game(num_players, default_aggression, num_decks_in_shoe, num_rounds)
    end = time.time()
    print(str( end - start ) + " seconds elapsed for this simulation.")

def num_players_prompt():
    print("How many players do you want? Minimum: 1 player. Maximum: 100 players.")

    num_players = input()
    return num_players
    #if type(num_players) is int:
    #    if(num_players > 0 and num_players < 100):
    #        return num_players
    #    else:
    #        print("Input something in the right range. Please try again.")
    #else:
    #    print("Something went wrong. Please try again.")
    

def num_rounds_prompt():
    print("How many rounds do you want to simulate?")
    num_rounds = input()
    return num_rounds

    #if type(num_rounds) is int:
    #    if(num_rounds > 0):
    #        return num_rounds
    #    else:
    #        print("Cannot have negative rounds. Please try again.")
    #else:
    #    print("Something went wrong. Please try again.")


main()
