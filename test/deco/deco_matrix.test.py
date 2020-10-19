from foba import number_matrix_collection, string_matrix_collection
from veho.matrix import init

from pyspare.deco.deco_matrix import deco_matrix

candidates = {
    'blank': [[]],
    'simple': init(8, 6, lambda x, y: x + y),
    'numeral': number_matrix_collection.flop_shuffle()[1],
    'literal': string_matrix_collection.flop_shuffle(3)[1],
}


def test():
    for key, matrix in candidates.items():
        print(key, matrix)
        config = {
            'top': 3,
            'bottom': 1,
            'left': 2,
            'right': 2
        }
        print(key, deco_matrix(matrix, **config))


test()
