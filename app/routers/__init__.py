from os import listdir
from pathlib import Path
from importlib import import_module

path_parent = Path('./app/routers')

# list
for module in listdir(path_parent):
    if 'router' in module:
        import_module(
            f'app.routers.{module[:-3]}'
        )
    