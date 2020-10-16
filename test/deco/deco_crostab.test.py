from crostab import Crostab
from foba import crostab_collection
from palett.presets import METRO, SUBTLE
from texting import LF

from pyspare.deco.deco_crostab import deco_crostab

candidates = {
    'AoEIIUnitsHpByStages': crostab_collection['AoEIIUnitsHpByStages'],
    'CountryGDPByYear': crostab_collection['CountryGDPByYear'],
}


def test():
    for key, table in candidates.items():
        table = Crostab(**table)
        config = {
            'top': 3,
            'bottom': 2,
            'left': 2,
            'right': 1,
            'presets': (METRO, SUBTLE)
        }
        print(key, table)
        print(key, LF + deco_crostab(table, **config))


test()
