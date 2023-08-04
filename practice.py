import pathlib
import random
import sys

sys.path.append(str(pathlib.Path(__file__).parent.absolute()))

import path


def main(argv):
    json_path = path.get_json_path(argv)
    glossary_json = path.read_glossary(json_path)

    # flatten the glossary
    glossary = {}
    for sub_glossary in glossary_json.values():
        glossary.update(sub_glossary)

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


if "__main__" == __name__:
    main(sys.argv)
