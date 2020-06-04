def no_dups(s):
    # Your code here
    words = {}

    words_list = s.split()

    for w in words_list:
        if w in words:
            words[w] += 1
        else:
            words[w] = 1

    return " ".join(words.keys())


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
