
from pathlib import Path

def childsWithSuffix(path: Path, suffix: str):
    return [p for p in path.iterdir() if p.suffix == suffix]


def getChildFiles(path: Path) -> list[Path]:
    return [p for p in path.iterdir() if p.is_file()]


def getChildFolders(path: Path) -> list[Path]:
    return [p for p in path.iterdir() if p.is_dir()]
