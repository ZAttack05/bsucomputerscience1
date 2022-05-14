"""
ex2.py
Plays a game where the computer tries to guess the user's number
"""

from breezypythongui import EasyFrame
#Imports

class compGuess(EasyFrame):
    """Guesses numbers between 1-100 given ranges by the user"""
    def __init__(self):
        """Initializes the game"""
        greeting="Click New Game to Start"
        EasyFrame.__init__(self, title="Guessing Game")
        self.Small=self.addButton(text="Too Small",row=2,column=1,command=self.Small,state="disabled")
        self.Large=self.addButton(text="Too Large",row=2,column=2, command=self.Large,state="disabled")
        self.Correct=self.addButton(text="Correct",row=2,column=3, command=self.Correct,state="disabled")
        self.New=self.addButton(text="New Game",row=3,column=2, command=self.NewGame)
        self.guessLabel = self.addLabel(text = greeting,row=0,column=2,sticky="N")
        #Adds widgets for 4 buttons(New Game, Too Large, Too Small, and Correct), and a label which shows the guesses.
        
    def NewGame(self):
        """Resets all values and chooses 50 as its first guess"""
        self.count=50
        self.upper=101
        self.lower=0
        self.guessCount=1
        self.guessLabel["text"] = "My guess is " + str(self.count)
        self.Small["state"]="normal"
        self.Correct["state"]="normal"
        self.Large["state"]="normal"
        
    def Large(self):
        """Uses upper and lower ranges to decrease the value of the next guess"""
        self.guessCount+=1
        self.upper=self.count
        avg=self.upper+self.lower
        self.count=avg//2
        self.guessLabel["text"] = "My next guess is " + str(self.count)
        
    def Small(self):
        """Uses upper and lower ranges to increase the value of the next guess"""
        self.guessCount+=1
        self.lower=self.count
        avg=self.upper+self.lower
        self.count=avg//2
        self.guessLabel["text"] = "My next guess is " + str(self.count)

        
    def Correct(self):
        """Disables all buttons and tells the user how many tries the computer took"""
        if self.guessCount==1:
            self.guessLabel["text"] = "I guessed your number in " + str(self.guessCount) + " Try"
        else:
            self.guessLabel["text"] = "I guessed your number in " + str(self.guessCount) + " Tries"
        self.Small["state"]="disabled"
        self.Correct["state"]="disabled"
        self.Large["state"]="disabled" 
        
def main():
    """The main function of the program"""
    compGuess().mainloop()

if __name__=="__main__":
    main()
