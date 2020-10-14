from foba import number_vector_collection, string_vector_collection

vector_collection = {
    'none': None,
    'empty': [],
    'numerals': [1, 1, '+2.0', 3, '5.0', 8, ' 13', 21],
    'literal': ['foo', 'bar', 'zen'],
    'cities': ['san fransisco', 'buenos aires', 'bern', 'kinshasa-brazzaville', 'nairobi']
}

vector_collection.update([
    string_vector_collection.flop_shuffle(10),
    number_vector_collection.flop_shuffle(10)
])
