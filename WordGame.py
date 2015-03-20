from flask import Flask, render_template, url_for, request, redirect, flash, session
from RandomWord import randword
from WordChecker import word_check
from sql_Database import sql_lite,readData
from read_db import readDataFirst
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#---------------------------------------------------------------------
app = Flask(__name__)

@app.route('/')
def begin():
    return render_template("play.html",
                           the_title="Welcome to the Word Game",
                           home_link=url_for("show"))
@app.route('/2', methods=["POST"])
def show():

    if request.form['submit'] == 'Play':
        random_word = randword()
        session['randword'] = random_word
        print("hello")
        return render_template("wordgame.html",
                               the_title="Begin",
                               word_to_guess= random_word,
                               the_save_url=url_for("saveformdata"))
    elif request.form['submit'] == 'Rank Board':
        readDataFirst()
        return render_template("rank_at_start.html",
                               the_title="Rank Board",
                               rank_list = session.get('list_sql_first'),
                               home_link = url_for("begin"), )

#---------------------------------------------------------------------
@app.route('/3')
def again():
    random_word = randword()
    session['randword'] = random_word
    print("hello")
    return render_template("wordgame.html",
                            the_title="Begin",
                            word_to_guess= random_word,
                            the_save_url=url_for("saveformdata"))
#use flash to display error syntax on fields
@app.route('/redisplay')
def reshow():
    return render_template("wordgame.html",
                           the_title="Begin",
                           word_to_guess= session.get('randword'),
                           the_save_url=url_for("saveformdata"))

#---------------------------------------------------------------------
@app.route('/saveform', methods=["POST"])
def saveformdata():
    if request.form['first_guess'] == '':
        flash("Sorry. You must tell me your guess. Try again")
        return redirect(url_for("reshow")) # display the flash message in this redirection link
    else:
        session['guess_one'] = request.form['first_guess']
        session['guess_two'] = request.form['second_guess']
        session['guess_three'] = request.form['third_guess']
        session['guess_four'] = request.form['fourth_guess']
        session['guess_five'] = request.form['fifth_guess']
        session['guess_six'] = request.form['sixth_guess']
        session['guess_seven'] = request.form['seventh_guess']

        word_check()
        if_everyting_ok = session.get('if_yes')

        if if_everyting_ok is True:
            lines = session.get('dict_list')
            return render_template("displayanswer.html",
                                   the_title="Congratulations",
                                   the_data=lines,
                                   time_taken= session.get('time_took'),
                                   rankboard = url_for("ranking"),
                                   home_link = url_for("show"), )
        else:
            lines = session.get('dict_list')
            return render_template("displayfail.html",
                               the_title="Validation Table",
                               the_data=lines,
                               time_taken= session.get('time_took'),
                               home_link = url_for("again"), )


@app.route('/ranktable', methods=["POST"])
def ranking():
    session['usr_name'] = request.form['name']
    sql_lite()
    readData()
    return render_template("rank.html",
                           the_title="Rank Board",
                           rank_list = session.get('list_sql'),
                           last_user = session.get('the_last_user'),
                           last_user_rank = session.get('rank_last_user'),
                           home_link = url_for("again"), )

app.config['SECRET_KEY'] = 'thisismysecretkeywhichyouwillneverguesshahahahahahahaha'
if __name__ == "__main__":
    	app.run(host='0.0.0.0')