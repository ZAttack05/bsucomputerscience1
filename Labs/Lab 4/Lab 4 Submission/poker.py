"""
File: cards.py

Module for playing cards, with classes Card, Deck, and Poker
"""

import random
from breezypythongui import EasyFrame
from tkinter import PhotoImage

'''Handles the GUI and rules of the game of my version of Poker'''
class Poker(EasyFrame):

    def __init__(self):
        """Sets up the window, widgets, and variables needed to run the game"""
        EasyFrame.__init__(self, title = "Poker, but I don't know the rules")

        self.uwins = 0
        self.owins = 0
        self.b = PhotoImage(file = "DECK/b.gif")

        self.nocard1 = None
        self.nocard2 = None
        self.nocard3 = None
        self.nocard4 = None
        self.nocard5 = None

        self.nucard1 = None
        self.nucard2 = None
        self.nucard3 = None
        self.nucard4 = None
        self.nucard5 = None
        
        self.utotal = 0
        self.ototal = 0

        self.ocard1 = self.addLabel(text = "", row = 1, column = 1, sticky="NSEW")
        self.ocard1["image"] = self.b

        self.ocard2 = self.addLabel(text = "", row = 1, column = 2, sticky="NSEW")
        self.ocard2["image"] = self.b

        self.ocard3 = self.addLabel(text = "", row = 1, column = 3, sticky="NSEW")
        self.ocard3["image"] = self.b

        self.ocard4 = self.addLabel(text = "", row = 1, column = 4, sticky="NSEW")
        self.ocard4["image"] = self.b

        self.ocard5 = self.addLabel(text = "", row = 1, column = 5, sticky="NSEW")
        self.ocard5["image"] = self.b

        self.card1 = self.addLabel(text = "", row = 3, column = 1, sticky="NSEW")
        self.card1["image"] = self.b

        self.card2 = self.addLabel(text = "", row = 3, column = 2, sticky="NSEW")
        self.card2["image"] = self.b

        self.card3 = self.addLabel(text = "", row = 3, column = 3, sticky="NSEW")
        self.card3["image"] = self.b

        self.card4 = self.addLabel(text = "", row = 3, column = 4, sticky="NSEW")
        self.card4["image"] = self.b

        self.card5 = self.addLabel(text = "", row = 3, column = 5, sticky="NSEW")
        self.card5["image"] = self.b

        self.newgame = self.addButton(text = "New Game", row = 4, column = 2, command = self.newGame)
        self.nextgame = self.addButton(text = "Next Round", row = 4, column = 4, command = self.NextRound, state= "disabled")
        self.flipu = self.addButton(text = "Flip your cards", row =5, column =3, command = self.flipCards, state = "disabled")
        self.flipo = self.addButton(text = "Flip your opponent's cards", row = 6, column = 3, command = self.FlipO, state = "disabled")
        self.winstatus = self.addLabel(text = "Click 'New Game' to Start a New Game.", row = 2, column = 3)
        self.opoints = self.addLabel(text = self.owins, row =2, column = 2)
        self.upoints = self.addLabel(text = self.uwins, row = 2, column = 4, sticky = "NSEW")

    '''Starts a new game by resetting the deck, buttons to default values, and text.'''
    def newGame(self):
        self.deck = Deck()
        for i in range(5):
            self.deck.shuffle()
        self.winstatus["text"] = "Click to reveal your cards."
        self.flipu["state"] = "active"
        self.uwins = 0
        self.owins = 0
        self.upoints["text"] = self.uwins
        self.opoints["text"] = self.owins

        self.ocard1["image"] = self.b
        self.ocard2["image"] = self.b
        self.ocard3["image"] = self.b
        self.ocard4["image"] = self.b
        self.ocard5["image"] = self.b

        self.card1["image"] = self.b
        self.card2["image"] = self.b
        self.card3["image"] = self.b
        self.card4["image"] = self.b
        self.card5["image"] = self.b

    '''Starts the next round by resetting the card total, enabling/disabling the proper buttons, and setting the cards to the back image once again.'''
    def NextRound(self):
        self.utotal = 0
        self.ototal = 0
        self.winstatus["text"] = "Click to reveal your cards."
        self.flipu["state"] = "active"
        self.nextgame["state"] = "disabled"

        self.ocard1["image"] = self.b
        self.ocard2["image"] = self.b
        self.ocard3["image"] = self.b
        self.ocard4["image"] = self.b
        self.ocard5["image"] = self.b

        self.card1["image"] = self.b
        self.card2["image"] = self.b
        self.card3["image"] = self.b
        self.card4["image"] = self.b
        self.card5["image"] = self.b

    '''This function flips all of the cards on screen to show your cards, adds the values of each card together, and displays the total.'''
    def flipCards(self):

        '''Flips the first card. Adds the value of the card to an overall total.'''
        string = str(self.deck.deal())
        if len(string) == 3:
            num = int(string[:2])
            print(str(num))
            self.utotal += num
        else:
            num = int(string[:1])
            self.utotal += num
            print(str(num))
        self.nucard1 = PhotoImage(file = "DECK/" + string + ".gif")
        self.card1["image"] = self.nucard1

        '''Flips the second card. Adds the value of the card to an overall total.'''
        string = str(self.deck.deal())
        if len(string) == 3:
            num = int(string[:2])
            print(str(num))
            self.utotal += num
        else:
            num = int(string[:1])
            self.utotal += num
            print(str(num))
        self.nucard2 = PhotoImage(file = "DECK/" + string + ".gif")
        self.card2["image"] = self.nucard2

        '''Flips the third card. Adds the value of the card to an overall total.'''
        string = str(self.deck.deal())
        if len(string) == 3:
            num = int(string[:2])
            print(str(num))
            self.utotal += num
        else:
            num = int(string[:1])
            self.utotal += num
            print(str(num))
        self.nucard3 = PhotoImage(file = "DECK/" + string + ".gif")
        self.card3["image"] = self.nucard3

        '''Flips the fourth card. Adds the value of the card to an overall total.'''
        string = str(self.deck.deal())
        if len(string) == 3:
            num = int(string[:2])
            print(str(num))
            self.utotal += num
        else:
            num = int(string[:1])
            self.utotal += num
            print(str(num))
        self.nucard4 = PhotoImage(file = "DECK/" + string + ".gif")
        self.card4["image"] = self.nucard4

        '''Flips the first card. Adds the value of the card to an overall total.'''
        string = str(self.deck.deal())
        if len(string) == 3:
            num = int(string[:2])
            print(str(num))
            self.utotal += num
        else:
            num = int(string[:1])
            self.utotal += num
            print(str(num))
        self.nucard5 = PhotoImage(file = "DECK/" + string + ".gif")
        self.card5["image"] = self.nucard5

        print(self.utotal)
        
        self.winstatus["text"] = "Your total is " + str(self.utotal) + ". Click to flip your opponents cards."
        self.flipu["state"] = "disabled"
        self.flipo["state"] = "active"

    '''Flips the opponents cards and calculates the total. Also calculates the winner.'''
    def FlipO(self):
        '''Flips the first card. Adds the value of the card to an overall total.'''
        string = str(self.deck.deal())
        if len(string) == 3:
            num = int(string[:2])
            print(str(num))
            self.ototal += num
        else:
            num = int(string[:1])
            self.ototal += num
            print(str(num))
        self.nocard1 = PhotoImage(file = "DECK/" + string + ".gif")
        self.ocard1["image"] = self.nocard1

        '''Flips the second card. Adds the value of the card to an overall total.'''
        string = str(self.deck.deal())
        if len(string) == 3:
            num = int(string[:2])
            print(str(num))
            self.ototal += num
        else:
            num = int(string[:1])
            self.ototal += num
            print(str(num))
        self.nocard2 = PhotoImage(file = "DECK/" + string + ".gif")
        self.ocard2["image"] = self.nocard2

        '''Flips the third card. Adds the value of the card to an overall total.'''
        string = str(self.deck.deal())
        if len(string) == 3:
            num = int(string[:2])
            print(str(num))
            self.ototal += num
        else:
            num = int(string[:1])
            self.ototal += num
            print(str(num))
        self.nocard3 = PhotoImage(file = "DECK/" + string + ".gif")
        self.ocard3["image"] = self.nocard3

        '''Flips the fourth card. Adds the value of the card to an overall total.'''
        string = str(self.deck.deal())
        if len(string) == 3:
            num = int(string[:2])
            print(str(num))
            self.ototal += num
        else:
            num = int(string[:1])
            self.ototal += num
            print(str(num))
        self.nocard4 = PhotoImage(file = "DECK/" + string + ".gif")
        self.ocard4["image"] = self.nocard4

        '''Flips the fifth card. Adds the value of the card to an overall total.'''
        string = str(self.deck.deal())
        if len(string) == 3:
            num = int(string[:2])
            print(str(num))
            self.ototal += num
        else:
            num = int(string[:1])
            self.ototal += num
            print(str(num))
        self.nocard5 = PhotoImage(file = "DECK/" + string + ".gif")
        self.ocard5["image"] = self.nocard5

        '''Since this will be the last function the player touches before a new round or game is started, the calculation for who won is located here.'''
        if self.utotal > self.ototal:
            self.uwins = self.uwins + 1
            print(str(self.uwins))
            self.upoints["text"] = str(self.uwins)
            if self.uwins == 2:
                self.winstatus["text"] = "Congratulations, you have won the game. Click new game to start a new game." + "\nYour opponent's score was " + str(self.ototal) + "."
            else:
                self.winstatus["text"] = "Congratulations, you have won this round. Win one more to win the game! Clikc next round to start the next round." + "\nYour opponent's score was " + str(self.ototal) + "."
                self.nextgame["state"] = "active"
        elif self.utotal < self.ototal:
            self.owins = self.owins + 1
            print(str(self.owins))
            self.opoints["text"] = str(self.owins)
            if self.owins == 2:
                self.winstatus["text"] = "Sorry, you lost. Click new game to start a new game" + "\nYour opponent's score was " + str(self.ototal) + "."
            else:
                self.winstatus["text"] = "Your opponent has won the round. If they win one more, you lose the game. Click next round to start the next round."+ "\nYour opponent's score was " + str(self.ototal) + "."
                self.nextgame["state"] = "active"
        elif self.utotal == self.ototal:
            self.winstatus["text"] = "Tie. No one gains a point. Click next roud to start the next round."+ "\nYour opponent's score was " + str(self.ototal) + "."
            self.nextgame["state"] = "active"

        self.flipo["state"] = "disabled"

class Card(object):
    """ A card object with a suit and rank."""

    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    SUITS = ('s', 'd', 'h', 'c')

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        self.rank = rank
        self.suit = suit

    
    def __str__(self):
        return str(self.rank) + self.suit

    def __lt__(self, other):
        return self.rank < other.rank

    def __len__(self):
       """Returns the number of cards left in the deck."""
       return len(str(self.rank) + self.suit)

class Deck(object):
    """ A deck containing 52 cards."""

    def __init__(self):
        """Creates a full deck of cards."""
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self.cards.append(c)

    def shuffle(self):
        """Shuffles the cards."""
        random.shuffle(self.cards)

    def deal(self):
        """Removes and returns the top card or None 
        if the deck is empty."""
        if len(self) == 0:
           return None
        else:
           return self.cards.pop(0)

    def __len__(self):
       """Returns the number of cards left in the deck."""
       return len(self.cards)

    def __str__(self): 
        """Returns the string representation of a deck."""
        result = ''
        for c in self.cards:
            result = result + str(c) + '\n'
        return result

'''Main function of the program.'''
def main():
    Poker().mainloop()

if __name__ == "__main__":
    main()