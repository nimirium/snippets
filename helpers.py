import json
from typing import Dict, List


def pretty_json(d: Dict):
    s = json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))
    return s


def print_pretty_json(d: Dict):
    s = pretty_json(d)
    print(s)


def recursive_get_keys(d: Dict, skip_keys: List = None) -> List:
    """
    d = {'z': {'y': {1: ''}}, 'a': 1, 'b': {'c': 3, 'd': []}}
    recursive_get_keys(d)
    => returns [1, 'b', 'y', 'z', 'd', 'c', 'a']

    :param d: Dict to extract keys from
    :param skip_keys:
    :return: List of all keys in the dictionary and inner dictionaries
    """

    if not skip_keys:
        skip_keys = []

    the_keys = set()
    for key, val in d.items():
        if key not in skip_keys:
            the_keys.add(key)
            if isinstance(val, dict):
                more_keys = recursive_get_keys(val)
                for k in more_keys:
                    the_keys.add(k)

    return list(the_keys)


class LazyIterator:
    """
    An iterator that will evaluate the items only when the iteration starts
    """

    def __init__(self, get_items):
        self._items = None
        self._count = None
        self._next_index = -1
        self._get_items = get_items

    def __iter__(self):
        return self

    def __next__(self):
        self._next_index += 1

        if self._items is None:
            self._items = self._get_items()
            self._count = len(self._items)

        if self._next_index < self._count:
            return self._items[self._next_index]

        raise StopIteration
