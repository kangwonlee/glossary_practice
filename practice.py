import pathlib
import random
import sys
from typing import List

sys.path.append(str(pathlib.Path(__file__).parent.absolute()))

import path


def main(argv):
    glossary = get_flat_glossary(argv)

    words = list(glossary.keys())
    random.shuffle(words)

    for word in words:
        v = random.randint(0, 1)
        if v:
            print(word)
            input()
            print(glossary[word])
            input()
        else:
            print(glossary[word])
            input()
            print(word)
            input()


def get_flat_glossary(argv:List[str]) -> dict:
    glossary_json = path.read_glossary(path.get_json_path(argv))

    glossary = {}

    for sub_glossary in glossary_json.values():
        glossary.update(sub_glossary)

    return glossary


if "__main__" == __name__:
    main(sys.argv)
