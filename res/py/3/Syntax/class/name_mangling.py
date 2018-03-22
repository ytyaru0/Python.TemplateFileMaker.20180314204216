class C:
    def __init__(self):
        self.__v = 'A'
    def Print(self): print(self.__v)

c = C()
c.Print()
c._C__v
#c.__v # AttributeError
