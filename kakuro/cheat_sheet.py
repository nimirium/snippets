import logging
from itertools import compress, product
from typing import List, Dict


def get_all_combinations(items):
    return (set(compress(items, mask)) for mask in product([0, 1], repeat=len(items)))


def generate_cheat_sheet() -> Dict[int, Dict[int, List[int]]]:
    cheat_sheet = {}
    combos = get_all_combinations(range(1, 10))
    for c in combos:
        n = len(c)
        if n > 1:
            s = sum(c)
            if not cheat_sheet.get(n):
                cheat_sheet[n] = {}
            if not cheat_sheet[n].get(s):
                cheat_sheet[n][s] = []
            cheat_sheet[n][s] = sorted(list(set(cheat_sheet[n][s] + list(c))))
    return cheat_sheet


cheat_sheet = generate_cheat_sheet()

logging.info("cheat_sheet: ")
logging.info(cheat_sheet)
