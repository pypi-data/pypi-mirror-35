from forbiddenfruit import curse as monkey_patch
from omakase.functions import *


for each in [list, dict, tuple]:
    monkey_patch(each, 'len', lambda self: len(self))


for each in [list, tuple]:
    monkey_patch(each, 'map', lambda self, function: map(function, self))
    monkey_patch(each, 'max', lambda self: max(self) if self else None)
    monkey_patch(each, 'min', lambda self: min(self) if self else None)
    monkey_patch(each, 'sum', lambda self: sum(self))
    monkey_patch(each, 'zip', lambda self, other: zip(self, other))
    monkey_patch(each, 'first', first)
    monkey_patch(each, 'last', last)
    monkey_patch(each, 'freq', freq)
    monkey_patch(each, 'groupby', groupby)
    monkey_patch(each, 'indexby', indexby)
    monkey_patch(each, 'join', join)
    monkey_patch(each, 'sortby', sortby)
    monkey_patch(each, 'reduce', reduce_sequence)


monkey_patch(list, 'filter', lambda self, function: filter(function, self))
monkey_patch(list, 'compact', compact_sequence)
monkey_patch(list, 'uniq', uniq)
monkey_patch(list, 'take', take)
monkey_patch(list, 'drop', drop)
monkey_patch(list, 'flatten', flatten)


monkey_patch(dict, 'compact', compact_mapping)


monkey_patch(tuple, 'list', lambda self: list(self))
