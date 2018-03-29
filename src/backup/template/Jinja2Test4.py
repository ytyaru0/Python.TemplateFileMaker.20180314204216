from jinja2 import Template, Environment, FileSystemLoader
import pathlib
import datetime

path_tpl = (pathlib.Path(__file__).parent.parent.parent.parent / 'res').resolve()
env = Environment(loader=FileSystemLoader(str(path_tpl )))
template = env.get_template('csv/test.csv')
print(template.render())
