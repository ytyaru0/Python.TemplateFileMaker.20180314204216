import pathlib
import os.path
import collections
from ConfigFile import ConfigFile

class CommandReplaceFile(ConfigFile):
    def __init__(self):
        super().__init__('command_replace')
        #self.__path_dir_root = pathlib.Path(__file__).resolve().parent.parent
        #self.__path_dir_res = self.__path_dir_root / 'res'
        #self.__path_file_replace = self.__path_dir_res / 'command_replace.tsv'
    
    def Load(self):
        #if not self.__path_file_replace.is_file():
        #    with self.__path_file_replace.open('w'): pass
        #if not self.FilePath.is_file():
        #    with self.FilePath.open('w'): pass
        self.__LoadDefaultFile()
        CommandsReplace = collections.namedtuple('CommandReplace', 'path command')
        data = []
        for s in self.LoadTsv():
            data.append(CommandsReplace(path=s[0], command=s[1]))
        return sorted(data, key=lambda d: len(d.path), reverse=True)

    def __LoadDefaultFile(self):
        if not self.FilePath.is_file():
            if self.DefaultFilePath.is_file():
                import shutil
                shutil.copyfile(self.DefaultFilePath, self.FilePath)
            else:
                with self.FilePath.open('w'): pass
        
    """
    @property
    def FilePath(self): return self.__path_file_replace
    @property
    def TemplateDir(self): return self.__path_dir_res
    
    def Load(self):
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
        #for d in data: print('*', d.path)
        return data
    """


if __name__ == '__main__':
    print(CommandReplaceFile().Load())
