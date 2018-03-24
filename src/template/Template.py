import re

class Template:
    def __init__(self, template:str):
        self.__place_holder = '<%'
        self.__template = template

    def GetVars(self):
        pass
    def __AnalizeVars(self):
        pass

# <% 0 %>
# <% Name %>
# <% Name:Default %>
# <% %Y年%m月%d日 %>
# <% py/Context/db/_DEFAULT.py %>
# <% py/Context/db/_DEFAULT.py:%{0} %{Name} %>
# PlaceHolderに囲まれた内容のうち : で分割される場合がある。
# これを左辺と右辺に分ける。
class PlaceHolderContent:
    def __init__(self, placeholder):
        self.__ph = placeholder
    """
    def Split(self, content):
        result = content
        if result.startswith(self.__ph.Start): result = result[len(self.__pf.Start):]
        if result.endswith(self.__ph.End): result = result[:-1*len(self.__pf.End)]
        re.sub('^' + self.__pf.Start + + +'$'
    """

# <% %> などに囲まれた文字列を取得する。
# 囲み文字列は指定できる。
class PlaceHolder:
    def __init__(self, start='<%', end = '%>'):
        self.__start = start
        self.__end = end
        #self.__pattern = re.compile(start + '.+?' + end)
        #self.__pattern = re.compile(start + '(.+?)' + end)
        self.__pattern = re.compile(start + '(?P<content>.+?)' + end)
    @property
    def Start(self): return self.__start
    @property
    def End(self): return self.__end
    def FindIter(self, target:str):
        return self.__pattern.finditer(target)
        #if not (self.Start in target and self.End in target):
        #    raise Exception('プレースホルダーが存在しません。: {}'.format(target))
        
if __name__ == '__main__':
    p = PlaceHolder()
    holders = p.FindIter('<% Name %> is <% Age %>.')
    print(holders)
    for h in holders:
        print(h, h.group('content'))
