class Pet:
    
    # implement __init__( name , type , tricks ):
    def __init__(self,name,type,tricks):
        self.name= name
        self.type= type
        self.tricks = tricks
        self.health = 90
        self.energy = 10
    
    
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy+=25
        return self
    
    
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy+=5
        
        
    # # play() - increases the pet's health by 5
    def play(self):
        self.health +=5
        
        
    # noise() - prints out the pet's sound
    def noise(self):
        print("Pet Class")

class Dragon(Pet):
    def __init__(self,name,type,tricks):
        super().__init__(name,type,tricks)
        