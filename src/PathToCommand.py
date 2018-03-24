import pathlib
import os.path
from CommandReplaceFile import CommandReplaceFile

class PathToCommand:
    def __init__(self):
        self.__replaces = CommandReplaceFile().Load()

    def To(self, path:str):
        # command_replace.tsvに存在するパスなら置換する
        p = self.__Replace(path)
        if p: return p
        # 存在しないなら/をspaceに置換する
        return self.__Plain(path)

    def __Replace(self, path:str):
        for r in self.__replaces:
            if path.startswith(r.path):
                new = os.path.join(*r.command.split(' '))
                new_path = os.path.join(new, *path.split(r.path)[1:])
                m = self.__MetaTemplate(new_path)
                if m: return m
                else: return self.__Plain(new_path)
        return None

    def __MetaTemplate(self, path:str):
        s = self.__SplitPath(path)
        name, ext = os.path.splitext(s[-1])
        if '_DEFAULT' == name: return ' '.join(s[:-1])
        else: return None
        
    def __Plain(self, path:str):
        s = self.__SplitPath(path)
        if '.' in s[-1]: s[-1] = os.path.splitext(s[-1])[0]
        return ' '.join(s)

    # テンプレートディレクトリからの相対パス
    # py/3/ のように先頭がパス形式でないため分割されない os.path.split()
    # 特殊なパスなのでWindowsでも\でなく/にする。
    # ~/root/_meta/path/ini/root.ini [Paths]root_db_template
    # ../res/
    def __SplitPath(self, path:str): return path.split('/')
