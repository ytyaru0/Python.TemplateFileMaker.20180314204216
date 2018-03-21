# https://docs.python.jp/3/library/argparse.html
import sys
for i in range(len(sys.argv)):
    print('{}: {}'.format(i, sys.argv[i]))

