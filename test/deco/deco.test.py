from pyspare.logger import says

from pyspare import deco, deco_dict
from test.assets.misc_collection import misc_candidates

print('deco_dict', deco_dict(misc_candidates))

print('deco', deco(misc_candidates))

says['misc'](deco(misc_candidates))
