def remove_punctuation(st, case='l'):
    """ takes in a string and returns a list of words with no punctuation"""
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}“”‘’~'
    all_words = st.split()
    cap_words = []
    for c in punctuation:
        st = st.replace(c, '')
    if case == 'u':
        for word in all_words:
            if word.istitle():
                cap_words.append(word)
        return cap_words
    if case == 'l':
        return all_words


def frequency_dictionary(words):
    freq_dict = {}
    for word in words:
        freq_dict[word] = words.count(word)
    return freq_dict


def strip_common_words(words):
    unique_words = []
    with open('1000words.txt', 'r') as common_words:
        common_words = common_words.read()
        for word in words:
            if word not in common_words:
                unique_words.append(word)
    return unique_words


def print_ranked_dictionary(dictionary, min_count=20):
    rankedList = sorted(dictionary, key=dictionary.get, reverse=True)
    # ranking the dictionary (print out ranked words)
    for i in range(0, len(rankedList)):
        key = rankedList[i]
        value = dictionary[key]
        if value > min_count:
            print(key, ' repeats ', value, ' times')


def main():
    with open('HarryPotter.txt', 'r') as text:
        text = text.read()
        word_list = remove_punctuation(text)
        #print(word_list)
        dictionary = frequency_dictionary(word_list)
        print_ranked_dictionary(dictionary)


main()
