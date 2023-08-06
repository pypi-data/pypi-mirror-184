from ast import parse
from flake8_property.checker import PropertyChecker

def test_positive_not_property():
    tree = parse('''
class K(object):
    def greet(self):
        pass
''')
    violations = list(PropertyChecker(tree).run())
    assert len(violations) == 0

def test_positive_property_simple():
    tree = parse('''
class K(object):
    __value = 1
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        self.__value = value
    @value.deleter
    def value(self):
        del self.__value
''')
    violations = list(PropertyChecker(tree).run())
    assert len(violations) == 0

def test_wrong_property_args():
    tree = parse('''
class K(object):
    __value = 1
    @property
    def value(self, value):
        self.__value = value
    @value.setter
    def value(self, value):
        self.__value = value
    @value.deleter
    def value(self):
        del self.__value
''')
    violations = list(PropertyChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('PT010 ')

def test_wrong_setter_name():
    tree = parse('''
class K(object):
    __value = 1
    @property
    def value(self):
        return self.__value
    @value.setter
    def value_(self, value):
        self.__value = value
    @value.deleter
    def value(self):
        del self.__value
''')
    violations = list(PropertyChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('PT011 ')

def test_wrong_setter_args():
    tree = parse('''
class K(object):
    __value = 1
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self):
        return self.__value
    @value.deleter
    def value(self):
        del self.__value
''')
    violations = list(PropertyChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('PT012 ')

def test_wrong_deleter_name():
    tree = parse('''
class K(object):
    __value = 1
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        self.__value = value
    @value.deleter
    def value_(self):
        del self.__value
''')
    violations = list(PropertyChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('PT013 ')

def test_wrong_deleter_args():
    tree = parse('''
class K(object):
    __value = 1
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        self.__value = value
    @value.deleter
    def value(self, value):
        self.__value = value
''')
    violations = list(PropertyChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('PT014 ')

def test_wrong_multiple_decorators():
    tree = parse('''
class K(object):
    __value = 1
    @property
    def value(self):
        return self.__value
    @value.deleter
    @property
    def value(self):
        del self.__value
''')
    violations = list(PropertyChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('PT015 ')
