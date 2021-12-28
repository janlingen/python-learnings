def get_n_longest_unique_words(words, n):
    lst = []
    for i in words:
        if words.count(i) == 1:
            lst.append(i)
    y = sorted(lst, key=len, reverse=True)
    return y[:n]