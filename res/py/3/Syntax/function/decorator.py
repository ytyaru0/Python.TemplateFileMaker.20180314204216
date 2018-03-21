def deco(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('*** start ***')
        func(*args,**kwargs)
        print('*** end ***')
    return wrapper

@deco
def method(): print('Method.')

if __name__ == '__main__':
    method()
