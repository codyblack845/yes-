#!/usr/bin/env python3
"""Create the static website ZIP for a manual Netlify upload."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "netlify-upload.zip"
ROOT_FILES = ("index.html", "styles.css", "articles.css", "refined.css", "script.js")


def build():
    paths = [ROOT / name for name in ROOT_FILES]
    for directory in ("articles", "assets"):
        if not (ROOT / directory).is_dir():
            raise RuntimeError(f"Missing website directory: {directory}")
        paths.extend(sorted(path for path in (ROOT / directory).rglob("*") if path.is_file()))

    for path in paths:
        if not path.is_file() or path.is_symlink():
            raise RuntimeError(f"Missing or unsupported website file: {path.relative_to(ROOT)}")

    temporary = OUTPUT.with_suffix(".zip.tmp")
    with ZipFile(temporary, "w", ZIP_DEFLATED) as archive:
        for path in paths:
            archive.write(path, path.relative_to(ROOT).as_posix())

    with ZipFile(temporary) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("The upload ZIP failed its integrity check")
        if "index.html" not in archive.namelist():
            raise RuntimeError("The homepage must be at the ZIP root")

    temporary.replace(OUTPUT)
    print(f"Created {OUTPUT.name}: {len(paths)} files, {OUTPUT.stat().st_size / 1024**2:.1f} MiB")


if __name__ == "__main__":
    build()
