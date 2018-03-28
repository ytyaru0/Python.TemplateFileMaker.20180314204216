import pathlib
import os.path
import shlex
from CommandsFile import CommandsFile 

class GetCompleteCandidate:
    def __init__(self, root_command):
        self.__root_command = root_command
        self.__comp_cword = None
        self.__comp_line = None
        self.__comp_point = None
    
    def Get(self, comp_cword, comp_line, comp_point):
        self.__comp_cword = comp_cword
        self.__comp_line = comp_line
        self.__comp_point = comp_point
        return self.__GetCandidate(CommandsFile().Load())
    
    # 現在の階層における候補リストを返す
    def __GetCandidate(self, datas):
        candidate = []
        del_root_cmd = self.__DelRootCmd(self.__comp_line)
        for d in datas:
            for c in d.commands:
                if self.__comp_line.endswith(' '):
                    if not c.startswith(del_root_cmd): continue
                    cand = c.replace(del_root_cmd, '').strip().split(' ')[0]
                else:
                    fix_cmd = ' '.join(del_root_cmd.split(' ')[:-1]) + ' '
                    if 0 == len(fix_cmd.strip()): cand = c.split(' ')[0]
                    else:
                        if not c.startswith(fix_cmd): continue
                        cand = c.replace(fix_cmd, '').strip().split(' ')[0]
                candidate.append(cand)
        return sorted(set(candidate), key=candidate.index)

    def __DelRootCmd(self, command:str):
        res = ''
        commands = shlex.split(command.lstrip())
        if commands[0] == self.__root_command: res = ' '.join(commands[1:])
        else: res = ' '.join(commands)
        return res


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4: raise Exception('起動引数エラー。root_command, comp_cword, comp_line, comp_pointの4つをください。')
    print(' '.join(GetCompleteCandidate(sys.argv[1]).Get(sys.argv[2], sys.argv[3], sys.argv[4])))
 
