class bird:
    def __init__(self):
        print("This is a bird")
    def name(self):
        print("bird")
    def swim(self):
        print("Can swim")

class penguin(bird):
    def __init__(self):
        super().__init__()
        print("This is penguin")
    def name(self):
        super().name()
        print("Penguin")
    def run(self):
        super().swim()
        print("Can run")

pop=penguin()

pop.name()

pop.run()
