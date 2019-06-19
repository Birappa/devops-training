class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname.upper(), self.lastname.upper())
x = Person("John", "Doe")
x.printname()