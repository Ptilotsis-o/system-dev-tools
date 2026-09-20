import sys
from pathlib import Path

src = Path(sys.argv[1])
dst = src.with_suffix(".thumb.txt")
dst.write_text("THUMB: " + src.read_text(), encoding="utf-8")
