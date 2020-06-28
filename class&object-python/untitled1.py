class parrot:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def sing(self,sing_name):
        return("{} now {}".format(self.n,sing_name))
    def dance(self,dance_name):
        return("{} now {}".format(self.n,dance_name))
blue=parrot("blue",3)
print(blue.sing("pop"))
print(blue.dance("hiphop"))