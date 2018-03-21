# https://docs.python.jp/3/library/argparse.html
import argparse
import sys
parser = argparse.ArgumentParser(description='description.')
parser.add_argument('path')
parser.add_argument('-e', '--extension')
parser.add_argument('-r', '--radix', type=int, default=10)
parser.add_argument('-a', '--alignment', action='store_true', default=False)

parser.add_argument('-l', '--file-list', action='append') # -f aa -f bb -f cc ...
parser.add_argument('-c', '--const', action='store_const', const='test.txt')
parser.add_argument('-t', '--type', choices=['py', 'sh', 'md'])
parser.add_argument('-req', '--required-args', required=True)

parser.add_argument('-m1', '--multi-list1', nargs='*') # `-m a b c d` -> m=[a,b,c,d]
parser.add_argument('-m2', '--multi-list2', nargs='+') # 最低でも1つないとエラー
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

parser.add_argument('-other', '--other-commands', nargs=argparse.REMAINDER) # 残りすべてをリストとして集める。他のツールに対して処理を渡すため

args = parser.parse_args()
#print(args.path)
#print(args.required_args)
#print(args.const)
print(dir(args))
for key, value in args.__dict__.items():
    print('{}: {}'.format(key, value))
