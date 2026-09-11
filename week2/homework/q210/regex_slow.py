import re

pattern = r"^[a-z]+\d{3}$"
data = [f"abc{i:03d}" for i in range(5000)]

matched = 0
for s in data:
    if re.compile(pattern).match(s):
        matched += 1
print("matched =", matched)
