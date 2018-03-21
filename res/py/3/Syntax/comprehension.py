a = [a+10 for a in [0,1,2]]
print(a)

b = [(a, b) for a in [1,2] for b in ['A','B']]
print(b)

c = [(a, b) for a in [1,2] for b in ['A','B'] if a == 2]
print(c)

d = [i if i%2==0 else str(i) for i in range(0, 10)]
print(d)

