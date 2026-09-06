words = open("words.txt", encoding="utf-8").read().split()
unique = []
seen = set()
for word in words:
    if word not in seen:
        unique.append(word)
        seen.add(word)
print("count=", len(unique))
