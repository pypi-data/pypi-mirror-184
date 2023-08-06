from . import Path
from typing import Iterable, Tuple, Generator, Dict, List, Union
import os
import re


def hashsum(
    hashfile: str,
    files: Iterable,
    *,
    header: str = None,
    algorithm: str = None,
    size: int = None
) -> Path:
    hashfile = Path(hashfile)

    if algorithm is None:
        algorithm = hashfile.suffix.lstrip('.')
        if algorithm not in hashfile.algorithms_available:
            raise ValueError('unknown suffix or specify algorithm')
    else:
        hashfile = hashfile.with_suffix(f".{algorithm}")

    with hashfile.open(mode='wt', encoding='utf-8') as f:
        if header != None:
            f.writelines(
                [f"# {line}\n" for line in header.split('\n') if line]
            )

            if f.seek(0, os.SEEK_END) > 0:
                f.write('\n')

        dest = hashfile.resolve().parent

        kwargs = {
            'algorithm': algorithm,
            'size': size
        }

        for file in map(lambda x: Path(x).resolve(), files):

            if file.is_relative_to(dest):
                filename = file.relative_to(dest)
            else:
                filename = file

            f.write(f"{file.hexdigest(**kwargs)} *{filename}\n")

    return hashfile


def hashparse(
    hashfile: str,
) -> Generator[Tuple[str, Path], None, None]:

    hashfile = Path(hashfile)

    root = hashfile.resolve().parent

    regex = re.compile(
        r'^(?P<hash>[a-f0-9]{8,}) \*(?P<filename>.*?)$',
        re.IGNORECASE
    )

    for match in map(lambda line: regex.match(line.strip()), hashfile.iter_lines(encoding='utf-8')):
        if match is None:
            continue

        try:
            hash, filename = match.group('hash'), Path(match.group('filename'))
        except IndexError:
            continue

        if not filename.is_absolute():
            filename = root.joinpath(filename)

        yield (hash, filename)


def hashcheck(
    hashfile: str,
    algorithm: str = None,
    *,
    size: int = None
) -> Dict[Union[bool, None], List[Path]]:

    if algorithm is None:
        algorithm = hashfile.suffix.lstrip('.')
        if algorithm not in hashfile.algorithms_available:
            raise ValueError('unknown suffix or specify algorithm')

    kwargs = {
        'algorithm': algorithm,
        'size': size
    }

    result = {True: [], False: [], None: []}

    for hash, file in hashparse(hashfile):
        try:
            key = hash == file.hexdigest(**kwargs)
        except (FileNotFoundError, PermissionError) as e:
            result[None].append(file)
        else:
            result[key].append(file)

    return result
