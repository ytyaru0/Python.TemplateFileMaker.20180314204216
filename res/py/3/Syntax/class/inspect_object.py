import inspect
class A:
    def __init__(self):
        pass

    def Run(self):
        #members = inspect.getmembers(object, inspect.isfunction)
        #members = inspect.getmembers(object)
        members = inspect.getmembers(object)
        define = 'class MyObject:' + '\n'
        #print(members)
        for m in members:
            #print(m)
            if '__new__' == m[0]: continue # 第一引数clsが取得できないから
            try:
                sig = inspect.signature(m[1])
                #print(sig)
                define += self.MakeFuncStr(m[0], sig) + '\n'
                #print(define)
            except:
                #print(m[0])
                pass
            #if inspect.isbuiltin(m[1]): print('builtin')
            #elif inspect.isfunction(m[1]): print('function')
            #elif inspect.ismethod(m[1]): print('method')
            #if inspect.ismethod(m[1]):
            #    print(m)
            #    args = inspect.signature(m[1])
            #    print(args)
        define += self.MakeFuncStr2()
        print(define)

    def MakeFuncStr(self, name, sig):
        #print(type(sig))
        #print(type(sig.parameters))
        #print(sig.parameters)

        parameters = ', '.join(str(p) for p in sig.parameters.values())
        call_prm = ', '.join([str(p) for p in sig.parameters.values() if 'self' != str(p)])
        res = ' '*4 + 'def ' + name + '(' + parameters + ')' + ':' + '\n' + ' '*4*2 + 'return ' + 'super().' + name + '(' + call_prm + ')'
        return res

    def MakeFuncStr2(self):
        return '\n    ' + '\n    '.join([
        'def __new__(cls, *args, **kwargs): return super().__new__(cls, *args, **kwargs)',
        'def __format__(self, format_spec): return super().__format__(format_spec)',
        'def __init_subclass__(cls): return super().__init_subclass__()',
        'def __bytes__(self): return super().__bytes__()',
        'def __bool__(self): return super().__bool__()',
        'def __getattr__(self, name): return super().__getattr__(name)',

        # ディスクリプタ
        'def __get__(self, instance, owner): return super().__get__(instance, owner)',
        'def __set__(self, instance, value): return super().__set__(instance, value)',
        'def __delete__(self, instance): return super().__delete__(instance)',
        'def __set_name__(self, owner, name): super().__set_name__(owner, name)',


        'def __instancecheck__(self, instance): return super().__instancecheck__(instance)',
        'def __subclasscheck__(self, subclass): return super().__subclasscheck__(subclass)',
        'def __call__(self, *args, **kwargs): return super().__call__(*args, **kwargs)',

        # コンテナ
        'def __len__(self): return super().__len__()',
        'def __length_hint__(self): return super().__length_hint__()',
        'def __getitem__(self, key): return super().__getitem__(key)',
        'def __missing__(self, key): return super().__missing__(key)',
        'def __setitem__(self, key, value): return super().__setitem__(key, value)',
        'def __delitem__(self, key): return super().__delitem__(key)',
        'def __iter__(self): return super().__iter__()',
        'def __reversed__(self): return super().__reversed__()',
        'def __contains__(self, item): return super().__contains__(item)',

        # 演算子オーバーライド
        'def __add__(self, other): return super().__add__(self, other)',
        'def __sub__(self, other): return super().__sub__(self, other)',
        'def __mul__(self, other): return super().__mul__(self, other)',
        'def __matmul__(self, other): return super().__matmul__(self, other)',
        'def __truediv__(self, other): return super().__truediv__(self, other)',
        'def __floordiv__(self, other): return super().__floordiv__(self, other)',
        'def __mod__(self, other): return super().__mod__(self, other)',
        'def __divmod__(self, other): return super().__divmod__(self, other)',
        'def __pow__(self, other): return super().__pow__(self, other)',
        'def __lshift__(self, other): return super().__lshift__(self, other)',
        'def __rshift__(self, other): return super().__rshift__(self, other)',
        'def __and__(self, other): return super().__and__(self, other)',
        'def __xor__(self, other): return super().__xor__(self, other)',
        'def __or__(self, other): return super().__or__(self, other)',

        'def __radd__(self, other): return super().__radd__(self, other)',
        'def __rsub__(self, other): return super().__rsub__(self, other)',
        'def __rmul__(self, other): return super().__rmul__(self, other)',
        'def __rmatmul__(self, other): return super().__rmatmul__(self, other)',
        'def __rtruediv__(self, other): return super().__rtruediv__(self, other)',
        'def __rfloordiv__(self, other): return super().__rfloordiv__(self, other)',
        'def __rmod__(self, other): return super().__rmod__(self, other)',
        'def __rdivmod__(self, other): return super().__rdivmod__(self, other)',
        'def __rpow__(self, other): return super().__rpow__(self, other)',
        'def __rlshift__(self, other): return super().__rlshift__(self, other)',
        'def __rrshift__(self, other): return super().__rrshift__(self, other)',
        'def __rand__(self, other): return super().__rand__(self, other)',
        'def __rxor__(self, other): return super().__rxor__(self, other)',
        'def __ror__(self, other): return super().__ror__(self, other)',

        'def __iadd__(self, other): return super().__iadd__(self, other)',
        'def __isub__(self, other): return super().__isub__(self, other)',
        'def __imul__(self, other): return super().__imul__(self, other)',
        'def __imatmul__(self, other): return super().__imatmul__(self, other)',
        'def __itruediv__(self, other): return super().__itruediv__(self, other)',
        'def __ifloordiv__(self, other): return super().__ifloordiv__(self, other)',
        'def __imod__(self, other): return super().__imod__(self, other)',
        'def __idivmod__(self, other): return super().__idivmod__(self, other)',
        'def __ipow__(self, other): return super().__ipow__(self, other)',
        'def __ilshift__(self, other): return super().__ilshift__(self, other)',
        'def __irshift__(self, other): return super().__irshift__(self, other)',
        'def __iand__(self, other): return super().__iand__(self, other)',
        'def __ixor__(self, other): return super().__ixor__(self, other)',
        'def __ior__(self, other): return super().__ior__(self, other)',

        'def __neg__(self): return super().__neg__()',
        'def __pos__(self): return super().__pos__()',
        'def __abs__(self): return super().__abs__()',
        'def __invert__(self): return super().__invert__()',
        'def __complex__(self): return super().__complex__()',
        'def __int__(self): return super().__int__()',
        'def __float__(self): return super().__float__()',
        'def __index__(self): return super().__index__()',
        'def __round__(self, ndigits): return super().__round__(ndigits)',
        'def __trunc__(self): return super().__trunc__()',
        'def __floor__(self): return super().__floor__()',
        'def __ceil__(self): return super().__ceil__()',

        # with句
        'def __enter__(self): return super().__enter__()',
        'def __exit__(self, exc_type, exc_value, traceback): return super().__exit__(exc_type, exc_value, traceback)',

        # async
        'def __await__(self): return super().__await__()',
        'def __aiter__(self): return super().__aiter__()',
        'def __anext__(self): return super().__anext__()',
        'def __aenter__(self): return super().__aenter__()',
        'def __aexit__(self, exc_type, exc_value, traceback): return super().__aexit__(exc_type, exc_value, traceback)'
        ])

if __name__ == '__main__':
    c = A()
    c.Run()
