import os
import re

HERE = os.path.dirname(__file__)   # the folder lin301.py lives in: data/

def ttr(words):
    return len(set(words)) / len(words)

def ttr_first(words, n=10000):
    return len(set(words[:n])) / len(words[:n])

def avg_word_len(words):
    total = 0
    for w in words:
        total += len(w)
    return total / len(words)

def load_words(filename):
    with open(os.path.join(HERE, "gutenberg", filename), "r", encoding="utf-8") as f:
        lines = f.readlines()

    while not lines[0].startswith("*** START"):
        lines = lines[1:]
    lines = lines[1:]
    while not lines[-1].startswith("*** END"):
        lines = lines[:-1]
    lines = lines[:-1]

    text = "".join(lines)
    words = re.split(r"[\W_]+", text.lower())
    return [w for w in words if w != ""]

def report(title, words):
    print(title, "TTR:", ttr(words))
    print(title, "TTR (10,000 words):", ttr_first(words))
    print(title, "Average Word Length:", avg_word_len(words))
    return ttr_first(words)

import sys
sys.path.append("../../data")
import lin301
import matplotlib.pyplot as plt

alice_ttr_10000 = lin_301.report("Alice", lin_301.load_words("alice.txt"))
mansfield_ttr_10000 = lin_301.report("Mansfield Park", lin_301.load_words("mansfield_park.txt"))
romeo_ttr_10000 = lin_301.report("Romeo and Juliet", lin_301.load_words("romeo.txt"))
sherlock_ttr_10000 = lin_301.report("Sherlock Holmes", lin_301.load_words("sherlock".txt"))

plt.bar(["Lewis Carroll", "Jane Austen", "William Shakespeare", "Conan Doyle"],
        [alice_ttr_10000, mansfield_ttr_10000, romeo_ttr_10000, sherlock_ttr_10000])
plt.title("TTR Comparison: Four Authors")
plt.xlabel("Author")
plt.ylabel("TTR")
plt.show()
