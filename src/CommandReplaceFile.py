import pathlib
import os.path
import collections
from ConfigFile import ConfigFile

class CommandReplaceFile(ConfigFile):
    def __init__(self):
        super().__init__('command_replace')
    
    def Load(self):
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


if __name__ == '__main__':
    print(CommandReplaceFile().Load())
