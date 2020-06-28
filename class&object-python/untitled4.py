class kingfisher:
    def fly(self):
        print("kingfisher can fly")
    def swim(self):
        print("kingfisher can swim")

class penguin:
    def fly(self):
        print("penguin can not fly")
    def swim(self):
        print("penguin can swim")

def common_fly(bird):
    bird.fly()
    
def common_swim(bird):
    bird.swim()
        
king=kingfisher()
pen=penguin()

common_fly(king)
common_fly(pen)

common_swim(king)
common_swim(pen)
