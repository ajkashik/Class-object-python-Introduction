class person:
    def __init__(self):
        self.t="charming"
    def give(self):
        print("the person is {}".format(self.t))
    def change(self,typ):
        self.t=typ

obj=person()
obj.give()

obj.t="boring"
obj.give()
 
obj.change("boring")
obj.give()
