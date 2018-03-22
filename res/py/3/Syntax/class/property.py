class A:
    @property
    def X(self): print('GET'); return self.__x;
    @X.setter
    def X(self, v): print('SET'); self.__x = v;
    @X.deleter
    def X(self): print('DEL'); del self.__x

a = A()
a.X = 321
a.X
del a.X
