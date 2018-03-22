import re
print(re.findall(r'[0-9]+', 'My age is 22 or 23.'))
print(re.sub(r'[0-9]+', 'AGE', 'My age is 22 or 23.'))
