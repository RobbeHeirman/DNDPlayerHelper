import glob
from os.path import join, dirname, basename, isfile


ordered = ['expansion', 'game_entity']

modules = glob.glob(join(dirname(__file__), "*.py"))
rest = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py') and f not in ordered]

__all__ = ordered + rest
