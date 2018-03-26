from string import Template
import re
class PositionalArgumentTemplate(Template):
    # (?i): 大文字小文字を区別しないモードを開始する
    # (?-i): 大文字小文字を区別しないモードを無効にする
    idpattern_default = Template.idpattern # (?-i:[_a-zA-Z][_a-zA-Z0-9]*)
    idpattern = '([0-9]+)'

    def find_place_holders(self, template:str):
        #for m in re.findall(self.pattern, template):
        #for m in re.finditer(self.pattern, template):
        for m in self.pattern.finditer(template):
            print(m, type(m))
            #print(dir(m))
            #print(len(m.groups()))
            print(m[0])
            #print(m.groups())
            #print(m, m.groups(), m.group('named'), type(m))
            #print(m.group('escaped'))
            #print(m.group('named'))
            #print(m.group('braced'))
            #print(m.group('invalid'))


if __name__ == '__main__':
    template_str = '${0} is Aug.'
    t = PositionalArgumentTemplate(template_str)
    print(template_str)
    print(dir(t))
    print(t.delimiter)
    print(t.idpattern)
    print(type(t.idpattern))
    print(t.flags)
    print(t.pattern)
    print(t.substitute(**{'0':'V'}))
    t.find_place_holders(template_str)
