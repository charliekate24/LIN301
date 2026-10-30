import re                                             # loads Python's regex toolkit

with open("../../data/gutenberg/alice.txt", encoding="utf-8") as f:  # opens alice.txt for reading
    text = f.read()                                   # reads the whole file into one string, called `text`

matches = re.findall(r"c.t", text)   # finds every match of "c_t"
print(matches)                       # take a look at what it found

matches_aou = re.findall(r"c[aou]t", text)   # finds "cat", "cot", or "cut"
print(len(matches_aou))                      # counts how many were found
print(*matches_aou, sep="\n")                # prints each match on a separate line

