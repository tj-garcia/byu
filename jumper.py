"""
File: game1.py
Author: Tyrone Garcia
Purpose: word gess game with classes
"""

import random
# Control game actions
class computer:
    def __init__(self):
        self.WordList = ["bat", "cat", "dog"]
        self.WordSelected = ""
        self.letters = []
        self.wrongLetters = []
        self.attemps = 0
        self.EndGame = "N"

    # Select a random word of the list
    def SelectWord(self):
        self.WordSelected = self.WordList[random.randint(0, len(self.WordList))-1]
        for x in range(len(self.WordSelected)):
            self.letters.append("_")


    # Draw player´s parachute:
    # Each wrong attemp do NOT draw a parachute part
    # player have only 4 attemps   
    def show(self):
        print()
        # Draw a man with the parachute
        if self.attemps < 1:
            print("  _")
        if self.attemps < 2:
            print("/ _ \\")
        if self.attemps < 3:
            print("\\   /")
        if self.attemps < 4:
            print(" \\ /")
        if self.attemps == 4:
            print("  X")
        else:
            print("  0")
        print("/ | \\")
        print("/   \\")
        print()
        print("")
        # Print the letters in the selected word
        for x in range(len(self.WordSelected)):
            print(self.letters[x], end=" ")
        print()
    
    # Ask the user for a new letter
    # and append it to the preview get letters
    def question(self):
        while self.EndGame == "N":
            option = ""
            while (not option.lower().isalpha()) or (len(option)!=1):
                option = input("Guess a letter [a-z]: " )
            self.searchLetter(option)


    #Search the letter in the list and determine if the game was ended
    def searchLetter(self, letter):
        exist = 0
        position = 0
        try:
            while position != -1 :
                position = self.WordSelected.find(letter, position, len(self.WordSelected))
                if position != -1:
                    exist = 1
                    self.letters[position] = letter
                    position += 1
        except:
            pass
        if exist == 0:
            self.attemps += 1
            self.wrongLetters.append(letter)
            if self.attemps == 4:
                self.ShowEnd(1)
                self.EndGame = "Y"
        if "_" not in self.letters: #self.letters.find("_", 0, len(self.letters))!=-1:
            self.ShowEnd(0)
            self.EndGame = "Y"
        self.show()

    # Show the correct message at the end of the game
    def ShowEnd(self, result):
        if result == 1:
            print("...............")
            print("...Game Over...")
            print("...............")
        else:
            print("...............")
            print("... You Won ...")
            print("...............")

# Main program
game1 = computer()
game1.SelectWord()
game1.show()
game1.question()

