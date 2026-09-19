import glob

files = sorted(glob.glob("chapter*.md"))
with open("book.md", "w", encoding="utf-8") as out:
    for f in files:
        with open(f, encoding="utf-8") as fh:
            out.write(fh.read() + "\n")
