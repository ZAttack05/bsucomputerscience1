"""
File: student.py
Resources to manage a student's name and test scores.
"""

from random import shuffle


class Student(object):
    """Represents a student."""

    def __init__(self, name, number, age):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        self.age = age
        for count in range(number):
            self.scores.append(0)

    def getAge(self):
        return self.age
    
    def setName(self, newName):
        self.name = newName
        
    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        if len(self.scores)==0:
            return "No score"
        else:
            return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
    
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, other):
        """Tests the two strings of the two students for equality"""
        if self.name == other.name:
            return True
        else:
            return False

    def __lt__(self, other):
        """Tests the two strings of the two students to see if one is less than the other"""
        if self.name < other.name:
            return True
        else:
            return False
    
    def __ge__(self, other):
        """Tests the two strings of the two students to see if one is greater than or equal to the other"""
        if self.name >= other.name:
            return True
        else:
            return False

"""The main function of the program"""
def main():
    """Gathers inputs for student names. Mainly to make multiple tests cases easier."""
    s1 = input("Please enter the first student's name: ")
    s2 = input("Please enter the second student's name: ")

    """Assigns user-inputed names into 2 student variables in the student class"""
    student1 = Student(s1, 6, 20)
    student2 = Student(s2, 6, 20)
    
    """Prints the results of comparisons"""
    print("The students names are equal: " + str(student2 == student1))
    print(s2 + " is less than " + s1 + ": " + str(student2 < student1))
    print(s2 + " is greater than or equal to " + s1 + ": " + str(student2 >= student1))

if __name__ == "__main__":
    main()


