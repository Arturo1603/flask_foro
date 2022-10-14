from os import listdir
from pathlib import Path
from importlib import import_module

path_parent = Path('./app/schemas')

# list
for module in listdir(path_parent):
    if 'schema' in module:
        import_module(
            f'app.schemas.{module[:-3]}'
        )
    