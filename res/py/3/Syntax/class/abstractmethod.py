from abc import ABCMeta, abstractmethod

class A(metaclass=ABCMeta):
    @abstractmethod
    def say(self): pass

class B(A):
    def say(self): print('B') 
class C(A):
    def say(self): print('C') 

if __name__ == '__main__':
    for c in [B(), C()]:
        c.say()
