from flask import session
from CheckRandomWord import check_in_given_word
import time
from DuplicationCheck import duplication_check
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def word_check():
    count=0;
    num_guess=0;
    all_true_answer=0
    guess_word_list =[]
    display_list=[]
    if_true = None
    rand_word_check = session.get('randword')
    guess_word_list.extend((session.get('guess_one'),session.get('guess_two'),session.get('guess_three'),session.get('guess_four'),session.get('guess_five'),session.get('guess_six'),session.get('guess_seven')))
    print(guess_word_list)

    for guess_word in guess_word_list:
        guess_word = guess_word.lower()
        if check_in_given_word(rand_word_check,guess_word):
            with open(os.path.join(APP_ROOT, 'threeOrMoreFile.txt'),'r') as three:
                for searchWord in three:
                    # This compares for guess word with each word on line and the word your searching for is equal to your guess word.
                    if guess_word == searchWord[:-1]:
                        print("check",guess_word)
                        #duplication_check(guess_word_list,inDict,guess_word)
                        if len(guess_word_list)!=len(set(guess_word_list)): # 3 != 2
                            duplication_check(display_list, guess_word, guess_word_list, set(guess_word_list))
                        else:
                            display_list.append(guess_word + "| True")
                            all_true_answer += 1

                        break
                    elif guess_word == rand_word_check:
                        display_list.append(guess_word + "| Same word not Allowed")
                        if_true = False
                        break
                else:
                    display_list.append(guess_word + "| Not in the dictionary or empty!")
                    num_guess += 1
                    print("[",num_guess,"]", "guess")
                    print("three or more characters word: ",count, "\n")
                    if_true = False
                    count = 0;
        else:
            display_list.append( guess_word + "| Not in the random word")
            if_true = False

    print(display_list)
    session['dict_list'] = display_list

    if all_true_answer == 7:
        if_true = True
        t_end = time.time()
        t_start = session.get('time_start')
        t_took = t_end - t_start
        session['time_took'] = t_took
        session['if_yes'] = if_true
    else:
        session['time_took'] = "Still wanna test the thickness of ice? Try Again"
        session['if_yes'] = if_true
