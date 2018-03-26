import sys, pathlib, configparser
parser = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
parser.read('/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/ini/root.ini')
#print(target)
#print(parser['Paths'])
target = pathlib.Path(parser['Paths']['root_script_py']) / 'os/file/'
sys.path.append(target)
#sys.path.append('/home/pi/root/script/py/os/file')
sys.path.append('/tmp/work/Python.NameGenerator.20180313180534/src/')
import collections
from NameGenerator import NameGenerator
from CommandToTemplate import CommandToTemplate
#pathlib.Path('/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/ini/root.ini')
#sys.path.append()

class Do:
    def __init__(self, args:list):
        self.__args = args
        parser = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        parser.read('/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/ini/work.ini')
        self.__path_dir_target = parser['Paths']['work_flow_do']

    def Run(self):
        #name = NameGenerator(self.__path_dir_target, self.__args[0], radix=36, is_alignment=True).Generate()
        name = NameGenerator(self.__path_dir_target, self.__args[0]).Generate()
        filepath = pathlib.Path(self.__path_dir_target) / (name + '.' + self.__args[0])
        try:
            with filepath.open('x') as f:
                f.write(CommandToTemplate(self.__args).To())
                return str(filepath)
        except:
            import os
            os.remove(filepath)
            import traceback
            traceback.print_exc()
    """
    def __GenerateName(self):
        Namespace = collections.namedtuple('Namespace', 'path_dir_target extension radix alignment')
        ns = Namespace(path_dir_target=self.__path_dir_target, extension=self.__args[0], radix=36, alignment=True)
        return NameGenerator(ns).Generate()
    """


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2: raise Exception('引数不足です。ファイル拡張子をください。')
    sys.stdout.flush()
    print(Do(sys.argv[1:]).Run())
    
