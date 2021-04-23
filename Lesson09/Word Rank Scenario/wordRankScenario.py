# 1 read file

# 2 remove punctuation and save as list of words
def remove_punctuation(st, case='a'):
    import string
    for c in string.punctuation:
        st = st.replace(c, '')
    if case == 'a':
        return st.split()
    if case == 'l':
        st = st.lower()
        return st.split()
    if case == 't':
        title_words = []
        for word in st.split():
            if word.istitle():
                title_words.append(word)
        return title_words


# 3 FILTER include option to filter out non capitalised words

# 4 Make a dictionary where each word is a key that has a value of how many times the word repeats
def frequency_dictionary(words):
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    freq_dict = {}
    for word in unique_words:
        freq_dict[word] = words.count(word)
    return freq_dict


# 5 FILTER include option to filter out all the common words
def strip_common_words(words):
    uniques = []
    common_words = open('1000words.txt', 'r')
    common_words = common_words.read()
    for word in words:
        if word.lower() not in common_words:
            uniques.append(word)
    return uniques


# 6 print ranked dictionary with top 100 words
def print_ranked_dictionary(dictionary, count=20):
    rankedList = sorted(dictionary, key=dictionary.get, reverse=True)
    for i in range(0, count):
        print(rankedList[i], 'repeats', dictionary[rankedList[i]], 'times')


def main():
    text = open('HarryPotter.txt', 'r')
    text = text.read()
    word_list = remove_punctuation(text, 't')
    uniques = strip_common_words(word_list)
    dictionary = frequency_dictionary(uniques)
    print_ranked_dictionary(dictionary,100)


main()
