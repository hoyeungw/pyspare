import inspect
from datetime import date

from texting import parenth

from pyspare import deco_entries, deco_object
from test.assets.classes import Message, Point


def print_info(instance):
    print('>')
    print('type:', (ty := type(instance)).__name__, parenth(ty))
    print('is class instance:', inspect.isclass(type(instance)))
    print('members:', deco_entries(inspect.getmembers(instance)))
    print('@property:', deco_entries(inspect.getmembers(type(instance), predicate=lambda o: isinstance(o, property))))
    print('method:', deco_entries(inspect.getmembers(instance, predicate=inspect.ismethod)))
    print('stringified', str(instance))
    print('deco', deco_object(instance))
    print()


candidates = {
    'point': Point(x=3, y=4, id='ball'),
    'message': Message('ford', 'ferrari', 'race'),
    'date': date.today()
}


def test():
    for key, ob in candidates.items():
        print_info(ob)


test()
