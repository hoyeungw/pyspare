from foba import number_matrix_collection, string_matrix_collection
from pyspare.deco.deco_matrix import deco_matrix
from veho.matrix import init

candidates = {
    'blank': [[]],
    'simple': init(8, 6, lambda x, y: x + y),
    'numeral': number_matrix_collection.flop_shuffle()[1],
    'literal': string_matrix_collection.flop_shuffle()[1],
}


def test():
    for key, matrix in candidates.items():
        print(key, matrix)
        print(key, deco_matrix(matrix))


test()
