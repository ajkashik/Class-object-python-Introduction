class number:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __str__(self):
        return('{} + {}j'.format(self.x,self.y))
        
    def __add__(self,another):
        x=self.x + another.x
        y=self.y + another.y
        return(number(x,y))
        
pop=number(3,4)
popy=number(2,6)
print(pop+popy)
