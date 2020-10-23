# 廖：__call__此程序的结果是输出输入的name
from dataclasses import dataclass


class Says:
    roster: dict
    effects: list

    def __init__(self):
        self.roster = {}
        self.effects = []

    def __call__(self, *args, **kwargs):
        pass

    def __getitem__(self, item):
        if item in self.roster: return self.roster[item]
        return self.aboard(item)
        pass

    def __getattr__(self, item):
        pass

    def aboard(self, name, preset=None):
        # preset, self.effects
        # if not preset:
        pal = Pal(str(name))
        self.roster[name] = pal
        return pal


@dataclass
class Pal:
    name: str

    def __call__(self, text):
        narrate(text, self)
        pass


def narrate(text, context):
    name = context.name
    print(name, text)


says = Says()
says['guy']('abc')


class Student1(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


h = Student1('MumU')
print('liao:', h())


# 我：__repr__ / __str__ 此程序的结果也是输出输入的name
class Student2(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student2 name:%s' % self.name

    __repr__ = __str__


l = Student2('U')
print('me:', l)
