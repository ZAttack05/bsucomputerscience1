"""
ex1.py
Converts temperature between Fahrenheit and Celsius
"""

from breezypythongui import EasyFrame
#Imports EasyFrame

class tempConverter(EasyFrame):
    """Initialzie Window for conversion"""
    def __init__(self):
        """Initializes GUI Elements"""
        EasyFrame.__init__(self, title="Temperature Converter")
        self.addLabel(text="Fahrenheit",row=0,column=0)
        self.addLabel(text="Celsius",row=0,column=3)
        self.addButton(text=">>>>",row=1,column=2,command=self.Celsius)
        self.addButton(text="<<<<",row=2,column=2,command=self.Fahrenheit)
        self.Fahrenheit=self.addFloatField(32.0,row=1,column=1,precision=1)
        self.Celsius=self.addFloatField(0.0,row=1,column=3,precision=1)
        #Creates two text fields, two labels for the text field, and two buttons for conversion.

    def Celsius(self):
        """Converts to Celsius"""
        f=self.Fahrenheit.getNumber()
        c=(f-32) * .5556
        self.Celsius.setNumber(c)
    def Fahrenheit(self):
        """Converts to Fahrenheit"""
        c=self.Celsius.getNumber()
        f=c*9/5+32
        self.Fahrenheit.setNumber(f)
def main():
    """The main function of the program"""
    tempConverter().mainloop()

if __name__=="__main__":
    main()
    
