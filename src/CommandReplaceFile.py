import pathlib
import shutil
import collections
from ConfigFile import ConfigFile
import sys
sys.path.append(pathlib.Path('~/root/_meta/path/').expanduser())
#sys.path.append('/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/')
from PathIni import PathIni

class CommandReplaceFile(ConfigFile):
    def __init__(self):
        super().__init__('command_replace')
        self.__path_file_this = pathlib.Path(PathIni()['work_meta_command_do']) / self.FilePath.name
        self.__path_dir_template = pathlib.Path(PathIni()['root_db_template']) / self.FilePath.name

    def Load(self):
        self.__LoadDefaultFile()
        CommandsReplace = collections.namedtuple('CommandReplace', 'path command')
        data = []
        for s in self.LoadTsv():
            data.append(CommandsReplace(path=s[0], command=s[1]))
        return sorted(data, key=lambda d: len(d.path), reverse=True)

    def __LoadDefaultFile(self):
        if not self.FilePath.is_file():
            for p in [pathlib.Path(PathIni()['root_meta_command_do']), self.DefaultFilePath]:
                if self.__Copy(p): return
            # コピーできるファイルがないなら空ファイル作成
            with self.FilePath.open('x'): pass
    
    def __Copy(self, filepath):
        if filepath.is_file():
            shutil.copyfile(filepath, self.FilePath)
            return True
        return Falseimport pathlib
