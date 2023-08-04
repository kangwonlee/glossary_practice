import json
import pathlib
import sys


def main(argv):
    json_path = get_json_path(argv)
    glossary_json = read_glossary(json_path)

    glob = proj_path().glob("*.glossary")

    for fpath in glob:
        glossary_name = fpath.relative_to(proj_path()).stem
        print(f"Processing {glossary_name}...")
        sub_glossary = glossary_json.get(glossary_name, {})
        sub_glossary.update(process_glossary(fpath))

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
        key = line[:i]
        value = line[i+3:]

        assert key not in glossary, key
        glossary[key] = value

    return glossary


def script_path() -> pathlib.Path:
    return pathlib.Path(__file__).absolute()


def proj_path() -> pathlib.Path:
    return script_path().parent.absolute()


def default_json_filename() -> str:
    return "glossary.json"


def get_json_path(argv) -> pathlib.Path:
    if 1 < len(argv):
        json_path = pathlib.Path(argv[1])
    else:
        json_path = pathlib.Path(default_json_filename())

    return json_path

 
def read_glossary(json_path:pathlib.Path, encoding:str="utf-8") -> dict:
    if json_path.exists():
        json_txt = json_path.read_text(encoding=encoding)
    else:
        json_txt = '{}'

    return json.loads(json_txt)


if "__main__" == __name__:
    main(sys.argv)
