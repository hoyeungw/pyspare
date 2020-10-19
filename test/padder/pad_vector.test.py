from texting import LF

from pyspare.padder.vector_padder import vector_padder

candidates = {
    'cities': ['paris', 'london', 'tokyo', 'delhi', 'vienna']
}


def test():
    for key, vec in candidates.items():
        print(key)
        padded = vector_padder(vec)
        print(LF.join(['\'' + word + '\'' for word in padded]))


test()
