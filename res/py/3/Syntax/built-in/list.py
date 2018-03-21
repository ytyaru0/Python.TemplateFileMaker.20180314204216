j = map(lambda v: v+1, range(3))
print(j, list(j))

k = filter(lambda v: v%2==0, range(10))
print(k, list(k))

print(all([True, True]))
print(any([True, False]))
print(sum([1,2,3]))
print(max([1,2,3]))
print(min([1,2,3]))
print(sorted([2,3,1]))
print(sorted([2,3,1], reverse=True))
print(sorted(['BBB','A',  'CC'], key=len))
print(sorted([2,3,10], key=str))
l = [{'age': 33}, {'age': 22}, {'age': 11}]
print(sorted(l, key=lambda d: d['age']))
class A:
    def __init__(self, name): self.name= name
    def __repr__(self): return self.name
l = [A('C'), A('A'), A('B')]
print(sorted(l, key=lambda c: getattr(c, 'name')))

