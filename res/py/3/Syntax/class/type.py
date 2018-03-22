cls = type('Human', (object,), dict(name=None, age=0))
ins = cls()

print(dir(ins))
assert(hasattr(ins, 'name'))
assert(hasattr(ins, 'age'))
assert(ins.name is None)
assert(ins.age == 0)
