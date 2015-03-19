from collections import Counter
#Compare if guessed word is in given word (random word)

def check_in_given_word( given_word, to_check):
    given_word_counter = Counter(given_word)
    word_counter = Counter(to_check)
    given_word_counter.subtract(word_counter)
    is_in_word_or_not=None;
    #if any -ve letter count is found, it is not in given_word
    if any([c < 0 for c in given_word_counter.values()]): #if characters are not match (leftover chars) they are -1.
        # do whatever you want, or return False
        print ("{} is NOT in {}".format(to_check, given_word))
        is_in_word_or_not=None;
    else:
        print ("{} is in {}".format(to_check, given_word))
        is_in_word_or_not=True;
    # print the counter for your info
    print (given_word_counter)
    return is_in_word_or_not