import re

pattern = r"^[a-z]+\d{3}$"
compiled = re.compile(pattern)
data = [f"abc{i:03d}" for i in range(5000)]

matched = 0
for s in data:
    if compiled.match(s):
        matched += 1
print("matched =", matched)
