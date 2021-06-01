class Student:
    def __init__(self):
        self.__name = None
        self.__RollNumber = None

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__RollNumber
    
    def setRollNumber(self, RollNumber):
        self.__RollNumber = RollNumber

demo1 = Student()
demo1.setName("Alex")
print("Name:", demo1.getName())
demo1.setRollNumber(3789)
print("Roll Number:", demo1.getRollNumber())