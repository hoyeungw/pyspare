from pyspare import deco_dict
from test.assets import entries_collection


def test():
    for key, entries in entries_collection.items():
        lex = dict(entries) if isinstance(entries, list) else {}
        print(key, deco_dict(lex, head=2, tail=1))


test()
