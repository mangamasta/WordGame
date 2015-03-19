from flask import session

def duplication_check(display_list, guess_word, full_guess_list, dup_list):
    dup_count = 0;
    single_count = 0
    for line in full_guess_list:
        if guess_word == line:
            dup_count += 1
            print("First loop: ", dup_count)

    for line in dup_list:
        if guess_word == line:
            single_count += 1
            print("Second loop: ",single_count)

    if dup_count != single_count:
        print(guess_word, "| Duplicate Found")
        display_list.append(guess_word + "| Duplicate")
    else:
        display_list.append(guess_word + "| True")
    return