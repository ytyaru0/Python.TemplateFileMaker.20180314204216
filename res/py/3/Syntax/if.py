if True: print('if')

if False: print('if')
else: print('else')

if False: print('if')
elif True: print('elif')
else: print('else')

if True and True: print('and')
else: print('BAD')
if True or False: print('or')
else: print('BAD')
if not False: print('not')
else: print('BAD')

if None: print('BAD')
else: print('None is False')
if 0: print('BAD')
else: print('0 is False')

if 0 < len('A'): print("'A' len is {}".format(len('A')))
else: print('BAD')

class C: pass
if isinstance(C(), C): print("isinstance")
else: print('BAD')

if 1 == 1: print('1 == 1')
if 'A' == 'A': print('A == A')
if C() is not None: print('C() is not None')

