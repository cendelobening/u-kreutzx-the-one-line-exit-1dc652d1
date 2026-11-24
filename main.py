"""Write a one-line resignation letter to the output directory.

Pure standard library. The letter is a single line of at most 140
characters, written as UTF-8 with no trailing newline.
"""

import os
import stat
import sys
import tempfile

LETTER = (
    "Dear Boss, I hereby resign \u2014 I came for the dream job, "
    "stayed for the free snacks, and I'm leaving because someone "
    "ate the last biscuit."
)

MAX_CHARS = 140


def check_letter(text):
    if not isinstance(text, str):
        raise ValueError("letter must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("letter must be 1 to 140 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("letter must be a single line")
    if text != text.strip():
        raise ValueError("letter must not have leading or trailing whitespace")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("letter must not contain control characters")
    if not any(ch.isalpha() for ch in text):
        raise ValueError("letter must contain at least one letter")


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_atomic(directory, filename, payload):
    os.makedirs(directory, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=directory, prefix=".entry-", suffix=".tmp")
    try:
        os.chmod(tmp_path, 0o644)
        with os.fdopen(fd, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.rename(tmp_path, os.path.join(directory, filename))
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    final_path = os.path.join(directory, filename)
    os.chmod(final_path, 0o644)
    return final_path


def verify(path, payload):
    with open(path, "rb") as handle:
        data = handle.read()
    if data != payload:
        raise ValueError("written bytes do not match the letter")
    text = data.decode("utf-8")
    if text.endswith("\n"):
        raise ValueError("output must not end with a newline")
    check_letter(text)
    mode = stat.S_IMODE(os.stat(path).st_mode)
    if mode != 0o644:
        raise ValueError("output mode must be 0644")
    return text


def main():
    check_letter(LETTER)
    payload = LETTER.encode("utf-8")
    directory = output_dir()
    # Atomic write: a reader of entry.txt only ever sees the full
    # letter or nothing, never a half-written file.
    path = write_atomic(directory, "entry.txt", payload)
    text = verify(path, payload)
    print("wrote %s (%d chars, %d bytes, no trailing newline)" % (path, len(text), len(payload)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
