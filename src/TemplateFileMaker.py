import glob
import os.path
import string
import math

# 特定のテンプレートファイルを作成する
class TemplateFileMaker:
    def __init__(self, args):
        self.__args = args

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='NameGenerator.',
    )
    parser.add_argument('path_file')
    parser.add_argument('extension')
    parser.add_argument('category', narg='*')
    args = parser.parse_args()
    if args.path_file is None: raise Exception('起動引数が足りません。対象ファイルパスを渡して下さい。')
    if args.extension is None: raise Exception('テンプレートの拡張子を渡して下さい。')
    TemplateFileMaker(args).Make()

