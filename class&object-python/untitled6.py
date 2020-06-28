class number:
    def __init__(self,real=0,imag=0):
        self.r=real
        self.i=imag
    def show(self):
        print(f'{self.r} + {self.i}j')

pop=number(3,5)
pop.show()

pop=number(7)
pop.show()

pop.extra=8
print(pop.r,pop.i,pop.extra)
