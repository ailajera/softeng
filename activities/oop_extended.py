
# let's upgrade this class!
class Pet:
    # define the properties inside __init__
    def __init__(self, name, pet_type) -> None:
        self.name = name
        self.pet_type = pet_type
        self.energy = 100

    # create the required methods here

    def eat(self):
        
        if self.energy >= 100:
            print(self.name, "doesn't like to eat.", self.energy)
        else: 
            gained_energy = 10
            self.energy += gained_energy 
            print(self.name, "already ate and has energy: ", self.energy)

    def sleep(self):

        if self.energy >= 100:
            print(self.name, "doesn't want to sleep", self.energy)
        else:
            gained_energy = 25
            self.energy += gained_energy
            print(self.name, "slept and has an energy: ", self.energy)

    def play(self):
        
        if self.energy < 20:
            print(self.name, "low energy, can't play anymore", self.energy)
        else: 
            lost_energy = 15
            self.energy -= lost_energy 
            print(self.name, "played and now tired with energy: ", self.energy)

    def show_status(self):
        print(f"{self.name} the {self.pet_type} has {self.energy} energy.")

#DOG

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name,pet_type) 
        pet_type = "dog"

    
    def sleep(self):

        if self.energy >= 100:
            print(f"{self.name } doesn't want to sleep")
        else:
            gained_energy = 25
            self.energy += gained_energy
            print(self.name, "slept and has an energy: ")

#CAT

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, pet_type)
        pet_type = "cat"

    def play(self):
        
        if self.energy < 20:
            print(f"{self.name}low energy, can't play anymore")
        else: 
            lost_energy = 15
            self.energy -= lost_energy 
            print(f"{self.name}played and now bored. It has {lost_energy} energy and the energy {self.energy} now")

#BIRD


class Bird(Pet):
    def __init__(self, name):
        super().__init__(name, pet_type)
        pet_type = "bird"

    def eat(self):
        
        if self.energy >= 100:
            print(f"{self.name} still full and doesn't like to eat.")
        else: 
            gained_energy = 10
            self.energy += gained_energy
            print(f"{self.name} already ate and has energy: ")    

    

    
