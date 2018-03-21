def func0(): return 0
print(func0())

def func1(arg): return arg
print(func1('A'))

def func2(arg='B'): return arg
print(func2())

def func3(a, b): return a + b
print(func3('A', 'B'))

def func4(a, b='b'): return a + b
print(func4('A', b='B'))

def func5(): print('func5')
r = func5()
print('func5 return is {}'.format(r))

def func(*args, **argv):
    print(args, argv)

func(1)
func(1, 2, 3)
func(name='A')
func(name='A', age=4)
func(1, 2, name='A', age=4)

l = [1, 2, 3]
d = {'name': 'A', 'age': 4}
func(*l, **d)
func(*[1, 2, 3], **{'name': 'A', 'age': 4})

l = list((1, 2, 3))
d = dict(name='A', age=4)
func(*l, **d)
