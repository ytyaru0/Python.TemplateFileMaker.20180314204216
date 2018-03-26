import sys
import os.path
from CommandsFile import CommandsFile

class TemplateFilePath:
    def Get(self, args):
        categolies, tmpl_vars = self.__SplitCategolyAndTemplateVars(args)
        input_command = ' '.join([a for a in categolies]).strip()
        f = CommandsFile()
        for d in f.Load():
            for c in d.commands:
                if c == input_command:
                    return os.path.join(f.TemplateDir, d.path)
        return None
    def __SplitCategolyAndTemplateVars(self, args):
        for i, a in enumerate(args):
            if a.startswith('-'): return args[:i], args[i:]
        return args, []
    def __IsKeyword(self, tmpl_args):
        for a in tmpl_args:
            if not a.startswith('-'): return True
        return False

if __name__ == '__main__':
    path = TemplateFilePath().Get(sys.argv[1:])
    if path: print(path)
    else: raise Exception('<ERROR> 指定したコマンドに該当するテンプレートファイルパスは存在しません。')
    """
    print(t.Get(sys.argv[1:])
    import sys
    import os.path
    from CommandsFile import CommandsFile
    input_command = ' '.join([a for a in sys.argv[1:]]).strip()
    f = CommandsFile()
    #print(input_command)
    for d in f.Load():
        for c in d.commands:
            #print('*'+c)
            if c == input_command:
                print(os.path.join(f.TemplateDir, d.path))
                sys.exit()
    raise Exception('<ERROR> 指定したコマンドに該当するテンプレートファイルパスは存在しません。')
    """

