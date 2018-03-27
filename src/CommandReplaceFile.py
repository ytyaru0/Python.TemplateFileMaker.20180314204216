import pathlib
import os.path
import shutil
import collections
from ConfigFile import ConfigFile
import sys
sys.path.append(os.path.expanduser('~/root/_meta/path/'))
#sys.path.append('/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/')
#/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/PathIni.py
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
            #for p in [self.__LoadMetaPath('root')['root_meta_command_do'], self.DefaultFilePath]:
                if self.__Copy(p): return
            # コピーできるファイルがないなら空ファイル作成
            with self.FilePath.open('x'): pass
    
    def __Copy(self, filepath):
        if filepath.is_file():
            shutil.copyfile(filepath, self.FilePath)
            return True
        return False

    """
    def __LoadMetaPath(self, file_name):
        path_config = self.__GetMetaPath(file_name)
        import configparser
        p = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        p.read(path_config)
        return p['Paths']
    def __GetMetaPath(self, file_name):
        paths = ['~/root/_meta/_meta/path/ini/', 
            '/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/ini/']
        for path in paths:
            path = pathlib.Path(path) / '{}.ini'.format(file_name)
            if path.is_file(): return path
        raise Exception('{}.iniファイルが存在しません。次のいずれかのディレクトリ配下に作成してください'.format(file_name))
        return None
    """
    

if __name__ == '__main__':
    print(CommandReplaceFile().Load())
