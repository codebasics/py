s = "I work in bloomberg founded by bloomberg work work"

tokens = s.split(" ")
d = {}
for token in tokens:
    if token in d:
        d[token] += 1
    else:
        d[token] = 1

print(d)