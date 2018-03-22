import pathlib
import os.path
import csv
from PathToCommand import PathToCommand
class ConfigFile:
    def __init__(self, file_name):
        self.__path_dir_root = pathlib.Path(__file__).resolve().parent.parent
        self.__path_dir_res = self.__path_dir_root / 'res'
        if file_name.endswith('.tsv'): self.__file_name = file_name
        else: self.__file_name = file_name + '.tsv'
        self.__LoadCommandsDirPathFromMetaFile()
        self.__p2c = PathToCommand()
    
    @property
    def FilePath(self): return self.__path_file_this
    @property
    def TemplateDir(self): return self.__path_dir_template
    
    def __LoadCommandsDirPathFromMetaFile(self):
        work_paths = self.__LoadMetaPath('work')
        root_paths = self.__LoadMetaPath('root')
        if work_paths is None: self.__path_file_this = self.__path_dir_res / self.__file_name
        else: self.__path_file_this = pathlib.Path(work_paths['work_meta_command_do']) / self.__file_name
        if root_paths is None: self.__path_dir_template = self.__path_dir_res
        else: self.__path_dir_template = pathlib.Path(root_paths['root_db_template'])

    def __LoadMetaPath(self, file_name):
        path_config = pathlib.Path('/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/ini/{}.ini'.format(file_name))
        if path_config.is_file():
            import configparser
            p = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
            p.read(path_config)
            return p['Paths']
        return None

    def LoadTsv(self):
        with self.__path_file_this.open() as f:
            tsv = csv.reader(f, delimiter='\t')
            for columns in tsv:
                if 1 == len(columns) and 0 == len(columns[0].strip()): continue
                if columns[0].strip().startswith('#'): continue
                yield columns


if __name__ == '__main__':
    c = ConfigFile('commands')
    print(c.FilePath)
    print(c.TemplateDir)

    c = ConfigFile('command_replace')
    print(c.FilePath)
    print(c.TemplateDir)
