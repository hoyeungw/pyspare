from pyspare.deco.deco_entries.deco_entries import deco_entries
from test.assets import entries_collection


def test():
    for key, entries in entries_collection.items():
        print(key, deco_entries(entries))


test()
