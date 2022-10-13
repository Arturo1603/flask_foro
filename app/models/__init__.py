from os import listdir
from pathlib import Path
from importlib import import_module

path_parent = Path('./app/models')

# list
for module in listdir(path_parent):
    if 'model' in module:
        import_module(
            f'app.models.{module[:-3]}'
        )
    