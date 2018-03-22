l = lambda a: a+1
print(l(100))

j = map(lambda v: v+1, range(3))
print(j, list(j))

k = filter(lambda v: v%2==0, range(10))
print(k, list(k))
