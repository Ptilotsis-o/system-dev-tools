with open("book.md", encoding="utf-8") as f:
    lines = f.readlines()

toc = ["# 目录\n"]
for line in lines:
    if line.startswith("# "):
        title = line.strip("# ").strip()
        toc.append(f"- {title}\n")

with open("final.md", "w", encoding="utf-8") as out:
    out.writelines(toc)
    out.write("\n")
    out.writelines(lines)
