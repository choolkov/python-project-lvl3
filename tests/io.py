from pathlib import Path


def get_content(path: Path, binary: bool = False):
    mode = 'rb' if binary else 'r'
    with open(path, mode=mode) as file:
        return file.read()
