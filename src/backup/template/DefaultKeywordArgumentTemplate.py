from string import Template
import re
class DefaultKeywordArgumentTemplate(Template):
    # (?i): 大文字小文字を区別しないモードを開始する
    # (?-i): 大文字小文字を区別しないモードを無効にする
    idpattern_default = Template.idpattern # (?-i:[_a-zA-Z][_a-zA-Z0-9]*)
    #idpattern = '(?-i:[_a-zA-Z][_a-zA-Z0-9]*?(:[_a-zA-Z][_a-zA-Z0-9]))'
    #idpattern = '(?-i:[_a-zA-Z][_a-zA-Z0-9]*:[_a-zA-Z][_a-zA-Z0-9])'
    #idpattern = '(?-i:[_a-zA-Z][_a-zA-Z0-9]*:)'
    #idpattern = '(?-i:[_a-zA-Z][_a-zA-Z0-9]*:[_a-zA-Z][_a-zA-Z0-9])'
    idpattern = '[_a-zA-Z][_a-zA-Z0-9]*\:.*'
    def GetNameAndDefaultValue(self, template):
        results = []
        for m in self.pattern.finditer(template):
            #print(re.findall(self.idpattern, m[0]))
            print(m)
            print(m[0])
            results.append(m[0].split(':'))
        print(results)
        return results


if __name__ == '__main__':
    #template_str = '${Name:AAA} is Aug.'
    template_str = '${Name:A} is Aug.'
    t = DefaultKeywordArgumentTemplate(template_str )
    print(dir(t))
    print(t.delimiter)
    print(t.idpattern)
    print(type(t.idpattern))
    print(t.substitute(**{'Name:A':'V'}))
    #print(t.substitute(**{'Name':'V'})) # このように指定したい
    t.GetNameAndDefaultValue(template_str )
