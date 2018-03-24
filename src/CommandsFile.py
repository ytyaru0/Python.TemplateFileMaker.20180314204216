import pathlib
import os.path
from io import StringIO
from PathToCommand import PathToCommand
from ConfigFile import ConfigFile
class CommandsFile(ConfigFile):
    def __init__(self):
        super().__init__('commands')
        self.__p2c = PathToCommand()

    def Make(self):
        if self.FilePath.is_file(): return
        with StringIO() as buf:
            for t in self.__LoadTemplateFiles():
                buf.write(t + '\t' + self.__p2c.To(t) + '\n')
            with self.FilePath.open('w', encoding='utf-8') as f:
                f.write(buf.getvalue())
    
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

