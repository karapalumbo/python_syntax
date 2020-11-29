def print_upper_words_2(words):
    """For a list of words, print each word on a separate line, 
    but in all uppercase
    """

    for word in words:
        print(word.upper())


# print_upper_words_2(["hello", "world"])


def print_upper_words_3(words):

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word)

# print_upper_words_3(["Emily", "has", "an", "elephant"])


def print_upper_words_4(words, words_start_with):

    for word in words:
        for letter in words_start_with:
            if word.startswith(letter):
                print(word)


print_upper_words_4(["hello", "hey", "goodbye", "yo", "yes"], ["h", "g"])
