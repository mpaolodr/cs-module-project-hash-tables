def word_count(s):
    # Your code here
    string_list = s.split()
    word_freq = {}
    ignored = ['"', ':', ';', ',', '.', '-', '+', '=', '/',
               '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '\\']

    # check each string and remove any characters in ignored list
    for i in range(len(string_list)):
        strip_word = ""

        for j in range(len(string_list[i])):
            if not string_list[i][j] in ignored:
                strip_word += string_list[i][j]

        string_list[i] = strip_word.lower()

    # count
    for word in string_list:
        # we'll only get an empty string if word only has special characters
        if word == "":
            return {}

        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
