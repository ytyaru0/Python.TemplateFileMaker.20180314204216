import pathlib
import os.path
class GetCompleteCandidate:
    def __init__(self, comp_cword, comp_line, comp_point):
        self.__comp_cword = comp_cword
        self.__comp_line = comp_line
        self.__comp_point = comp_point
        self.__path_dir_root = pathlib.Path(__file__).resolve().parent.parent
        self.__path_dir_res = self.__path_dir_root / 'res'
        self.__path_file_commands = self.__path_dir_res / 'commands.tsv'
    
    @property
    def FilePath(self): return self.__path_file_commands
    @property
    def TemplateDir(self): return self.__path_dir_res
    
    def Set(self):
        data = self.__LoadTemplateFiles()

    def __LoadTemplateFiles(self):
        data = []
        with self.__path_file_commands.open() as f:
            for line in f.read().split('\n'):
                data.append(line.split('\t'))
        return data

    def __MakeCandidate(self, data):
        candidate = []
        for d in data:
            candidate.append(d[1].split(' ')[self.__comp_cword-1])
        return candidate 

if __name__ == '__main__':
    c = CommandsFileMaker()
    c.Make()
    """
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
    """

