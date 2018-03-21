import pathlib
import os.path
from CommandReplaceFile import CommandReplaceFile

class PathToCommand:
    def __init__(self):
        self.__replaces = CommandReplaceFile().Load()
        #for i, r in enumerate(self.__replaces): print('***{}{}'.format(i, r.path))

    def To(self, path):
        # command_replace.tsvに存在するパスなら置換する
        #for i, r in enumerate(self.__replaces): print('***{}{}'.format(i, r.path))
        for r in self.__replaces:
            #print(r.path)
            if path.startswith(r.path):
                #print('**'+r.path)
                new = '/'.join(r.command.split(' '))
                #print(os.path.join(new, *path.split(r.path)[1:]))
                return self.__Plain(os.path.join(new, *path.split(r.path)[1:]))
        # 存在しないなら/をspaceに置換する
        return self.__Plain(path)

    def __Plain(self, path):
        s = path.split('/')
        if '.' in s[-1]: s[-1] = os.path.splitext(s[-1])[0]
        return ' '.join(s)

