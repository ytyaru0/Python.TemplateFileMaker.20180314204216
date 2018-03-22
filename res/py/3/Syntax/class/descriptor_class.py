class Descriptor:
    def __init__(self): self.val = None
    def __get__(self, o, t):
        print('GET'); return self.val;
    def __set__(self, o, v):
        print('SET'); self.val = v;
class A:
    v = Descriptor()
    
A.v
A.v = 100
print(A.v)

