from test.assets import vector_collection
from pyspare.deco.deco_vector import deco_vector


def test():
    for key, vec in vector_collection.items():
        print(key, deco_vector(vec, head=3, tail=2))


test()
