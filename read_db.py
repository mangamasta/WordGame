import sqlite3 as lite
from flask import session
import sys

def readDataFirst():

    sql = "SELECT usr_name,time FROM rank ORDER BY time "
    con = lite.connect('rank.db')
    sql_list_first = []
    with con:
        cur = con.cursor()
        for row in cur.execute(sql):
            sql_list_first.append(row)
            print(row)
        session['list_sql_first'] = sql_list_first


