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
