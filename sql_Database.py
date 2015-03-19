import sqlite3 as lite
from flask import session
import sys

def sql_lite():
    full_time = session.get('time_took')
    user = session.get('usr_name')
    usr_time =(
        (user, full_time)
    )

    con = lite.connect('C:/Users/Yoseph/IdeaProjects/WordGame/rank.db')

    with con:
        cur = con.cursor()
        #cur.execute("DROP TABLE IF EXISTS rank")
        #cur.execute("CREATE TABLE rank(ID INTEGER PRIMARY KEY   AUTOINCREMENT, usr_name TEXT, time INT)")
        cur.execute("INSERT INTO rank(usr_name, time) VALUES( ?, ?)", usr_time) #NB wont work for ID unless user name and time mention here.



def readData():

    sql = "SELECT usr_name,time FROM rank ORDER BY time "
    con = lite.connect('C:/Users/Yoseph/IdeaProjects/WordGame/rank.db')
    sql_list = []
    with con:
        cur = con.cursor()
        last_user = cur.execute('SELECT MAX(id),usr_name,time FROM rank').fetchone()
        last_user_rank = 1
        for row in cur.execute(sql):
            sql_list.append(row)
            print(row)
        session['list_sql'] = sql_list

        for row in cur.execute('SELECT ID,usr_name,time FROM rank ORDER BY time asc'):
            if last_user[2] > row[2]:
                last_user_rank += 1
            else:
                break
        session['the_last_user'] = last_user[1] # 1 refers to the column
        session['rank_last_user'] = last_user_rank
        print(last_user, last_user_rank)


