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

        three_others = random.sample(words, 3)

        choices = list(set([word] + three_others))

        random.shuffle(choices)

        if v:
            print(word)
            print('=' * 20)
            for j, w in enumerate(choices):
                print(j+1, glossary[w])
            input()

            print('#' * 20)
            print(glossary[word])
        else:
            print(glossary[word])
            print('=' * 20)
            for j, w in enumerate(choices):
                print(j+1, w)
                print()
            input()

            print('#' * 20)
            print(word)

        print('#' * 20)


def get_flat_glossary(argv:List[str]) -> dict:
    glossary_json = path.read_glossary(path.get_json_path(argv))

    glossary = {}

    for sub_glossary in glossary_json.values():
        glossary.update(sub_glossary)

    return glossary


if "__main__" == __name__:
    main(sys.argv)
