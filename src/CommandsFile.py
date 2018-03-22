import pathlib
import os.path
from PathToCommand import PathToCommand
from ConfigFile import ConfigFile
class CommandsFile(ConfigFile):
    def __init__(self):
        super().__init__('commands')
        self.__p2c = PathToCommand()

    def Make(self):
        temps = self.__LoadTemplateFiles()
        with self.FilePath.open('w', encoding='utf-8') as f:
            for t in temps:
                f.write(t + '\t' + self.__p2c.To(t) + '\n')

    def __LoadTemplateFiles(self):
        files = []
        for path in self.TemplateDir.glob('*/**/*.*'):
            files.append(str(path.relative_to(self.TemplateDir)))
        files.sort()
        return files

    def Load(self):
        self.Make()
        import collections
        CommandsFile = collections.namedtuple('CommandsFile', 'path commands')
        data = []
        for s in super().LoadTsv():
            data.append(CommandsFile(path=s[0], commands=s[1:]))
        return data

