import random
import string

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

following_words = {}
start_letter = [letter for letter in string.ascii_uppercase]
end_punc = ['!', '.', '?']


# split file into words
# if no param is given to split, it will split using whitespaces
split_words = words.split()


# loop through my split_words list and somehow make a key for each word
#  the value will be a list that follows every instance of that word

for i in range(len(split_words)):

    if (i + 1) < len(split_words):

        if split_words[i] in following_words:
            following_words[split_words[i]].append(split_words[i + 1])

        else:
            following_words[split_words[i]] = [split_words[i + 1]]

    else:

        # last index of split_words arr
        following_words[split_words[i]] = []


# TODO: construct 5 random sentences
# Your code here


# function to choose random start word
def start_word():

    key = random.choice(list(following_words.keys()))

    if (key[0] in start_letter) or ((key[0] == '"' and key[1] in start_letter)):
        return key

    else:
        return start_word()


# function to check if word is a stop word
def check_stop_word(s):

    if s[-1] in end_punc:
        return True

    if s[-1] == '"' and s[-2] in end_punc:
        return True

    if len(following_words[s]) == 0:
        return True

    return False


# function to generate sentences
def generate_sentence(word):

    if not check_stop_word(word):
        new_word = random.choice(following_words[word])

        return [word] + generate_sentence(new_word)

    return [word]


for i in range(5):
    random_start = start_word()
    print(" ".join(generate_sentence(random_start)), end=" ")
