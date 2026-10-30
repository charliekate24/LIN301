word = "spin" 
starts_p = word[0] == "p"
starts_t = word[0] == "t"
starts_k = word[0] == "k"
aspirated = starts_p or starts_t or starts_k

print(word, aspirated) 