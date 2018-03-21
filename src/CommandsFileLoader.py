import pathlib
import os.path
from CommandsFileMaker import CommandsFileMaker
class CommandsFileLoader:
    def __init__(self):
        self.__path_dir_root = pathlib.Path(__file__).resolve().parent.parent
        self.__path_dir_res = self.__path_dir_root / 'res'
        self.__path_file_commands = self.__path_dir_res / 'commands.tsv'
    
    @property
    def FilePath(self): return self.__path_file_commands
    @property
    def TemplateDir(self): return self.__path_dir_res
    
    def Load(self):
        CommandsFileMaker().Make()
        import collections
        CommandsFile = collections.namedtuple('CommandsFile', 'path commands')
        data = []
        with self.__path_file_commands.open() as f:
            for line in f.read().split('\n'):
                if 0 == len(line.strip()): continue
                s = line.split('\t')
                data.append(CommandsFile(path=s[0], commands=s[1:]))
        return data


if __name__ == '__main__':
    c = CommandsFileLoader()
    print(c.Load())

