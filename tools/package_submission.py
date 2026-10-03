"""Package only the inference files named in submission_manifest.json.

The template refuses to run until the released rules have been checked and the
manifest has rules_confirmed=true. Use the organizer's required upload format.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import sys
import zipfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "submission_manifest.json"
HANDOFF = ROOT / "handoff"
PACKAGE = HANDOFF / "judge_submission"


def inside_workspace(raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Unsafe source path: {raw}")
    resolved = (ROOT / path).resolve()
    if not resolved.is_relative_to(ROOT):
        raise ValueError(f"Source escapes workspace: {raw}")
    if resolved.is_relative_to(HANDOFF):
        raise ValueError(f"Source cannot be in handoff/: {raw}")
    return resolved


def judge_path(raw: str) -> PurePosixPath:
    path = PurePosixPath(raw)
    if not raw or path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
        raise ValueError(f"Unsafe judge-facing name: {raw}")
    if "\\" in raw or ":" in raw:
        raise ValueError(f"Use a relative forward-slash name: {raw}")
    return path


def main() -> None:
    config = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if config.get("rules_confirmed") is not True:
        raise ValueError("Read the released rules, update the manifest, then set rules_confirmed=true.")
    entries = config.get("files")
    if not isinstance(entries, list) or not entries:
        raise ValueError("Manifest needs at least one file.")
    if not isinstance(config.get("make_zip"), bool):
        raise ValueError("make_zip must be true or false.")

    checked: list[tuple[Path, PurePosixPath]] = []
    names: set[str] = set()
    for entry in entries:
        source = inside_workspace(entry["source"])
        target = judge_path(entry["judge_name"])
        if not source.is_file():
            raise FileNotFoundError(f"Missing submission file: {source}")
        if str(target) in names:
            raise ValueError(f"Duplicate judge-facing name: {target}")
        names.add(str(target))
        checked.append((source, target))

    HANDOFF.mkdir(exist_ok=True)
    if PACKAGE.exists():
        shutil.rmtree(PACKAGE)
    PACKAGE.mkdir()
    receipt = []
    for source, target in checked:
        output = PACKAGE.joinpath(*target.parts)
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, output)
        digest = hashlib.sha256(output.read_bytes()).hexdigest()
        receipt.append({"name": str(target), "bytes": output.stat().st_size, "sha256": digest})

    (HANDOFF / "local_receipt.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    archive = HANDOFF / "judge_submission.zip"
    if archive.exists():
        archive.unlink()
    if config["make_zip"]:
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zipped:
            for output in PACKAGE.rglob("*"):
                if output.is_file():
                    zipped.write(output, output.relative_to(PACKAGE).as_posix())
    print(f"Packaged {len(receipt)} file(s) in {PACKAGE}")
    if config["make_zip"]:
        print(f"ZIP: {archive}")
    print(f"Local receipt: {HANDOFF / 'local_receipt.json'}")
    print("Run the organizer's evaluator on the packaged files before uploading.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(f"Packaging failed: {error}", file=sys.stderr)
        raise SystemExit(1)
