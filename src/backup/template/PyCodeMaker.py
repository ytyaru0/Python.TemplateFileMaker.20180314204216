# 戻り値の有無や何を返すべきかは判定できない
import io
import inspect
class PyCodeMaker:
    def Make(self, target):
        with io.StringIO() as buf:
            #for name in dir(target):
            #    buf.write(name + '\n')
            buf.write(str(inspect.getmembers(target))+ '\n')
            return buf.getvalue()


if __name__ == '__main__':
    print(PyCodeMaker().Make(type))
    print(PyCodeMaker().Make(object))
    print(inspect.getfile(type))
