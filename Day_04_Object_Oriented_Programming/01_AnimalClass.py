#we use 'class' keyword to declare class in python

class Animal():
    
    #static/class level variable => this can be accessed either by Animal or self or class instance
    eat = "veg"
    
    #constructor  
    #note : Python provides a default constructor that takes no arguments and does nothing. if needed
    
    #default constructor
    def __init__(self):
        pass
        
    #parameterized constructor
    def __init__(self,name):
        self.name = name
    
    #method in a class
    def animal(self):
        # print("My name is {} and I eat {}".format(self.name,self.eat)) #we can either use self or Animal
        print("My name is {} and I eat {}".format(self.name,Animal.eat))
        
    

#Object/Instance creation
myAnimal = Animal(name="Tommy")
    
#method call
myAnimal.animal()