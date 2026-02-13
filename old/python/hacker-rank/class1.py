class Abc:  
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def __setattr__(self, attr, val):
        if (attr == "a"):
            "a being set to {}".format(val)
        elif (attr == "b"):
            "b being set to {}".format(val)
    
    def __getattr__(self, attr):
        if (attr == 'sum'):
            return self.a + self.b + self.c
        elif (attr == "a"):
            return 10
        elif (attr == "b"):
            return 20
        elif (attr == "c"):
            return 30
        else:
            raise AttributeError("No such attribute")

inst = Abc()
print(inst.a)
print(inst.b)
print(inst.c)
print(inst.sum)
inst.a = 20
inst.b = 30
print(inst.sum)
