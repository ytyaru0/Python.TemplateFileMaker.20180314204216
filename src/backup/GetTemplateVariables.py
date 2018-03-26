import sys
import os.path
from CommandsFile import CommandsFile

from jinja2 import Template, Environment, FileSystemLoader, meta
import pathlib

class TemplateVariable:
    def Get(self, path:str):
        env = Environment(loader=FileSystemLoader(str(CommandsFile().TemplateDir)))
        template = env.get_template(path)
        print(template.filename)
        with pathlib.Path(template.filename).open() as f:
            ast = env.parse(f.read())
            return meta.find_undeclared_variables(ast)

if __name__ == '__main__':
    tpl_vars = TemplateVariable().Get('py/3/_DEFAULT.py')
    print(tpl_vars)
