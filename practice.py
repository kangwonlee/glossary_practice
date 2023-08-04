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

    n = len(words)

    for i, word in enumerate(words):
        v = random.randint(0, 1)

        three_others = random.sample(words, 3)

        choices = list(set([word] + three_others))

        random.shuffle(choices)

        print(f"{'#' * 20}\n{i+1}/{n}")

        ans = None
        if v:
            print(word)
            print('=' * 20)
            for j, w in enumerate(choices):
                print(j+1, glossary[w])
                print()
                if w == word:
                    ans = j+1
            reply=int(input())

            print('#' * 20)
            print("correct" if reply == ans else "wrong")
            print(ans, glossary[word])
        else:
            print(glossary[word])
            print('=' * 20)
            for j, w in enumerate(choices):
                print(j+1, w)
                print()
                if w == word:
                    ans = j+1
            reply=int(input())

            print('#' * 20)
            print("correct" if reply == ans else "wrong")
            print(ans, word)


def get_flat_glossary(argv:List[str]) -> dict:
    glossary_json = path.read_glossary(path.get_json_path(argv))

    glossary = {}

    for sub_glossary in glossary_json.values():
        glossary.update(sub_glossary)

    return glossary


if "__main__" == __name__:
    main(sys.argv)
