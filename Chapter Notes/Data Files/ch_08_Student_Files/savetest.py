"""
File: layoutdemo.py
"""

from breezypythongui import EasyFrame

class LayoutDemo(EasyFrame):
    """Displays labels in the quadrants."""

    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self)
        self.addLabel(text = "(0, 0)", row = 0, column = 0, sticky = "SE")
        self.addLabel(text = "(0, 1)", row = 0, column = 1, sticky = "SE")
        self.addLabel(text = "(1, 0)", row = 1, column = 0, sticky = "SE")
        self.addLabel(text = "(1, 1)", row = 1, column = 1, sticky = "SE")
        
        self.addLabel(text = "(0, 2)", row = 0, column = 2, \
                      sticky = "SE",rowspan=3, columnspan=3, background = 'blue')
        

def main():
    """Instantiate and pop up the window."""
    LayoutDemo().mainloop()

if __name__ == "__main__":
    main()

'''
'''
