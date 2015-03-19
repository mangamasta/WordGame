import random
import os
import time
from flask import session
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
def randword():
    t_start = time.time()
    sevOrMoreWord= os.path.join(APP_ROOT, 'sevOrMoreFile.txt')
    sev = open(sevOrMoreWord).read().splitlines()
    word = random.choice(sev)

    session['time_start'] = t_start
    return word