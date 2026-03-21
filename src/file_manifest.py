from __future__ import annotations

from pathlib import Path
import csv
from typing import Iterable


ALLOWED_EXTENSIONS = {
    ".csv",
    ".txt",
    ".xlsx",
    ".xls",
    ".json",
    ".png",
    ".jpg",
    ".jpeg",
    ".pdf",
}


def iter_files(root: Path, allowed_extensions: Iterable[str] = ALLOWED_EXTENSIONS):
    """Yield files under root with selected extensions."""
    allowed = {ext.lower() for ext in allowed_extensions}
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in allowed:
            yield path


def build_manifest(input_dir: Path, output_csv: Path) -> None:
    """Create a simple manifest CSV for files stored in input_dir."""
    input_dir = input_dir.resolve()
    rows = []

    for path in iter_files(input_dir):
        stat = path.stat()
        rows.append(
            {
                "relative_path": str(path.relative_to(input_dir)),
                "extension": path.suffix.lower(),
                "size_bytes": stat.st_size,
            }
        )

    rows.sort(key=lambda r: r["relative_path"].lower())

    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["relative_path", "extension", "size_bytes"],
        )
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    input_dir = Path("data_examples")
    output_csv = Path("data_examples/file_manifest.csv")
    build_manifest(input_dir, output_csv)
    print(f"Manifest written to: {output_csv}")
