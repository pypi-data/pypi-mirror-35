from .__version__ import VERSION
from .homectl import main
from .config import Config
from . import config_ifttt

# import importlib
# import pkgutil

# homectl_plugins = {
#     name: importlib.import_module(name)
#     for finder, name, ispkg in pkgutil.iter_modules()
#     if name.startswith('homectl_')
# }
