# https://docs.python.jp/3/library/argparse.html
import argparse
import sys
class ${Name}:
    def __init__(self):
        self.__parser = None
        self.__args = None

    def Run(self):
        self.__MakeParser()
        self.__args = self.__parser.parse_args()
        self.__Action()

    def __MakeParser(self):
        self.__parser = argparse.ArgumentParser(description='description.')
        self.__parser.add_argument('path')
        self.__parser.add_argument('-e', '--extension')
        self.__parser.add_argument('-r', '--radix', type=int, default=10)
        self.__parser.add_argument('-a', '--alignment', action='store_true', default=False)

        self.__parser.add_argument('-l', '--file-list', action='append') # -f aa -f bb -f cc ...
        self.__parser.add_argument('-c', '--const', action='store_const', const='test.txt')
        self.__parser.add_argument('-t', '--type', choices=['py', 'sh', 'md'])
        self.__parser.add_argument('-req', '--required-args', required=True)

        self.__parser.add_argument('-m1', '--multi-list1', nargs='*') # `-m a b c d` -> m=[a,b,c,d]
        self.__parser.add_argument('-m2', '--multi-list2', nargs='+') # 最低でも1つないとエラー
        self.__parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

        self.__parser.add_argument('-other', '--other-commands', nargs=argparse.REMAINDER) # 残りすべてをリストとして集める。他のツールに対して処理を渡すため

    def __Action(self):
        for key, value in self.__args.__dict__.items():
            print('{}: {}'.format(key, value))


if __name__ == '__main__':
    c = ${Name}()
    c.Run()

