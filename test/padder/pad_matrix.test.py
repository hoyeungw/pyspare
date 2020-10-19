from texting import COSP, LF

from pyspare.padder.matrix_padder import matrix_padder

candidates = {
    'cities': [
        ['1', 'paris', '++++'],
        ['1.1', 'san fransisco', '+'],
        ['1.2', 'tokyo', '+++'],
        ['1.3', 'delhi', '+'],
        ['1.4', 'vienna', '++'],
    ]
}


def test():
    for key, vec in candidates.items():
        print(key)
        padded = matrix_padder(vec)
        print(LF.join(['[' + COSP.join(row) + ']' for row in padded]))


test()
