import pathlib
import os.path
class CommandsFileMaker:
    def __init__(self):
        self.__path_dir_root = pathlib.Path(__file__).resolve().parent.parent
        self.__path_dir_res = self.__path_dir_root / 'res'
        self.__path_file_commands = self.__path_dir_res / 'commands.tsv'
    
    @property
    def FilePath(self): return self.__path_file_commands
    @property
    def TemplateDir(self): return self.__path_dir_res
    
    def Make(self):
        temps = self.__LoadTemplateFiles()
        path = self.__path_dir_res / 'commands.tsv'
        with self.__path_file_commands.open('w', encoding='utf-8') as f:
            for t in temps:
                f.write(t + '\t' + self.__MakeCommand(t) + '\n')

    def __LoadTemplateFiles(self):
        files = []
        root = pathlib.Path(__file__).resolve().parent.parent / 'res'
        for path in self.__path_dir_res.glob('**/*.*'):
            if path.name == self.__path_file_commands.name: continue
            files.append(str(path.relative_to(self.__path_dir_res)))
        files.sort()
        return files

    def __MakeCommand(self, path):
        s = path.split('/')
        if '.' in s[-1]: s[-1] = os.path.splitext(s[-1])[0]
        return ' '.join(s)


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

