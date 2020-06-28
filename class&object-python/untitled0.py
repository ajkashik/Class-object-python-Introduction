class parrot:
    first_name='bird'
    def __init__(self,name,weight):
        self.n=name
        self.w=weight
        
obj1=parrot('tuki',2)
obj2=parrot('muli',3)

print('tuki is a {}'.format(obj1.__class__.first_name))
print('muli is a {}'.format(obj2.__class__.first_name))

print('{} is {} gm'.format(obj1.n,obj2.w))
print('{} is {} gm'.format(obj2.n,obj2.w))
