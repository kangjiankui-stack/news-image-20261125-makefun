#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261125.

Copies the pre-built front-page image (entry.png, in this repo) to
/output/entry.png. Deterministic: same input bytes, same output bytes.
No network, no randomness.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    dst = "/output/entry.png"
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, dst)
    # Verify the copy is byte-identical so both grader runs agree.
    with open(src, "rb") as f:
        want = f.read()
    with open(dst, "rb") as f:
        got = f.read()
    if want != got:
        raise SystemExit("entry.png copy mismatch")
    print(f"wrote {dst} ({len(got)} bytes)")


if __name__ == "__main__":
    main()
