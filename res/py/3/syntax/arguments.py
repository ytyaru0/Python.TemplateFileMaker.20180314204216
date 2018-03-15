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

l = list((1, 2, 3))
d = dict(name='A', age=4)
func(*l, **d)
