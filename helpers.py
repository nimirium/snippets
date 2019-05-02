import json
from typing import Dict


def pretty_json(d: Dict):
    s = json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))
    return s


def print_pretty_json(d: Dict):
    s = pretty_json(d)
    print(s)
