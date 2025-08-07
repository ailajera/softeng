class Pet:
    # define the properties inside __init__
    def __init__(self, name, pet_type) -> None:
        self.name = name
        self.pet_type = pet_type
        self.energy = 100

    # create the required methods here

    def eat(self):
        self.energy += 10
        print(self.name, "already ate and has energy: ", self.energy)

    def sleep(self):
        self.energy += 25
        print(self.name, "slept and has an energy: ", self.energy)

    def play(self):
        self.energy -= 15
        print(self.name, "played and now tired with energy: ", self.energy)

    def show_status(self):
        print(f"{self.name} the {self.pet_type} has {self.energy} energy.")
