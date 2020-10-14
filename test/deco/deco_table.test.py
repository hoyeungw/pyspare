from crostab import Table
from foba import table_collection
from texting import LF

from pyspare.deco.deco_tabular.deco_table import deco_table

candidates = {
    'BistroDutyRoster': table_collection['BistroDutyRoster'],
    'AeroEngineSpecs': table_collection['AeroEngineSpecs'],
}


def test():
    for key, table in candidates.items():
        table = Table.from_dict(table)
        print(key, table)
        print(key, LF + deco_table(table))


test()
