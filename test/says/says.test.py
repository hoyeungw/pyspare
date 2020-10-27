from foba.dicts.dict_strings import dict_collection

from pyspare import deco_dict, says


def test():
    name, lex = dict_collection.flop_shuffle(7)
    print(name, deco_dict(lex))
    for key, value in lex.items():
        pal = says[key].asc
        pal(value)


test()
