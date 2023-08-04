import json
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent.absolute()))

import path


def main(argv):
    json_path = path.get_json_path(argv)
    glossary_json = path.read_glossary(json_path)

    glob = path.proj_path().glob("*.glossary")

    for fpath in glob:
        glossary_name = fpath.relative_to(path.proj_path()).stem
        print(f"Processing {glossary_name}...")
        sub_glossary = glossary_json.get(glossary_name, {})
        sub_glossary.update(process_glossary(fpath))
        glossary_json[glossary_name] = sub_glossary

    json_path.write_text(json.dumps(glossary_json, indent=4))


def process_glossary(fpath:pathlib.Path) -> dict:
    """
    Read a glossary file and return a dictionary of terms and definitions.
    """
    assert isinstance(fpath, pathlib.Path), fpath
    assert fpath.exists()
    assert fpath.is_file()

    txt = fpath.read_text()
    lines = txt.splitlines()

    glossary = {}

    for line in lines:
        i = line.index(" - ")
        key = line[:i].strip()
        value = line[i+3:].strip()

        assert key not in glossary, key
        glossary[key] = value

    return glossary


if "__main__" == __name__:
    main(sys.argv)
