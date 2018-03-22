import pathlib
import os.path
from PathToCommand import PathToCommand
from ConfigFile import ConfigFile
class CommandsFile(ConfigFile):
    def __init__(self):
        super().__init__('commands')
        self.__p2c = PathToCommand()
        """
        self.__path_dir_root = pathlib.Path(__file__).resolve().parent.parent
        self.__path_dir_res = self.__path_dir_root / 'res'
        self.__file_name = 'commands.tsv'
        #self.__path_file_commands = self.__path_dir_res / self.__file_name
        self.__LoadConfigFile()
        self.__p2c = PathToCommand()
        """
    """
    @property
    def FilePath(self): return self.__path_file_commands
    @property
    def TemplateDir(self): return self.__path_dir_res
       
    def __LoadConfigFile(self):
        self.__path_file_commands = self.__LoadCommandsDirPathFromMetaFile()
        if self.__path_file_commands is None:
            self.__path_file_commands = self.__path_dir_res / self.__file_name
    """
    """
    def __LoadCommandsDirPathFromMetaFile(self):
        path_config = pathlib.Path('/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/ini/work.ini')
        if path_config.is_file():
            import configparser
            p = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
            p.read(path_config)
            path_file_commands = pathlib.Path(p['Paths']['work_meta_command_do']) / self.__file_name
            path_file_commands.parent.mkdir(parents=True, exist_ok=True)
            return path_file_commands
        return None
    """
    def Make(self):
        #if self.__path_file_commands.is_file(): return
        temps = self.__LoadTemplateFiles()
        with self.FilePath.open('w', encoding='utf-8') as f:
        #with self.__path_file_commands.open('w', encoding='utf-8') as f:
            for t in temps:
                f.write(t + '\t' + self.__p2c.To(t) + '\n')

    def __LoadTemplateFiles(self):
        files = []
        for path in self.TemplateDir.glob('*/**/*.*'):
            files.append(str(path.relative_to(self.TemplateDir)))
        #for path in self.__path_dir_res.glob('*/**/*.*'):
            #files.append(str(path.relative_to(self.__path_dir_res)))
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

    """
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
    """
    def __MakeCommands(self, commands):
        res = []
        for c in commands: res.append(self.__p2c.To(c))
        return res
    """

