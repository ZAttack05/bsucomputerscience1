"""
File: listboxdemo.py
"""

from breezypythongui import EasyFrame

class ListBoxDemo(EasyFrame):
    """Illustrates command buttons and user events."""

    def __init__(self):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, title = "Button Demo")

        # A single label in the first row.
        self.addLabel(text = "Please select one item:",
                                   row = 0, column = 0,
                                   columnspan = 1, sticky = "NSEW")

        # Two command buttons in the second row.
        self.myListBox = self.addListbox(row = 1, column = 0,
                                         listItemSelected = self.listItemSelected)
        self.myListBox.insert(0, "A")
        self.myListBox.insert(1, "B")
        self.myListBox.insert(2, "C")
        self.myListBox.insert(3, "D")
        self.myListBox.insert(4, "E")
        self.myListBox.insert(5, "F")
        self.myListBox.insert(6, "G")
        self.myListBox.insert(7, "H")
        self.myListBox.insert(8, "I")
        # A display label in the third row.
        self.dispLabel = self.addLabel(text = "Your selection is:",
                                   row = 3, column = 0,
                                   sticky = "NSEW")
    # Methods to handle user events.
    def listItemSelected(self, index):
        """Responds to the selection of an item in the list box.
        Updates the label fields with the current item."""
        self.dispLabel["text"]="Your selection is: " + self.myListBox.getSelectedItem()

def main():
    """Instantiate and pop up the window."""
    ListBoxDemo().mainloop()

if __name__ == "__main__":
    main()
