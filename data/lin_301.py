import os
import re
import pandas as pd

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

def ly_rate(words):
    count = 0
    for w in words:
        if w.endswith("ly"):
            count += 1
    return count / len(words) * 1000

def stopword_rate(words, stopwords):
    count = 0
    for w in words:
        if w in stopwords:
            count += 1
    return count / len(words)

def load_text(filename):
    with open(os.path.join(HERE, "gutenberg", filename), "r", encoding="utf-8") as f:
        lines = f.readlines()
    while not lines[0].startswith("*** START"):
        lines = lines[1:]
    lines = lines[1:]
    while not lines[-1].startswith("*** END"):
        lines = lines[:-1]
    lines = lines[:-1]
    return "".join(lines)

def load_words(filename):
    text = load_text(filename)
    words = re.split(r"[\W_]+", text.lower())
    return [w for w in words if w != ""]

def report(title, words):
    print(title, "TTR:", ttr(words))
    print(title, "TTR (10,000 words):", ttr_first(words))
    print(title, "Average Word Length:", avg_word_len(words))
    print(title, "-ly words per 1,000:", ly_rate(words))
    return ttr_first(words)

def book_to_df(filename, label):
    text = load_text(filename)
    chapters = re.split(r"(?im)^CHAPTER\s+(?:[IVXLCDM]+|\d+)\b", text)
    chapters = chapters[1:]
    rows = []
    chapter_num = 0
    for chapter in chapters:
        chapter_num += 1
        words = re.split(r"[\W_]+", chapter.lower())
        words = [w for w in words if w != ""]
        for w in words:
            rows.append({"word": w, "chapter": chapter_num})
    df = pd.DataFrame(rows)
    df["text"] = label
    return df

def add_columns(df):
    df["length"] = df["word"].str.len()
    df["is_ly"] = df["word"].str.endswith("ly")
    return df

def book_to_spacy_df(filename, label, nlp):
    text = load_text(filename)
    chapters = re.split(r"(?im)^CHAPTER\s+(?:[IVXLCDM]+|\d+)\b", text)
    chapters = chapters[1:]
    rows = []
    chapter_num = 0
    for chapter in chapters:
        chapter_num += 1
        doc = nlp(chapter)
        sentence_num = 0
        for sent in doc.sents:
            sentence_num += 1
            for token in sent:
                if token.is_alpha:
                    rows.append({"word": token.text.lower(),
                                 "lemma": token.lemma_.lower(),
                                 "pos": token.pos_,
                                 "is_stop": token.is_stop,
                                 "sentence": sentence_num,
                                 "chapter": chapter_num})
    df = pd.DataFrame(rows)
    df["text"] = label
    return df

def book_to_svo_df(filename, label, nlp):
    text = load_text(filename)
    chapters = re.split(r"(?im)^CHAPTER\s+(?:[IVXLCDM]+|\d+)\b", text)
    chapters = chapters[1:]
    rows = []
    chapter_num = 0
    for chapter in chapters:
        chapter_num += 1
        doc = nlp(chapter)
        for token in doc:
            if token.pos_ == "VERB":
                subjects = [c for c in token.children if c.dep_ == "nsubj"]
                objects = [c for c in token.children if c.dep_ == "dobj"]
                if subjects and objects:
                    rows.append({"subject": subjects[0].lemma_.lower(),
                                 "verb": token.lemma_.lower(),
                                 "object": objects[0].lemma_.lower(),
                                 "chapter": chapter_num})
    df = pd.DataFrame(rows)
    df["text"] = label
    return df

def is_vowel(letter):
    vowels = "aeiouāēīōū"
    return letter in vowels

def cv_pattern(word):
    pattern = ""
    for letter in word:
        if is_vowel(letter):
            pattern += "V"
        else:
            pattern += "C"
    return pattern 

def syllabify(word):
    syllables = []
    current = ""
    for letter in word:
        current += letter
        if is_vowel(letter):
            syllables.append(current)
            current = ""
    return syllables

def count_syllables(word):
    return len(syllabify(word))
