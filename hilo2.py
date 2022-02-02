"""
File: hilo2.py
Author: Tyrone Garcia
Purpose: Hi Lo guess game with classes
"""
import random

class Cards:
    """Control game course

    Attributes:
        value: to save a current value.
        old_value: to save tha value variable when the game generate a new ones.
        is_new: to select the correct message to show.
    """    
    def __init__(self):
        self.value = 0
        self.old_value = 0
        is_new = 0
        
    def generate(self):
        #Generate a new value for the value variable
        self.old_value = self.value
        self.value = int(random.uniform(1, 13))

    def show(self, is_new):
        # Show the card value in the screen     
        if is_new == 0:
            print (f"\nThe Card is: {self.value}")
        else:
            print (f"Next Card was: {self.value}")


class Person:
    """Control persona actions and game history

    Attributes:
        selection: save the player l/h selection.
        score: track the player score throught the game.
        play_again: save y/n selection of the player.
    """
    def __init__(self):
        self.selection = ""
        self.score = 300
        self.play_again = "y"

    def guess(self):
        # Compute the score if the player h/l selection was correct
        self.score += 100
        return self.score

    def no_guess(self):
        # Compute the score if the player h/l selection was NOT correct
        self.score -= 75
        return self.score

    def show_score(self):
        # Print the score in the screen
        print(f"Your score is: {self.score}")
        return self.score

    def your_turn(self):
        # Let to the user select l or n as your answer (only l or n)
        self.selection = ""
        while self.selection.lower() not in ["h", "l"]:
            try:
                self.selection = input("Higher or lower? [h/l] ")
            except:
                print("Only h or l, please")
        return self.selection

# Game from here
gamer = Person() # Instance of person
play = Cards()   # Instance of cards
# Run the game while user selection is y
while (gamer.play_again == "y") and (gamer.score > 0):
    gamer.play_again = ""
    play.generate()
    play.show(0)
    gamer.your_turn()
    play.generate()
    play.show(1)
    # Verify and compute the user selection and score
    if (gamer.selection == "l") and (play.value < play.old_value):
        gamer.guess()
    elif (gamer.selection == "l") and (play.value > play.old_value):
        gamer.no_guess()
    elif (gamer.selection == "h") and (play.value > play.old_value):
        gamer.guess()
    elif (gamer.selection == "h") and (play.value < play.old_value):
        gamer.no_guess()
    # Show the player score
    gamer.show_score()
    # ask for play again
    while (gamer.play_again.lower() not in ["y", "n"]) and (gamer.score > 0):
        gamer.play_again = input("Play again? [y/n] ")
