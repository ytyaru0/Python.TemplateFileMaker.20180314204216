import pathlib
import os.path
from CommandsFileLoader import CommandsFileLoader
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
        return self.__GetCandidate(CommandsFileLoader().Load())
    
    # 現在の階層における候補リストを返す
    def __GetCandidate(self, datas):
        #print('line:', self.__comp_line)
        #print('cword:', self.__comp_cword)
        #print('point:', self.__comp_point)
        #print('datas:', len(datas))
        #candidate = []
        #candidate = set()
        candidate = []
        #now_command = self.__comp_line.replace(self.__root_command, '').strip()
        del_root_cmd = self.__comp_line.replace(self.__root_command, '').lstrip()
        for d in datas:
            for c in d.commands:
                #print(c)
                #now_command = self.__CompPoint2Command()
                #print(now_command)
                #if c.startswith(now_command):
                if self.__comp_line.endswith(' '):
                    if not c.startswith(del_root_cmd): continue
                    cand = c.replace(del_root_cmd, '').strip().split(' ')[0]
                else:
                    fix_cmd = ' '.join(del_root_cmd.split(' ')[:-1]) + ' '
                    if 0 == len(fix_cmd.strip()): cand = c.split(' ')[0]
                    else:
                        if not c.startswith(fix_cmd): continue
                        cand = c.replace(fix_cmd, '').strip().split(' ')[0]
                    #cand = c.replace(fix_cmd, '').strip().split(' ')[0]
                candidate.append(cand)
        return sorted(set(candidate), key=candidate.index)
        #return candidate 

    def __CompPoint2Command(self):
        points = self.__comp_point.split('\n')
        points.reverse()
        return ' '.join(points)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4: raise Exception('起動引数エラー。root_command, comp_cword, comp_line, comp_pointの4つをください。')
    print(' '.join(GetCompleteCandidate(sys.argv[1]).Get(sys.argv[2], sys.argv[3], sys.argv[4])))
    #print(GetCompleteCandidate(sys.argv[1]).Get(sys.argv[2], sys.argv[3], sys.argv[4]))
 
