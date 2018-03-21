import pathlib
import os.path
from PathToCommand import PathToCommand
class CommandsFile:
    def __init__(self):
        self.__path_dir_root = pathlib.Path(__file__).resolve().parent.parent
        self.__path_dir_res = self.__path_dir_root / 'res'
        self.__path_file_commands = self.__path_dir_res / 'commands.tsv'
        self.__p2c = PathToCommand()    
    @property
    def FilePath(self): return self.__path_file_commands
    @property
    def TemplateDir(self): return self.__path_dir_res
    
    def Make(self):
        #if self.__path_file_commands.is_file(): return
        temps = self.__LoadTemplateFiles()
        with self.__path_file_commands.open('w', encoding='utf-8') as f:
            for t in temps:
                f.write(t + '\t' + self.__p2c.To(t) + '\n')

    def __LoadTemplateFiles(self):
        files = []
        root = pathlib.Path(__file__).resolve().parent.parent / 'res'
        for path in self.__path_dir_res.glob('*/**/*.*'):
            if path.name == self.__path_file_commands.name: continue
            files.append(str(path.relative_to(self.__path_dir_res)))
        files.sort()
        return files

    def Load(self):
        self.Make()
        import collections
        CommandsFile = collections.namedtuple('CommandsFile', 'path commands')
        data = []
        with self.__path_file_commands.open() as f:
            for line in f.read().split('\n'):
                if 0 == len(line.strip()): continue
                if line.strip().startswith('#'): continue
                s = line.split('\t')
                data.append(CommandsFile(path=s[0], commands=s[1:]))
                #data.append(CommandsFile(path=s[0], commands=self.__MakeCommands(s[1:])))
        return data
    """
    def __MakeCommands(self, commands):
        res = []
        for c in commands: res.append(self.__p2c.To(c))
        return res
    """

