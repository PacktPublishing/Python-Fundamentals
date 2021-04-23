# 1 read file

# 2 remove punctuation and save as list of words
def remove_punctuation(st, case = 'a'):
    import string
    for c in string.punctuation:
        st = st.replace(c, '')
    if case == 'a':
        return st.split()
    if case == 'l':
        st = st.lower()
        return st.split()
    if case == 'u':
        title_words = []
        for word in st.split():
            if word.istitle():
                title_words.append(word)
        return title_words

# 3 FILTER include option to filter out non capitalised words

# 4 Make a dictionary where each word is a key that has a value of how many times the word repeats
def frequency_dictionary():
    pass


# 5 FILTER include option to filter out all the common words

# 6 print ranked dictionary with top 100 words
def print_ranked_dictionary(st):
    pass


def main():
    text = open('HarryPotter.txt', 'r')
    text = text.read()
    word_list = remove_punctuation(text,'a')
    print(word_list)
    #dictionary = frequency_dictionary(word_list)
    #print_ranked_dictionary(dictionary)


main()
