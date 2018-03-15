class ${Name}Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['A'] = 1
        return type.__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        setattr(cls, 'B', 2)

class ${Name}:
    def __init__(self):
        pass
