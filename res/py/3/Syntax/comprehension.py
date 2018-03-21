a = [a+10 for a in [0,1,2]]
print(a, type(a))

b = [(a, b) for a in [1,2] for b in ['A','B']]
print(b)

c = [(a, b) for a in [1,2] for b in ['A','B'] if a == 2]
print(c)

d = [i if i%2==0 else str(i) for i in range(0, 10)]
print(d)

e = {str(i):i for i in range(0, 3)}
print(e, type(e))

f = {k+str(v):v for k,v in zip(['A','B'], [1,2])}
print(f)

g = {v+1 for v in range(3)}
print(g, type(g))

h = (v+1 for v in range(3))
print(h, type(h))
for i in h: print(i)

i = tuple(v for v in range(3))
print(i, type(i))

j = map(lambda v: v+1, range(3))
print(j, list(j))

k = filter(lambda v: v%2==0, range(10))
print(k, list(k))

