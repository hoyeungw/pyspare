from crostab import Crostab
from foba import crostab_collection
from texting import LF

from pyspare.deco.deco_crostab import deco_crostab

candidates = {
    'AoEIIUnitsHpByStages': crostab_collection['AoEIIUnitsHpByStages'],
    'CountryGDPByYear': crostab_collection['CountryGDPByYear'],
}


def test():
    for key, table in candidates.items():
        table = Crostab(**table)

        print(key, table)
        print(key, LF + deco_crostab(table))


test()
