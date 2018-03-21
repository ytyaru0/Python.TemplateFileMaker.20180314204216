import pathlib
import os.path
#from CommandsFileMaker import CommandsFileMaker
class CommandReplaceFile:
    def __init__(self):
        self.__path_dir_root = pathlib.Path(__file__).resolve().parent.parent
        self.__path_dir_res = self.__path_dir_root / 'res'
        self.__path_file_replace = self.__path_dir_res / 'command_replace.tsv'
    
    @property
    def FilePath(self): return self.__path_file_replace
    @property
    def TemplateDir(self): return self.__path_dir_res
    
    def Load(self):
#        CommandsFileMaker().Make()
        if not self.__path_file_replace.is_file():
            with self.__path_file_replace.open('w'): pass
        import collections
        CommandsReplace= collections.namedtuple('CommandReplace', 'path command')
        data = []
        with self.__path_file_replace.open() as f:
            for line in f.read().split('\n'):
                if 0 == len(line.strip()): continue
                if line.strip().startswith('#'): continue
                path, command = line.split('\t')
                data.append(CommandsReplace(path=path, command=command))
        data = sorted(data, key=lambda d: len(d.path), reverse=True)
        #data = sorted(data, key=lambda d: len(d.path), reverse=True)
        #data = sorted(data, key=lambda d: getattr(d, 'path'), reverse=True)
        #sorted(data, key=lambda d: len(d.path))
        #sorted(data, key=lambda d: len(d.command), reverse=True)
        #print('************************ ', data)
        #for d in data: print('*', d.path)
        #print('************************ ', data)
        return data

if __name__ == '__main__':
    print(CommandReplaceFile().Load())
