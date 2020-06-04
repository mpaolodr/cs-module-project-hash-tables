# Your code here
import string


def histo(filename):

    with open(filename, "r") as f:
        file = f.read()

    words = file.split()

    # will be used for justifying to left
    longest_word = ""

    # removing special chars and getting longest word
    for i in range(len(words)):

        new_word = ""

        for j in words[i]:

            if j.isalnum():
                new_word += j

        words[i] = new_word.lower()

        if len(words[i]) > len(longest_word):
            longest_word = words[i]

    # store count
    word_freq = {}

    # count number of words
    for word in words:

        if word in word_freq:
            word_freq[word] += "#"
        else:
            word_freq[word] = "#"

    # sort by number of requency
    num_of_words_freq = {key: val for key, val in sorted(
        word_freq.items(), key=lambda item: len(item[1]), reverse=True)}

    # sort alphabetically
    alpha_freq = {key: val for key, val in sorted(
        word_freq.items(), key=lambda key: key)}

    # number of frequency
    for key in num_of_words_freq:
        print(
            f"""{key.ljust(len(longest_word), " ")} {num_of_words_freq[key]}""")

    # alphabetical order
    for key in alpha_freq:
        print(
            f"""{key.ljust(len(longest_word), " ")} {alpha_freq[key]}""")


print(histo("./robin.txt"))
