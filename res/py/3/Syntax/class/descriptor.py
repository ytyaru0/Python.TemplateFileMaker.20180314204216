class Descriptor:
    def __init__(self): self.val = None
    def __get__(self, obj, type=None):
        print('GET'); return self.val;
    def __set__(self, obj, value):
        print('SET'); self.val = value;
    def __delete__(self, obj):
        print('DEL'); del obj;
    def __set_name__(self, owner, name):
        print('NAME:', name);
        self.name = name

class A:
    v = Descriptor()

a = A()
a.v
a.v = 100
del a.v
