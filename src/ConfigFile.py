import pathlib
import os.path
import csv
class ConfigFile:
    def __init__(self, file_name):
        self.__path_dir_root = pathlib.Path(__file__).resolve().parent.parent
        self.__path_dir_res = self.__path_dir_root / 'res'
        if file_name.endswith('.tsv'): self.__file_name = file_name
        else: self.__file_name = file_name + '.tsv'
        self.__LoadCommandsDirPathFromMetaFile()
    
    @property
    def FilePath(self): return self.__path_file_this
    @property
    def TemplateDir(self): return self.__path_dir_template
    @property
    def DefaultFilePath(self): return self.__path_dir_res / self.__file_name

    def __LoadCommandsDirPathFromMetaFile(self):
        #work_paths = self.__LoadMetaPath('work')
        #root_paths = self.__LoadMetaPath('root')
        work_paths = self.__LoadMetaPath('work')
        root_paths = self.__LoadMetaPath('root')
        self.__path_file_this = pathlib.Path(work_paths['work_meta_command_do']) / self.__file_name
        self.__path_dir_template = pathlib.Path(root_paths['root_db_template']) / self.__file_name
        """
        if not self.__path_file_this.is_file():
            self.__path_file_this = self.__path_dir_res / self.__file_name
        self.__path_dir_template = pathlib.Path(root_paths['root_db_template'])
        if not self.__path_dir_template.is_dir():
            self.__path_dir_template = self.__path_dir_res
        """
        if not self.__path_dir_template.is_dir():
            self.__path_dir_template = self.__path_dir_res
        self.__path_file_this.parent.mkdir(parents=True, exist_ok=True)

    def __LoadMetaPath(self, file_name):
        #path_config = pathlib.Path('~/root/_meta/_meta/path/ini/{}.ini'.format(file_name))
        #path_config = pathlib.Path('/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/ini/{}.ini'.format(file_name))
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
