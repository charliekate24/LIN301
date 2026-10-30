import re
from collections import Counter
import matplotlib.pyplot as plt

stopwords = ["the", "to", "and", "of", "a", "her", "i", "in", "was", "it",
             "she", "he", "be", "that", "you", "not", "had", "as", "his", "for",
             "with", "is", "have", "but", "at", "so", "all", "my", "been", "him",
             "on", "by", "could", "would", "very", "no", "what", "which", "they",
             "were", "there", "me", "an", "must", "this", "said", "from", "or",
             "will", "any", "much", "than", "such", "their", "them", "if", "do",
             "did", "one", "when", "your", "more", "are", "we", "who", "up",
             "out", "down", "into", "s", "t"]

try:
    with open("../../data/gutenberg/alice.txt", "r", encoding="utf-8") as f:
        alice_text = f.read()
except FileNotFoundError:
    print("Couldn't find that file — check the filename and location.")

alice_list = re.split(r"[\W]+", alice_text.lower())    # lowercase this time!
alice_list = [w for w in alice_list if w != ""]

alice_content = [w for w in alice_list if w not in stopwords]
alice_top15 = Counter(alice_content).most_common(15)

alice_labels = [pair[0] for pair in alice_top15]
alice_freqs = [pair[1] for pair in alice_top15]

plt.bar(alice_labels, alice_freqs)
plt.title("Top 15 Content Words in Alice in Wonderland")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()    # keeps the rotated labels from getting cut off
plt.savefig("alice_top15.png")    # saves to the folder you're running from
plt.show()