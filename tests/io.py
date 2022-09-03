from pathlib import Path


def get_content(path: Path, bytes_: bool = False):
    mode = 'rb' if bytes_ else 'r'
    with open(path, mode=mode) as file:
        return file.read()
