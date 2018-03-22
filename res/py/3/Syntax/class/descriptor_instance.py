class A:
    def getX(self): print('GET'); return self.__x;
    def setX(self, v): print('SET'); self.__x = v;
    def delX(self): print('DEL'); del self.__x;
    X = property(getX, setX, delX)

a = A()
a.X = 123
a.X
print(a.X)
del a.X
