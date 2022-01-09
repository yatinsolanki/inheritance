

#class definition

class Animal:
    #1. properties

    #2. constructor

    #3. method

    def eat(self):
        print("hello from eat method")

    def sleep(self):
        print("hello fron sleep method")

#class instatiation
#we need to create object of class

myobject = Animal()

#now you can access the members of class

myobject.eat()


#1. class definition

class dog(Animal):
    #1.properties

    #2. constructor
    def __init__(self):
        print("helllo from Dog init method")

    #3. method

    def bark(self):
        print("BHOW BHOW")

mydog = dog()
mydog.bark()

mydog.eat()