from .version import __version__
from re import compile
from six import string_types
from ast import walk, FunctionDef, Name, Attribute, Str, Dict

try:
    from ast import Starred
except ImportError:
    Starred = None

PT010 = "PT010 the number of arguments for property decorator body is wrong (should be 1)."
PT011 = "PT011 the name of setter function is wrong."
PT012 = "PT012 the number of arguments for setter function is wrong (should be 2)."
PT013 = "PT013 the name of setter function is wrong."
PT014 = "PT014 the number of arguments for setter function is wrong (should be 1)."
PT015 = "PT015 multiple decorators were used to declare property."

class PropertyChecker(object):
    name = 'flake8_property'
    version = __version__

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for node in walk(self.tree):
            if not isinstance(node, FunctionDef):
                continue
            isProperty = 0
            for deco in node.decorator_list:
                if isinstance(deco, Name):
                    if deco.id == 'property':
                        isProperty += 1
                        if len(node.args.args) != 1:
                            yield node.lineno, node.col_offset, PT010, type(self)
                if isinstance(deco, Attribute):
                    if deco.attr == 'setter':
                        isProperty += 1
                        if node.name != deco.value.id:
                            yield node.lineno, node.col_offset, PT011, type(self)
                        if len(node.args.args) != 2:
                            yield node.lineno, node.col_offset, PT012, type(self)
                    if deco.attr == 'deleter':
                        isProperty += 1
                        if node.name != deco.value.id:
                            yield node.lineno, node.col_offset, PT013, type(self)
                        if len(node.args.args) != 1:
                            yield node.lineno, node.col_offset, PT014, type(self)
            if isProperty > 1:
                yield node.lineno, node.col_offset, PT015, type(self)
