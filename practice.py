import json
import pathlib
import sys


def main(argv):
    json_path = get_json_path(argv)
    glossary_json = read_glossary(json_path)

    glob = proj_path().glob("*.glossary")
    print(tuple(glob))
    print(TypeError(glossary_json))


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
