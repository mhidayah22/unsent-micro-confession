"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to entry.txt: a To: line naming who
the message was meant for, and the unsent message itself, one line written
exactly as it was typed, with no explanation after it.
"""

import os
from pathlib import Path

TO_LINE = "To: my little brother"
MESSAGE = (
    "I took the money out of your birthday card to buy lunch that week, "
    "and every birthday since I've put the same amount back in, "
    "in cash, with no note."
)

ENTRY = TO_LINE + "\n" + MESSAGE


def output_dir() -> Path:
    """Where the grader collects the entry.

    Honour MAKEFUN_OUTPUT_DIR first, then /output when it exists, and only
    then a local output folder next to this file. Never the working
    directory: the grader runs with a read-only working directory.
    """
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    if Path("/output").is_dir():
        return Path("/output")
    return Path(__file__).resolve().parent / "output"


def main() -> None:
    if not 1 <= len(ENTRY) <= 260:
        raise SystemExit("entry must be 1 to 260 characters")
    if not 1 <= len(MESSAGE) <= 200 or "\n" in MESSAGE:
        raise SystemExit("message must be one line of 1 to 200 characters")

    # Set the umask before creating anything, so the output folder ends up
    # 0755 and entry.txt 0644: the grader collects them as another user.
    os.umask(0o022)
    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    os.chmod(target, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
