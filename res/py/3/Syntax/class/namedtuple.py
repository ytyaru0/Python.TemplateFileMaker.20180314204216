import collections
cls = collections.namedtuple('Human', 'Name Age')
print(type(cls))
ins = cls(Name='NAME', Age=123)
print(type(ins))
print(ins)
print(ins.Name, ins.Age)
#ins.Name = 'NAME' # AttributeError: can't set attribute

